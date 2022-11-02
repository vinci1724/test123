def file_to_str(my_input):
    text = list()
    with open(my_input, encoding="utf-8") as r:
        for line in r:
            text.append(line)
    r.close()
    return text

def space(text):
    new_text = list()
    for line in text:
        str = ''
        space_count = 0
        for symbol in line:
            if symbol == ' ' and space_count == 0:
                space_count += 1
                continue
            if symbol == ' ' and space_count >= 1:
                space_count += 1
                continue
            else:
                str += symbol
                space_count = 0
        new_text.append(str)
    return new_text

def count(text):
    val = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0 }
    for line in text:
        # print(line)
        split_count = 0
        char_count = 0            
        for symbol in line:
            if symbol == '│' or symbol == '|':
                if char_count > val[split_count]:
                    val[split_count] = char_count
                split_count += 1
                char_count = 0
            else:
                char_count += 1
    return val

def fancy(text, val):
    new_text = list()
    for line in text:
        split_count = 0
        char_count = 0            
        str = ''
        for symbol in line:
            if symbol == '│' or symbol == '|':
                point = val[split_count]
                if split_count >= 1:
                    point = val[split_count] + 1
                for i in range(char_count, point):
                    str += ' '
                split_count += 1
                char_count = 0
            else:
                char_count += 1
            str += symbol
        new_text.append(str)
    return new_text

def str_to_file(text, my_output):
    with open(my_output, 'w', encoding="utf-8") as w:
        for line in text:
            w.write(line)
    w.close()

#my_input = 'input.txt'
# my_input = '20220701120008.txt'
# my_input = 'qwe.txt'
my_input = 'qwe.txt'
my_output = 'output.txt'
text = file_to_str(my_input)
text = space(text)
val = count(text)
text = fancy(text, val)
str_to_file(text, my_output)