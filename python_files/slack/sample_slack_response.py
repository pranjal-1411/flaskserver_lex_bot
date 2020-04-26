# user.info reply 

'''
Formatted JSON Data
{
   "ok":True,
   "user":{
      "id":"U011CEW3XTR",
      "team_id":"T011BCF0TRD",
      "name":"p.gupta.pranjal140003",
      "deleted":False,
      "color":"e96699",
      "real_name":"Pranjal Alternate",
      "tz":"Asia/Kolkata",
      "tz_label":"India Standard Time",
      "tz_offset":19800,
      "profile":{
         "title":"",
         "phone":"",
         "skype":"",
         "real_name":"Pranjal Alternate",
         "real_name_normalized":"Pranjal Alternate",
         "display_name":"Pranjal Alternate",
         "display_name_normalized":"Pranjal Alternate",
         "status_text":"",
         "status_emoji":"",
         "status_expiration":0,
         "avatar_hash":"gb65b55057c6",
         "email":"p.gupta.pranjal140003@gmail.com",
         "image_24":"https://secure.gravatar.com/avatar/b65b55057c6b71c7ae99b76e9cb8c586.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-24.png",
         "image_32":"https://secure.gravatar.com/avatar/b65b55057c6b71c7ae99b76e9cb8c586.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-32.png",
         "image_48":"https://secure.gravatar.com/avatar/b65b55057c6b71c7ae99b76e9cb8c586.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-48.png",
         "image_72":"https://secure.gravatar.com/avatar/b65b55057c6b71c7ae99b76e9cb8c586.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-72.png",
         "image_192":"https://secure.gravatar.com/avatar/b65b55057c6b71c7ae99b76e9cb8c586.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-192.png",
         "image_512":"https://secure.gravatar.com/avatar/b65b55057c6b71c7ae99b76e9cb8c586.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-512.png",
         "status_text_canonical":"",
         "team":"T011BCF0TRD"
      },
      "is_admin":False,
      "is_owner":False,
      "is_primary_owner":False,
      "is_restricted":False,
      "is_ultra_restricted":False,
      "is_bot":False,
      "is_app_user":False,
      "updated":1586541740
   }
}

'''

#chat.postMessage

'''
{
   "ok":True,
   "channel":"D011M87PWG3",
   "ts":"1586543609.001200",
   "message":{
      "bot_id":"B011M87P5PV",
      "type":"message",
      "text":"just keep trying",
      "user":"U011M87P7B5",
      "ts":"1586543609.001200",
      "team":"T011BCF0TRD",
      "bot_profile":{
         "id":"B011M87P5PV",
         "deleted":False,
         "name":"CheckBot",
         "updated":1586539066,
         "app_id":"A011W3NBM17",
         "icons":{
            "image_36":"https://a.slack-edge.com/80588/img/plugins/app/bot_36.png",
            "image_48":"https://a.slack-edge.com/80588/img/plugins/app/bot_48.png",
            "image_72":"https://a.slack-edge.com/80588/img/plugins/app/service_72.png"
         },
         "team_id":"T011BCF0TRD"
      }
   }
}
'''

# query json on event -- message 

'''
{
   "token":"eeH1pT4oN0byzzkJ35B8mAS1",
   "team_id":"T011BCF0TRD",
   "api_app_id":"A011W3NBM17",
   "event":{
      "client_msg_id":"bbf423c7-2dbf-437d-bd29-53bc84704f88",
      "type":"message",
      "text":"Hi",
      "user":"U011CEW3XTR",
      "ts":"1586541809.000400",
      "team":"T011BCF0TRD",
      "blocks":[
         {
            "type":"rich_text",
            "block_id":"gIr+",
            "elements":[
               {
                  "type":"rich_text_section",
                  "elements":[
                     {
                        "type":"text",
                        "text":"Hi"
                     }
                  ]
               }
            ]
         }
      ],
      "channel":"D011CEW449M",
      "event_ts":"1586541809.000400",
      "channel_type":"im"
   },
   "type":"event_callback",
   "event_id":"Ev011X5D11FT",
   "event_time":1586541809,
   "authed_users":[
      "U011M87P7B5"
   ]
}
'''

# event callback app home opened
'''
{
   "token":"eeH1pT4oN0byzzkJ35B8mAS1",
   "team_id":"T010WHY3L81",
   "api_app_id":"A011W3NBM17",
   "event":{
      "type":"app_home_opened",
      "user":"U010TRDA89Y",
      "channel":"D0126QW0LC8",
      "tab":"home",
      "event_ts":"1586885306.098839"
   },
   "type":"event_callback",
   "event_id":"Ev011U0VQ534",
   "event_time":1586885306
}
'''


# auth slack response 

'''

{
    "ok": true,
    "access_token": "xoxb-17653672481-19874698323-pdFZKVeTuE8sk7oOcBrzbqgy",
    "token_type": "bot",
    "scope": "commands,incoming-webhook",
    "bot_user_id": "U0KRQLJ9H",
    "app_id": "A0KRD7HC3",
    "team": {
        "name": "Slack Softball Team",
        "id": "T9TK3CUKW"
    },
    "enterprise": {
        "name": "slack-sports",
        "id": "E12345678"
    },
    "authed_user": {
        "id": "U1234",
        "scope": "chat:write",
        "access_token": "xoxp-1234",
        "token_type": "user"
    }
}

'''


# interactive block action event

'''

{
   "type":"block_actions",
   "user":{
      "id":"U010TRDA89Y",
      "username":"pranjalguptacse",
      "name":"pranjalguptacse",
      "team_id":"T010WHY3L81"
   },
   "api_app_id":"A011W3NBM17",
   "token":"eeH1pT4oN0byzzkJ35B8mAS1",
   "container":{
      "type":"message",
      "message_ts":"1587928856.002600",
      "channel_id":"D0126QW0LC8",
      "is_ephemeral":False
   },
   "trigger_id":"1093183883748.1030610122273.df546b95de7a4c3dca12735e64e71f2e",
   "team":{
      "id":"T010WHY3L81",
      "domain":"pranjal-hq"
   },
   "channel":{
      "id":"D0126QW0LC8",
      "name":"directmessage"
   },
   "message":{
      "bot_id":"B0126QW0AQG",
      "type":"message",
      "text":"Would you like to play a game?",
      "user":"U0126QW0C5N",
      "ts":"1587928856.002600",
      "team":"T010WHY3L81",
      "blocks":[
         {
            "type":"section",
            "block_id":"Nor",
            "text":{
               "type":"mrkdwn",
               "text":"*Apply Leave*",
               "verbatim":False
            }
         },
         {
            "type":"section",
            "block_id":"+lC",
            "text":{
               "type":"mrkdwn",
               "text":"Leave Type(Availaible Quotas)",
               "verbatim":False
            },
            "accessory":{
               "type":"static_select",
               "placeholder":{
                  "type":"plain_text",
                  "text":"Sick",
                  "emoji":True
               },
               "options":[
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"Sick",
                        "emoji":True
                     },
                     "value":"value-0"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"Vacation",
                        "emoji":True
                     },
                     "value":"value-1"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"Travel",
                        "emoji":True
                     },
                     "value":"value-2"
                  }
               ],
               "action_id":"YSc"
            }
         },
         {
            "type":"section",
            "block_id":"I4r+3",
            "text":{
               "type":"mrkdwn",
               "text":"Select start date",
               "verbatim":False
            },
            "accessory":{
               "type":"datepicker",
               "initial_date":"1990-04-28",
               "placeholder":{
                  "type":"plain_text",
                  "text":"Select a date",
                  "emoji":True
               },
               "action_id":"2Omxo"
            }
         },
         {
            "type":"section",
            "block_id":"13qR",
            "text":{
               "type":"mrkdwn",
               "text":"Select end date.",
               "verbatim":False
            },
            "accessory":{
               "type":"datepicker",
               "initial_date":"1990-04-28",
               "placeholder":{
                  "type":"plain_text",
                  "text":"Select a date",
                  "emoji":True
               },
               "action_id":"BS/"
            }
         },
         {
            "type":"actions",
            "block_id":"pgPdC",
            "elements":[
               {
                  "type":"button",
                  "action_id":"q3iaw",
                  "text":{
                     "type":"plain_text",
                     "text":"Cancel",
                     "emoji":True
                  },
                  "style":"danger",
                  "value":"click_me_123"
               },
               {
                  "type":"button",
                  "action_id":"O2sj",
                  "text":{
                     "type":"plain_text",
                     "text":"Submit",
                     "emoji":True
                  },
                  "style":"primary",
                  "value":"click_me_123",
                  "confirm":{
                     "title":{
                        "type":"plain_text",
                        "text":"Are you sure?",
                        "emoji":True
                     },
                     "text":{
                        "type":"mrkdwn",
                        "text":"Apply for leave ?",
                        "verbatim":False
                     },
                     "confirm":{
                        "type":"plain_text",
                        "text":"Do it",
                        "emoji":True
                     },
                     "deny":{
                        "type":"plain_text",
                        "text":"Stop, I've changed my mind!",
                        "emoji":True
                     }
                  }
               }
            ]
         }
      ]
   },
   "response_url":"https://hooks.slack.com/actions/T010WHY3L81/1087015122802/rr2f53sZS8GnO2uJWRW6TW8d",
   "actions":[
      {
         "confirm":{
            "title":{
               "type":"plain_text",
               "text":"Are you sure?",
               "emoji":True
            },
            "text":{
               "type":"mrkdwn",
               "text":"Apply for leave ?",
               "verbatim":False
            },
            "confirm":{
               "type":"plain_text",
               "text":"Do it",
               "emoji":True
            },
            "deny":{
               "type":"plain_text",
               "text":"Stop, I've changed my mind!",
               "emoji":True
            }
         },
         "action_id":"O2sj",
         "text":{
            "type":"plain_text",
            "text":"Submit",
            "emoji":True
         },
         "value":"click_me_123",
         "style":"primary",
         "type":"button",
         "action_ts":"1587928904.302058"
      }
   ]
}

'''