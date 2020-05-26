import python_files.slack.slack_helper as slack
from flask import Response
import logging
import requests
from  python_files.aws_helper.lex_helper import sendSlotValuesToLex ,getSlotValuesFromLex
import os
import json
import python_files.asanify_server.helper as asanify_helper

def handle_interaction_main( payload ):
    
    logging.info(f'Payload is {payload}')
    if payload['type']=='block_actions':
        
        block_id = payload['message']['blocks'][0]['block_id']
        if block_id == 'ApplyLeave':
            return initiate_apply_leave(payload)
    
    if payload['type']=='view_submission':
        which_modal = payload['view']['blocks'][0]['block_id']
        
        if which_modal=='ApplyLeave':
            return submit_apply_leave(payload)
                
    return Response(status=200)

def initiate_apply_leave(payload):
    trigger_id = payload['trigger_id']
    file_path = os.path.join( os.getenv('ROOT_PATH'),'python_files/slack/blocks/apply_leave/complete_form.json')
    view = None
    with open(file_path,'r') as view_json:
        view = json.load(view_json)
    ts = payload['container']['message_ts'] 
    channel_id = payload['container']['channel_id']
    view['callback_id'] = channel_id + "," + ts
    #view['blocks'][1]['element']['options'] = get_leave_options(channel_id)
    slack.open_modal(trigger_id,view)
    
    return Response(status=200)

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

def submit_apply_leave(payload):
    
    values = payload['view']['state']['values']
    
    leave_type = values['leave_type']['leave_type_action']['selected_option']['value']
    from_date = values['from_date']['from_date_action']['selected_date']
    to_date = values['to_date']['to_date_action']['selected_date']
    note = values['additional_note']['additional_note_action']['value']
    channel_id,ts = payload['view']['callback_id'].split(',')
    response = asanify_helper.send_leave_request_to_asanify(channel_id,from_date,to_date,leave_type)
    slack.update_slack_message(channel_id=channel_id,ts=ts,text=response)
    
    return Response(status=200)

