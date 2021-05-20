class Cipher():
    "Cipher class encrypt or decrypt text by given interval"

    def __init__(self, text: str, interval: int):
        self.text = text
        self.interval = interval

    def encrypt(self):
        "encrpyting text by given interval"
        cipher = ""
        for char in self.text:
            if char.isupper():
                new_index = ((ord(char) + (self.interval - 65)) % 26) + 65
                new_char = chr(new_index)
                cipher += new_char
            elif char.islower():
                new_index = ((ord(char) + (self.interval - 97)) % 26) + 97
                new_char = chr(new_index)
                cipher += new_char
            else:
                cipher += char
        return cipher

    def decrypt(self):
        "decrpyting text by given interval"
        cipher = ""
        for char in self.text:
            if char.isupper():
                new_index = ((ord(char) + (self.interval - 65)) % 26) + 65
                new_char = chr(new_index)
                cipher += new_char
            elif char.islower():
                new_index = ((ord(char) + (self.interval - 97)) % 26) + 97
                new_char = chr(new_index)
                cipher += new_char
            else:
                cipher += char
        return cipher


def cipher(text, shiftkey):
    t = Cipher(text, shiftkey)
    result = t.encrypt()
    return result


# TESTS#
# text = Cipher("Mars Rover landed at 6:00 CET!", 6)
# print(text.encrypt())
# sifra = Cipher("Sgxy Xubkx rgtjkj gz 6:00 IKZ!", -6)
# print(sifra.decrypt())
print(cipher("Mars Rover landed at 6:00 CET!", 3))
print(cipher("Abcd", 2))  # should return "Cdef"
print(cipher("message", -1))  # should return "ldrrzfd"
print(cipher("ZZ Top", 3))  # should return "CC Wrs"
