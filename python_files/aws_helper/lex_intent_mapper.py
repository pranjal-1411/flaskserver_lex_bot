import requests   
import logging
import python_files.slack.slack_helper as slack_helper

def _main_map_lex_intent( intentName , query =None, source = None ):
    if query is None : return
    if source == 'slack':
        slack_intent( intentName,query )
             

def slack_intent( intentName , query ):
    
    intent_list = [ "attendanceClockIn","attendanceClockOut" ]
    if intentName not in intent_list:
        return 
    logging.info( f'Intent Mapped is {intentName}' )
    workspace_id = query['team_id'] #"T011BCF0TRD" for checkbot in pranjal ws
    user_id = query['event']['user'] #"U010TRDA89Y"
    user_info = slack_helper.get_user_info( user_id,workspace_id )
    if user_info is None :
        return
    
    email = user_info['profile']['email']
    js = {
    "workspace_id":workspace_id,
    "email":email
    }
    if intentName=='attendanceClockIn':
        js["clock_type"] = "IN"
    if intentName=='attendanceClockOut':
        js["clock_type"] = "OUT" 
    logging.info(js)
    url = "https://api.asanify.com/api/attendance/slack/dev/clock"
    response = requests.post(url,json = js)                     
    
    
if __name__ == "__main__":
    slack_intent("attendanceClockIn",None)  
    
      
# url = "https://api.asanify.com/api/attendance/slack/dev/clock"

# js = {
# "workspace_id":"ABCD",
# "email":"check@gmail.com",
# "clock_type":"IN"
# }
# response = requests.post(url,json = js)
# print(response.headers)                         
# print(response.json()['success'])     