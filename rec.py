import os
import shutil
import xml.etree.ElementTree as ET
from PIL import Image

source_folder = 'Y:/Theme/icon/make/rec'#你想要设置成自定义图标的文件夹地址
bfd = 'zip/my_stock/media/theme/uxicons/xxxhdpi'

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
create_folder(bfd)

def crbg(inpath, outpath):
    with Image.open(inpath) as img:
        img = img.convert('RGB')
        pixel_color = img.getpixel((40, 40))
        new_image = Image.new('RGB', (200, 200), pixel_color)
        new_image.save(outpath)

tree = ET.parse('allApps.xml')
root = tree.getroot()

for icon in root.findall('icon'):
    package = icon.get('package')
    ic_path = os.path.join(source_folder, f"{package}.png")
    fg_path = os.path.join(f'{bfd}/{package}', "recfg.png")
    bg_path = os.path.join(f'{bfd}/{package}', "recbg.png")
    if os.path.isfile(ic_path):
        try:
            shutil.copy2(ic_path, fg_path)
            crbg(ic_path, bg_path)
        except:
            print(package)
            pass
