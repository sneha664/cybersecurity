from collections import Counter
import re

ctext = """UQ UZ D EMDRQUNRX GDB . TPB DYM TM ZUQQUIO UI D GDYW YJJH YMDGUIO QPUZ HMZZDOM ? EMFDRZM UZ UZ NRI , ERQ UN TM GJ IJQ OMQ HJYM M ’Z TM TUXX ZQDB PMYM NJYMSMY"""

# ==============================
# CLEAN TEXT
# ==============================
text = re.sub(r'[^A-Z]', '', ctext.upper())

# ==============================
# SINGLE LETTER FREQUENCY
# ==============================
print("\n===== SINGLE LETTER FREQUENCY =====")

freq = Counter(text)
total = len(text)

print("\nTOP 5 LETTERS:")
for letter, count in freq.most_common(5):
    print(letter, count)

# ==============================
# DIGRAM ANALYSIS
# ==============================
print("\n===== DIGRAMS =====")

digrams = [text[i:i+2] for i in range(len(text)-1)]
digram_freq = Counter(digrams)

for pair, count in digram_freq.most_common(10):
    print(pair, "->", count)

# ==============================
# TRIGRAM ANALYSIS
# ==============================
print("\n===== TRIGRAMS =====")

trigrams = [text[i:i+3] for i in range(len(text)-2)]
trigram_freq = Counter(trigrams)

for tri, count in trigram_freq.most_common(10):
    print(tri, "->", count)

# ==============================
# SIMPLE MANUAL SUBSTITUTION TOOL
# ==============================
def substitute(text, old, new):
    return text.replace(old.upper(), new.lower())

# Example substitution (you can change manually)
ctext = substitute(ctext, 'M', 'e')

print("\n===== AFTER SUBSTITUTION =====")
print(ctext)
