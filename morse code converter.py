#morse code -> english, vise versa
#accept string/output string
#reminder to make string input capitals if alphabet, else leave as is
#use string.replace(<target>, <replace>)

morse_dict = {'A':'.-', 'B':'-...', 
            'C':'-.-.', 'D':'-..', 'E':'.', 
            'F':'..-.', 'G':'--.', 'H':'....', 
            'I':'..', 'J':'.---', 'K':'-.-', 
            'L':'.-..', 'M':'--', 'N':'-.', 
            'O':'---', 'P':'.--.', 'Q':'--.-', 
            'R':'.-.', 'S':'...', 'T':'-', 
            'U':'..-', 'V':'...-', 'W':'.--', 
            'X':'-..-', 'Y':'-.--', 'Z':'--..', 
            '1':'.----', '2':'..---', '3':'...--', 
            '4':'....-', '5':'.....', '6':'-....', 
            '7':'--...', '8':'---..', '9':'----.', 
            '0':'-----', ', ':'--..--', '.':'.-.-.-', 
            '?':'..--..', '/':'-..-.', '-':'-....-', 
            '(':'-.--.', ')':'-.--.-'}

def morse(english_input):
    output = ''

    english_input = english_input.upper()
    
    for c in english_input:
        if c != ' ':
            output += morse_dict[c] + ' '
        else:
            output += ' '

    return output

def english(morse_input):
    output = ''

    '''code section here just swaps keys with values from morse_dict'''
    morse_swapped = {}
    morse_klist = list(morse_dict.keys())
    morse_vlist = list(morse_dict.values())
    for k, v in zip(morse_klist, morse_vlist):
        morse_swapped[v] = k

    temp_list = morse_input.split(' ')

    for word in temp_list:
        if word == ' ' or word == '':
            output += ' '
        else:
            output += morse_swapped[word]

    return output

while True:
    try:
        english_input = input("Enter string\n")
        print(morse(english_input))
        morse_input = input("Input morse\n")
        print(english(morse_input))
    except ValueError:
        continue

