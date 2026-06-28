# cybersecurity
# 🔐 Caesar Cipher Cryptography Lab (Cyber Security)

## 📌 Aim
To implement a Caesar Cipher encryption and decryption system using Python and simulate secure communication between sender and receiver. Also, to demonstrate how a brute-force attack can break the cipher.

---

## 📖 Theory

The Caesar Cipher is a substitution cipher in cryptography where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

It is one of the simplest encryption techniques used to understand the basics of cryptography.

---

## 🔑 Mathematical Formula

### Encryption:
C = (P + K) mod 26

### Decryption:
P = (C - K) mod 26

Where:
P = Plaintext character
C = Ciphertext character
K = Secret key (shift value)

### Encryption:
    Encryption is the process of converting plain text (readable data) into cipher text (unreadable data) using a secret key. It is used to protect information so that only authorized users can read it.

### Decryption:
     Decryption is the reverse process of encryption. It converts cipher text back into plain text using the same secret key, so the original message can be     understood again.

---

## 🔄 Working Process

### 🟢 Sender Side
1. Plaintext message is taken.
2. Key K is generated.
3. Each character is encrypted using Caesar cipher.
4. Ciphertext is generated and sent along with key.

---

### 🔵 Receiver Side
1. Ciphertext and key are received.
2. Reverse shift is applied.
3. Original plaintext is recovered.



### 🔹 Brute Force Algorithm
1. Take ciphertext only (unknown key)
2. Try all keys from 1 to 25
3. Decrypt using each key
4. Observe readable output to find correct key

---

## 📡 Communication Model

Sender Side:
Plaintext → Encryption → Ciphertext + Key

Receiver Side:
Ciphertext + Key → Decryption → Plaintext

## 💣 Brute Force Attack

In brute force attack, the attacker does not know the key. Therefore, all possible keys from 1 to 25 are tried.

The correct plaintext is identified by observing readable output.
## 🚀 Conclusion

- Caesar cipher is a basic encryption technique.
- It works using simple shift operations.
- Encryption and decryption are inverse operations.
- It is vulnerable to brute force attack due to limited key space (1–25).

---

## 📚 Learning Outcome

- Understanding of basic cryptography concepts
- Implementation of encryption and decryption in Python
- Concept of secure communication
- Introduction to brute force attacks in cybersecurity

---
