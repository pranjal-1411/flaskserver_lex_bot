import asyncio
from botbuilder.core import ActivityHandler, TurnContext,MessageFactory,CardFactory
from botbuilder.core.teams import TeamsInfo
from botbuilder.schema import ChannelAccount,SuggestedActions,CardAction,ActionTypes,Activity,ActivityTypes,Attachment
import python_files.ms_team.bot as ms_bot
import logging
import os
import python_files.aws_helper.lex_helper as lex_helper
import python_files.asanify_server.helper as asanify_helper
import json


import threading
async def handle_interaction( turn_context : TurnContext ):
    
    intent = turn_context.activity.value['intent']
    
    if intent=="ApplyLeave":
        return await interaction_apply_leave(turn_context)
         
    

async def interaction_apply_leave( turn_context:TurnContext):
    
    values = turn_context.activity.value
    user_id = '123456' #turn_context.activity.channel_data['tenant']['id']
    end_form = False
    card = None
    if values["step"] == "leave_type":
        received_data = { 'leave_type':values['leave_type']  }
        logging.error( f'Received Data is {received_data}' )
        lex_helper.sendSlotValuesToLex(received_data,intentName='ApplyLeave',sender_id=user_id)
        card = ms_bot.create_adaptive_card_attachment('ApplyLeave','from_date.json')
    
    if values["step"] == "from_date":
        received_data = { 'from_date':values['from_date']  }
        logging.error( f'Received Data is {received_data}' )
        lex_helper.sendSlotValuesToLex(received_data,intentName='ApplyLeave',sender_id=user_id)
        card = ms_bot.create_adaptive_card_attachment('ApplyLeave','to_date.json')
    
    if values["step"] == "to_date":
        received_data = { 'to_date':values['to_date']  }
        logging.error( f'Received Data is {received_data}' )
        lex_helper.sendSlotValuesToLex(received_data,intentName='ApplyLeave',sender_id=user_id)
        end_form = True
        
    lex_data = lex_helper.getSlotValuesFromLex('ApplyLeave',user_id,session_attributes=True)
    
    if end_form:
        response = send_leave_data_to_asanify(user_id, lex_data['slots'] )
        card_path = os.path.join( os.getenv('ROOT_PATH'),'python_files/ms_team/cards','ApplyLeave','end_form.json' )
        with open(card_path, "rb") as in_file:
            card_data = json.load(in_file)
            card_data
        card_data["body"][2]["text"] = response
        card = CardFactory.adaptive_card(card_data) 
    
    message = Activity(
                type=ActivityTypes.message,
                attachments=[card]
            )
    logging.error(lex_data)
    session_attributes = lex_data['session_attributes']
    
    message.id = session_attributes['activity_id']
    await turn_context.update_activity( message )


def send_leave_data_to_asanify( emp_code, data ):
    
    return asanify_helper.send_leave_request_to_asanify( emp_code,data['from_date'],data['to_date'],data['leave_type'],"Sick" ) 