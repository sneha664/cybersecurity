from encrypt import caesare
from decrypt import caesard

# Secure Key
roll_no = 1
k = roll_no % 26


x = "SNEHA SHAH"

print("========== SENDER ==========")
print("Plaintext :", x)
print("Key       :", k)

y = caesare(k, x)

print("Ciphertext:", y)

print("\nSending Ciphertext and Key...")
print("Ciphertext Sent:", y)
print("Key Sent       :", k)

# ---------------- Receiver Side ----------------
print("\n========== RECEIVER ==========")
print("Received Ciphertext:", y)
print("Received Key       :", k)

received_text = caesard(k, y)

print("Recovered Plaintext:", received_text)