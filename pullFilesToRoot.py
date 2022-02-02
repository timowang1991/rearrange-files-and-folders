import os

def getFolders(path):
    return sorted(list(filter(lambda f: os.path.isdir(os.path.join(path, f)), os.listdir(path))))

def handleFilePath(path):
    filesOrDirs = os.listdir(path)
    for fileOrDir in filesOrDirs:
        joinedPath = os.path.join(path, fileOrDir)
        print('handling joinedPath', joinedPath)
        if os.path.isdir(joinedPath):
            handleFilePath(joinedPath)
        else: # elif joinedPath.find('SYNOPHOTO_THUMB') == -1 and joinedPath.find('SYNOFILE_THUMB') == -1 and joinedPath.find('SynoEAStream') == -1 and joinedPath.find('SynoResource') == -1 and joinedPath.find('Thumbs.db') == -1:
            print('moving joinedPath', joinedPath)
            os.rename(joinedPath, joinedPath.replace(path, '.'))

folders = getFolders('.')

for folder in folders:
    handleFilePath(folder)
