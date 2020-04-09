from flask import Flask, render_template, request,Response,jsonify
import json
import python_files.slack_helper as slack
from python_files.aws_helper.lex_helper import generateResponse,createMessageDict
from python_files.aws_helper.sns_helper import publish_message_from_slack_to_sns
import sys
import os
import requests
#from threading import Thread

import logging
logging.basicConfig( )
logging.getLogger().setLevel(logging.WARNING)

from datetime import datetime

# Elastic Beanstalk initalization
app = Flask(__name__)
app.debug=False


rootDir = app.root_path
# change this to your own value
app.secret_key = 'cC1YCIWOj9GkjbkjbkjbgWspgNEo2'   


@app.route('/test', methods=['GET','POST'])
def temp():
    return "Hello World"


@app.route('/', methods=['GET','POST'])
def index():
    '''
        
            { {
                "by":"server",
                "userId":'123',
                "text":"Hello, what would you like to do?",
                "time":"UNIX_TIMESTAMP"
                }
            }
    '''
    senderId = request.form['userId']
    text = request.form.get('text')
   
    if request.files:
        files_dict = request.files.to_dict()
        for fileName,fileObject in files_dict.items():
            filePath = os.path.join(rootDir,'processedAttachment', fileName)
            fileObject.save(filePath)
            fileType = 'image'
            if fileObject.content_type.find('application') != -1:
                fileType = 'pdf'
            message = createMessageDict( senderId, text,has_attachment=True,attach_path=filePath,attach_type=fileType )
    else:
        message = createMessageDict( senderId,text )
                   
    return jsonify(generateResponse( message,rootDir ))      
 

@app.route('/slack/events', methods=['POST'])
def slack_route():
    # to do  ---- check for request authenticity 
    
    query = request.json
    
    hdr = request.headers.get('X-Slack-Retry-Reason')
    if hdr:
        logging.info( f"Slack event timeout {hdr} " )
        return Response(status=200) 
    
    if query['type'] == 'url_verification' :
        return query.get('challenge')
    
    if query['type']=='event_callback':
       
        if slack.check_event(query['event']) is False:
            return Response(status=200)
        
        message = json.dumps(query['event'])
        publish_message_from_slack_to_sns(message,rootDir)
       
    return Response(status=200) 

@app.route('/sns', methods = ['GET', 'POST', 'PUT'])
def sns():
    # AWS sends JSON with text/plain mimetype
    try:
        js = json.loads(request.get_data())
    except:
        pass
    
    hdr = request.headers.get('X-Amz-Sns-Message-Type')
  
    if hdr == 'SubscriptionConfirmation' and 'SubscribeURL' in js:
        r = requests.get(js['SubscribeURL'])
    
    if hdr == 'Notification':
       
        message = json.loads(js['Message'])
        slack._main_process_slack_event(message,rootDir)
        #print(type(js['message']))


    return 'OK\n'
    

 
if __name__ == '__main__':
    app.run(ssl_context='adhoc')






#Thread(target= slack._main_process_slack_event , args=(query['event'],rootDir) ).start()