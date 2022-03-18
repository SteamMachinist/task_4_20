# 20. Обработать HTML-файл, убрав все теги, т.е. должен остаться только текст. Каждую последовательность удаленных
# тегов заменить на один пробел.
# Например: "<html><head><title>Моя страница</title><head><h1>Привет, Я Колян!<BR />Закурить есть?</h1></head></body>"
# после удаления тегов превратится в " Моя страница Привет, Я Колян! Закурить есть? "

def read_from_file(filepath):
    file = open(filepath, 'r', encoding="utf-8")
    text = file.read()
    file.close()
    return text


def write_to_file(text, filepath):
    file = open(filepath, 'w', encoding="utf-8")
    file.write(text)
    file.close()


def replace_tags_with_space(html):
    # regex = r"(<.*?>)+"
    # result = re.sub(regex, " ", html, 0, re.MULTILINE)

    chars_list = list(html)
    char_index = 0
    flag = False
    while char_index < len(chars_list) - 1:
        if chars_list[char_index] == "<":
            for tags_beginning in range(char_index, len(chars_list) - 1):
                if tags_beginning == len(chars_list) - 2:
                    flag = True
                if (chars_list[tags_beginning] == ">" and chars_list[tags_beginning + 1] != "<") or flag:
                    new_list = chars_list[0:char_index]
                    new_list.append(" ")
                    new_list.extend(chars_list[tags_beginning + 1 + int(flag):len(chars_list)])
                    chars_list = new_list
                    break
        else:
            char_index += 1
    return "".join(chars_list)


if __name__ == '__main__':
    without_tags = replace_tags_with_space(read_from_file("input/input2.html"))
    write_to_file(without_tags, "output/output2.txt")
