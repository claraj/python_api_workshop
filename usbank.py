import requests
import os

apiKey = os.environ['APIKEY']   # TODO set this environment variable in PyCharm or for your OS

# Used for all the requests 
print(apiKey)

header = {'apiKey': apiKey}



print('\nLOCATION API CALL\n')

# Example fetching data from ATM location API
atm_location_url = 'https://alpha-api.usbank.com/innovation-locations/v1/StringQuery?application=parasoft&transactionid=afae903d-8946-4f88-a958-4bdbcf0bed6f&output=json&searchtype=A&stringquery=55403&branchfeatures=BOP'

response = requests.get(atm_location_url, headers=header).json()

reply = response['GetListATMorBranchReply']
atmList = reply['ATMList']  # Todo extract specific location data needed

for atm in atmList:
    print(atm)



print('\nLOAN RATE API CALL\n')

# Example fetching data from Loan Rates API

autoloan = 'https://alpha-api.usbank.com/innovation-rate/v1/GetAutoLoanRates?application=RIB&output=json&branchnumber=1&zipcode=80130&regionid=1&loanamount=24000&loantermmonths=12&loanproduct=NEW'

rateResponse = requests.get(autoloan, headers=header).json()
print(rateResponse)
rate = rateResponse['AutoLoanRates']['RateTier']['Rate']
print('The rate is ', rate)


print('\nACCOUNTS AND USERS API CALL\n')

doc_users_url = 'https://alpha-api.usbank.com/innovation/v1/user/'  # What the documentation seems to say
users_url = 'http://jcm-bank-43157.appspot.com/users'    # The server that the request is being proxied to - but the proxing seems to be failing 

response  = requests.get(users_url, headers=header).json()
print(response)

users = response['UserList']

for user in users:
    print(user)   # Example {'LegalParticipantIdentifier': '000995928731567433'} these are IDs used to make more calls for user account info


example_user = users[0]
"""
Make sure server is up, figure out URL
Make GET request to get all users id    or all account int   -- these should have list of IDs for users or accounts

Make POST request about specific user 
Make POST request about specific account   


response = requests.post(url, data= {"whatever":"whatever"} ).json()

"""


get_account_info_url = 'http://jcm-bank-43157.appspot.com/user/accounts/'    # The server the message is proxied to, according to Postman, although it's 404'ing
get_account_info_url = 'https://alpha-api.usbank.com/innovation/v1/user/accounts'    # What the docs say, although it's not proxying 

user_id = example_user['LegalParticipantIdentifier']
print(user_id)
data = {'LegalParticipantIdentifier': example_user['LegalParticipantIdentifier'] }  # find this out from query to /users endpoint
account_info = requests.post(get_account_info_url, headers=header, data=data).json()
print(account_info)





