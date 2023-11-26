CASE, WORD = map(str, input().split())
camel_list = ""
snake_list = ""
pascal_list = ""

if CASE == "1":
    # 단어의 첫 글자가 대문자, 첫 글자는 소문자 사용
    for i, word in enumerate(WORD, 1):
        if i == 1:
            camel_list += word.lower()
            snake_list += word.lower()
            pascal_list += word.upper()
        elif word == word.upper():
            camel_list += word
            snake_list += f"_{word.lower()}"
            pascal_list += word.upper()
        else:
            camel_list += word.lower()
            snake_list += word.lower()
            pascal_list += word.lower()
elif CASE == "2":
    flag = False
    # 소문자만 사용, 단어 사이 언더바
    for i, word in enumerate(WORD, 1):
        if i == 1:
            camel_list += word.lower()
            snake_list += word.lower()
            pascal_list += word.upper()
        elif word == "_":
            flag = True
            snake_list += word
        elif flag == True:
            camel_list += word.upper()
            snake_list += word.lower()
            pascal_list += word.upper()
            flag = False
        else:
            camel_list += word.lower()
            snake_list += word.lower()
            pascal_list += word.lower()
elif CASE == "3":
    # 카멜 표기법 + 첫글자 대문자
    for i, word in enumerate(WORD, 1):
        if i == 1:
            camel_list += word.lower()
            snake_list += word.lower()
            pascal_list += word.upper()
        elif word == word.upper():
            camel_list += word.upper()
            snake_list += f"_{word.lower()}"
            pascal_list += word.upper()
        else:
            camel_list += word.lower()
            snake_list += word.lower()
            pascal_list += word.lower()

print(camel_list)
print(snake_list)
print(pascal_list)