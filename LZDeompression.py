from LZCompression import LZCompression
from Tag import Tag

class LZDecompression:
    __tags:list[Tag]
    textCompressed:LZCompression
    def __init__(self,textCompressed):
        self.__textCompressed = textCompressed
        self.__tags = textCompressed.getCurrentTags()
        if not self.__vaildTags():
            raise ValueError("some error in tags,try again.")


    @classmethod
    def from_tags(cls,tags):
        obj = cls.__new__(cls)
        obj.__textCompressed = None
        obj.__tags = tags
        if not obj.__vaildTags():
            raise ValueError("some error in tags,try again.")
        return obj

    def __vaildTags(self):
        szWindowSearch = 0

        for tag in self.__tags:
            pos = tag.pos
            lenght = tag.length
            nextChar = tag.nextChar

            if pos < 0 or lenght < 0:
                return False

            if lenght > 0 and pos == 0:
                return False

            if pos > 0 and lenght == 0:
                return False

            if pos > szWindowSearch:
                return False

            szWindowSearch += lenght + (1 if nextChar else 0)

        return True

    def getTags(self):
        cnt = 1
        for tag in self.__tags:
            print(f"tag {cnt}:<pos = {tag.pos},len = {tag.length},nextChar = {tag.nextChar}>")
            cnt += 1


    def decompress(self):
        text = ''
        for tag in self.__tags:
            stepsBack = tag.pos
            length = tag.length
            startPos = text.__len__() - stepsBack
            nextChar = tag.nextChar
            if stepsBack < length :
                endPos = text.__len__() - 1
                move = 0
                for i in range(length):
                    # print(text[startPos + move])
                    text += text[startPos + move]
                    move += 1
                    # rotate on string and protect from out of range
                    move %= (endPos - startPos + 1)
                text += nextChar
            else:
                for i in range(length):
                    text += text[startPos + i]
                text += nextChar
        return text



