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
    intentName = lex_response.get('intentName') 
    if intentName == 'ApplyLeave':
        slack_intent_action.apply_leave(query)
        response = {"ignoreLex":True}
        return response
    
    return {}    
    
    
if __name__ == "__main__":
    slack_intent("attendanceClockIn",None)  
    
