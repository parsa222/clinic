#clinic
    made by parsa222
    required modules:
    csv
    hashlib
    pandas
    winsound


most of the modules are already installed by default
if its not installed
try typing
    pip install <module name>
    such as:
    pip install pandas
in the command prompt

instruction:
you can either register on the main menu
or login with the default patient users
you can change the passwords as well
dont try to manually change it in the csv file
change the password when you are logged in and select <change password>
----------------

there are 3 types of users:

1- patient
    can book an appointment

2- doctors
    can check the appointments
    add items to buy list for clinic

3- admin
    add doctor user
    remove any users from database
    check buylist




all the passwords are encrypted (md5 hash) to be more secured!
-----
LIST OF USERS:

all patient users (u can also register yours):

    ali alizade
        user(code melli): 1234
        password = 1234

        mamad mamadi
            user = 6789
            password = mamad

    hassan hassani
        user = 4321
        pass = 4321
------
doctor users (u can also add a doctor user by loggin in as admin):

    dr.bob bobby
        user = 0000
        pass = 0000

    dr.alex smith
     user = 0001
     pass = 0001
-------------
    
    admin user :
        user = admin
        pass = admin
-----------------------

dont forgot to report if u notice any bugs in the program


PS... do not try to delete the admin user when logged in as admin!
