import requests
import logging

url = "https://71f345c7-e619-4430-8261-a751682c1e51.mock.pstmn.io/api/leave/balance/read"
js = {
        "ASAN_EMPCODE": "XXXX"      
}
response = requests.post(url=url,json=js)
sample_option = {
						"text": {
							"type": "plain_text",
							"text": "Sick",
							"emoji": True
						},
						"value": "value-0"
					}
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
						"value": "value-0"
					}
        #logging.error(sample_option)
        options.append(sample_option)
        
logging.error(options)
