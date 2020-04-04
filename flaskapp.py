from flask import Flask, render_template, request
import json
from python_files.main  import generateResponse
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
    message = {} 
    message[ 'sender' ] = { 'id': request.form['userId']   } 
    message[ 'message'] = {
        'text' : request.form.get('text')
    }
    if request.files:
        message['message']['attachment'] = {}
        files_dict = request.files.to_dict()
        for fileName,fileObject in files_dict.items():
            filePath = os.path.join(rootDir,'processedAttachment', fileName)
            fileObject.save(filePath)
            message['message']['attachment']['path'] = filePath
            fileType = 'image'
            if fileObject.content_type.find('application') != -1:
                fileType = 'file'
            message['message']['attachment']['type'] = fileType 
               
    return generateResponse( message,rootDir )      
 
if __name__ == '__main__':
    app.run()
