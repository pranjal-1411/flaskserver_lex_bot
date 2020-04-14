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