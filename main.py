from LZCompression import LZCompression
from Tag import Tag
from LZDeompression import LZDecompression
# some testcases:{
# Single character: A
# Normal text: ABCDEFG
# Repeated character: AAAAAA
# Repeated pattern: ABABABAB
# Long repeated pattern: ABCABCABCABC
# Mixed text: CABRCCDRRRRDDD
# Empty text:
# }
 
text=input("enter your text")
compressor= LZCompression(text)
compressor.compress()
compressor.trace()
compressor.printCompressionRatio()

 
decoder = LZDecompression(compressor)
decomp=decoder.decompress()
if text==decomp :
    print("PASSED")
else:
    print("FAILED")

print(text)
print(decomp)
