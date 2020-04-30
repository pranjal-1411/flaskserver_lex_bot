import requests   
import logging
import python_files.slack.slack_helper as slack_helper
import python_files.slack.slack_intent_action as slack_intent_action

def _main_map_lex_intent( lex_response , query =None, source = None ):
    if query is None : return {}
    if lex_response.get('dialogState') != 'Fulfilled': return {}
    if source == 'slack':
        return slack_intent( lex_response,query )
             

def slack_intent( lex_response , query ):
    intentName ='ApplyLeave' #lex_response['intentName']
    # logging.error("Successful ------------------------- ")
    # # response = {
    # #     "ignoreLex":True,
    # #     "message":"Respose from Asanify and not from lex"
    # # }
    # # return response
    # intent_list = [ "attendanceClockIn","attendanceClockOut","ApplyLeave" ]
    # if intentName not in intent_list:
    #     response = { "ignoreLex":False } 
    #     return response
    
    if intentName == 'ApplyLeave':
        slack_intent_action.apply_leave(query)
        response = {"ignoreLex":True}
        return response
        
    
    # logging.info( f'Intent Mapped is {intentName}' )
    # workspace_id = query['team_id'] #"T011BCF0TRD" for checkbot in pranjal ws
    # user_id = query['event']['user'] #"U010TRDA89Y"
    # user_info = slack_helper.get_user_info( user_id,workspace_id )
    # if user_info is None :
    #     return
    
    # email = user_info['profile']['email']
    # js = {
    # "workspace_id":workspace_id,
    # "email":email
    # }
    # if intentName=='attendanceClockIn':
    #     js["clock_type"] = "IN"
    # if intentName=='attendanceClockOut':
    #     js["clock_type"] = "OUT" 
    # logging.info(js)
    # url = "https://api.asanify.com/api/attendance/slack/dev/clock"
    # response = requests.post(url,json = js)                     



    
    
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