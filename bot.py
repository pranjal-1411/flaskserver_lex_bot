import os
import json
from slackclient import SlackClient

CLIENT_ID = ""
CLIENT_SECRET = ""
VERIFICATION_TOKEN = ""
class Bot(object):
    def __init__(self):
        super(Bot, self).__init__()
        # When we instantiate a new bot object, we can access the app
        # credentials we set earlier in our local development environment.
        self.oauth = {"client_id": CLIENT_ID,
                      "client_secret": CLIENT_SECRET,
                      # Scopes provide and limit permissions to what our app
                      # can access. It's important to use the most restricted
                      # scope that your app will need.
                      "scope": "bot"}
        self.verification = VERIFICATION_TOKEN 
        self.client = SlackClient("")

    def auth(self, code):
        """
        Here we'll create a method to exchange the temporary auth code for an
        OAuth token and save it in memory on our Bot object for easier access.
        """
        auth_response = self.client.api_call("oauth.access",
                                             client_id=self.oauth['client_id'],
                                             client_secret=self.oauth[
                                                            'client_secret'],
                                             code=code) 
        #don't know the auth_response type that's why commented out                                     
        #self.user_id = auth_response["bot"]["bot_user_id"]
        #self.client = SlackClient(auth_response["bot"]["bot_access_token"])

    def say_hello(self, message):
        """
        Here we'll create a method to respond when a user DM's our bot
        to say hello!
        """
        channel = message["channel"]
        hello_message = "I want to live! Please build me."
        # Add message attachments here!

        self.client.api_call("chat.postMessage",
                             channel=channel,
                             text=hello_message,
                             attachments=json.dumps(message_attachments))