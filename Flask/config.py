class Config:
    SECRET_KEY = '143589'  

def get_rooms():
    return [
        {"id": '1',"name": "ECR 1", "type": "Classroom", "capacity": 120, "location": "Ecole Central School of Engineering", "floor": "Ground Floor"},
        {"id": '2',"name": "ECR 2", "type": "Classroom", "capacity": 120, "location": "Ecole Central School of Engineering", "floor": "Ground Floor"},
        {"id": '3',"name": "ECR 3", "type": "Classroom", "capacity": 60, "location": "Ecole Central School of Engineering", "floor": "Ground Floor"},
        {"id": '4',"name": "ECR 4", "type": "Classroom", "capacity": 120, "location": "Ecole Central School of Engineering", "floor": "Ground Floor"},
        {"id": '5',"name": "ECR 5", "type": "Classroom", "capacity": 120, "location": "Ecole Central School of Engineering", "floor": "Ground Floor"},
        {"id": '6',"name": "ECR 6", "type": "Classroom", "capacity": 60, "location": "Ecole Central School of Engineering", "floor": "Ground Floor"},
        {"id": '7',"name": "ELT 1", "type": "Lecture Hall", "capacity": 250, "location": "Ecole Central School of Engineering", "floor": "Ground Floor"},
        {"id": '8',"name": "ELT 2", "type": "Lecture Hall", "capacity": 250, "location": "Ecole Central School of Engineering", "floor": "Ground Floor"},
        {"id": '9',"name": "Courtyard Stage", "type": "Event Stage", "capacity": None, "location": "Ecole Central School of Engineering Courtyard", "floor": "Ground Floor"},
        {"id": '10',"name": "APJ Abdul Kalam Auditorium", "type": "Auditorium", "capacity": 1100, "location": "Ecole Central School of Engineering", "floor": "Ground Floor"},
        {"id": '11',"name": "Convention Center", "type": "Convention Hall", "capacity": 600, "location": "Convention Center", "floor": "Ground Floor"},
        {"id": '12',"name": "SOL SOM Stage/Courtyard", "type": "Event Stage", "capacity": None, "location": "School of Management and School of Law Courtyard", "floor": "Ground Floor"},
        {"id": '13',"name": "ECR 7", "type": "Classroom", "capacity": 120, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '14',"name": "ECR 8", "type": "Classroom", "capacity": 60, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '15',"name": "ECR 9", "type": "Classroom", "capacity": 120, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '16',"name": "ECR 10", "type": "Classroom", "capacity": 60, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '17',"name": "ECR 11", "type": "Classroom", "capacity": 120, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '18',"name": "ECR 12", "type": "Classroom", "capacity": 60, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '19',"name": "ECR 13", "type": "Classroom", "capacity": 120, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '20',"name": "ECR 14", "type": "Classroom", "capacity": 60, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '21',"name": "ECR 15", "type": "Classroom", "capacity": 120, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '22',"name": "ECR 16", "type": "Classroom", "capacity": 120, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '23',"name": "ETR 3", "type": "Tutorial Room", "capacity": 20, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '24',"name": "ETR 4", "type": "Tutorial Room", "capacity": 20, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '25',"name": "ETR 5", "type": "Tutorial Room", "capacity": 20, "location": "Ecole Central School of Engineering", "floor": "First Floor"},
        {"id": '26',"name": "ELT 3", "type": "Lecture Hall", "capacity": 250, "location": "Ecole Central School of Engineering", "floor": "Second Floor"},
        {"id": '27',"name": "ELT 4", "type": "Lecture Hall", "capacity": 250, "location": "Ecole Central School of Engineering", "floor": "Second Floor"},
        {"id": '28',"name": "ELT 5", "type": "Lecture Hall", "capacity": 250, "location": "Ecole Central School of Engineering", "floor": "Second Floor"},
        {"id": '29',"name": "ELT 6", "type": "Lecture Hall", "capacity": 250, "location": "Ecole Central School of Engineering", "floor": "Second Floor"},
        {"id": '30',"name": "ELT 7", "type": "Lecture Hall", "capacity": 250, "location": "Ecole Central School of Engineering", "floor": "Second Floor"},
        {"id": '31',"name": "ECR 17", "type": "Classroom", "capacity": 60, "location": "Ecole Central School of Engineering", "floor": "Second Floor"},
        {"id": '32',"name": "ECR 18", "type": "Classroom", "capacity": 60, "location": "Ecole Central School of Engineering", "floor": "Second Floor"},
        {"id": '33',"name": "ETR 6", "type": "Tutorial Room", "capacity": 20, "location": "Ecole Central School of Engineering", "floor": "Second Floor"},
        {"id": '34',"name": "ETR 7", "type": "Tutorial Room", "capacity": 20, "location": "Ecole Central School of Engineering", "floor": "Second Floor"},
        {"id": '35',"name": "ETR 8", "type": "Tutorial Room", "capacity": 20, "location": "Ecole Central School of Engineering", "floor": "Second Floor"},
    ]

def get_sample_users():
    return {
        'admin1': {'password': 'admin1pass', 'role': 'super_admin'},
        'admin2': {'password': 'admin2pass', 'role': 'approval_admin'},
        'room_admin_user': {'password': 'roomadminpass', 'role': 'room_admin'},
        'club_user1': {'password': 'clubuser1pass', 'role': 'club_user'},
    }
