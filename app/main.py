from __future__ import annotations

import argparse
import logging
from pathlib import Path
from services.log_service import LogService

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data" 
LOG_JSON = DATA_DIR / "logs.json"
LOG_TXT = BASE_DIR / "app.log"

def setup_logging() -> None:
     logging.basicConfig(
         level=logging.DEBUG,
         format="%(asctime)s [%(levelname)s] %(message)s",
         handlers=[
             logging.FileHandler(LOG_TXT, encoding="utf-8"),
             logging.StreamHandler()
         ],
     )
     
def cmd_add(service: LogService, message: str) -> None:
    logs = service.load()
    new_log = service.add(message)
    logs.append(new_log)
    service.save(logs)
    logging.info("新しいログを追加しました。%s", new_log)
    print(f"追加: {new_log.id} | {new_log.timestamp} | {new_log.message}")

    
def cmd_list(service: LogService) -> None:
    logs = service.load()
    if not logs:
        print("ログが存在しません。")
        return
    for x in logs:
        print(f"{x.id} | {x.timestamp} | {x.message}")
        
def cmd_delete(service: LogService, log_id: str) -> None:
    logs = service.load()
    logs, deleted = service.delete_by_id(logs, log_id)
    if not deleted:
        print(f"ID {log_id} のログは見つかりませんでした。")
        return
    service.save(logs)
    print(f"ID {log_id} のログを削除しました。")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="学習ログツール")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    parser_add = subparsers.add_parser("add", help="新しいログを追加します。")
    parser_add.add_argument("message", type=str, help="ログメッセージ")
    
    parser_list = subparsers.add_parser("list", help="全てのログを表示します。")
    
    parser_delete = subparsers.add_parser("delete", help="指定したIDのログを削除します。")
    parser_delete.add_argument("id", type=str, help="削除するログのID")
    
    return parser

def main() -> None:
    setup_logging()
    DATA_DIR.mkdir(exist_ok=True)
    service = LogService(DATA_DIR)
    
    parser = build_parser()
    args = parser.parse_args()
    
    try:
        if args.command == "add":
            cmd_add(service, args.message)
        elif args.command == "list":
            cmd_list(service)
        elif args.command == "delete":
            cmd_delete(service, args.id)
    except Exception :
        logging.exception("エラーが発生しました。")
        print("エラーが発生しました。詳細はログファイルを確認してください。")
    
if __name__ == "__main__":
    main()
