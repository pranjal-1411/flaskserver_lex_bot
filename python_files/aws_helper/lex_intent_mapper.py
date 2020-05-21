import requests   
import logging
import python_files.slack.slack_helper as slack_helper
import python_files.slack.slack_intent_action as slack_intent_action

def _main_map_lex_intent( lex_response , query =None, source = None,turn_context=None )->dict:
    
    if source == 'slack':
        if query is None : return {}
        return slack_intent( lex_response,query )
    
    if source == 'ms':
        return ms_intent(lex_response,turn_context)
    return {}          

def slack_intent( lex_response , query ):
    intentName =  'ApplyLeave' #lex_response['intentName']
    logging.error(f'Intent Name is {intentName}')
    
    
    if intentName == 'ApplyLeave':
        slack_intent_action.apply_leave(query)
        response = {"ignoreLex":True}
        return response   
    return {}

def ms_intent(lex_response,turn_context):
    intentName =lex_response['intentName']
    
    if intentName == 'ApplyLeave':
        return {"ignoreLex":True,'intent':'ApplyLeave'}
    
    return {}
        
if __name__ == "__main__":
    slack_intent("attendanceClockIn",None)  
    
      
