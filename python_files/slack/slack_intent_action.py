
import python_files.slack.slack_helper as slack_helper
import logging

def apply_leave(query):
    
    channel_id = query['event']['channel']
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
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Sick",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Vacation",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Travel",
							"emoji": True
						},
						"value": "value-2"
					}
				]
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
    
    
def attendanceClockIn(query):
    pass
def attendanceClockOut(query): 
    pass