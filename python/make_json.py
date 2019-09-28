#coding=utf-8

import json
import glob
import os
from PIL import Image


def make_json():
    # 建立字典
    dict = {"data":[]}
    # 获取指定目录下所有jpg文件
    list = glob.glob(r'../media/photo/thumb/*.jpg')

    cnt = 0
    page = 0
    for i in list:
        # 读取图片信息
        img = Image.open(i)
        w, h = img.size

        # 获取文件名
        name = os.path.join(i[21:])
        # 添加键值对并写入字典
        temp = {"name":name, "width":w, "height":h}
        dict["data"].append(temp)

        cnt += 1
        if (cnt > 99):
            cnt = 0
            page += 1

            # 创建json文件
            file_name = "../json/photo_thumb" + str(page) + ".json"
            with open(file_name, "w") as file:
                # 把字典按照json样式可视化显示
                json_str = json.dumps(dict, indent=1)
                file.write(json_str)
                file.close()
                dict = {"data":[]}
    
    print("finish")

if __name__=='__main__':
    make_json()
