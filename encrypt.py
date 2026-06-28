def caesare(shift, text):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result
# encrypted = ""

# for ch in message:
#     cipher_char = caesar_encode(ch, shift)
#     print(ch, "->", cipher_char)
#     encrypted += cipher_char