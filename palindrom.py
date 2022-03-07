def is_palindorme(word):
    return word[::-1]== word
print(is_palindorme("Kajak"))
print(is_palindorme("potop"))

#opcja druga z prosba aby Kajak rowniez zwracal True
def is_palindorme(word):
    return word.lower()[::-1]== word.lower()
print(is_palindorme("Kajak"))
print(is_palindorme("potop"))

#opcja trzecia - funkcja dla calego zdania

def is_palindrome(tekst):
    zdanie = tekst(filter(lambda char: char.isalnum(), tekst))
    return zdanie[::-1]== zdanie










