#!/usr/bin/env python3

import sys
from ibm1_library import *
import punctuation


def clean_sentence(sentence: str):
    sentence = sentence.strip()
    result = ""
    white_space = 0
    for c in sentence:
        white_space = white_space + 1 if c == " " else 0
        if white_space > 1:
            continue
        if c not in punctuation.PUNCTUATION:
            result += c
    return result


def load_sentence_aligned_corpus(source_file: str, target_file: str):
    with open(source_file, "r") as f:
        source_sentences = f.readlines()

    with open(target_file, "r") as f:
        target_sentences = f.readlines()

    if len(source_sentences) != len(target_sentences):
        raise ValueError("Files don't have the same number of sentences")

    pairs = []
    for i in range(len(source_sentences)):
        source_sentence = clean_sentence(source_sentences[i])
        target_sentence = clean_sentence(target_sentences[i])
        pairs.append((source_sentence.split(" "), target_sentence.split(" ")))
    return pairs


if __name__ == "__main__":
    args = sys.argv

    if len(args) != 2 + 1:
        print("Usage: ")
        print(f"{args[0]} <source_sentences> <target_sentences>")
        exit()

    sentence_pairs = load_sentence_aligned_corpus(args[1], args[2])

    print("Sentence pairs loaded")
    probability = calc_alignment_probability(sentence_pairs)

    for key in probability.keys():
        if probability[key] > 0.2:
            print(f"{key}: {probability[key]}")
