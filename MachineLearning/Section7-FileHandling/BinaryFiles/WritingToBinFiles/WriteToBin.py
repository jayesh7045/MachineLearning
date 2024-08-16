data  = b'\x00\x01\x02\x03\x04'
with open("example.bin", "wb") as file:
    file.write(data)


# Using this the same values will be stored in the bin file example.bin
# x00 -> 0000 0000
# x01 -> 0000 0001
# x02 -> 0000 0010
# w+ mode is used to open up the file in reading as well as the writing and if the file does not exists then the file will be created

    