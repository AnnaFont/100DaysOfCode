alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Function that allows to encode a word
def caesar_encode_decode(word_in, shift_in, function_in):
    if function_in == "decode":
        shift_in = - shift_in
    # Encode the word
    new_word = ""
    for letter in word_in:
        if letter not in alphabet:
            new_word = new_word + letter
        else:
            index_alphabet = alphabet.index(letter) + shift_in
            # it could be used easier: index_alphabet = %= len(alphabet)
            if index_alphabet >= len(alphabet):
                index_alphabet = index_alphabet - len(alphabet)
            new_word = new_word + alphabet[index_alphabet]
    print("The new word is", new_word)
    return new_word


# Caesar Cipher - encode the messages
wordIn = ""
continueLoop = True
while continueLoop:
    funcIn = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
    if funcIn == "encode":
        wordIn = input("Type your message:").lower()
    shiftIn = int(input("Type the shift number:"))
    wordIn = caesar_encode_decode(wordIn, shiftIn, funcIn)
    if input("Continue playing? (Yes/No)").lower() == "no":
        continueLoop = False
