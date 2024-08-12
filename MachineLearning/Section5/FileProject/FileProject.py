def read_content_from_file(file_path):
    word_count = {}
    with open(file_path, "r") as file:
        for line in file:
            words = line.split();
            for word in words:
                word = word.lower().strip('.,?!;:"\/')
                word_count[word] = word_count.get(word, 0)+1
    return word_count;

file_path = 'sample.txt';
dict = read_content_from_file(file_path);
print(type(dict))
for key, value in dict.items():
    print(f"{key} : {value}")

                
