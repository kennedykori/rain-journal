from colorama import Fore, Back, Style
from pyfiglet import Figlet
f = Figlet(font='slant')
a = f.renderText('Welcome')
print(Fore.GREEN + a)


def rainjournal(username):
    print "Please Enter Username To Continue"
    name = raw_input("Enter your username : ").format(username)
    print "Welcome {0} ".format(username) + name.capitalize()
    print(type(name))
    while (len(name) <= 0):
        print "Kindly provide username or logout"
        name = raw_input("Enter your username : ").format(username)

rainjournal('')
