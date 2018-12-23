import requests
import azure.storage.blob as azblob
from requests_oauthlib import OAuth1Session
import json


def download_content(source_url, img_name):
    """
    画像をURLからダウンロードする
    :param source_url: ダウンロード先URL
    :param img_name: ファイル名
    :return: コンテナ内画像ファイルパス
    """

    # 画像をゲットする
    response = requests.get(source_url)

    # ゲットした画像をファイルに保存する
    img_out_path = img_name

    img_out = open(img_out_path, 'wb')
    img_out.write(response.content)
    img_out.close()

    return img_out_path


def upload_blob(local_path, file_name):
    """
    ファイルをblobにuploadする
    :param local_path: ローカルに吐き出したファイルのパス
    :param file_name: 画像名
    :return:
    """
    # blob setting
    account_name = 'xxxx'
    account_key = 'xxxxx'
    container_name = '$web'

    block_blob_service = azblob.BlockBlobService(account_name=account_name, account_key=account_key)
    block_blob_service.create_blob_from_path(container_name, file_name, local_path)


def search_twitter():
    """
    ツイートの検索とメディア情報の取得
    :return:
    """
    # Twitter configと認証
    consumer_key = 'xxxxx'
    consumer_seacret = 'xxxxxx'
    access_token = 'xxxxx'
    access_token_seacret = 'xxxxx'

    twitter_oauth = OAuth1Session(consumer_key, consumer_seacret, access_token, access_token_seacret)

    # tweetの取得
    url = "https://api.twitter.com/1.1/search/tweets.json"
    # 検索条件。今回は対象ユーザの一番最新のツイートを取得
    params = {
        'q': 'from:maaya8585',
        'count': 1
    }

    res = twitter_oauth.get(url, params=params)
    tweet_json = json.loads(res.text)

    return tweet_json


def create_media_url(media_info):
    """
    メディアコンテンツの種類に応じて、コンテンツURLを変更する
    :param media_info: twitter search API で取得できるmedia情報
    :return: 取得対象URL, 画像名
    """
    media_url = media_info['media_url']

    if media_url.find('video_thumb') >= 0:
        video = media_info['video_info']['variants'][0]
        media_url = video['url'].split('?')[0]

    url_split = media_url.split('/')
    content_name = url_split[-1]

    return media_url, content_name


def main():
    tweet = search_twitter()
    tw_content = tweet['statuses'][0]['extended_entities']

    if tw_content['media']:
        for media in tw_content['media']:
            # 画像名の取得
            content_url, content_name = create_media_url(media)

            # 画像をダウンロードする
            local_img_path = download_content(content_url, content_name)

            # storage blobにアップロードする
            upload_blob(local_img_path, content_name)

    else:
        print('画像がありません')


if __name__ == '__main__':
    main()