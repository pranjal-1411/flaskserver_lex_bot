import requests
import logging
url = "https://24ac1a95-f9f1-40b1-88b0-399710d4da94.mock.pstmn.io/api/leave/request"
# js ={
#     "ASAN_EMPCODE":emp_code,
#     "FROM_DATE":frm_date,
#     "TO_DATE":to_date,
#     "POLICY_ID":policy_id,
#     "NOTE":"Note",
#     "ADDITIONAL_RECIPIENTS":""
# }
response = requests.post(url=url)
        
logging.error(response.json())
