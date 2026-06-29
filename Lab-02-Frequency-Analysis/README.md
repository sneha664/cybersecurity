# Frequency Analysis of a Monoalphabetic Substitution Cipher

## Aim

To perform frequency analysis on a monoalphabetic substitution cipher by counting the occurrence of letters, digrams, and trigrams, and use manual substitution to assist in decrypting the ciphertext.

---

# Objective

* To understand the concept of frequency analysis in classical cryptography.
* To calculate the frequency of individual letters in a ciphertext.
* To identify the most frequent digrams and trigrams.
* To compare the obtained frequencies with the Standard Frequency Distribution (SFD) of the English language.
* To perform manual substitutions to gradually decrypt the encrypted message.

---

# Theory

Frequency analysis is one of the oldest and most effective techniques for breaking a **monoalphabetic substitution cipher**. In this type of cipher, each plaintext letter is replaced with another letter while maintaining a one-to-one mapping.

Since English letters do not occur with equal frequency, some letters appear more often than others. For example, the letter **E** is the most common letter in English, followed by **T, A, O, I,** and **N**. By comparing the frequency of letters in the ciphertext with the Standard Frequency Distribution (SFD), probable substitutions can be identified.

In addition to single-letter frequencies, common two-letter combinations (digrams) such as **TH, HE, IN, ER** and three-letter combinations (trigrams) such as **THE, AND, ING** provide additional clues that help recover the original plaintext.

The decryption process is usually iterative. After making an initial substitution, the partially decrypted text is examined, and further substitutions are performed until the complete message is obtained.

---

# Standard Frequency Distribution (SFD)

| Letter | Frequency (%) | Letter | Frequency (%) |
| ------ | ------------: | ------ | ------------: |
| A      |           8.2 | N      |           6.7 |
| B      |           1.5 | O      |           7.5 |
| C      |           2.8 | P      |           1.9 |
| D      |           4.3 | Q      |           0.1 |
| E      |          12.7 | R      |           6.0 |
| F      |           2.2 | S      |           6.3 |
| G      |           2.0 | T      |           9.1 |
| H      |           6.1 | U      |           2.8 |
| I      |           7.0 | V      |           1.0 |
| J      |           0.2 | W      |           2.4 |
| K      |           0.7 | X      |           0.2 |
| L      |           4.0 | Y      |           2.0 |
| M      |           2.4 | Z      |           0.1 |

---



---

# Procedure

1. Import the required Python libraries (`collections` and `re`).
2. Store the ciphertext in a string variable.
3. Remove all non-alphabetic characters using regular expressions.
4. Count the frequency of each alphabet using `Counter`.
5. Display the five most frequent letters.
6. Generate and count digrams.
7. Generate and count trigrams.
8. Create a substitution function for replacing guessed cipher letters.
9. Perform manual substitution.
10. Display the updated ciphertext after substitution.

---



---

# Output

Example output produced by the program:

```
===== SINGLE LETTER FREQUENCY =====

TOP 5 LETTERS:
M 16
Q 11
U 10
Z 9
D 8

===== DIGRAMS =====

TM -> 5
UZ -> 4
QP -> 4
...

===== TRIGRAMS =====

UQZ -> 3
TMZ -> 3
...

===== AFTER SUBSTITUTION =====

UQ UZ D EeDRQUNRX GDB . TPB DYe Te ZUQQUIO UI D GDYW
YJJH YeDGUIO QPUZ HeZZDOe ? EeFDRZe UZ UZ NRI ,
ERQ UN Te GJ IJQ OeQ HJYe e'Z Te TUXX ZQDB PeYe NJYeSeY
```

*(The exact frequencies may vary depending on the ciphertext.)*

---

# Result

The program successfully performed frequency analysis by calculating the frequencies of letters, digrams, and trigrams. Manual substitution was applied to partially decrypt the ciphertext, demonstrating how frequency analysis can be used to attack monoalphabetic substitution ciphers.

---

# Conclusion

Frequency analysis is an effective cryptanalysis technique for monoalphabetic substitution ciphers because English letters and letter combinations follow predictable frequency patterns. By analyzing single letters, digrams, and trigrams and comparing them with the Standard Frequency Distribution, likely substitutions can be identified. Although a single substitution does not fully decrypt the message, repeated substitutions gradually reveal the original plaintext. This experiment demonstrates the practical application of statistical analysis in classical cryptography.

---

# Applications

* Cryptanalysis of classical substitution ciphers.
* Learning cryptographic attack techniques.
* Information security education.
* Pattern recognition in encrypted text.
* Understanding historical cipher-breaking methods.

---

# Limitations

* The program does not automatically determine substitutions.
* Manual guessing is required for complete decryption.
* Works best with sufficiently long ciphertexts.
* Not suitable for modern encryption algorithms such as AES or RSA.

---

