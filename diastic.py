#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

# table of chars to strip and what to replace them with
BAD_CHARS_DICT = {"\n": " ",
                  "[": "",
                  "]": "",
                  "{": "",
                  "}": "",
                  "(": "",
                  ")": "",
                  "♠": "",
                  "✔": "",
                  '/': "",
                  '7"': "",
                  "'": "",
                  ".": "",
                  '-': "",
                  ":": "",
                  "&": "",
                  "#": "",
                  ",": " "}


def clean_source_text(raw_chars, bad_chars_dict):
    cleaned_chars = raw_chars

    for (bad_char, new_char) in bad_chars_dict.items():
        cleaned_chars = cleaned_chars.replace(bad_char, new_char)

    return cleaned_chars


# #######################################################
# #######################################################

random.seed()

# read in everything, warts and all

txt = open("../idle_noise_11_30.txt")
raw_contents = txt.read()
txt.close()

# remove unwanted chars
clean_text = clean_source_text(raw_contents, BAD_CHARS_DICT)

# remove duplicate words
word_list = clean_text.split(" ")
word_set = set()
for aWord in word_list:
    word_set.add(aWord)

# while len(word_set) > 0:
#    a_word = word_set.pop()
#    print a_word


poem_words = []

seed_phrase = "idle noise in the morning"
# seed_phrase = "abcdefg"
seed_words = seed_phrase.split(" ")
seed_count = len(seed_words)
seed_phrase = seed_phrase.replace(" ", "")


def pick_random_word(word_list):
    indx = random.randint(0, len(word_list) - 1)
    return word_list[indx]


for char_idx in range(len(seed_phrase)):
    # find a word from the list that matches
    target_char = seed_phrase[char_idx]
    matched = False


#    print "\nTarget Char:",
#    print target_char,
#    print char_idx

    for a_word in word_list:
        if len(a_word) > char_idx and a_word[char_idx] == target_char:

            # don't reuse the same word
            if a_word in poem_words:
                print "REUSING"
                continue
            else:
                # print "Adding ",
                # print a_word,
                # print " ind: ",
                # print char_idx
                poem_words.append(a_word)
                matched = True
            break

    if matched is False:
        # failed to find a word
        replacement_word = pick_random_word(word_list)
        poem_words.append(replacement_word)
        print "FAILED on Target Char:",
        print target_char,
        print char_idx,
        print "Using <%r> instead" % (replacement_word)


for aw in poem_words:
    print aw
