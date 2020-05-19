# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import asyncio
from botbuilder.core import ActivityHandler, TurnContext,MessageFactory,CardFactory
from botbuilder.core.teams import TeamsInfo
from botbuilder.schema import ChannelAccount,SuggestedActions,CardAction,ActionTypes,Activity,ActivityTypes,Attachment
from python_files.aws_helper.lex_helper import createMessageDict,generateResponse
import logging

import os
import json


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    def __init__(self):
        super().__init__()
        self.x = True
    
    async def on_turn(self, turn_context):
        #logging.error(turn_context.activity) 
        
        async def handler(context,activities, next):
            for activity in activities:
                self.savedActivity = activity
            return await next()
        
        turn_context.on_send_activities(handler)
        
        return await super().on_turn(turn_context)
        
    
    
    
    async def on_message_activity(self, turn_context: TurnContext):
        #print(turn_context.activity)
        # member_id =turn_context.activity.recipient.id
        # text = turn_context.activity.text
        # message = createMessageDict(member_id,text)
        # await turn_context.send_activity(f'Hi hardcoded')
        #await turn_context.delete_activity('1589659491674')
        # lexResponse =  generateResponse(message)
        # if lexResponse:
        #     for message in lexResponse['messages']:
        #         await turn_context.send_activity(message['text'])
        
        
        if self.x:
            message = Activity(
                type=ActivityTypes.message,
                attachments=[self._create_adaptive_card_attachment( '/mnt/f/python3resolve/python_files/ms_team/temp2.json')],
            )

            response = await turn_context.send_activity(message)
            logging.error(response)
            self.activityToUpdateId = response.id
            self.x = False 
        else:
            card2 = self._create_adaptive_card_attachment('/mnt/f/python3resolve/python_files/ms_team/temp.json')
            message = Activity(
                type=ActivityTypes.message,
                attachments=[card2],
            )
            message.id = self.activityToUpdateId
            await turn_context.update_activity(message)
            # self.savedActivity.id = self.activityToUpdateId
            # self.savedActivity.attachments = [card2]
            # logging.error(self.savedActivity)
            #await turn_context.delete_activity(self.activityToUpdateId)
            #await turn_context.send_activity("Ahemmmmmmmmm")
            #await turn_context.send_activity(message)
            
            
        #return await turn_context.send_activity(reply)
    
    def _create_adaptive_card_attachment(self,card_path) -> Attachment:
        """
        Load a random adaptive card attachment from file.
        :return:
        """
        
        with open(card_path, "rb") as in_file:
            card_data = json.load(in_file)

        return CardFactory.adaptive_card(card_data)    

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")






#  members = await TeamsInfo.get_team_members(turn_context)
#         #
#         for item in members:
#             logging.error(item.email)

# member = await TeamsInfo.get_member(turn_context, turn_context.activity.from_property.id)
#         logging.error(member)