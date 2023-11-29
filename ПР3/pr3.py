from random import choice
from re import findall
cryptMode = input("[1] Encrypt | [2] Decrypt: ").upper()
if cryptMode not in ['1','2']:
    print("Error!")
    raise SystemExit
startMessage = input("Text: ")
bookKey = input("Key: ")
def regular(text):
    template = r"[0-9]+"
    return findall(template, text)
def encryptDecrypt (mode, message, key, final = ""):
    with open (key) as bookKey:
        book = bookKey.read()
    if mode == '1':
        for symbolMessage in message:
            listIndexKey = []
            for indexKey, symbolKey in enumerate(book):
                if symbolMessage == symbolKey:
                    listIndexKey.append(indexKey)
            try: final += str(choice(listIndexKey)) + '/'
            except IndexError: pass
    else:
        for numbers in regular(message):
            for indexKey, symbolKey in enumerate(book):
                if numbers == str(indexKey):
                    final += symbolKey
    return final
print("Result:", encryptDecrypt(cryptMode, startMessage, bookKey))
