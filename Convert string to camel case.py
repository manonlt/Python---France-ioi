
#Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be 
#capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).


def to_camel_case(text):
    text = text.replace('-', ' ').replace('_', ' ')
    l = []
    for i in text.split(" "):
        l.append(i)

    liste = []
    for pl, mot in enumerate(l):
    
        if pl == 0:
            liste.append(mot)
        else:
            liste.append(mot[0].upper() + mot[1:])

    return ''.join(liste)
