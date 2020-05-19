import python_files.slack.slack_helper as slack
from flask import Response
import logging
import requests
from  python_files.aws_helper.lex_helper import sendSlotValuesToLex ,getSlotValuesFromLex
import os
import json
import python_files.asanify_server.helper as asanify_helper

def handle_interaction_main( payload ):
    
    block_id = payload['message']['blocks'][0]['block_id']
    if block_id == 'ApplyLeave':
        return interaction_apply_leave(payload)
    
    return Response(status=200)


def interaction_apply_leave(payload):
    
    channel_id = payload['container']['channel_id']
    intentName = 'ApplyLeave'
    
    ts =payload['container']['message_ts']
    action = payload['actions'][0] 
    #logging.error(f'------ ts previous {action["action_ts"]}')
    blocks = payload['message']['blocks']
    
    if action['block_id']=='submit' and action['value'] == 'cancel':
        slack.update_slack_message(channel_id,ts,text="Cancelled leave application" )
        return Response(status=200)
    
    if action['block_id']=='submit' and action['value']=='submit':
        slots = getSlotValuesFromLex(intentName,channel_id)
        
        leave_id = slots['leave_type']
        fdate = slots['from_date']
        tdate = slots['to_date']
        logging.error(f'{leave_id} {fdate}  {tdate}')
        response = asanify_helper.send_leave_request_to_asanify(channel_id,fdate,tdate,leave_id)
        slack.update_slack_message(channel_id,ts,text=response)
        return Response(status=200)
    
    slot_key = action['block_id']
    slot_value = None
    blocks_path = os.path.join(os.getenv('ROOT_PATH'),'python_files/slack/blocks/apply_leave')
    new_blocks = None
    if slot_key == 'leave_type':
        slot_value = action['selected_option']['value']
        received_data = { slot_key:slot_value  }
        sendSlotValuesToLex(received_data,intentName=intentName,sender_id=channel_id)
        blocks_path = os.path.join(blocks_path,'from_date.json')
        with open(blocks_path,'r') as block_json:
            new_blocks = json.load(block_json)
    
    if slot_key == 'from_date':
        slot_value = action['selected_date']
        received_data = { slot_key:slot_value  }
        sendSlotValuesToLex(received_data,intentName=intentName,sender_id=channel_id)
        blocks_path = os.path.join(blocks_path,'to_date.json')
        with open(blocks_path,'r') as block_json:
            new_blocks = json.load(block_json)
        
        #blocks[ind]['accessory']["placeholder"] = action['selected_option']['text']
        
    if slot_key == 'to_date':
        slot_value = action['selected_date']
        received_data = { slot_key:slot_value  }
        response = sendSlotValuesToLex(received_data,intentName=intentName,sender_id=channel_id)
        blocks_path = os.path.join(blocks_path,'confirmation.json')
        with open(blocks_path,'r') as block_json:
            new_blocks = json.load(block_json)
        slots = response['slots']
        final_text = response['message']
        new_blocks[1]['text']['text'] = final_text
        
    slack.update_slack_message(channel_id,ts,text=None ,blocks=new_blocks)
    

    logging.error( received_data )
        
    
    return Response(status=200)

