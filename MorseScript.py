"""
Morse.py
Convert text files to Morse Code.
"""
"""
This package must be import in command-line style (= console based)
>>> import sys
"""
morseFunc = lambda character: character.isalnum() and bin(
'  ETIANMSURWDKGOHVF L PJBXCYZQ  54 3   2     16       7   8 90'
.find(character.upper()))[3:].replace('0', '.').replace('1', '-') or character
# characters will be converted to corresponding Morse code.
"""
This script is based on tree representation of Morse code key and a tree search.
A satisfying picture of mentioned tree is available here:
    https://en.wikipedia.org/wiki/File:Morse_code_tree3.png

Assume '1' as '-' and '0' as '.'

Character           Morsed          Binary          Decimal
'E'                 '.'             0b1 0           2
'T'                 '-'             0b1 1           3
'I'                 '..'            0b1 00          4
'A'                 '.-'            0b1 01          5
'N'                 '-.'            0b1 10          6
'M'                 '--'            0b1 11          7
'S'                 '...'           0b1 000         8
'U'                 '..-'           0b1 001         9
...

As it's obvious, by sorting English alphabet in Morse tree in an array, Binary
value of each character's index, from 4th digit to end, represents it's Morsed-
form with '0's and '1's.
Base of our algorithm is this simple principle.
"""
morseCode = lambda word:''.join([''+morseFunc(character) for character in word])
# "morseCode(word)" converts a single word or a string into Morse code.
"""
Uncomment these lines below to have console-based arguments passing:
>>> source = open(sys.argv[1], 'r')
>>> morsed = open(sys.argv[1] + 'm.txt', 'w')
>>> morsed.write(morseCode(source.read()))
"""
def morseFile(address): # NOTE: File must be saved as an ANSI decoded text
    sourceFile = open(address, 'r').read()  # read the text file and save as as
                                            # string variable "sourceFile"
    name = 'morsed_' + address.split('\\')[-1]  # generate morsed text name as
                                                # morsed_filename.txt
    morsedFile = open(name, 'w')                # open a new file to save text
                                                # converted in Morse code.
    morsedText = morseCode(sourceFile)
    morsedFile.write(morsedText)    # write the string into file.
    morsedFile.close()  # close file
    print(morsedText)
