import os
from slackclient import SlackClient
import requests 
from python_files.aws_helper.lex_helper import createMessageDict,generateResponse
from flask import Response
import json
import logging
import csv

import hmac
import hashlib
import base64
import time
import binascii


def get_auth_token( temp_response_code ):
    
    slack_client = SlackClient(os.getenv("SLACK_TOKEN"))
    auth_response = slack_client.api_call("oauth.v2.access",
                client_id=os.getenv("CLIENT_ID"),
                client_secret=os.getenv("CLIENT_SECRET"),
                code=temp_response_code)
    logging.info(auth_response)
    
    if auth_response["ok"] is False:
        logging.error(f'Error during authentication: {auth_response}')
        return False
    logging.info(f'Auth successful {auth_response}' )
    access_token = auth_response['access_token']
    team_id = auth_response["team"]["id"]
    path_to_oauth_file = os.path.join(os.getenv('ROOT_PATH'),"python_files","slack","slack_oauth.csv")
    
    with open(path_to_oauth_file, "a") as auth_csv:
        auth_csv.write(f'{team_id},{access_token}')
        
    return True    
   
def verify_slack_request( request ):
    key = os.getenv('SLACK_SIGNING_SECRET')
    byte_key = binascii.unhexlify(key)
    timestamp = request.headers['X-Slack-Request-Timestamp']
    if abs(time.time()-int(timestamp)) > 60*5 :
        return False 
    req = str.encode('v0:' + str(timestamp) + ':') + request.get_data()
    my_signature = 'v0=' + hmac.new(
        str.encode(key),
        req, hashlib.sha256
    ).hexdigest()
    
    slack_signature = request.headers['X-Slack-Signature']
    return hmac.compare_digest( my_signature,slack_signature )
     

def check_event( event ):
    if event.get('channel_type') and event['channel_type'] != 'im':
        return False
        
    if event.get('subtype') and event['subtype'] =='bot_message':
        return False
    
    return True

def _main_process_slack_event(query,rootDir):
    event = query['event']
    team_id = query["team_id"]
    access_token = find_access_token(team_id)
    
    if event['type'] == "app_home_opened":
        publish_home_page( event['user'],access_token )
        return 
    
    message = None 
    lexResponse = None
    
    if check_event(event) is False:
        return 
    
    channelId = event['channel']
    if event.get('subtype') and event['subtype'] =='file_share':
        
        for File in event['files']:
            downloadPath = os.path.join(rootDir,'processedAttachment', File['name'])
            downloadFile(File['name'],File['url_private'],File['filetype'],downloadPath) ; 
            #slack.send_message('Bot received '+ File['name'],channelId )
            message = createMessageDict(channelId,None,has_attachment=True,attach_path=downloadPath,attach_type=File['filetype'])   
        lexResponse =  generateResponse(message,rootDir,query,"slack")
    
    if event['type'] == 'message' and event.get('blocks') :
        text = event['blocks'][0]['elements'][0]['elements'][0]['text']
        if event['blocks'][0]['elements'][0]['elements'][0]['type']=='text':
            logging.info( f'Text received from slack is {text}' )
            #slack.send_message( channelId,'Bot received '+ text )
            message = createMessageDict(channelId,text)
        lexResponse =  generateResponse(message,rootDir,query,"slack")
    
    if lexResponse:
        for message in lexResponse['messages']:
            send_message_to_slack( channelId, message['text'],access_token )

def find_access_token( team_id ):
    #os.environ['ROOT_PATH'] = "/mnt/f/python3resolve" 
    path_to_oauth_file = os.path.join(os.getenv('ROOT_PATH'),"python_files","slack","slack_oauth.csv")
    with open(path_to_oauth_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if len(row) ==0 :
                continue 
            if row[0] == team_id:
                logging.error(row[1])
                return row[1]
        
    return None 

def publish_home_page( user_id,access_token=None ):
    if access_token is None:
        access_token = os.getenv("SLACK_TOKEN")
    slack_client = SlackClient(access_token)
    response = slack_client.api_call(
        "views.publish",
        user_id=user_id,
        view={
   "type":"home",
   "blocks":[
      {
         "type":"section",
         "text":{
            "type":"mrkdwn",
            "text":"<https://asanify.com| Asanify> - the next gen HR & payroll tool for your business."
         }
      },
      {
         "type":"divider"
      },
      {
         "type":"context",
         "elements":[
            {
               "type":"mrkdwn",
               "text":"*About:* Asanify believes in the principles of #AWE: #Asanify, #WorkIsWonderful and #Engage which translate to simplicity, fairness and data driven transparency in today's world where most of the HR processes are complex, manual and menial which hinders business growth.\n\n Asanify solves for the above through a delightful user experience wherein the entire HR operations can be run directly on a chatbot. Additionally, Asanify provides rich set of people and behavioural insights for data driven people decisions.\n\nWe'd love to connect with any such company whose beliefs resonate with ours to explore how we can create value together."
            }
         ]
      },
      {
         "type":"divider"
      },
      {
         "type":"context",
         "elements":[
            {
               "type":"mrkdwn",
               "text":"*Features*"
            }
         ]
      },
      {
         "type":"context",
         "elements":[
            {
               "type":"mrkdwn",
               "text":"• Payroll\n• Attendance Monitoring\n• Leave Management\n• Analytics\n• Tax Savings & Investments\n • Employee Management\n• And many such HR related functionalities . . ."
            }
         ]
      },
      {
         "type":"divider"
      },
      {
         "type":"section",
         "text":{
            "type":"mrkdwn",
            "text":"Login to Asanify for more"
         },
         "accessory":{
            "type":"button",
            "text":{
               "type":"plain_text",
               "text":"Login",
               "emoji":True
            },
            "url":"https://asanify.com/Auth/Login"
         }
      },
      {
         "type":"divider"
      },
      {
         "type":"context",
         "elements":[
            {
               "type":"mrkdwn",
               "text":"_By using this app you agree to our terms and policies_"
            }
         ]
      },
      {
         "type":"context",
         "elements":[
            {
               "type":"mrkdwn",
               "text":"<https://asanify.com/Privacy | Privacy Policy>"
            },
            {
               "type":"mrkdwn",
               "text":"<https://asanify.com/Terms | Terms & Conditions>"
            },
            {
               "type":"mrkdwn",
               "text":"<https://asanify.com/Cancellation | Cancellation & Refund Policy>"
            }
         ]
      }
   ]
}
    )
    

    
    
def send_message_to_slack(channel_id, message,access_token=None):
    
    if access_token is None:
        access_token = os.getenv("SLACK_TOKEN")
    slack_client = SlackClient(access_token)

    response = slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='Asanifybot',
        icon_emoji=':robot_face:'
    )

    logging.info( f'Response from slack.post api is {response } '  )
    
def get_user_info( user_id, workspace_id ):
    access_token = find_access_token(workspace_id)
    if access_token is None:
        access_token = os.getenv("SLACK_TOKEN")
    slack_client = SlackClient(token= access_token)
    response = slack_client.api_call(
        method = "users.info",
        user=user_id
    )
    
    if not response['ok']:
        logging.error( "Unable to retrieve user info" )
        logging.error(response)
        return None   

    return response['user']

def downloadFile( fileName , fileUrl , extension ,  downloadPath , access_token=None):
    
    logging.info(fileUrl)
    if access_token is None:
        access_token = os.getenv('SLACK_TOKEN')
    r = requests.get(fileUrl, headers={'Authorization': 'Bearer %s' % access_token}) 
 
    
    if r.status_code != 200:
        logging.error('File Download Error ') 
        return 
    
    with open(downloadPath,'wb') as f: 
        f.write(r.content) 


if __name__ == '__main__':
    #send_message_to_slack("D011M87PWG3","just keep trying")
    slack_client = SlackClient(token= "xoxb-1045423027863-1055279789379-m1DsGB0mO0dzboVxgntMm1Du")
    #slack_client.api_call("auth_test", json = {})
    # params = {'channel':channel_id,
    #     'text':message,
    #     'username':'Asanifybot',
    #     'icon_emoji':':robot_face:' }
    # res =requests.post( url='https://slack.com/api/chat.postMessage',data=params,headers={'Authorization': f'Bearer {SLACK_TOKEN}'} )
    # print(res.json)
    #logging.error( f' res is {res} ' )
    response = slack_client.api_call(
        method = "users.info",
        user="U011L9L5T4J"
    )

    logging.error( f'Response from slack.post api is {response } '  )

# pRANJAL ALTER IN SACHIN WORK "U011CEW3XTR"
# PRANJAL IN SACHIN WORK "U011L9L5T4J"
#xoxp-1045423027863-1054326197154-1046494602007-f91b2e3ef505a9bf9221ae647398e7dd
#D011L9L6Q58