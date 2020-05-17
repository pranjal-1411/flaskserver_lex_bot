import requests   
import logging
import python_files.slack.slack_helper as slack_helper
import python_files.slack.slack_intent_action as slack_intent_action

def _main_map_lex_intent( lex_response , query =None, source = None )->dict:
    if query is None : return {}
    if source == 'slack':
        return slack_intent( lex_response,query )
   
    return {}          

def slack_intent( lex_response , query ):
    intentName =lex_response['intentName']
    logging.error(f'Intent Name is {intentName}')
   
    
    if intentName == 'ApplyLeave':
        slack_intent_action.apply_leave(query)
        response = {"ignoreLex":True}
        return response
        
    return {}

def ms_intent(lex_response,query):
    pass
    
if __name__ == "__main__":
    slack_intent("attendanceClockIn",None)  
    
      
