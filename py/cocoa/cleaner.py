import os
import json
import pandas as pd


target_path = os.path.join('C:\\', 'Users', 'maishid', 'work-m', 'github', 'toolbox', 'py', 'cocoa', 'ExposureChecks-2020-08-06.json')

cocoa_json = json.load(open(target_path))
cocoa_df = pd.read_json(json.dumps(cocoa_json['ExposureChecks']))
# cocoa_df.to_csv('ExposureChecks.csv')
