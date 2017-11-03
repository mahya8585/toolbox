# -*- coding: UTF-8 -*-
import json
import sys

sys.path.append('../Lib')
import requests

# チャネル一覧の取得
channel_list_api = 'https://slack.com/api/channels.list?token=xxxxxxxx&pretty=1'
result_channels = requests.get(channel_list_api).json()
print(result_channels['channels'])

# slack表示文言の作成
link_url_prefix = 'https://xxxxxx.slack.com/archives/'
message = '気になるchannelにJoinしてみましょう。\n'
for channel in result_channels['channels']:
    if not channel['is_archived']:
        channel_name = str(channel['name'])
        description = channel['purpose']['value'].encode('unicode-escape').decode('unicode-escape').encode('utf-8')
        channel_id = str(channel['id'])

        message = message + '<' + link_url_prefix + channel_id + ' | #' + channel_name + '>  :  ' + description + '\n'

# slack通知
incoming_url = 'https://hooks.slack.com/services/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'

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
