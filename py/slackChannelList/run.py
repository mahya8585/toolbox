# -*- coding: UTF-8 -*-
import json
import sys

sys.path.append('../Lib')
import requests
 
# get channel list
channel_list_api = 'https://slack.com/api/channels.list?token=xoxp-2876607195-xxxxxx&pretty=1'
result_channels = requests.get(channel_list_api).json()
print(result_channels['channels'])

# create slack message
link_url_prefix = 'https://xxxxxx.slack.com/archives/'
message = '気になるchannelにJoinしてみましょう。\n'
for channel in result_channels['channels']:
    if not channel['is_archived']:
        channel_name = str(channel['name'])
        description = channel['purpose']['value'].encode('unicode-escape').decode('unicode-escape').encode('utf-8')
        channel_id = str(channel['id'])

        message = message + '<' + link_url_prefix + channel_id + ' | #' + channel_name + '>  :  ' + description + '\n'

# send slack
incoming_url = 'https://hooks.slack.com/services/xxxx/xxxx/xxxx'

post_body = {
    'text': message,
    'username': 'channel keeper',
    'icon_emoji': ':dancers:',
    'channel': 'general'
}
header = {
    'Content-Type': 'application/json'
}
requests.post(incoming_url, headers=header, data=json.dumps(post_body))

print('finish to send slack.')
