from Tag import Tag
class LZCompression:
    __tags: list[Tag]
    def __init__(self,orignalString):
        if not orignalString:
            raise ValueError("Input can't be empty.")

        self.__orignalString = orignalString
        # tags is a list of stored tags of string compression
        self.tags = []

    def setText(self,text):
        self.__orignalString = text

    def getCurrentText(self):
        return  self.__orignalString
    
    def getCurrentTags(self):
        return  self.__tags

    def compress(self):
        # write your code here
        pass