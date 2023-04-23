# Функция для конвертации текста в ASCII-графику
from data import ascii_dict
def ascii_art(text, type="LETTER"):
    text = text.lower()  # Преобразование текста в нижний регистр

    # Перебор символов в тексте и создание ASCII-графики
    if(type == "LETTER"):
        ascii_text = [[""],[""],[""],[""],[""]]
        for char in text:
            if char in ascii_dict["LETTER"]:
                ascii_text[0] += ascii_dict["LETTER"][char][0]
                ascii_text[1] += ascii_dict["LETTER"][char][1]
                ascii_text[2] += ascii_dict["LETTER"][char][2]
                ascii_text[3] += ascii_dict["LETTER"][char][3]
                ascii_text[4] += ascii_dict["LETTER"][char][4]
            else:
                ascii_text += char
    

    elif (type == "bubble"):
        ascii_text = [[""],[""],[""]]
        
        for char in text:
            if char in ascii_dict["bubble"]:
                ascii_text[0] += ascii_dict["bubble"][char][0]
                ascii_text[1] += ascii_dict["bubble"][char][1]
                ascii_text[2] += ascii_dict["bubble"][char][2]
            else:
                ascii_text[0] += ascii_dict["bubble"]["undefined"][0]
                ascii_text[1] += ascii_dict["bubble"]["undefined"][1]
                ascii_text[2] += ascii_dict["bubble"]["undefined"][2]


    for row in ascii_text:
        print(*row)


# Пример использования
text = input()
ascii_text = ascii_art(text, 'bubble')

