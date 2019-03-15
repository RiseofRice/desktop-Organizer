import os, sys
from pathlib import Path
directory = {
    'images': [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],

    'videos': ['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mng',
                '.qt', '.mpg', '.mpeg', '.3pg'],
                
    'Docs': [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx", '.pdf'],

    'Archives': [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],

    'Audio': [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],

    'Plaintext': [".txt", ".in", ".out", ''],

    'scripts': ['.py', '.js', '.go', 'cpp', '.cs'],

    'html':  ['.html'],

    'EXE': ['.exe', '.bat', '.sh']
}

file_formats = {file_format: directory
                for directory, file_formats in directory.items()
                for file_format in file_formats }

def organize():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in file_formats:
            directory_path = Path(file_formats[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass

if __name__ == '__main__':
    organize()