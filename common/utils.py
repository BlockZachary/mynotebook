# -*- coding:utf-8 -*-
# Author: Zachary
from pathlib import Path


def get_file_name_patrs(filename):
    pos = filename.rfind('.')
    if pos == -1:
        return filename, ''
    return filename[:pos], filename[pos + 1:]


def get_save_filepath(filePath: Path, filename: str):
    save_file = filePath.joinpath(filename)
    if not save_file.exists():
        return save_file

    name, ext = get_file_name_patrs(filename)
    index = 1
    while True:
        save_file = filePath.joinpath(f'{name}_{index}.{ext}')
        if not save_file.exists():
            return save_file
        index += 1
