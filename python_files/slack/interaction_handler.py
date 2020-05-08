import python_files.slack.slack_helper as slack
from flask import Response
import logging
import requests
from  python_files.aws_helper.lex_helper import sendSlotValuesToLex 


def handle_interaction_main( payload ):
    
    block_id = payload['message']['blocks'][0]['block_id']
    if block_id == 'ApplyLeave':
        return interaction_apply_leave(payload)
    
    return Response(status=200)


def interaction_apply_leave(payload):
    
    channel_id = payload['container']['channel_id']
    
    
    ts =payload['container']['message_ts']
    action = payload['actions'][0] 
    #logging.error(f'------ ts previous {action["action_ts"]}')
    blocks = payload['message']['blocks']
 
    if action['block_id']=='submit' and action['value'] == 'cancel':
        slack.update_slack_message(channel_id,ts,text="Cancelled leave application" )
        return Response(status=200)
    
    if action['block_id']=='submit' and action['value']=='submit':
        leave_type = blocks[1]['accessory']['placeholder']['text']
        start_date = blocks[2]['accessory']['initial_date']
        end_date = blocks[3]['accessory']['initial_date']
        policy_id = payload['message']['text']
        response = send_leave_request_to_asanify(channel_id,start_date,end_date,policy_id,leave_type)
        slack.update_slack_message(channel_id,ts,text=response)
        return Response(status=200)
    
       
    
    slot_key = action['block_id']
    slot_value = None
    if action['type']=='static_select':
        #blocks[ind]['accessory']["placeholder"] = action['selected_option']['text']
        slot_value = action['selected_option']['value']
    if action['type']=='datepicker':
        slot_value = action['selected_date']
    #slack.update_slack_message(channel_id,ts,text=text ,blocks=blocks)
    intentName = 'addExpense'
    received_data = { slot_key:slot_value  }
    logging.error( received_data )
    response = sendSlotValuesToLex(received_data,intentName=intentName,sender_id=channel_id)
    return Response(status=200)
    
    
    
    return Response(status=200)

def send_leave_request_to_asanify(emp_code,frm_date,to_date,policy_id,policy_name):
    
    #url ="https://71f345c7-e619-4430-8261-a751682c1e51.mock.pstmn.io/api/leave/request"
    url = "https://24ac1a95-f9f1-40b1-88b0-399710d4da94.mock.pstmn.io/api/leave/request"
    js ={
        "ASAN_EMPCODE":emp_code,
        "FROM_DATE":frm_date,
        "TO_DATE":to_date,
        "POLICY_ID":policy_id,
        "NOTE":"Note",
        "ADDITIONAL_RECIPIENTS":""
    }
    logging.error(f'Sent request {emp_code} {frm_date} {policy_id} {policy_name}')
    response = requests.post(url=url,json=js)
    
    if response.status_code == 200:
        return f'Successfully applied for leave under category {policy_name} leave from {frm_date} to {to_date}'
    else:
        return response.json()['msg']