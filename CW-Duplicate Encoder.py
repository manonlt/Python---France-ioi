#The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, 
#or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
#Exemples : "din" => "(((" / "recede" => "()()()" / "Success" => ")())())" / "(( @" => "))(("

def duplicate_encode(word):
    word = word.lower()
    l = []
    for i in word:
        if word.count(i) == 1:
            l.append("(")
        else:
            l.append(")")
    return ''.join(l)
