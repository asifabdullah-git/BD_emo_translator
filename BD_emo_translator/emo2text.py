import re
import emo_code


#bangla_emo_unicode = codecs.open("bangla_emo_unicode.py", "r", "utf-8")
#f = codecs.open("bangla_emo_unicode.py", "r", "utf-8")

__all__ = ['emoji', 'emoticons']


def emoji(string):

    __entities = {}
    __value = []
    __mean = []
    __location = []
    flag = True
    try:
        pro_string = str(string)
        for pos, ej in enumerate(pro_string):
            if ej in bangla_emo_unicode.BD_UNICODE_EMO:
                try:
                    __value.append(ej)
                    __mean.append(emo_code.BD_UNICODE_EMO[ej])
                    __location.append([pos, pos])
                except Exception as e:
                    flag = False
                    __entities.append({"flag": False})
                    return __entities

    except Exception as e:
        flag = False
        __entities.append({"flag": False})
        return __entities
    if len(__value) < 1:
        flag = False
    __entities = {
        'value': __value,
        'mean': __mean,
     #   'location': __location,
        'flag': flag
    }

    return __entities


def emoticons(string):

    __entities = []
    flag = True
    try:
        pattern = u'(' + u'|'.join(k for k in emo_code.EMOTICONS) + u')'
        __entities = []
        __value = []
        __location = []
        matches = re.finditer(r"%s" % pattern, str(string), re.IGNORECASE)
        for et in matches:
            __value.append(et.group().strip())
            __location.append([et.start(), et.end()])

        __mean = []
        for each in __value:
            __mean.append(emo_code.EMOTICONS_EMO[each])

        if len(__value) < 1:
            flag = False
        __entities = {
            'value': __value,
    #        'location': __location,
            'mean': __mean,
            'flag': flag
        }
    except Exception as e:
        __entities = [{'flag': False}]
        #print("No emoiticons found")
        return __entities

    return __entities


def test_emo():
    test = "এটা খুব ভালো কাজ করেছ  😀 💑"
    #test = "i love you :###.."
    print(emoji(test))
    print(emoticons(test))
    return None


def about():
    text = "emot library: emoji and emoticons library for python. It return emoji or emoticons from string with location of it. \nAuthors: \n Abdullah Al Asif: asifabdullah6@gmail.com or https://github.com/asifabdullah-git \n \n\nInspired from: Neel Shah and Subham Rohilla"
    print(text)
    return None


if __name__ == '__main__':
    test_emo()
