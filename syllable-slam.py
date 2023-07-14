import sys

def count_vowels(word):
    count = 0
    vowel_state = False
    word = word.lower()
    if word.isalpha() != True:
        return 0
    # count vowel groups
    # when we encounter a vowel we set vowel_state to true and 
    # add 1 to the count, we ignore all further vowels until a
    # consonant is encountered, which resets vowel_state
    # we dont reset on y as it might be a vowel
    place = 0
    for c in word:

        if c in ('a', 'e', 'i', 'o', 'u', 'y'):
            # vowel state is false and this is not a final e 
            # (if final e is not the only vowel)
            if vowel_state is False and not (place == len(word)-1 and c == 'e' and count > 0):
                count = count+1
                vowel_state = True
 
        else:
            vowel_state = False    

 
        if c == 'y' and place == 0:
            count = count-1

        # ending in "ed" only adds a syllable when preceded by t
        # otherwise the e is effectively silent
        elif c == 'd' and place == len(word)-1:        
            if word[place - 1] == 'e' and word[place - 2] != 't' and count > 1:
                count = count - 1

        # "ble" ending is a syllable
        elif c == 'e' and place == len(word)-1:        
            if word[place - 1] == 'l' and word[place - 2] == 'b':
                count = count + 1

        # "io" is ee-oh except in "ion" where its mostly pronounced "on"
        # and "cio" is "sho"
        elif c == 'o' and place != len(word)-1:        
            if (word[place - 1] == 'i' and word[place +1] != 'n' and word[place-2] != 'c') or (word[place-1] == 'u'):
                count = count + 1


        place = place+1
    if "ia" in word:
        count = count+1
    print(count)
    return count

for word in sys.stdin:
    if 'Exit' == word.strip():
        break
    count_vowels(word.strip()) ## pass that into the function which will print the number of syllables

