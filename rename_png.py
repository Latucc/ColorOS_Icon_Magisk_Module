#根据xml的内容将png重命名为包名

import xml.etree.ElementTree as ET
import os
tree = ET.parse('allApps.xml')
root = tree.getroot()
raw_folder = 'raw'

for icon in root.findall('icon'):
    name = icon.get('name')
    package = icon.get('package')
    old_file_path = os.path.join(raw_folder, name)
    new_file_path = os.path.join(raw_folder, f"{package}.png")
    if old_file_path != new_file_path:
        try:
            os.rename(old_file_path, new_file_path)
        except:
            pass