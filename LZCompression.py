from Tag import Tag
class LZCompression:
    __tags: list[Tag]
    # lengthText : int
    def __init__(self,orignalString : str):
        if not orignalString:
            raise ValueError("Input can't be empty.")

        self.__orignalString = orignalString
        # tags is a list of stored tags of string compression
        self.__tags = []
        # self.lengthText = orignalString.__len__()

    def setText(self,text):
        self.__orignalString = text

    def getCurrentText(self):
        return  self.__orignalString
    
    def getCurrentTags(self):
        return  self.__tags

    def compress(self):
        # write your code here
        pass