import json
import requests
import pytz
from datetime import datetime
from bs4 import BeautifulSoup
from azure.storage.blob import BlockBlobService, AppendBlobService

# blob setting
account_name = 'blob account name'
account_key = 'blob account key'
container_name = 'container name'
blob_name = 'hogehoge.log'


def get_log():
    """
    blobからログをダウンロードする
    :return:
    """
    print('get success log')
    block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
    block_blob_service.get_blob_to_path(container_name, blob_name, blob_name)


def append_log(today):
    """
    ログ情報をblobにあげる。事前にblobアカウント・blob containerを作っておくこと
    :param today:
    :return:
    """
    print('append log')
    append_blob_service = AppendBlobService(account_name=account_name,
                                            account_key=account_key)
    append_blob_service.append_blob_from_text(container_name, blob_name, 'test' + '\n')


def has_today_log():
    """
    本日付のログを持っているか否かを判定する
    :return: true:保持 false:未保持
    """
    f = open(blob_name, 'rb')
    has_today_log = False
    for log in f.readlines():
        if log.strip() == today:
            has_today_log = True
            break;
    f.close()

    print(has_today_log)
    return has_today_log

def extract_entries(adventar):
    """
    アドベンターのページからエントリ情報だけを取得する
    :param adventar: request.textデータ
    :return: エントリ情報json
    """
    # data-reactをJSONに整形(とりあえずhtml_parserで回すよー
    adventar_soup = BeautifulSoup(adventar.text, 'html.parser')
    divs = adventar_soup.find_all('div')
    target_json = ''
    for div in divs:
        target_attrs = 'data-react-props'
        if target_attrs in div.attrs:
            target_json = json.loads(div.attrs[target_attrs])

    # ブログエントリ情報
    return target_json['entries']


def send_slack_channel(append_message):
    """
    slackにデータ送信する
    :param append_message: 送信した文字列
    :return:
    """
    # slack表示文言の作成
    message = 'PyLadies Tokyo Adventar ' + today + '\n' + append_message

    # slack通知
    incoming_url = 'https://hooks.slack.com/services/xxxxxx/xxxxxx/xxxxxxxxxxxx'

    post_body = {
        'text': message,
        'username': 'AdventarBot',
        'icon_emoji': ':santa:',
        'channel': 'advent_calendar'
    }
    header = {
        'Content-Type': 'application/json'
    }
    requests.post(incoming_url, headers=header, data=json.dumps(post_body))

    print('finish to send slack.')


# メイン処理ここから
# 本日日付
now = datetime.now().replace(tzinfo=pytz.timezone('Japan'))
today = datetime.strftime(now, '%Y-%m-%d')

# すでにブログ公開済みか確認する
# AppendBlobService(account_name=account_name, account_key=account_key).create_blob(container_name, blob_name)
get_log()

# ブログslack送付済みの場合はここで処理終了
if has_today_log() is False:
    # adventarの取得
    adventar_url = 'https://adventar.org/calendars/2462'
    adventar = requests.get(adventar_url)

    # 実行日のブログが公開されていたらslackで対象チャネルに送信
    for entry_info in extract_entries(adventar):
        if entry_info['date'] == today:
            url = entry_info['url']
            if url is not None and url != '':
                # ログを追加
                append_log(today + u'\n')
                # slack送信
                send_slack_channel(url)

else:
    print('## send slack yet. finish this function. ##')

print('function end.')
