import requests
import logging
import os 
import json

def get_leave_balance( emp_code ):
    
    url = "https://71f345c7-e619-4430-8261-a751682c1e51.mock.pstmn.io/api/leave/balance/read"
    js = {
			"ASAN_EMPCODE": emp_code      
	}
    response = requests.post(url=url,json=js) 
    return response

def send_leave_request_to_asanify(emp_code,frm_date,to_date,policy_id,policy_name=None):
    
    url ="https://71f345c7-e619-4430-8261-a751682c1e51.mock.pstmn.io/api/leave/request"
    #url = "https://24ac1a95-f9f1-40b1-88b0-399710d4da94.mock.pstmn.io/api/leave/request"
    js ={
        "ASAN_EMPCODE":emp_code,
        "FROM_DATE":frm_date,
        "TO_DATE":to_date,
        "POLICY_ID":policy_id,
        "NOTE":"Note",
        "ADDITIONAL_RECIPIENTS":""
    }
    logging.error(f'Sent request {emp_code} {frm_date} {policy_id} {policy_name}')
    response = requests.post(url=url,json=js)
    
    if response.status_code == 200:
        return f'Successfully applied for leave under category {policy_name} leave from {frm_date} to {to_date}'
    else:
        return response.json()['msg']




'''
{
Method: POST
Endpoint: api/leave/balance/read
Description: Get the leave balances policy wise
Expected JSON by Server:
If applying for self
{
        ASAN_EMPCODE: XXXX      
}
if applying on behalf of an Employee (Admin only route)
{
       REPORTEE_ ASAN_EMPCODE: XXXX      
}
Returned JSON
{
      ASAN_EMPCODE: XXXXX,
      LEAVE_BALANCES:[ //Array of balances leave policy wise
    {
          BALANCE: 10//Current Balance,
          AVAILABLE: 10 //Available currently, different from balance if any pending leave,
          POLICY_NAME: 'Sick Leave',
          DESCRUPTION: '',
          POLICY_ID: 'XXXX_ID_XXXX' //uinique identifier for policy
    },
    {
          BALANCE: 10//Current Balance,
          AVAILABLE: 10 //Available currently, different from balance if any pending leave,
          POLICY_NAME: 'Sick Leave',
          DESCRUPTION: '',
          POLICY_ID: 'XXXX_ID_XXXX' //uinique identifier for policy
    },
    ....
    ....
     ]
}
######################################################################################################################################
Method: POST
Endpoint: api/leave/policy/read
Description: Get the leave policy details
Expected JSON:
{
        POLICY_ID: XX_policy_id_XXX,
}
Returned JSON:
//Example JSON returned for sick leave policy
{
  "POLICY_ID": "76065c3100324ff98a679b04cca88071",
  "POLICY_NAME": "Sick Leave",
  "DESCRIPTION": null,
  "LEAVE_TYPE": "Sick Leave",
  "CREATED_DATE": "2020-02-24",
  "IS_ACCRUAL_FIXED": null,
  "TOTAL_PER_YEAR": 6,
  "IS_HOLIDAY_EXCLUDED": null,
  "IS_WEEKEND_EXCLUDED": null,
  "LIMIT_INCLUSION": null,
  "INCLUSION_TYPE": null,
  "MAX_CONSECUTIVE": null,
  "APPLY_BEFORE_DAYS": "1",
  "ACCRUAL_METHOD": "THROUGHOUT_EVERY_PERIOD",
  "IS_ACCRUAL_AT_BEGINNING": "False",
  "ACCRUAL_FREQUENCY": "MONTHLY",
  "WAITING_PERIOD_LENGTH": "90",
  "WAITING_PERIOD_UNIT": "WaitingPeriodUnit.DAY",
  "MAX_CARRY_DAYS": "0",
  "MAX_BALANCE_DAYS": null,
  "NEGATIVE_BALANCE_ALLOWED": "True",
  "INITIAL_PROBATION_BALANCE": null,
  "IS_DOJ_CONSIDERED": null,
  "IS_ACCRUAL_RESET": null
}
######################################################################################################################################
Method: POST
Endpoint: api/leave/request
Description: Get the leave balances policy wise
{
          ASAN_EMPCODE: 'XXXX',//For self or If Admin applies,
    OR
          REPORTEE_ASAN_EMPCODE: 'XXXX'//If manager os applying,
          FROM_DATE: "2020-05-12",
          TO_DATE: "2020-05-13",
          POLICY_ID: "POLICY _ID",
          NOTE: 'Note',
          ADDITIONAL_RECIPIENTS: '',//Whether this leave request should be seen by another employee
}
Returned JSON
If Success 200 returned,
If not err.response.data
{
        msg: 'Error_Message',
}

}
'''