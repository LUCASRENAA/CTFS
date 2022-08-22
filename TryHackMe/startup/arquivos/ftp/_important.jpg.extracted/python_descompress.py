# import zlib and decompress
import zlib
  
  
f = open('39.zlib', 'r')
for line in f:
	print(zlib.decompress(line))
   
# using zlib.compress(s) method

print("Compressed String")

  
print("\nDecompressed String")

