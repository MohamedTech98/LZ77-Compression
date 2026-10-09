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

# Single character: (0,0,A)
# Normal text: (0,0,A);(0,0,B);(0,0,C)
# Repeated character: (0,0,A);(1,1,A);(1,1,A);(1,1,A)
# Repeated pattern: (0,0,A);(0,0,B);(2,2,A);(2,2,A)
# Repeated ABC: (0,0,A);(0,0,B);(0,0,C);(3,3,A);(3,3,B);(3,3,C)
# Text with spaces: (0,0,H);(0,0,i);(0,0, );(0,0,A)
#  Longer repeated sequence: (0,0,A);(0,0,B);(0,0,C);(3,3,D);(6,3,E)
# }
 
from LZCompression import LZCompression
from Tag import Tag
from LZDeompression import LZDecompression

while True:
    print("********************************************************************************")
    print("welcome to LZ77 Compression and Decompression")
    print("Please choose an option:")
    print("1. Compress a text")
    print("2. Decompress a text")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        text = input("Enter the text to compress: ")
        compressor = LZCompression(text)
        compressor.compress()
        compressor.trace()
        compressor.printCompressionRatio()

    elif choice == '2':
        tags_input = input("Enter the tags in the format (pos,length,nextChar) separated by semicolons: ")
        tags_list = []
        for tag_str in tags_input.split(';'):
            pos, length, nextChar = tag_str.strip().strip('()').split(',')
            tags_list.append(Tag(int(pos), int(length), nextChar))
        decoder = LZDecompression.from_tags(tags_list)
        decompressed_text = decoder.decompress()
        print("Decompressed text:", decompressed_text)
       
       

    elif choice == '3':
        print("Exiting the program.")
        break
