# oTree REST API の作例

参考: https://otree.readthedocs.io/ja/latest/misc/rest_api.html

- `handlename` app の AdminReport
    - 実験者スクリーンの Payments タブの右隣．
    - コードは `__init__.py` の `vars_for_admin_report()` と `admin_report.html` を参照せよ．
- `/api/participant_vars/{participant_code}` エンドポイント
    - ある `player` で `player.participant.code` が `{participant_code}` である人の `player.participant.vars` を更新することができる．
    - 作例では `studentid` key と `handlename` key の値を更新している．
    - デバッグ用に `prisoner` app の `Introduction` ページで `player.participant.vars` を表示している．
- 環境変数 `OTREE_REST_KEY` を設定することを忘れずに！
    - リクエストのヘッダーに `otree-rest-key` というkeyで `OTREE_REST_KEY` の値を渡さなければならない．
    - 一応 `.env` ファイルに記述している．
