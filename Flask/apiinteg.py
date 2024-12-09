import requests

class ApiIntegration:

    #api_endpoint = "http://localhost:8888/event"

    def authenticate_user(login_id, password):
        # append authenticate
        api_endpoint = "http://localhost:8888/event"
        authenticate_url = api_endpoint + '/authenticate'
        # create json
        # post json to api endpoint
        
        login_request_json = F'"loginId":"{login_id}", "password":"{password}"' 
        login_request_json = '{'+ login_request_json +'}'
        
        headers = {
            #"Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "Content-Type": "application/json"
        }
        response = requests.post(authenticate_url, data=login_request_json, headers=headers)
        return response

    def get_available_rooms(event_date, start_time, end_time, capacity, jwt):
        # append availablerooms
        api_endpoint = "http://localhost:8888/event"
        available_rooms_url = api_endpoint + '/rooms/available'
        # post json to api endpoint
        available_rooms_request_json = F'"eventDate":"{event_date}", "startTime":"{start_time}", "endTime":"{end_time}", "capacity":"{capacity}"'
        available_rooms_request_json = '{'+ available_rooms_request_json +'}'
        headers = {
            "Authorization": jwt,
            "Content-Type": "application/json"
        }
        
        response = requests.post(available_rooms_url, data=available_rooms_request_json, headers=headers)
        return response

    def create_event(event_name, event_desc, event_date, start_time, end_time, expected_attendance, user_id, room_id, jwt):
        # append createevent
        api_endpoint = "http://localhost:8888/event"
        create_event_url = api_endpoint + '/create'
        # post json to api endpoint
        create_event_request_json = F'"name":"{event_name}", "description":"{event_desc}", "date":"{event_date}", "startTime":"{start_time}", "endTime":"{end_time}", "expectedStrength":"{expected_attendance}", "bookingStatus":"Pending", "userId":"{user_id}", "roomId":"{room_id}"'
        create_event_request_json = '{'+ create_event_request_json +'}'
        headers = {
            "Authorization": jwt,
            "Content-Type": "application/json"
        }
        print(create_event_request_json)
        response = requests.post(create_event_url, data=create_event_request_json, headers=headers)
        return response

    def get_events(user_id, role_id, jwt):
        # append events
        api_endpoint = "http://localhost:8888/event"
        #get_events_url = 'api_endpoint + "/events/user/{userId}/role/{roleId}'
        #get_events_url = get_events_url.replace("{userId}", user_id)
        #get_events_url = get_events_url.replace("{roleId}", role_id)
        # post json to api endpoint
        get_events_url = F'/events/user/{user_id}/role/{role_id}'
        get_events_url = api_endpoint + get_events_url
        headers = {
            "Authorization": jwt,
            "Content-Type": "application/json"
        }
        response = requests.get(get_events_url, headers=headers)
        return response

    def manage_event(event_id, user_id, status,jwt):
        # append createevent
        api_endpoint = "http://localhost:8888/event"
        manage_event_url = api_endpoint + '/manage'     # api end point
        # post json to api endpoint
        headers = {
            "Authorization": jwt,
            "Content-Type": "application/json"
        }
        print(manage_event_url)
        manage_event_request_json = F'"eventId":{event_id}, "status":"{status}", "approvedBy":{user_id}'
        manage_event_request_json = '{'+ manage_event_request_json +'}'
        print(manage_event_request_json)

        response = requests.post(manage_event_url, data=manage_event_request_json,headers=headers)
        return response.json
    
    
