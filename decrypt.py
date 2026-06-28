def caesard(shift, text):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char

    return result
# decrypted = ""

# for ch in encrypted:
#     plain_char = caesar_decode(ch, shift)
#     print(ch, "->", plain_char)
#     decrypted += plain_char