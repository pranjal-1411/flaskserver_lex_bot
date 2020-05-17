# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import asyncio
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.core.teams import TeamsInfo
from botbuilder.schema import ChannelAccount
from python_files.aws_helper.lex_helper import createMessageDict,generateResponse
import logging

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        #print(turn_context.activity)
        member_id =turn_context.activity.recipient.id
        text = turn_context.activity.text
        message = createMessageDict(member_id,text)
        logging.error(turn_context.activity.id)
        #member = await TeamsInfo.get_member(turn_context, member_id)
        #
        #logging.error(member)
        await turn_context.send_activity(f'Hi hardcoded')
        await turn_context.delete_activity('1589659491674')
        # lexResponse =  generateResponse(message)
        # if lexResponse:
        #     for message in lexResponse['messages']:
        #         await turn_context.send_activity(message['text'])
        

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
