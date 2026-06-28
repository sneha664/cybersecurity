from decrypt import caesard

# Intercepted Ciphertext
ciphertext = input("Enter the intercepted ciphertext: ")

print("\nTrying all possible keys...\n")

# Outer Loop (Key = 1 to 25)
for k in range(1, 26):

    plaintext = ""

    # Inner Loop (Character by Character)
    for ch in ciphertext:
        plaintext += caesard(k, ch)

    print("Key =", k, "->", plaintext)