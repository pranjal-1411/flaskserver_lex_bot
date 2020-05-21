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
      "message_ts":"1588863588.001000",
      "channel_id":"D0126QW0LC8",
      "is_ephemeral":False
   },
   "trigger_id":"1133972427488.1030610122273.11edac8f7616a0ec6ace8a9e40738290",
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
      "text":"This content can't be displayed.",
      "user":"U0126QW0C5N",
      "ts":"1588863588.001000",
      "team":"T010WHY3L81",
      "blocks":[
         {
            "type":"section",
            "block_id":"ApplyLeave",
            "text":{
               "type":"mrkdwn",
               "text":"*Apply Leave*",
               "verbatim":False
            }
         },
         {
            "type":"section",
            "block_id":"type",
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
                        "text":"ravel Leave (Avl: 10)",
                        "emoji":True
                     },
                     "value":"XXXX_ID_XXXX"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"Sick Leave (Avl: 10)",
                        "emoji":True
                     },
                     "value":"XXXX_ID_XXXX"
                  }
               ],
               "action_id":"AoFX"
            }
         },
         {
            "type":"section",
            "block_id":"fdate",
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
               "action_id":"n1DSG"
            }
         },
         {
            "type":"section",
            "block_id":"tdate",
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
               "action_id":"OQqjJ"
            }
         },
         {
            "type":"actions",
            "block_id":"submit",
            "elements":[
               {
                  "type":"button",
                  "action_id":"4TQLD",
                  "text":{
                     "type":"plain_text",
                     "text":"Cancel",
                     "emoji":True
                  },
                  "style":"danger",
                  "value":"cancel"
               },
               {
                  "type":"button",
                  "action_id":"fYAM",
                  "text":{
                     "type":"plain_text",
                     "text":"Submit",
                     "emoji":True
                  },
                  "style":"primary",
                  "value":"submit",
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
   "response_url":"https://hooks.slack.com/actions/T010WHY3L81/1116313793572/BERVcqmLf6F4k28okq7U1uv5",
   "actions":[
      {
         "type":"static_select",
         "action_id":"AoFX",
         "block_id":"type",
         "selected_option":{
            "text":{
               "type":"plain_text",
               "text":"ravel Leave (Avl: 10)",
               "emoji":True
            },
            "value":"XXXX_ID_XXXX"
         },
         "placeholder":{
            "type":"plain_text",
            "text":"Sick",
            "emoji":True
         },
         "action_ts":"1588864433.163334"
      }
   ]
}

'''


# view_submission modal 

'''
{
   "type":"view_submission",
   "team":{},
   "user":{},
   "api_app_id":"A011W3NBM17",
   "token":"eeH1pT4oN0byzzkJ35B8mAS1",
   "trigger_id":"1144773140372.1030610122273.682b5f565f2bf40aa558bd84a57d095a",
   "view":{
      "id":"V014SCND48Y",
      "team_id":"T010WHY3L81",
      "type":"modal",
      "blocks":[
         {
            "type":"divider",
            "block_id":"VfIa"
         },
         {
            "type":"input",
            "block_id":"Date_hai",
            "label":{
               "type":"plain_text",
               "text":"Select leave type (Bal/Avl)",
               "emoji":True
            },
            "optional":False,
            "element":{
               "type":"static_select",
               "action_id":"Date_action_hai",
               "placeholder":{
                  "type":"plain_text",
                  "text":"Select an item",
                  "emoji":True
               },
               "options":[
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"*this is plain_text text*",
                        "emoji":True
                     },
                     "value":"value-0"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"*this is plain_text text*",
                        "emoji":True
                     },
                     "value":"value-1"
                  },
                  {
                     "text":{
                        "type":"plain_text",
                        "text":"*this is plain_text text*",
                        "emoji":True
                     },
                     "value":"value-2"
                  }
               ]
            }
         },
         {
            "type":"input",
            "block_id":"uprW",
            "label":{
               "type":"plain_text",
               "text":"Select start date",
               "emoji":True
            },
            "optional":False,
            "element":{
               "type":"datepicker",
               "initial_date":"2020-04-28",
               "placeholder":{
                  "type":"plain_text",
                  "text":"Select a date",
                  "emoji":True
               },
               "action_id":"zMNHZ"
            }
         },
         {
            "type":"input",
            "block_id":"nRg",
            "label":{
               "type":"plain_text",
               "text":"Select end date ",
               "emoji":True
            },
            "optional":False,
            "element":{
               "type":"datepicker",
               "initial_date":"2020-04-28",
               "placeholder":{
                  "type":"plain_text",
                  "text":"Select a date",
                  "emoji":True
               },
               "action_id":"GGK"
            }
         },
         {
            "type":"input",
            "block_id":"tDSyk",
            "label":{
               "type":"plain_text",
               "text":"Additional Note ?",
               "emoji":True
            },
            "optional":True,
            "element":{
               "type":"plain_text_input",
               "multiline":True,
               "action_id":"4DgJ"
            }
         }
      ],
      "private_metadata":"",
      "callback_id":"",
      "state":{
         "values":{
            "uprW":{
               "zMNHZ":{
                  "type":"datepicker",
                  "selected_date":"2020-04-11"
               }
            },
         "nRg":{
               "GGK":{
                  "type":"datepicker",
                  "selected_date":"2020-04-28"
               }
            },
            "Date_hai":{
               "Date_action_hai":{
                  "type":"static_select",
                  "selected_option":{
                     "text":{
                        "type":"plain_text",
                        "text":"*this is plain_text text*",
                        "emoji":True
                     },
                     "value":"value-1"
                  }
               }
            },
            "tDSyk":{
               "4DgJ":{
                  "type":"plain_text_input"
               }
            }
         }
      },
      "hash":"1590080185.b1f1c3ac",
      "title":{
         "type":"plain_text",
         "text":"Apply Leave",
         "emoji":True
      },
      "clear_on_close":False,
      "notify_on_close":False,
      "close":{
         "type":"plain_text",
         "text":"Cancel",
         "emoji":True
      },
      "submit":{
         "type":"plain_text",
         "text":"Submit",
         "emoji":True
      },
      "previous_view_id":"None",
      "root_view_id":"V014SCND48Y",
      "app_id":"A011W3NBM17",
      "external_id":"",
      "app_installed_team_id":"T010WHY3L81",
      "bot_id":"B0126QW0AQG"
   },
   "response_urls":[

   ]
}
'''