import os

from pathlib import Path


img_paths = list(Path('./a_files').iterdir())
walker = 1
for img_path in img_paths:
    old = str(img_path)
    new = f"{str(img_path.parent)}/{walker}.jpg"
    walker +=2
    os.rename(old,new)