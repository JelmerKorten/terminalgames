#passwordmanagar file
#store and organise user name and password
#we will sort of encrypt it, as practice


#create a decoder
#placeholder for the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
characters = [' ','?','!','.',',','\'']

#adjust for capitals
def dogstring1(string,keyword):
    dogstring = ''
    index = 0
    for i in range(len(string)):
        if not string[i] in characters:
            dogstring += keyword[index % len(keyword)]
            index += 1
        else:
            dogstring += string[i]
    # print(dogstring)
    return dogstring


#adjust for caps
def str_coder(string,keyword,side='decode',length=6):

    if not side.lower() in ['code','decode']:
        print('Select a valid offset, either  \'decode\' (default) or specify \'code\'')
        return
    
    if side == 'code':
        string = string*length

    new_string = '' #temp new string

    dogstring = dogstring1(string,keyword) #call on the dogstring creator function

    #offset
    for character_index in range(len(string)):
        if string[character_index] in characters: #if it's one of these chars, dont change
            new_string += string[character_index]
        else: #if it's one of these, change by offset
            charindex = alphabet.find(string[character_index])
            offset = alphabet.find(dogstring[character_index])
            if side.lower() == 'code':
                newchar = alphabet[((charindex + offset)%52)] #allows for overflow to go back to start of alphabet
            else:
                newchar = alphabet[((charindex - offset)%52)] #allows for overflow to go back to start of alphabet
            new_string += newchar

    if side == 'decode':
        return new_string[:(int(len(string)/length))]
    return new_string


#get personal decoding password
master_pwd = input('What is your personal password?\n')

#viewing passwords
def view():
    try:
        with open('files/passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split('|')
                user = str_coder(user,master_pwd,'decode')
                passw = str_coder(passw,master_pwd,'decode')
                print(f'User: {user} -- Passwmord: {passw}')
    except FileNotFoundError:
        print("Sorry, you're the first to login, no file yet.")


#adding passwords
def add():
    name = input('Account Name:\n')
    name = str_coder(name, master_pwd, 'code')
    pwd = input('Password:\n')
    pwd = str_coder(pwd,master_pwd,'code')
    

    with open('files/passwords.txt', 'a') as f:
        f.write(name + '|' + pwd + '\n')


#ask if add or view?
print('Would you like to add a new password, or view existing ones?')
while True:
    mode = input('(add/view or "q" to quit)\n').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue