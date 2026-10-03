from LZCompression import LZCompression
from Tag import Tag
from LZDeompression import LZDecompression

compression = [
    Tag(0,0,'A'),
    Tag(0,0,'B'),
    Tag(2,8,'')
    ]
compression = [
    Tag(0,0,'C'),
    Tag(0,0,'A'),
    Tag(0,0,'B'),
    Tag(0,0,'R'),
    Tag(3,1,'C'),
    Tag(2,1,'D'),
    Tag(7,4,'R'),
    Tag(3,5,'D')
    ]

decoder = LZDecompression.from_tags(compression)

# decoder.getTags()

print(decoder.decompress())