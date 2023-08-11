def main():

    inventory = ()
    selection = "a"
    morseCode = ""
    index = -1

    inventory = (
        (".-"), ("-..."), ("-.-."), #this third is letters A-Z in order
        ("-.."), ("."),("..-."),
        ("--."),("...."), (".."), 
        (".---"),("-.-"), (".-.."), 
        ("--"), ("-."),("---"), 
        (".--."), ("--.-"), (".-."), 
        ("..."),("-"), ("..-"),
        ("...-"),(".--"), ("-..-"),
        ("-.--"), ("--.."),

        ("-----"), #this third is numbers 0-9 in order
        (".----"), ("..---"), ("...--"), 
        ("....-"), ("....."),("-...."), 
        ("--..."), ("---.."),("----."),

        ("/"), ("..--.."), (".-.-.-"),
        ("--..--")
        )

    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ?.,'

    while selection != "q" and selection != "Q":
        print("\nMORSE CODE CONVERTER MENU")
        print("---------------------------")
        print("a) Enter a String to convert")
        print("q) Quit the program")

        selection = input("\nPlease make a selection: ")

        while selection != "a" and selection != "q":
            print("Invalid selection. Please try again!")
            selection = input("\nPlease make a selection: ")

        if selection in ("a","A"):
            morseCode = ""
            words = input("Please enter a word: ")
            words = words.upper()

            while words == False:
                print("\nInvalid Input. Try Again!")
                words = input("Please enter a word: ")
                words = words.upper()
                words = words.isalnum()

            for word in words:
                wordIndex = characters.index(word)
                if wordIndex >= 0:
                    morseCode = morseCode + inventory[wordIndex] + " "

            print("\nThe morse code for the word(s) " + words + " is: " + morseCode)

main()