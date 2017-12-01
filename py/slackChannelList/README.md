# slack にchannel一覧を投稿するFunction
- Azure Functionsの利用を想定したツール
- 現在有効なchannel名を取得し、slackに投稿する

## 準備
- Azure Functionsを立てる
    - Python キュートリガー選択
- 関数の統合ページから詳細エディタを開いて `function.json` を記載する
    - トリガー名や時間などはご自由に
- `run.py` をfunctionに登録
- Kuduから以下作業
    - cd D:\home\site\tools
    - nuget.exe install -Source https://www.siteextensions.net/api/v2/ -OutputDirectory D:\home\site\tools python352x64
    - mv /d/home/site/tools/python352x64.3.5.2.6/content/python35/* /d/home/site/tools/
    - D:\home\site\tools\python.exe -m pip install xxxx
        - requests


- slack takenを取得する
    - [https://api.slack.com/custom-integrations/legacy-tokens](https://api.slack.com/custom-integrations/legacy-tokens)
- channellistが取れることを確認する
    - [https://api.slack.com/methods/channels.list/test](https://api.slack.com/methods/channels.list/test)
    - `run.py` の `channel_list_api` に記載する
- slackドメインを `link_url_prefix` に記載する

- incomming hooks を取得する
    - [https://api.slack.com/incoming-webhooks](https://api.slack.com/incoming-webhooks)
