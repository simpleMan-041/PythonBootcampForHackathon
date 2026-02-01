# StudyLog CLI

学習内容をコマンドラインから記録・管理するための  
シンプルな Python 製 CLI ツールです。
設計学習及びハッカソン参加に向けて技術やライブラリを抑える目的で作成。

## 概要
- 学習ログを追加・一覧表示・削除できる
- JSON ファイルに保存
- logging による実行履歴・エラー追跡対応

ハッカソンや個人学習のログ管理用途を想定しています。

---

## 使用技術
- Python 3.x
- 標準ライブラリ
  - argparse
  - pathlib
  - json
  - datetime
  - uuid
  - logging

---

## セットアップ
```bash
python -m venv venv
venv\Scripts\activate
```
## 使い方
- ログ追加    例: python app/main.py add "Day6: CLIツール完成"
- 一覧表示    例: python app/main.py list
- 直近N件表示 例: python app/main.py tail 3
- 削除        python app/main.py delete <id>

