file = open('Login.txt', 'a')
newUser = True

while newUser:
    user = input('Are you a new user? y/n, press q to quit: ')
    if user == 'y':
        print('Create an account.\n')
        newUsername = input('Enter New Username: ')
        with open('Login.txt', 'r') as e:
            for line in e:
                loginInfo = line.strip().split(',')
                if newUsername == loginInfo[0]:
                    print('Error: that username is already in use.')
                    break
                else:
                    print('Username accepted\n')
                    newUsername = newUsername.strip()
                    newPassword = input('Enter New Password: ')
                    if len(newPassword) < 5:
                        print('Error: Not enough characters.')
                    elif len(newPassword) > 16:
                        print("Error: Not enough characters")
                    else:
                        confirmPass = input('Confirm your password: ')
                        if confirmPass == newPassword:
                            print('Account Created')
                            newPassword = newPassword.strip()
                            file.write(newUsername)
                            file.write(',')
                            file.write(newPassword)
                            file.write('\n')
                            file.close()
                            print('Your login details have been saved.')
            
    else:
        newUser = False

    if user == 'n':
        userName = input('Enter your username: ').strip()   
    with open('Login.txt', 'r') as f:
        for line in f:
            loginInfo = line.strip().split(',')
            if userName == loginInfo[0]:
                passWord = input('Enter your password: ').strip()
                if passWord == loginInfo[1]:
                    print('Login successful')
                else:
                    print('Incorrect password')
            else:
                print('Username does not exist')
        else:
            print('invalid input')
            break
    
while not newUser:
    if user == 'q':
        print('Quitting...')
        break