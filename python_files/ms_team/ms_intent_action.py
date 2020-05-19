import asyncio
from botbuilder.core import ActivityHandler, TurnContext,MessageFactory,CardFactory
from botbuilder.core.teams import TeamsInfo
from botbuilder.schema import ChannelAccount,SuggestedActions,CardAction,ActionTypes,Activity,ActivityTypes,Attachment
import python_files.ms_team.bot as ms_bot
import logging
import os
import python_files.aws_helper.lex_helper as lex_helper
import time
async def process_intent( intent_name, turn_context:TurnContext ):
    
    try:
        
        if intent_name=='ApplyLeave':
            await apply_leave(turn_context)
        return 
    except Exception as exception:
        raise exception
    

async def apply_leave(turn_context:TurnContext):
    
    #logging.error(turn_context.activity.channel_data)
    user_id = '123456'#turn_context.activity.channel_data['tenant']['id']
    
    message = Activity(
                type=ActivityTypes.message,
                attachments=[ms_bot.create_adaptive_card_attachment( intent_name="ApplyLeave",card_name='leave_type.json')],
            )
    response = await turn_context.send_activity(message)
    session_attributes = {
        'activity_id':response.id
    }
    lex_helper.sendSlotValuesToLex({},intentName='ApplyLeave',sender_id=user_id,session_attributes=session_attributes)
    


    