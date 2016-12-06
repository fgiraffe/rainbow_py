#import subprocess
#
#subprocess.call(["which", "python"])

txt = open("../idle_noise_11_30.txt")
contents = txt.read()
contents = contents.replace("\n", " ")
contents = contents.replace("[", "")
contents = contents.replace("]", "")
contents = contents.replace(")", "")
contents = contents.replace("(", "")
contents = contents.replace("'", "")
contents = contents.replace(".", " ")
contents = contents.replace(",", " ")
word_list = contents.split(" ")
txt.close()

poem_words = []

seed_phrase = "idle noise in the morning"
seed_words = seed_phrase.split(" ")
seed_count = len(seed_words)

seed_phrase = seed_phrase.replace(" ", "")
for char_idx in range(len(seed_phrase)):
    # find a word from the list that matches
    target_char = seed_phrase[char_idx]
    
    for a_word in word_list:
        if len(a_word) > char_idx and a_word[char_idx] == target_char:
            
            #don't reuse the same word
            if a_word in poem_words:
                continue
            else:
                poem_words.append(a_word)
            break
    
for aw in poem_words:
    print aw
    

