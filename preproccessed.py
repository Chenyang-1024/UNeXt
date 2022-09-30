import os
import shutil

path = r'/data/cy/datasets/ISIC2018/masks/4'
cnt = 0
for file_name in os.listdir(path):
    src = os.path.join(path, file_name)
    dst = os.path.join(path, file_name[:12] + file_name[-4:])
    print(dst)
    os.rename(src, dst)