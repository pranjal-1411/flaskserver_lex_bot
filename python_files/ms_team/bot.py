# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import asyncio
from botbuilder.core import ActivityHandler, TurnContext,MessageFactory,CardFactory
from botbuilder.core.teams import TeamsInfo
from botbuilder.schema import ChannelAccount,SuggestedActions,CardAction,ActionTypes,Activity,ActivityTypes,Attachment
import python_files.aws_helper.lex_helper as lex_helper
import logging
import python_files.ms_team.interaction_handler as interaction_handler
import os
import json
import python_files.ms_team.ms_intent_action as ms_intent_action
CARDS = ["/python_files/ms_team/temp2.json"]

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    
    
    
    async def on_message_activity(self, turn_context: TurnContext):
        
        member_id =turn_context.activity.recipient.id
        if turn_context.activity.text is not None:
            text = turn_context.activity.text
            message = lex_helper.createMessageDict(member_id,text)
            #await turn_context.send_activity(f'Hi hardcoded')
            lexResponse = lex_helper.generateResponse(message,None,None,'ms',turn_context)
           
            if lexResponse:
                if lexResponse.get('intent'):
                    await ms_intent_action.process_intent(lexResponse['intent'],turn_context)
                for message in lexResponse['messages']:
                    await turn_context.send_activity(message['text'])
        elif turn_context.activity.value is not None:
            await interaction_handler.handle_interaction( turn_context )

             
            
            
                    
        
        
        
        #await temp(turn_context)
    
        

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")



async def temp( turn_context:TurnContext ):
    await turn_context.send_activity("This shit works")

def create_adaptive_card_attachment(intent_name,card_name) -> Attachment:
        card_path = os.path.join( os.getenv('ROOT_PATH'),'python_files/ms_team/cards',intent_name,card_name )
        with open(card_path, "rb") as in_file:
            card_data = json.load(in_file)

        return CardFactory.adaptive_card(card_data)

#  members = await TeamsInfo.get_team_members(turn_context)
#         #
#         for item in members:
#             logging.error(item.email)

# member = await TeamsInfo.get_member(turn_context, turn_context.activity.from_property.id)
#         logging.error(member)