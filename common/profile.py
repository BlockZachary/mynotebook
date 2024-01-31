# -*- coding:utf-8 -*-
# Author: Zachary
from pathlib import Path


class Profile:
    __image_path = None

    @staticmethod
    def get_image_path():
        project_path = Path(__file__).parent.parent  # 获取项目根目录
        images_path = project_path.joinpath("data/images")
        if not images_path.exists():
            images_path.mkdir(parents=True)
        Profile.__image_path = images_path
        return images_path
