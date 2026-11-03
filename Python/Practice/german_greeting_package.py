#English to German 
greetings_dict = {
    "Hallo": "Hello",
    "Hi": "Hi",
    "Hey": "Hey",
    "Guten Morgen": "Good morning",
    "Guten Tag": "Good day",
    "Guten Abend": "Good evening",
    "Gute Nacht": "Good night",
    "Grüß Gott": "Hello",
    "Grüß Sie": "Hello",
    "Hallo zusammen": "Hello all",
    "Na?": "Whats up",
    "Servus": "Hi/Bye",
    "Moin": "Hello",
    "Moin moin": "Hello",
    "Grüzi": "Hello",
    "Salü": "Hi",
    "Tach": "Hi"
    }


def german(word):
    english(word)

def english(word):
    for word1 in greetings_dict:
        if word1 == word:
            print(f"{word}: {greetings_dict[word]}")
