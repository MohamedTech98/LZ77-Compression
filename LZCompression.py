from Tag import Tag
class LZCompression:
    __tags: list[Tag]
    # lengthText : int
    def __init__(self, orignalString : str, windowSize : int = 20, lookaheadSize : int = 10):
        if not orignalString:
            raise ValueError("Input can't be empty.")
        if windowSize < 1 or lookaheadSize < 1:
            raise ValueError("Window size and look ahead size must be at least 1.")

        self.__orignalString = orignalString
        self.__tags = []
        self.__windowSize = windowSize
        self.__lookaheadSize = lookaheadSize

    def setText(self,text):
        if not text:
            raise ValueError("Input can't be empty.")
        self.__orignalString = text
        self.__tags = []

    def getCurrentText(self):
        return  self.__orignalString
        
    def getCurrentTags(self):
        return  self.__tags

    def findLongestMatch(self, pos):
        data = self.__orignalString
        bestPos = 0
        bestLength = 0

        startWindow = max(0, pos - self.__windowSize)
        maxLen = min(self.__lookaheadSize, len(data) - pos - 1)

        for i in range(pos - 1, startWindow - 1, -1):
            length = 0
            while length < maxLen and data[length + i] == data[pos + length]:
                length += 1
            if length > bestLength:
                bestLength = length
                bestPos = pos - i

        return bestPos, bestLength

    def compressionRatio(self):
        if not self.__tags:
            raise ValueError("Call compress() first")

        originalSize = len(self.__orignalString) * 8  # each char is 8 bits

        maxPos = max(tag.pos for tag in self.__tags)
        maxLen = max(tag.length for tag in self.__tags)
        posBits = max(1, maxPos.bit_length())
        lenBits = max(1, maxLen.bit_length())
        symbolBits = 8  # each char is 8 bits
        tagSize = posBits + lenBits + symbolBits
        compressedSize = len(self.__tags) * tagSize
        return {
            "originalSize": originalSize,
            "posBits": posBits,
            "lenBits": lenBits,
            "tagSize": tagSize,
            "numberOfTags": len(self.__tags),
            "compressedSize": compressedSize,
            "compressionRatio": originalSize / compressedSize,
        }

    def printCompressionRatio(self):
        ratio = self.compressionRatio()
        print(f"Original Size: {ratio['originalSize']} bits")
        print(f"Pos Bits: {ratio['posBits']} bits")
        print(f"Len Bits: {ratio['lenBits']} bits")
        print(f"Tag Size: {ratio['tagSize']} bits")
        print(f"Number of Tags: {ratio['numberOfTags']}")
        print(f"Compressed Size: {ratio['compressedSize']} bits")
        print(f"Compression Ratio: {ratio['compressionRatio']:.2f}")    

    def trace(self):
        if not self.__tags:
            raise ValueError("Call compress() first.")
 
        data = self.__orignalString
        w1 = max(15, self.__windowSize + 2)
        w2 = max(13, self.__lookaheadSize + 2)
 
        print(f"{'step':<6}{'pos':<6}{'search buffer':<{w1}}{'look-ahead':<{w2}}tag")
        print("".ljust(12 + w1 + w2 + 14, "-"))
 
        pos = 0
        for step, tag in enumerate(self.__tags, start=1):
            searchBuffer = data[max(0, pos - self.__windowSize):pos]
            lookahead = data[pos:pos + self.__lookaheadSize]
            print(f"{step:<6}{pos:<6}{searchBuffer:<{w1}}{lookahead:<{w2}}"
                  f"<{tag.pos},{tag.length},'{tag.nextChar}'>")
            pos += tag.length + 1


    def compress(self):
        data=self.__orignalString
        self.__tags=[]
        pos=0
        while pos < len(data):
            bestposDIST,bestlength =self.findLongestMatch(pos)
            nextChar=data[pos+bestlength]
            self.__tags.append(Tag(bestposDIST,bestlength,nextChar))
            pos+=(bestlength+1)
