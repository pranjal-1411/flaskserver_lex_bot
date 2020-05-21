
import python_files.slack.slack_helper as slack_helper
import requests
import logging
import os 
import json

import python_files.asanify_server.helper as asanify_helper



def apply_leave(query):
    
    channel_id = query['event']['channel']
    options = get_leave_options( channel_id )

    file_path = os.path.join( os.getenv('ROOT_PATH'),'python_files/slack/blocks/apply_leave/initiate_button.json')
    blocks = None
    
    with open(file_path,'r') as block_json:
        blocks = json.load(block_json)
    #blocks[1]['accessory']['options'] = options    
    access_token =None #slack_helper.find_access_token(query['team_id'])
    slack_helper.send_message_to_slack(channel_id,blocks=blocks,access_token=access_token)
    
def get_leave_options( emp_code ):
    
	response = asanify_helper.get_leave_balance(emp_code)
	options = [] 
	if response.status_code==200:
		for item in response.json()['LEAVE_BALANCES']:
			leave = f'{item["POLICY_NAME"]} (Avl: {item["AVAILABLE"]})'
			sample_option = {
							"text": {
								"type": "plain_text",
								"text": leave,
								"emoji": True
							},
							"value": item["POLICY_ID"]
						}
			options.append(sample_option)

	return options
        
def attendanceClockIn(query):
    pass
def attendanceClockOut(query): 
    pass

    # workspace_id = query['team_id'] #"T011BCF0TRD" for checkbot in pranjal ws
    # user_id = query['event']['user'] #"U010TRDA89Y"
    # user_info = slack_helper.get_user_info( user_id,workspace_id )
    # if user_info is None :
    #     return
    
    # email = user_info['profile']['email']
    # js = {
    # "workspace_id":workspace_id,
    # "email":email
    # }
    # if intentName=='attendanceClockIn':
    #     js["clock_type"] = "IN"
    # if intentName=='attendanceClockOut':
    #     js["clock_type"] = "OUT" 
    # logging.info(js)
    # url = "https://api.asanify.com/api/attendance/slack/dev/clock"
    # response = requests.post(url,json = js)                     

# url = "https://api.asanify.com/api/attendance/slack/dev/clock"

# js = {
# "workspace_id":"ABCD",
# "email":"check@gmail.com",
# "clock_type":"IN"
# }
# response = requests.post(url,json = js)
# print(response.headers)                         
# print(response.json()['success'])     