import json
import os
import shutil

SONGLIST_JSON_PATH = "rawData/songs/songlist"
DL_FOLDER_PATH = "rawData/dl"
SONGS_FOLDER_PATH = "rawData/songs"

SOURCE_DIR = "rawData/songs"
DEST_DIR = "organizedSongs"

def move_all_songs(source_dir, dest_dir):
    # Ensure destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    for item in os.listdir(source_dir):
        src_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        shutil.move(src_path, dest_path)
        print(f"Moved: {src_path} → {dest_path}")

FILE_MAP = {
    "": "base.ogg",
    "_0": "0.aff",
    "_1": "1.aff",
    "_2": "2.aff",
    "_3": "3.aff",
    "_4": "4.aff",
    "_audio_3": "base_3.ogg",
    "_video.mp4": "video.mp4",
    "_video_1080.mp4": "video_1080.mp4",
    "_video_audio.ogg": "video_audio.ogg",
}


def rename_folders():
    """
    Rename folders in SONGS_FOLDER_PATH that start with 'dl_'
    by removing the 'dl_' prefix.
    """
    for folder_name in os.listdir(SONGS_FOLDER_PATH):
        folder_path = os.path.join(SONGS_FOLDER_PATH, folder_name)
        if os.path.isdir(folder_path) and folder_name.startswith("dl_"):
            new_name = folder_name[3:]
            new_path = os.path.join(SONGS_FOLDER_PATH, new_name)
            os.rename(folder_path, new_path)
            print(f"Renamed: {folder_name} → {new_name}")
        else:
            print(f"No rename needed for: {folder_name}")


def move_file_if_exists(src_path, dest_path):
    """
    Moves a file from src_path to dest_path if it exists.
    Returns True if a file was moved, otherwise False.
    """
    if os.path.exists(src_path):
        shutil.move(src_path, dest_path)
        print(f"Moved {src_path} → {dest_path}")
        return True
    print(f"File not found, skipping: {src_path}")
    return False


def main():
    rename_folders()

    # Load song IDs from songlist JSON
    with open(SONGLIST_JSON_PATH, encoding="utf-8") as songlist_file:
        songlist_data = json.load(songlist_file)
        song_ids = [song["id"] for song in songlist_data["songs"]]

    files_processed = 0

    for song_id in song_ids:
        base_path = os.path.join(DL_FOLDER_PATH, song_id)
        dest_dir = os.path.join(SONGS_FOLDER_PATH, song_id)
        os.makedirs(dest_dir, exist_ok=True)

        for suffix, final_name in FILE_MAP.items():
            # If song_id == "testify", add ".pre" to the path
            if song_id == "testify":
                source = f"{base_path}{suffix}.pre"
            else:
                source = f"{base_path}{suffix}"

            destination = os.path.join(dest_dir, final_name)
            if move_file_if_exists(source, destination):
                files_processed += 1

    print(f"Processed {files_processed} files")
    move_all_songs(SOURCE_DIR, DEST_DIR)
    print("All songs moved to organizedSongs folder")
    

if __name__ == "__main__":
    main()
