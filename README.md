# IzuminBot

## なにこれ

進捗を生やしたり頑張りを報告するといずみんが褒めてくれる、デベロッパーなデレマスP向けSlackBot

## 必要な環境
* Python 3.6以上

## 使い方
1. 自分のPCやVPSなどのマシンにクローンします
1. `pip install slackbot`します
1. SlackのワークスペースにBotsのカスタムインテグレーションを追加します
1. トークンを取得し、`slackbot_settings_default.py`のToken部分を書き換え、`slackbot_settings.py`という名前で保存します
1. ワークスペースの任意のチャンネルにいずみんを招待します
1. コンソールから`run.py`を起動します
1. 進捗を報告します
1. いずみんが褒めてくれます！

### ボットインテグレーションの追加方法
**注意** : ボットインテグレーションの追加はあなたがワークスペースの管理者か、管理者から権限をもらっている必要があります

https://my.slack.com/services/new/bot にアクセスし、画面の指示に従ってください

インテグレーションの追加に成功するとAPI Tokenが表示され、またボットユーザーの名前やアイコンを設定できるようになります

