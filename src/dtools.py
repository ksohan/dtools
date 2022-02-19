import os
import shutil

class DTools:
    def __init__(self) -> None:
        pass

    def removeFolder(self, folderName):
        if os.path.isdir(folderName):
            try:
                shutil.rmtree(folderName)
            except Exception as e:
                print(str(e))
        else:
            print("{} doesn't exist".format(folderName))

    def createFolder(self, folderName, removeExisting = False):
        if os.path.isdir(folderName):
            if removeExisting:
                self.removeFolder(folderName)
            else:
                print("Folder already exists. If you want to remove it, use param removeExisting = True")
                return
        try:
            os.mkdir(folderName)
        except Exception as e:
            print(str(e))
