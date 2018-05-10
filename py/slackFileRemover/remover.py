"""
slack workspace内の指定日付よりも古いファイルを削除する処理
"""
import requests
import datetime


def create_id_list(slack_files):
    """
    ファイルリスト情報からファイルIDを抽出してリスト化する
    :param slack_files: slackファイルリスト情報 json
    :return: ファイルIDリスト
    """
    if slack_files['paging']['total'] == 0:
        return []

    file_ids = []
    if slack_files['ok'] is True:
        for sf in slack_files['files']:
            file_ids.append(sf['id'])
    else:
        print('ファイルリスト取得に失敗しました')
        raise Exception

    return file_ids


def get_target_files(token, threshold_date):
    """
    slack workspace内のファイル情報を取得する
    指定日付よりも古いデータのみを抽出する
    :param token: workspace token (https://api.slack.com/custom-integrations/legacy-tokens)
    :param threshold_date: str yyyy/MM/dd この日付より古い日付を抽出する
    :return: 抽出されたファイルIDのリスト
    """
    # 閾値となる日付
    threshold_timestamp = str(int(datetime.datetime.strptime(threshold_date, '%Y/%m/%d').timestamp()))

    file_url = 'https://slack.com/api/files.list?pretty=1&token=' + token + '&ts_to=' + threshold_timestamp
    slack_files = requests.get(file_url).json()

    file_ids = create_id_list(slack_files)

    page_count = int(slack_files['paging']['pages'])
    if 1 < page_count:
        # 100件以上はページングされてしまうのでもう一度取りに行かねばならぬ
        for page in range(2, page_count + 1):
            paging_url = file_url + '&page=' + str(page)
            paging_files = requests.get(paging_url).json()
            file_ids.extend(create_id_list(paging_files))

    return file_ids


def delete_file(file_ids, token):
    """
    指定日付よりも古い日付のファイルを削除する
    :param file_ids: 削除対象ファイルIDリスト
    :param token: workspace token
    """
    delete_url = 'https://slack.com/api/files.delete?pretty=1&token=' + token + '&file='
    for file_id in file_ids:
        print(file_id + 'を削除します')
        response = requests.post(delete_url + file_id)

        if response.json()['ok'] is False:
            print(file_id + 'の削除に失敗しました')
            raise Exception


if __name__ == "__main__":
    workspace_token = 'xoxp-YOUR-WORKSPACE-TOKEN'
    threshold = 'yyyy/MM/dd'

    files_info = get_target_files(workspace_token, threshold)
    print(str(len(files_info)) + '件のファイルを削除します')

    delete_file(files_info, workspace_token)

    print('作業終了')
