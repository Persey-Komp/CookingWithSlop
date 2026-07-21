#!/usr/bin/env python3
"""
Word Salad Generator
---------------------
Takes a large word list and randomly selects a chunk of words (count varies
between ~100 and ~170) to produce a strange, grammar-free word salad in the
style of the "Markovian Parallax Denigrate" spam incident.

Usage:
    python word_salad.py path/to/wordlist.txt output.txt

The wordlist file should contain one word per line (or words separated by
whitespace) -- it can be a dictionary file, a scraped corpus, etc.
"""

import random
import sys
import re


def load_words(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    # split on any whitespace, strip punctuation, drop empties
    raw = re.split(r"\s+", text)
    words = [re.sub(r"[^\w'-]", "", w) for w in raw]
    words = [w for w in words if w]
    return words


def generate_salad(words, min_count=100, max_extra=70):
    count = min_count + random.randint(0, max_extra)
    if count > len(words):
        count = len(words)
    chosen = random.sample(words, count)

    # Lightly mimic the original incident's look: capitalize first word of
    # pseudo-sentences, no real punctuation logic, just abrupt periods now
    # and then to break it into chunks.
    output_tokens = []
    sentence_len = 0
    for i, word in enumerate(chosen):
        token = word
        if sentence_len == 0:
            token = token.capitalize()
        output_tokens.append(token)
        sentence_len += 1
        # randomly end a "sentence" every 5-12 words
        if sentence_len >= random.randint(5, 12):
            output_tokens[-1] += "."
            sentence_len = 0

    if not output_tokens[-1].endswith("."):
        output_tokens[-1] += "."

    salad = " ".join(output_tokens)
    return salad, count


def main():
    if len(sys.argv) != 3:
        print("Usage: python word_salad.py <wordlist_file> <output_file>")
        sys.exit(1)

    wordlist_path = sys.argv[1]
    output_path = sys.argv[2]

    words = load_words(wordlist_path)
    if not words:
        print("No words found in wordlist file.")
        sys.exit(1)

    salad, count = generate_salad(words)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(salad + "\n")

    print(f"Generated salad with {count} words.")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
