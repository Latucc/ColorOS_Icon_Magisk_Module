import os
import zipfile

def zip_folder(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, relative_path)

folder_to_zip = 'zip'
output_zip_file = '我的图标_magisk.zip'

zip_folder(folder_to_zip, output_zip_file)
