import sys

class Anti_soft_Drink():
    print ""
    print "This is a console program that predicts when a user will be diabetic."
    ## Introduction By Raindolf ##
   
    print ""
    print ""
    ## Creatin a space for the user to input his or her details ##
    print "Please enter your full name:"
    name = raw_input()
    print "Welcome " + name + ", this is a basic Python program that predicts when u are liable to be diabetic."
    print ""
    while True:
        print "Please enter the number of times you take soft drinks in a week: "
        soft_num = int(input())
        
        if 21 <= soft_num <= 30:
            print "Stop taking soft drinks or you will have yourself to blame once you are diagnosed with diabetis"
            
        elif 11 <= soft_num <= 20:
            print "You have to reduce it to less than 5 in a week or you will be diabetic in not less than 5 years"
            
        elif 3 <= soft_num <= 10:
            print "Please Reduce your intake of soft drinks or in 15 yrs you will be diabetic"
            
             else:
            print ""
            print ""
            print "Thanks " + name + " , for taking my Anti-Soft drink advice."
          
            sys.exit()
## Send me your emails for more raindolf@oasiswebsoft.com ##
