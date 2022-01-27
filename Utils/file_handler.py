# class for file handling in the problems
class FileHandler:
    def __init__(self, filePath) -> None:
        self.file = open(filePath)

    def readData(self) -> str:
        return self.file.read()

    def __del__(self) -> None:
        self.file.close()
