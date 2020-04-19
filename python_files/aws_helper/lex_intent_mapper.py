import requests   
import logging
import python_files.slack.slack_helper as slack_helper

def _main_map_lex_intent( lex_response , query =None, source = None ):
    if query is None : return {}
    return {}
    if lex_response.get('dialogState') != 'Fulfilled': return {}
    if source == 'slack':
        return slack_intent( lex_response,query )
             

def slack_intent( lex_response , query ):
    
    logging.error("Successful ------------------------- ")
    response = {
        "ignoreLex":True,
        "message":"Respose from Asanify and not from lex"
    }
    return response
    

if __name__ == "__main__":
    slack_intent("attendanceClockIn",None)  
    
