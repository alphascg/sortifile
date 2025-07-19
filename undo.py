import os
import json
import shutil

UNDO_LOG_PATH = os.path.join(os.path.dirname(__file__), ".sortifile", "last_run.json")

def undo_last_run():
    if not os.path.exists(UNDO_LOG_PATH):
        print("Undo not possible, no log file found.")
        return

    with open(UNDO_LOG_PATH, "r", encoding="utf-8") as f:
        entries = json.load(f)

    undone = 0
    removed_folders = set()

    for entry in entries:
        src = entry["to"]
        dst = entry["from"]

        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, dst)
            print(f"Undid: {os.path.relpath(src)} → {os.path.relpath(dst)}")
            undone += 1
            removed_folders.add(os.path.dirname(src))  # Zielordner merken
        else:
            print(f"File not found (skipped): {src}")

    print(f"\n✅ {undone} File(s) undid.")

    print("\nChecking for empty folders to delete...")
    for folder in sorted(removed_folders, key=len, reverse=True):  # tiefste Ordner zuerst
        try:
            if os.path.isdir(folder) and not os.listdir(folder):
                os.rmdir(folder)
                print(f"Deleted previously created folder: {os.path.relpath(folder)}")
        except Exception as e:
            print(f"Could not delete folder: {folder} - {e}")

    # Lösche Undo-Log
    os.remove(UNDO_LOG_PATH)
