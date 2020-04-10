import os
from slackclient import SlackClient
import requests 
from python_files.aws_helper.lex_helper import createMessageDict,generateResponse
from flask import Response
import json
import logging


SLACK_TOKEN = os.getenv('SLACK_TOKEN')



def check_event( event ):
    if event['channel_type'] != 'im':
        return False
        
    if event.get('subtype') and event['subtype'] =='bot_message':
        return False
    
    return True

def _main_process_slack_event(event,rootDir):
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
        lexResponse =  generateResponse(message,rootDir)
    
    if event['type'] == 'message' and event.get('blocks') :
        text = event['blocks'][0]['elements'][0]['elements'][0]['text']
        if event['blocks'][0]['elements'][0]['elements'][0]['type']=='text':
            logging.info( f'Text received from slack is {text}' )
            #slack.send_message( channelId,'Bot received '+ text )
            message = createMessageDict(channelId,text)
        lexResponse =  generateResponse(message,rootDir)
    
    if lexResponse:
        for message in lexResponse['messages']:
            send_message_to_slack( channelId, message['text'] )

def send_message_to_slack(channel_id, message):
    SLACK_TOKEN = 'xoxb-1045423027863-1055819276197-M13clKAlRI2veSKHjS0mn82e'
    slack_client = SlackClient(token= SLACK_TOKEN)
    #slack_client.api_call("auth_test", json = {})
    # params = {'channel':channel_id,
    #     'text':message,
    #     'username':'Asanifybot',
    #     'icon_emoji':':robot_face:' }
    # res =requests.post( url='https://slack.com/api/chat.postMessage',data=params,headers={'Authorization': f'Bearer {SLACK_TOKEN}'} )
    # print(res.json)
    #logging.error( f' res is {res} ' )
    response = slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='Asanifybot',
        icon_emoji=':robot_face:', 
        token = f'Bearer {SLACK_TOKEN}'
    )

    logging.error( f'Response from slack.post api is {response } '  )
    

def downloadFile( fileName , fileUrl , extension ,  downloadPath):
    print(fileUrl)
    
    r = requests.get(fileUrl, headers={'Authorization': 'Bearer %s' % SLACK_TOKEN}) 
 
    
    if r.status_code != 200:
        logging.error('File Download Error ') 
        return 
    
    with open(downloadPath,'wb') as f: 
        f.write(r.content) 


if __name__ == '__main__':
    send_message_to_slack("D0112QMRSTV","just keep trying")
