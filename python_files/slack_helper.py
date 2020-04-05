import os
from slackclient import SlackClient
import requests 


SLACK_TOKEN = os.getenv('SLACK_TOKEN')

slack_client = SlackClient(SLACK_TOKEN)

def send_message(channel_id, message):
   
    response = slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='Asanifybot',
        icon_emoji=':robot_face:'
    )
    #print(response)

def downloadFile( fileName , fileUrl , extension ,  downloadPath):
    print(fileUrl)
    
    r = requests.get(fileUrl, headers={'Authorization': 'Bearer %s' % SLACK_TOKEN}) 
 
    
    if r.status_code != 200:
        print('File Download Error _________________________________') 
        return 
 
    with open(downloadPath,'wb') as f: 
        f.write(r.content) 


if __name__ == '__main__':
    send_message("D0112QMRSTV","just keep trying")
