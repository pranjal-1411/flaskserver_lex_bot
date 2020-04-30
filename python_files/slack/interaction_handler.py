import python_files.slack.slack_helper as slack
from flask import Response
import logging
def handle_interaction_main( payload ):
    
    block_id = payload['message']['blocks'][0]['block_id']
    logging.error(block_id)
    if block_id == 'ApplyLeave':
        return interaction_apply_leave(payload)
    
    return Response(status=200)


def interaction_apply_leave(payload):
    channel_id = payload['container']['channel_id']
    ts =payload['container']['message_ts']
    action = payload['actions'][0] 
    #logging.error(payload)
    blocks = payload['message']['blocks']
    if action['block_id'] != "submit":
        ind = (int)(action['block_id'])
        if action['type']=='static_select':
            blocks[ind]['accessory']["placeholder"] = action['selected_option']['text']
        if action['type']=='datepicker':
            blocks[ind]['accessory']["initial_date"] = action['selected_date']
        slack.update_slack_message(channel_id,ts,blocks=blocks)
        return Response(status=200)
    
    if action['value'] == 'cancel':
        slack.update_slack_message(channel_id,ts,text="Cancelled leave application" )
        return Response(status=200)
    
    if action['value']=='submit':
        leave_type = blocks[1]['accessory']['placeholder']['text']
        start_date = blocks[2]['accessory']['initial_date']
        end_date = blocks[3]['accessory']['initial_date']
        text = f'Successfully applied for leave under category {leave_type} leave from {start_date} to {end_date}'
        slack.update_slack_message(channel_id,ts,text=text)
        return Response(status=200)
    
    return Response(status=200)