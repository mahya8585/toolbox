import json
import requests


# チャネル一覧の取得
channel_list_api = 'https://slack.com/api/channels.list?token=xoxxxxxxxxxxxxxxxxxxxxxxx&pretty=1'
result_channels = requests.get(channel_list_api).json()
print(str(result_channels['channels']))

# slack表示文言の作成
link_url_prefix = 'https://xxxxxxxxxx.slack.com/archives/'
message = '気になるchannelにJoinしてみましょう。\n'
for channel in result_channels['channels']:
    if not channel['is_archived']:
        channel_name = str(channel['name'])
        description = str(channel['purpose']['value'])
        channel_id = str(channel['id'])

        message = message + '<' + link_url_prefix + channel_id + ' | #' + channel_name + '>  :  ' + description + '\n'

# slack通知
incoming_url = 'https://hooks.slack.com/services/xxxx/xxxx/xxxxxxxxx'

post_body = {
    'text': message,
    'username': 'Pyladies Japan',
    'icon_emoji': ':dancers:',
    'channel': 'general'
}
header = {
    'Content-Type': 'application/json'
}
requests.post(incoming_url, headers=header, data=json.dumps(post_body))

print('finish to send slack.')
