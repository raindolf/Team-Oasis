import sys

class Anti_soft_Drink():
    print '''Diabetes mellitus, often simply referred to as diabetes, \n is a group of metabolic diseases in which a person has high blood sugar, \
either because the body does not produce enough insulin, 
or because cells do not respond to the insulin that is produced.
This high blood sugar produces the classical symptoms of \n polyuria (frequent urination), polydipsia (increased thirst) and \n  polyphagia (increased hunger)"
    This is a console program that predicts if a user is liable to
    be diabetic.'''
    ## Introduction By Tonte ##
   
    print ""
    print ""
    ## Creating a space for the user to input his or her details ##
    print "Please enter your name:"
    name = raw_input()
    print "Welcome " + name + ", this is a basic Python program that predicts if your lifestyle makes you prone to diabetes."
    print " After every test you are awarded with points at the end,\
    the fewer points you have, the better"

    print " This program comprises of a series of tests"
    raw_input( "Press <enter> to begin" )

print " Are you male or female"
user_gender = raw_input ( " m / f    ")
if user_gender == "m":
    print "Males are more likely to be diabetic"
    point_0= int(3)
    print "You have gained 3 points"
elif user_gender == "f":
    print " Females are less likely to be diabetic"
    point_0 = int(0)
    print " You have gained 0 points"

raw_input( "press <enter> to continue" )


print " How old are you?"   
user_age = int (input())
if 44< user_age <55 :
        print " You are more prone to diabetes"
        point_1= int(4)
        print " you have gained 4 points"
elif 66< user_age <200:
        print "Your age group is tme most prone to diabetes"
        point_1= int(8)
        print " You have gained 8 points"

elif 55<= user_age <=64:
        print "People of this age group are prone to diabetes"
        point_1= int(6)
        print "You have gained 6 points"

elif 35< user_age <= 44:
        print " You are less prone to get diabetes"
        point_1 = int(2)
        print "you have two points"
elif 1<= user_age <=35:
        print " Getting diabetes is virtually impossible at this age unless you \
live a very unhealthy lifestyle or have a family history of diabetes"
        point_1 = int(0)
        print "you have 0 points"


raw_input( "press <enter> to continue" )

print " Do you smoke?  "
user_smoke = raw_input ("Type yes or no  " )
if user_smoke == "yes":
       print " Please try and desist from this habit, smoking can also cause lung cancer,kidney failure and other fatal disease"
       point_2= int (2)
       print "You have gained 2 points"
elif user_smoke== "no":
       print "Ok, as you may know, smoking is bad for our health. I am happy that you don't smoke"
       point_2= int(0)
       print " you have gained 0 points"

raw_input( "press <enter> to continue" )

print "Have either of your parents, or any of your brothers or sisters \
been diagnosed with diabetes (type 1 or type 2)?"
user_famhistory = raw_input ("Type yes or no  " )
if user_famhistory == "yes":
    print "you are at higher risk of getting diabetes"
    point_3= int(3)
    print "you have gained 3 points"

elif user_famhistory == "no":
    print "You are of lower risk"
    point_3 = int(0)
    print "you have gained 0 points"

raw_input( "press <enter> to continue" )


print "Are you currently taking medication for high blood pressure?"
user_bp = raw_input ("Type yes or no  " )
if user_bp == "yes":
    print " You are at higher risk"
    point_4= int(2)
    print "you have gained 2 points"
elif user_bp == "no":
    print " You are at lower risk"
    point_4= int(0)
    print " you have gained 0 points"

raw_input( "press <enter> to continue" )

print"How often do you eat vegetables or fruit?"
print "Everyday or not Everyday"
user_fruit = raw_input ("Type e or n  " )
if user_fruit == "e":
    print "Eating fruits everyday is essential to our health"
    point_5 = int(0)
    print "you have gained 0 points"

elif user_fruit == "n":
    print "Eating fruits everyday is essential to our health "
    point_5= int(1)
    print "you have gained 1 points"

    


raw_input( "press <enter> to continue" )

print" On average, would you say you do at least 2.5 hours of physical activity per week)?"
print "(for example, 30 minutes a day on 5 or more days a week)"
user_activity = raw_input ("Type yes or no  " )
if user_activity == "yes":
    point_6 = int(0)
    print " You have gained 0 points"
elif user_activity == "no":
    point_6= int(2)
    print "you have gained 2 points"

    
raw_input( "press <enter> to continue" )


print ". Have you ever been found to have high blood glucose (sugar)?"
print "(for example, in a health examination, during an illness, during pregnancy)"
user_sugar= raw_input ("Type yes or no  " )
if user_sugar == "yes":
    point_7= int(6)
    print "You have gained 6 points"
elif user_sugar == "no":
    point_7= int(0)
    print " you have gained 0 points"
    

raw_input( "press <enter> to continue" )

print " We have come to the end of our tests"
raw_input( "press <enter> to view your results" )


print" At the end of the test you have"
total = point_0 + point_1 + point_2 + point_3 + point_4 + point_5 + point_6 + point_7
print total
print "points"

raw_input( "press <enter> to continue" )





print" "
print" "
print" "
print" "
print"compare your results with the one below "
print" "
print '''5 or less: Low risk

Approximately one person in every 100 will develop diabetes.

\n
6 - 11: Intermediate risk

For scores of 6-8, approximately one person in every 50 will develop diabetes.
\

\For scores of 9-11, approximately one person in every 30 will develop diabetes.

\n
12 or more: High risk

For scores of 12-15, approximately one person in every 14 will develop diabetes.
For scores of 16-19, approximately one person in every seven will develop diabetes.
For scores of 20 and above, approximately one person in every three will develop diabetes.

NB. The overall score may overestimate the risk of diabetes in those aged less than 25 years'''
    


    





    
    




        


raw_input("Press <enter> to exit ")    
       
   

## Send me your emails for more raindolf@oasiswebsoft.com ##
## Kindly add us on fb www.fb.com/oasisweb ##
## Raindolf , I have updated the sourcecode and removed the 'while' statement,
## it is a loop and i don't get its use in the code.
## I also noticed that there is no result if soft_num is less than 3, so i added one.
## It also crashes when the user enters data that is not a number

