# -*- coding:utf-8 -*-
# Author: Zachary
from common.profile import Profile


class ImageService:

    def get_image_filename_list(self):
        image_path = Profile.get_image_path()
        filename_list = []
        if image_path.exists():
            for filename in image_path.iterdir():
                if filename.is_file():
                    filename_list.append(filename.name)
        return filename_list
