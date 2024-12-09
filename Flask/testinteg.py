import json
import apiinteg

api_integ = apiinteg.ApiIntegration

#test rooms available
'''
jwt = "TBD"
available_rooms_result_json = api_integ.get_available_rooms("2024-11-20","10.30","11.30", 11, jwt)
result = available_rooms_result_json.json()
print(type(result).__name__)
if type(result).__name__ =="dict" and "errorCode" in result.keys():
    if(result["errorCode"] == "NO_DATA_FOUND"):
        print(result["message"])
        print(result["status"])
if type(result).__name__ == "list":
    print("data received")
'''


#test event create
'''
jwt = "TBD"
create_event_result_json = api_integ.create_event("API Test event" ,"test first evnt API", "2024-11-21","10.30","11.30", 112, 1, 1, jwt)
result = create_event_result_json.json()
print(result)
print('done')
'''
#test get events

jwt = "TBD"
get_events_result_json = api_integ.get_events(1, 1, jwt)
result = get_events_result_json.json()
print(result)
print('done')



#test authentication
'''
result_json = api_integ.authenticate_user("clubuser1","clubuser1")
#result_json = '{"error": "Invalid credentials or user not found.", "status": "failed"}'
#result_json = '{"error": "", "status": "success", "loginId": "admin", "role": "1", "name": "Admin", "createEvent": true, "viewEvents": true, "approveEvent": true}'

result = result_json.json()
print(result)
print(result["status"])

if (result["status"] == "failed"):
    print(result["error"])

if (result["status"] == "success"):
    print(result["loginId"])
    print(result["name"])
    print(result["createEvent"])
    print(result["role"])
    if result['role'] == 'club_user':
        print('role -> club_user')
    if result['createEvent'] == True:
        print('createEvent -> true')
'''