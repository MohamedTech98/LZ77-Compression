from LZCompression import LZCompression

class LZDecompression:
    __tags:list
    textCompressed:LZCompression
    def __init__(self,textCompressed):
        self.__textCompressed = textCompressed
        self.__tags = textCompressed.getCurrentTags()

    def getTags(self):
        cnt = 1
        for tag in self.__tags:
            print(f"tag {cnt}:<pos = {tag.pos},len = {tag.length},nextChar = {tag.nextChar}")
            cnt += 1

    def decompress(self):
        # write your code here
        pass

