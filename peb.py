import os
import shutil

source_folder = 'Y:/Theme/icon/make/peb'#你想要设置成鹅卵石图标的文件夹地址

bfd = 'zip/my_stock/media/theme/uxicons/xxxhdpi'

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
create_folder(bfd)

for filename in os.listdir(source_folder):
    if filename.endswith('.png'):
        icname = os.path.splitext(filename)[0]
        target_dir = os.path.join(bfd, icname)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        source_file = os.path.join(source_folder, filename)
        target_file = os.path.join(target_dir, 'peb.png')
        shutil.copy2(source_file, target_file)

