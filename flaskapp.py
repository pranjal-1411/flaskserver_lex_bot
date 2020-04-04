from flask import Flask, render_template, request,Response,jsonify
import json
import python_files.slack_helper as slack
from python_files.main import generateResponse
import sys
import os

# Elastic Beanstalk initalization
app = Flask(__name__)
app.debug=True


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
    rootDir = app.root_path
    senderId = request.form['userId']
    text = request.form.get('text')
   
    if request.files:
        files_dict = request.files.to_dict()
        for fileName,fileObject in files_dict.items():
            filePath = os.path.join(rootDir,'processedAttachment', fileName)
            fileObject.save(filePath)
            fileType = 'image'
            if fileObject.content_type.find('application') != -1:
                fileType = 'file'
            message = createMessageDict( senderId, text,has_attachment=True,attach_path=filePath,attach_type=fileType )
    else:
        message = createMessageDict( senderId,text )
                   
    return jsonify(generateResponse( message,rootDir ))      
 

@app.route('/slack', methods=['POST'])
def slack_route():
    # to do  ---- check for request authenticity 
    rootDir = app.root_path
    query = request.json 
    #print(query)
    if query['type'] == 'url_verification' :
        return query.get('challenge')
    
    if query['type']=='event_callback':
        print(query)
        message = None 
        lexResponse = None
        event = query['event']
        
        if event['channel_type'] != 'im':
            return Response()
        
        channelId = event['channel']
        
        if event.get('subtype') and event['subtype'] =='file_share':
           
            for File in event['files']:
                downloadPath = os.path.join(rootDir,'processedAttachment', File['name'])
                slack.downloadFile(File['name'],File['url_private'],File['filetype'],downloadPath) ; 
                #slack.send_message('Bot received '+ File['name'],channelId )
                message = createMessageDict(channelId,None,has_attachment=True,attach_path=downloadPath,attach_type=File['filetype'])
                
            lexResponse =  generateResponse(message,rootDir)
        
        if event['type'] == 'message' and event.get('blocks') :
            text = event['blocks'][0]['elements'][0]['elements'][0]['text']
            if event['blocks'][0]['elements'][0]['elements'][0]['type']=='text':
                print(text,'-------------')
                #slack.send_message( channelId,'Bot received '+ text )
                message = createMessageDict(channelId,text)

            lexResponse =  generateResponse(message,rootDir)
        
        if lexResponse:
            for message in lexResponse['messages']:
                slack.send_message( channelId, message['text'] )
                
        
    #print(request.json)    
    return Response() 
    

def createMessageDict(senderId , text , has_attachment=False, attach_path=None,attach_type=None   ):
    
    message = {} 
    message[ 'sender' ] = { 'id': senderId  } 
    message[ 'message'] = {
        'text' : text
    }
    
    if has_attachment:
       message['message']['attachment'] = {}
       message['message']['attachment']['path'] = attach_path
       message['message']['attachment']['type'] = attach_type

    return message


 
if __name__ == '__main__':
    app.run()
