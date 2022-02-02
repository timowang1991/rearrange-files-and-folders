import os
import zipfile
import shutil

zipFiles = sorted(list(filter(lambda f: f.startswith('takeout-20211225T132853Z-'), os.listdir('.'))))

with zipfile.ZipFile(zipFiles[0], 'r') as zip_ref:
    zip_ref.extractall('./main')

def handleFilePath(path):
    filesOrDirs = os.listdir(path)
    for fileOrDir in filesOrDirs:
        joinedPath = os.path.join(path, fileOrDir)
        print('handling joinedPath', joinedPath)
        if os.path.isdir(joinedPath):
            handleFilePath(joinedPath)
        else:
            newFilePath = path.replace('tempextractdir', 'main')
            if not os.path.exists(newFilePath):
                print('path not exist, creating one, path:', newFilePath)
                os.makedirs(newFilePath)
            os.rename(joinedPath, joinedPath.replace('tempextractdir', 'main'))

for i, zipFile in enumerate(zipFiles[1:]):
    with zipfile.ZipFile(zipFile, 'r') as zip_ref:
        zip_ref.extractall('./tempextractdir')
        handleFilePath('tempextractdir')
        shutil.rmtree('./tempextractdir')

        
