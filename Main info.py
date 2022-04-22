print("Information Storer")
add = input("Would you like to add information? (Yes/ No) \n").lower()
if add == "yes":
    def write_file():
        myFile = open("information.txt","w")
        keepGoing = True
        while keepGoing:
            website = input("What is the website? \n")
            space = " "
            myFile.write(website)
            myFile.write(space)
            username = input("What is the username? \n")
            myFile.write(username)
            myFile.write(space)
            password = input("What is the password? \n")
            myFile.write(password)
            myFile.write("\n")
            print("Information Stored")
            keepGoing = False
        myFile.close()
    write_file()

elif add == "no":
        myFile = open("information.txt","r")
        word = input("What website do you want to search for? \n")
        search = " "
        search = myFile.readline()
        line = search.split()
        print(line)
        """
        while(s):
            search = myFile.readline()
            line = search.split()"""
else:
    (exit)
    
