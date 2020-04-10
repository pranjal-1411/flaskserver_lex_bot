import os 
os.environ['ROOT_PATH'] = "/mnt/f/python3resolve" 
path_to_oauth_file = os.path.join(os.getenv('ROOT_PATH'),"python_files","slack","slack_oauth.csv")
teamid = "12345" 
token = "sdfsafef"    
with open(path_to_oauth_file, "a") as auth_csv:
    auth_csv.write(f'{teamid},{token}')

# import csv

# with open(path_to_oauth_file) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for row in csv_reader:
#         print(f'{row[0]} {row[1]} ')
        
 