import requests
import zipfile
import io
import os
import shutil

def download_zip():
    url = f'https://github.com/Light-Projects/LSSE-DB/archive/refs/tags/LSS.zip'

    response = requests.get(url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall('.')

        try:
            os.rename("LSSE-DB-LSS", "LSSE")
            print("Folder successfully renamed!")
        except FileNotFoundError:
            print("Error: The specified source folder does not exist.")
        except PermissionError:
            print("Error: You do not have permission to rename this folder.")
        except OSError:
            pass

        try:
            shutil.rmtree('LSSE-DB-LSS')
        except FileNotFoundError:
            pass


        print(f"Successfully downloaded and extracted LSSE database.")
    else:
        print(f"Failed to download. Status code: {response.status_code}")


download_zip()