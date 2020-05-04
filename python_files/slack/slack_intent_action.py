
import python_files.slack.slack_helper as slack_helper
import requests
import logging

def apply_leave(query):
    
    channel_id = query['event']['channel']
    options = get_leave_options( channel_id )
    blocks= [
		{   "block_id":"ApplyLeave",
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Apply Leave*"
			}
		},
		{   "block_id":"1",
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Leave Type(Availaible Quotas)"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Sick",
					"emoji": True
				},
				"options": options
			}
		},
		{   "block_id":"2",
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Select start date"
			},
			"accessory": {
				"type": "datepicker",
				"initial_date": "1990-04-28",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a date",
					"emoji": True
				}
			}
		},
		{   "block_id":"3",
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Select end date."
			},
			"accessory": {
				"type": "datepicker",
				"initial_date": "1990-04-28",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a date",
					"emoji": True
				}
			}
		},
		{   "block_id":"submit",
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Cancel"
					},
					"style": "danger",
					"value": "cancel"
				},
				{   
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Submit"
					},
					"style": "primary",
					"value": "submit",
                    "confirm": {
						"title": {
							"type": "plain_text",
							"text": "Are you sure?"
						},
						"text": {
							"type": "mrkdwn",
							"text": "Apply for leave ?"
						},
						"confirm": {
							"type": "plain_text",
							"text": "Do it"
						},
						"deny": {
							"type": "plain_text",
							"text": "Stop, I've changed my mind!"
						}
					}
				}
			]
		}
	]
    access_token =None #slack_helper.find_access_token(query['team_id'])
    slack_helper.send_message_to_slack(channel_id,blocks=blocks,access_token=access_token)
   
     
def get_leave_options( emp_code ):
    
	url = "https://71f345c7-e619-4430-8261-a751682c1e51.mock.pstmn.io/api/leave/balance/read"
	js = {
			"ASAN_EMPCODE": emp_code      
	}
	response = requests.post(url=url,json=js)
	options = [] 
	if response.status_code==200:
		for item in response.json()['LEAVE_BALANCES']:
			leave = f'{item["POLICY_NAME"]} (Avl: {item["AVAILABLE"]})'
			sample_option = {
							"text": {
								"type": "plain_text",
								"text": leave,
								"emoji": True
							},
							"value": item["POLICY_ID"]
						}
			options.append(sample_option)

	return options
        
def attendanceClockIn(query):
    pass
def attendanceClockOut(query): 
    pass