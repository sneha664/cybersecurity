# ==============================
# Caesar Cipher Encryption
# ==============================
def caesare(shift, text):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


# ==============================
# Caesar Cipher Decryption
# ==============================
def caesard(shift, text):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char

    return result


# ==============================
# MAIN PROGRAM (Sender & Receiver)
# ==============================

# Secure Key (from roll number)
roll_no = 1
k = roll_no % 26

# Plaintext message
x = "SNEHA SHAH"

print("========== SENDER ==========")
print("Plaintext :", x)
print("Key       :", k)

# Encryption process (Sender side)
y = caesare(k, x)

print("Ciphertext:", y)

print("\nSending Ciphertext and Key...")
print("Ciphertext Sent:", y)
print("Key Sent       :", k)

# ==============================
# Receiver Side
# ==============================

print("\n========== RECEIVER ==========")
print("Received Ciphertext:", y)
print("Received Key       :", k)

# Decryption process (Receiver side)
received_text = caesard(k, y)

print("Recovered Plaintext:", received_text)