
import python_files.slack.slack_helper as slack_helper
import requests
import logging
import os
import json

sample_option = {
							"text": {
								"type": "plain_text",
								"text": "leave",
								"emoji": True
							},
							"value": "XXXX"
						}


def apply_leave(query):
    
    channel_id = query['event']['channel']
    options = [sample_option]
    
    file_path = os.path.join( os.getenv('ROOT_PATH'),'python_files/slack/blocks/apply_leave.json')
    blocks = None
    
    with open(file_path,'r') as block_json:
        blocks = json.load(block_json)
    blocks[1]['accessory']['options'] = options    
    access_token =None #slack_helper.find_access_token(query['team_id'])
    slack_helper.send_message_to_slack(channel_id,blocks=blocks,access_token=access_token)
   
    