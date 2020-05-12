

import json
import os
root_dir = '/mnt/f/python3resolve'
filePath = os.path.join(root_dir,'python_files/slack/blocks/apply_leave/from_date.json')

with open(filePath,'r') as jsFile:
    data = json.load(jsFile)
    print(data[0])
    