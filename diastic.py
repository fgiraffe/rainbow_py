#!/usr/bin/python
# -*- coding: utf-8 -*-

# http://intercapillaryspace.blogspot.com/\
# 2012/03/mac-lows-diastic-process-in-gale.html


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


def pick_random_word(word_list):
    indx = random.randint(0, len(word_list) - 1)
    return word_list[indx]


def clean_source_text(raw_chars, bad_chars_dict):
    """ remove any unwanetd characters from given text
    raw_chars -- characters to be read and cleaned
    bad_chars_dict -- dict of characters that are NOT allowed in raw_chars

    returns character array of "clean" text
    """
    cleaned_chars = raw_chars

    for (bad_char, new_char) in bad_chars_dict.items():
        cleaned_chars = cleaned_chars.replace(bad_char, new_char)

    return cleaned_chars


def gather_source_words(file_name):
    clean_words = []

    # read in everything, warts and all
    txt = open("../idle_noise_11_30.txt")
    raw_contents = txt.read()
    txt.close()

    # remove unwanted chars
    clean_text = clean_source_text(raw_contents, BAD_CHARS_DICT)

    # remove duplicate words by adding them to a set
    # also remove the 1 character words

    word_list = clean_text.split(" ")
    word_set = set()
    for aWord in word_list:
        if len(aWord) > 1:
            word_set.add(aWord)

    clean_words = list(word_set)

    return clean_words


def create_poem_diastic(poem_seed, poem_src_words):
    poem_words = []

    for char_idx in range(len(poem_seed)):
        # find a word from the list that "matches"
        target_char = seed_phrase[char_idx]
        matched = False

        for a_word in word_list:
            if len(a_word) > char_idx and a_word[char_idx] == target_char:

                # don't reuse the same word
                if a_word in poem_words:
                    print "REUSING"
                    continue
                else:
                    poem_words.append(a_word)
                    matched = True
                break

        if matched is False:
            # failed to find a word
            replacement_word = pick_random_word(word_list)
            poem_words.append(replacement_word)

    return poem_words


# #######################################################
# #######################################################

if __name__ == '__main__':
    random.seed()
    word_list = gather_source_words("../idle_noise_11_30.txt")

    orig_seed_phrase = "idle noise in the morning"
    # seed_phrase = "abcdefg"
    seed_phrase = orig_seed_phrase.replace(" ", "")

    poem = create_poem_diastic(seed_phrase, word_list)

    for aw in poem:
        print aw
