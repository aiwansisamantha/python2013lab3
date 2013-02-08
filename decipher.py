# Filename: decipher.py
# Author: Samantha Ai
# Description: You are provided an encrypted text document MYSTERY.IN. Performing suitable automatic document analysis to generate the top 3 words which you feel will
#              best represent its semantics.

# it is related to a Fibonacci number 5
# there is a uniqueness property about 5
# each character is ASCII shifted by 5

try:
    infile = open("MYSTERY.IN", 'r')
    outfile = open("RESULT.OUT", 'w')
    x = 5
    lines = infile.readlines()
    result = ''
    # decipher text
    for line in lines:
        for i in range(0, len(line)-1):
            if ord(line[i]) < 5:
                line[i] == chr(ord(line[i]) + 128)
            decrypted = chr(ord(line[i]) - 5)
            result = result + decrypted
    print(result)

    # automatic document analysis
    words = []
    n = 0
    l = 0
    for i in range(0, len(result)-2):
        if ord(result[i]) < 65 or  90 < ord(result[i]) < 97 or ord(result[i]) > 122:
            words.append(result[:i])
            result = result[i+1:]
    print(words)

    # remove all punctuations
    # convert to upper/lower case
    # add all words to list
    # remove non-significant words (eg articles, pronouns, etc)
    # compute frequencies of remaining words
    # analyse top 3 most frequent words
    
    outfile.close()
    infile.close()
except IOError:
    print("Error reading from MYSTERY.IN or writing to RESULT.OUT.")
