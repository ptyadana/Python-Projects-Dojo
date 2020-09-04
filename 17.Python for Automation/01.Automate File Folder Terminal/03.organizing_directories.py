# organize files accordingly
import os
from pathlib import Path


SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}


def pick_directory(file_type):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == file_type:
                return category
    return "MISC"


def organize_directory(path_to_process, destination_path):
    for item in os.scandir(path_to_process):
        if item.is_dir():
            continue

        file_path = Path(item)
        file_type = file_path.suffix.lower()
        directory_name = pick_directory(file_type)

        directory_path = Path(destination_path + directory_name)
        print(directory_path)
        if directory_path.is_dir() != True:
            directory_path.mkdir()

        # move the file into that directory
        file_path.rename(directory_path.joinpath(item.name))


if __name__ == "__main__":
    print(pick_directory(".pdf"))
    organize_directory("../00.data/OrganizeMe", "../00.data/AfterOrganized/")
