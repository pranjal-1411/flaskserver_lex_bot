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
    
    
    #reimplement this part..... do slot filling
    
    return Response(status=200)