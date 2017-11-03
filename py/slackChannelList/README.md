# slack にchannel一覧を投稿するFunction
- Azure Functionsの利用を想定したツール
- 現在有効なchannel名を取得し、slackに投稿する

## 準備
- Azure Functionsを立てる
    - Python キュートリガー選択
- Kuduから次のディレクトリに `Lib.zip` をアップロード
    - D:\home\site\wwwroot
- 関数の統合ページから詳細エディタを開いて `function.json` を記載する
    - トリガー名や時間などはご自由に
- `run.py` をfunctionに登録


- slack takenを取得する
    - [https://api.slack.com/custom-integrations/legacy-tokens](https://api.slack.com/custom-integrations/legacy-tokens)
- channellistが取れることを確認する
    - [https://api.slack.com/methods/channels.list/test](https://api.slack.com/methods/channels.list/test)
    - `run.py` の `channel_list_api` に記載する
- slackドメインを `link_url_prefix` に記載する

- incomming hooks を取得する
    - [https://api.slack.com/incoming-webhooks](https://api.slack.com/incoming-webhooks)
