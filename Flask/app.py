from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, TimeField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from config import get_rooms
import apiinteg

api_integ = apiinteg.ApiIntegration

app = Flask(__name__)
app.secret_key = '143589'  

users = {
    'admin1': {'password': 'admin1pass', 'role': 'super_admin'},
    'admin2': {'password': 'admin2pass', 'role': 'approval_admin'},
    'room_admin_user': {'password': 'roomadminpass', 'role': 'room_admin'},
    'club_user1': {'password': 'clubuser1pass', 'role': 'club_user'},
    'club_user2': {'password': 'clubuser2pass', 'role': 'club_user'}
}

roles = {
    'super_admin': {
        'can_view_events': True,
        'can_approve_events': True,
        'can_create_events': True,
    },
    'approval_admin': {
        'can_view_events': True,
        'can_approve_events': True,
        'can_create_events': False,
    },
    'room_admin': {
        'can_view_events': True,
        'can_approve_events': False,
        'can_create_events': False,
    },
    'club_user': {
        'can_view_events': True,
        'can_approve_events': False,
        'can_create_events': True,
    },
}

rooms = get_rooms()
events = []  

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class CreateEventForm(FlaskForm):
    event_name = StringField('Event Name', validators=[DataRequired(), Length(max=100)])
    event_description = StringField('Event Description', validators=[DataRequired(), Length(max=200)])
    expected_attendance = IntegerField('Expected Attendance', validators=[DataRequired(), NumberRange(min=1)])
    event_date = StringField('Event Date (YYYY-MM-DD)', validators=[DataRequired()])
    start_time = StringField('Start Time (HH:MM)', validators=[DataRequired()])
    end_time = StringField('End Time (HH:MM)', validators=[DataRequired()])
    submit = SubmitField('Create Event')

    def validate_event_date(self, field):
        try:
            datetime.strptime(field.data, '%Y-%m-%d')
        except ValueError:
            raise ValidationError('Invalid date format. Use YYYY-MM-DD.')

    def validate_times(self):
        start = datetime.strptime(self.start_time.data, '%H:%M').time()
        end = datetime.strptime(self.end_time.data, '%H:%M').time()
        if start >= end:
            raise ValidationError('End time must be after start time.')

def check_room_availability(room_name, event_date, start_time, end_time):
    for event in events:
        if event['room_name'] == room_name and event['event_date'] == event_date:
            if start_time < event['end_time'] and end_time > event['start_time']:
                return False  
    return True 

def get_all_events():
    return events 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # use apiinteg.py and authenticate user. 
        # after successful authentication set id, name, role, permissions into session
        result_json = api_integ.authenticate_user(username, password)
        result = result_json.json()
        if (result["status"] == "success"):
            session['userid'] = result["id"]
            session['username'] = result["name"]
            session['loginid'] = username
            session['roleid'] = result["roleId"]
            session['role'] = result["role"]
            session['viewevents'] = result["viewEvents"]
            session['createevent'] = result["createEvent"]
            print(session['createevent'])
            session['manageevent'] = result["manageEvent"]
            session['jwt'] = result["jwt"]
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'login_failed')

    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    current_user_role = session.get('role')
    return render_template('dashboard.html', username=session.get('username'), role=current_user_role)

@app.route('/view_events')
def view_events():
    current_user_role = session.get('role')
    
    #role: 
    #if current_user_role and roles[current_user_role]['can_view_events']:
    if session['viewevents'] == True:
        # use apiinteg.py and get events from java api
        get_events_result_json = api_integ.get_events(session["userid"], session["roleid"], session["jwt"])
        result = get_events_result_json.json()
        print(result)
        data_type = type(result).__name__
        if data_type == "list":
            events = result
        '''
        events_data = get_all_events()  
        events = []
        for event in events_data:
            event_info = {
                'name': event.get('name', 'N/A'),
                'event_date': event.get('event_date', 'Not set'),
                'start_time': event.get('start_time', 'Not set'),  
                'end_time': event.get('end_time', 'Not set'),      
                'room_name': event.get('room_name', 'Not assigned'),
                'status': event.get('status', 'Unknown')
            }
            events.append(event_info)
            '''
        
        return render_template('view_events.html', events=events)
    else:
        flash('You do not have permission to view events.', 'danger')
        return redirect(url_for('dashboard'))


from datetime import datetime
from flask import flash, redirect, render_template, request, session, url_for

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    #current_user_role = session.get('role')  
    form = CreateEventForm()  

    #if current_user_role and roles[current_user_role]['can_create_events']:
    if session['role'] == 'club_user' and session['createevent'] == True:
        if request.method == 'POST':
            event_name = form.event_name.data
            event_description = form.event_description.data
            expected_attendance = form.expected_attendance.data
            event_date_str = form.event_date.data
            start_time_str = form.start_time.data
            end_time_str = form.end_time.data

            # Validate expected attendance
            try:
                expected_attendance = int(expected_attendance) if expected_attendance else 0
            except (ValueError, TypeError):
                flash('Expected attendance must be a valid number.', 'danger')
                return redirect(url_for('create_event'))

            # Validate and parse the event date
            try:
                event_date = datetime.strptime(event_date_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid event date format. Use YYYY-MM-DD.', 'danger')
                return redirect(url_for('create_event'))

            # Validate and parse start and end times
            try:
                start_time = datetime.strptime(start_time_str, '%H:%M').time()
                end_time = datetime.strptime(end_time_str, '%H:%M').time()
            except ValueError:
                flash('Invalid time format. Use HH:MM.', 'danger')
                return redirect(url_for('create_event'))

            # Check if end_time is after start_time
            if start_time >= end_time:
                flash('End time must be after start time.', 'danger')
                return redirect(url_for('create_event'))
            
            # Check room availability, use ApiInteg.py and get avaialble rooms
            available_rooms_result_json = api_integ.get_available_rooms(event_date, start_time, end_time, expected_attendance, session.get("jwt"))
            available_rooms = available_rooms_result_json.json()
            data_type = type(available_rooms).__name__
            if data_type == "dict" and "errorCode" in available_rooms.keys():
                if(available_rooms["errorCode"] == "NO_DATA_FOUND"):
                    flash('No available rooms found for the expected attendance on the selected date and time.', 'danger')
                    return redirect(url_for('create_event'))
            else:
                return render_template('select_room.html', rooms=available_rooms, 
                                       event_name=event_name, event_description=event_description,
                                       expected_attendance=expected_attendance,
                                       event_date=event_date, start_time=start_time, end_time=end_time)
                
            '''
            available_rooms = []
            for room in rooms:
                room_capacity = room.get('capacity')
                if room_capacity is not None and room_capacity >= expected_attendance:
                    if check_room_availability(room['name'], event_date, start_time, end_time):
                        available_rooms.append(room)
            
            if available_rooms:
                return render_template('select_room.html', rooms=available_rooms, 
                                       event_name=event_name, event_description=event_description,
                                       expected_attendance=expected_attendance,
                                       event_date=event_date, start_time=start_time, end_time=end_time)
            else:
                flash('No available rooms found for the expected attendance on the selected date and time.', 'danger')
                return redirect(url_for('create_event'))
            '''
        return render_template('create_event.html', form=form)
    else:
        flash('You do not have permission to create events.', 'danger')
        return redirect(url_for('dashboard'))


@app.route('/confirm_event', methods=['POST'])
def confirm_event():
    #current_user_role = session.get('role')

    #if current_user_role and roles[current_user_role]['can_create_events']:
    if session['role'] == 'club_user' and session['createevent'] == True:
        room_id = request.form.get('room_id')  

        if room_id is None:
            flash('No room selected. Please select a room.', 'danger')
            return redirect(url_for('create_event'))

        print(f"Received room_id: {room_id}")

        selected_room = next((room for room in rooms if room['id'] == room_id), None)

        if selected_room is None:
            print(f"Selected room not found for room_id: {room_id}. Available rooms: {rooms}")
            flash('Invalid room selected. Please try again.', 'danger')
            return redirect(url_for('create_event'))  

        event_name = request.form.get('event_name')
        event_description = request.form.get('event_description')
        expected_attendance = request.form.get('expected_attendance')
        event_date = request.form.get('event_date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')

        print(f"Creating event: {event_name}, {event_description}, {expected_attendance}, {event_date}, {start_time}, {end_time}")
        #use apiinteg.py and save event
        create_event_result_json = api_integ.create_event(event_name ,
                                                          event_description,
                                                          event_date,
                                                          start_time,
                                                          end_time, 
                                                          expected_attendance, 
                                                          session["userid"], 
                                                          room_id, 
                                                          session["jwt"])
        result = create_event_result_json.json()
        if result["status"] == 'success':
            flash(f'Event "{event_name}" confirmed with room "{selected_room["name"]}" and submitted for approval.', 'success')
        else:
            flash('Event creation failed', 'danger')

        '''
        new_event = {
            'name': event_name,
            'description': event_description,
            'expected_attendance': expected_attendance,
            'event_date': event_date,
            'start_time': start_time,
            'end_time': end_time,
            'room_id': room_id,  
            'room_name': selected_room['name'],  
            'approved_by': 'admin2',  
            'status': 'Pending', 
        }

        events.append(new_event) 
        '''
        #use apiinteg.py and get events
        #get_events_result_json = api_integ.get_events(session["userid"], session["roleid"], session["jwt"])
        #events = get_events_result_json.json()

        return redirect(url_for('view_events'))  
    else:
        flash('You do not have permission to confirm events.', 'danger')
        return redirect(url_for('dashboard'))  

@app.route('/approve_event/<int:event_id>', methods=['POST'])
def approve_event(event_id):
    current_user_role = session.get('role')

    if current_user_role == 'approval_admin':
        '''if 0 <= event_id < len(events):
            event_to_approve = events[event_id]  
            event_to_approve['status'] = 'Approved'
            event_to_approve['approved_by'] = session.get('username')  
            flash(f'Event "{event_to_approve["name"]}" approved successfully!', 'success')
        else:
            flash('Event not found.', 'danger')
            '''
        manage_result_json = api_integ.manage_event(event_id,session["userid"], "Approved", session.get("jwt"))
        
    else:
        flash('You do not have permission to approve events.', 'danger')
        
        


    return redirect(url_for('view_events'))

@app.route('/reject_event/<int:event_id>', methods=['POST'])
def reject_event(event_id):
    current_user_role = session.get('role')

    if current_user_role == 'approval_admin':
        '''
        if 0 <= event_index < len(events):
            event_to_reject = events[event_index]  
            event_to_reject['status'] = 'Rejected'
            event_to_reject['approved_by'] = session.get('username')  
            flash(f'Event "{event_to_reject["name"]}" rejected successfully!', 'danger')
        else:
            flash('Event not found.', 'danger')
        '''
        manage_result_json = api_integ.manage_event(event_id, session["userid"] ,"Rejected", session.get("jwt"))
    else:
        flash('You do not have permission to reject events.', 'danger')
    

    return redirect(url_for('view_events'))

    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


