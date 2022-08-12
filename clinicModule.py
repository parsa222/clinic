import csv
import hashlib
import pandas as pd
import soundeffectsmodule as sem
loggedin = False
is_admin = False
is_dr = False

user_pass = [[], []]
name_ln = [[], []]
# access[0] = dr or not
# access[1] = admin or not
access = [[], []]
#docusers = [] not needed anymore
userIndex = -1
interror = "INVALID ENTRY, you have to type a number!!!"
numberror = "the number that u have typed is not in the list!!"

patient_select = {1: "Make appointment",
                  2: "view made appointments",
                  3: "Change Password",
                  4: "Logout"}

doctor_select = {1: "view patient's appointments",
                 2: "add to buy list",
                 3: "Change Password",
                 4: "Logout"}

admin_select = {1: "view and delete users",
                2: "add Doctor user",
                3: "View shop list",
                4: "Change Password",
                5: "Logout"}

select1 = {1: "login",
           2: "register",
           3: "available doctors",
           4: "about us",
           5: "QUIT app"}


class Show:

    def show1(self):
        print("<-------------------->")
        print(("\033[1m Main Menu \033[0m"))
        for i in select1:
            print(f"{i}.{select1[i]}")

    def showpatient(self):
        print("<-------------------->")
        print(("\033[1m Patient \033[0m"))
        for i in patient_select:
            print(f"{i}.{patient_select[i]}")

    def select1(self):
        while True:
            try:
                si1 = int(input("select a number:"))
                if si1 == 1:
                    print("enter ur code melli and password:")
                    auth.login()
                    break
                elif si1 == 2:
                    print("register")
                    auth.register()
                    break
                elif si1 == 3:
                    print("-----")
                    print("available doctors:")
                    self.showdrlist()
                    break
                elif si1 == 4:
                    print("this is an online doctor appointment scheduling!")
                    break
                elif si1 == 5:
                    print("")
                    sounds.quitsound()
                    print("\033[1m <---GOODBYE!---> \033[0m")
                    quit()
                else:
                    print(numberror)
            except ValueError:
                print(interror)

    def showdrlist(self):
        auth.importing()
        for i in user_pass[0]:
            if access[0][user_pass[0].index(i)] == "1":
                print(f"dr.{name_ln[0][user_pass[0].index(i)]} {name_ln[1][user_pass[0].index(i)]}")
        print("------")
        auth.logout(playsound= False)

    def patientmenu(self):
        global loggedin
        #while loggedin:
        try:
            ps = int(input("what do you want to do (1-4): "))
            if ps == 1:
                print("complete the form.")
                appointment.createappointment()
            elif ps == 2:
                print("list of made appointment:")
                self.showPatientSchedule()
                print("ATTENTION:\nyou can not cancel your appointment,"
                      "contact your doctor to cancel it.")
            elif ps == 3:
                    print("change your password.")
                    auth.changepass()
            elif ps == 4:
                print("logged out!")
                print("----------")
                auth.logout()


            else:
                print(numberror)
        except ValueError:
            print(interror)

    def showdr(self):
        print("<-------------------->")
        print(("\033[1m Doctor \033[0m"))
        for i in doctor_select:
            print(f"{i}.{doctor_select[i]}")

    def drmenu(self):
        global loggedin
        global is_dr
        # while loggedin and is_dr:
        try:
            ps = int(input("what do you want to do (1-4): "))
            if ps == 1:
                print("schedule")
                self.showDrschedule()
            elif ps == 2:
                print("type everything that you need "
                      "so the ADMIN can buy it.")
                appointment.addShoplist()
            elif ps == 3:
                print("change pass.")
                auth.changepass()
            elif ps == 4:
                print("logged out!")
                print("----------")
                auth.logout()
            else:
                print(numberror)
        except ValueError:
            print(interror)

    def showadmin(self):
        print("<-------------------->")
        print(("\033[1m ADMIN \033[0m"))
        for i in admin_select:
            print(f"{i}.{admin_select[i]}")

    def adminmenu(self):
        global loggedin
        global is_admin
        # while loggedin and is_admin:
        try:
            ps = int(input("what do you want to do (1-4): "))
            if ps == 1:
                print("here are the registered users.")
                auth.deluser()
            elif ps == 2:
                print("complete the form to add a doctor user.")
                auth.DrRegister()
            elif ps == 3:
                print("needed items:")
                appointment.viewShoplist()
            elif ps == 4:
                print("change pass.")
                auth.changepass()

            elif ps == 5:
                print("logged out!")
                print("----------")
                auth.logout()
            else:
                print(numberror)
        except ValueError:
            print(interror)

    def showPatientSchedule(self):
        with open("schedule.csv", mode="r") as f:
            reader = csv.reader(f)
            next(reader)
            for i in reader:
                if i[0] == name_ln[0][userIndex] and i[1] == name_ln[1][userIndex]:
                    # print(i)
                    print(f"time: {i[4]}")
                    print(f"day: {i[3]}")
                    print(f"dr: {i[2]}")
                    print("<=>")

    def showDrschedule(self):
        with open("schedule.csv", mode="r") as f:
            reader = csv.reader(f)
            next(reader)
            for i in reader:
                if i[2] == f"dr.{name_ln[0][userIndex]} {name_ln[1][userIndex]}":
                    # print(i)
                    print(f"time: {i[4]}")
                    print(f"day: {i[3]}")
                    print(f"Patient: {i[0]} {i[1]}")
                    print("<=>")

class Auth:
    #md5 encoding
    def hashp(self, passw):
        return hashlib.md5(passw.encode()).hexdigest()

    def register(self):
        while True:
            print("plz fill in the patient registration form.")
            name = input("name: ")
            last_name = input("last name: ")
            code_melli = input("code melli(this will be your username to login): ")
            passw = input("your password: ")
            passw2 = input("re-enter your password:")
            is_dr = 0
            is_admin = 0
            self.importing()
            if code_melli in user_pass[0]:
                print(f"a user with {code_melli} id already exists")
            else:
                if passw == passw2:

                    with open("users.csv", mode="a", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow([name, last_name, code_melli,
                                        self.hashp(passw),is_dr,is_admin ])


                    print(f"{name}, you have successfully registered,\n"
                        f"now login with you username and password")
                    self.login()
                    break

                else:
                    print("your passwords does not seem to match, try again")

    def importing(self):

        global user_pass
        global name_ln
        global access

        with open("users.csv", mode="r") as f:
            reader = csv.reader(f)
            next(reader)
            # importing data from csv file
            for i in reader:
                user_pass[0].append(i[2])
                user_pass[1].append(i[3])
                name_ln[0].append(i[0])
                name_ln[1].append(i[1])
                access[0].append(i[4])
                access[1].append(i[5])

    def login(self):
        self.importing()
        while True:
            user = input("user(code melli):")
            passw = input("password:")
            global userIndex
            if user in user_pass[0] and self.hashp(passw) == user_pass[1][user_pass[0].index(user)]:
                userIndex = user_pass[0].index(user)
                print("logged in ")

                global loggedin
                global is_dr
                global is_admin
                loggedin = True
                if access[0][userIndex] == "1":
                    is_dr = True
                if access[1][userIndex] == "1":
                    is_admin = True
                print("-----------")
                if is_dr:
                    print(f"hello, dr.{name_ln[0][userIndex]} {name_ln[1][userIndex]}")
                elif not is_dr:
                    print(f"hello, {name_ln[0][userIndex]} {name_ln[1][userIndex]}")
                print("----------")
                sounds.loginsound()
                print("list of available actions:")
                    # show
                break
            else:
                print("invalid user name or password!")

    def logout(self,playsound=True):
        # resets everything
        global loggedin
        global is_admin
        global is_dr
        global user_pass
        global name_ln
        global access
        global userIndex
        loggedin = False
        is_admin = False
        is_dr = False
        user_pass = [[], []]
        name_ln = [[], []]
        access = [[], []]
        userIndex = -1
        self.playsound = playsound
        if playsound:
            sounds.logoutsound()

    def changepass(self):

        print("it is recommended to use a strong password")
        oldpass = input("enter your old password:")
        newpass = input("enter your new password:")
        newpass2 = input("re-enter your new password:")
        df = pd.read_csv("users.csv")
        if self.hashp(oldpass) == df.loc[userIndex, "passw"] and newpass == newpass2:
            df.loc[userIndex, "passw"] = self.hashp(newpass)
            df.to_csv("users.csv", index=False)
            print("password changed!")

        else:
            print("something went wrong, please try again!!")

    def DrRegister(self):
        print("plz fill in the doctor's registration form.")
        name = input("name: ")
        last_name = input("last name: ")
        code_melli = input("code melli or username to login: ")
        passw = input("password: ")
        passw2 = input("re-enter password: ")
        is_dr = 1
        is_admin = 0
        self.importing()
        if code_melli in user_pass[0]:
            print(f"a user with {code_melli} id already exists")
        else:
            if passw == passw2:

                with open("users.csv", mode="a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([name, last_name, code_melli,
                                     self.hashp(passw), is_dr, is_admin])

                print(f"dr.{name} {last_name} has been succefully added! ")

            else:
                print("passwords does not seem to match, try again")

    def deluser(self):
        df = pd.read_csv("users.csv")
        print(df)
        while True:
            try:
                userdel = int(input("select the number of the user that you want to delete"
                                    "(type -1 to cancel):"))
                if userdel == 0:

                    print("seriously? you tried to delete the admin user?"
                          "you CANT do that!!!!")
                    sounds.errorsound()
                elif userdel == -1:
                    print("no users were deleted")
                    break
                else:
                    try:
                        print("successfully removed user:", df.loc[userdel, "code_melli"])
                        df.drop(userdel, axis=0, inplace=True)
                        df.to_csv("users.csv", index=False)
                    except KeyError:
                        print(numberror)
                    break
            except ValueError:
                print(interror)


class Appointment:
    def chooseDr(self):
        # importing()
        docusers = []
        for i in user_pass[0]:
            if access[0][user_pass[0].index(i)] == "1":
                docusers.append(f"dr.{name_ln[0][user_pass[0].index(i)]}"
                                f" {name_ln[1][user_pass[0].index(i)]}")
        # print(docusers) # del later
        while True:
            for c, i in enumerate(docusers):
                print(f"{c + 1}. {i}")
            try:
                choosedr = int(input("select the number of the doctor:"))
                try:
                    print(docusers[choosedr - 1], "is selected!")
                    return docusers[choosedr - 1]
                except IndexError:
                    print(numberror)
            except ValueError:
                print(interror)

    def chooseday(self):
        weekdays = {1: "Saturday",
                    2: "sunday",
                    3: "monday",
                    4: "tuesday",
                    5: "wednesday",
                    6: "thursday",
                    7: "friday(OFF day)"}

        for i in weekdays:
            print(f"{i}.{weekdays[i]}")
        while True:
            try:
                day = int(input("which day: "))
                if 1 <= day <= 6:
                    print(f"{weekdays[day]} selected!")
                    return weekdays[day]

                elif day == 7:
                    print("between all these days? why did you choose friday? "
                          "NO DOCTORS ARE AVAILABLE ON THAT DAY!!!")
                    sounds.errorsound()
                else:
                    print(numberror)
            except ValueError:
                print(interror)

    def choosetime(self):
        times = {1: "9 AM",
                 2: "10 AM",
                 3: "11 AM",
                 4: "1 PM",
                 5: "6 PM",
                 6: "7 PM",
                 7: "8 PM",
                 9: "9 PM"}

        for i in times:
            print(f"{i}.-> {times[i]}")
        while True:
            try:
                time = int(input("which time: "))
                if 1 <= time <= 9:
                    print(f"{times[time]} selected!")
                    return times[time]
                else:
                    print(numberror)
            except ValueError:
                print(interror)

    def createappointment(self):
        while True:
            name = name_ln[0][userIndex]
            last_name = name_ln[1][userIndex]
            print("-----")
            dr = self.chooseDr()
            print("-----")
            day = self.chooseday()
            print("-----")
            time = self.choosetime()
            print("-----")
            print(f"your appointment details:\n"
                  f"day : {day} \n"
                  f"time: {time}\n"
                  f"dr: {dr}")
            confirm = input("do you confirm the details(yes/no)?").lower()
            if confirm == "yes":
                with open("schedule.csv", mode="a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([name, last_name, dr,
                                     day, time])
                print("success")
                break
            elif confirm == "no":
                print("Cancalled")
                break
            else:
                print("only yes or no is acceptable")


    def addShoplist(self):
        items = []
        amount = []
        while True:
            items.append(input("type the item that you want: "))
            amount.append(input("how much:"))
            if input("press s to stop/any key to add again:").lower() == "s":
                with open("buylist.csv", mode="a", newline="") as f:
                    writer = csv.writer(f)
                    for i, x in zip(items, amount):
                        writer.writerow([i, x])
                print("added to shoplist.")
                break
            else:
                print("new entry!")

    def viewShoplist(self):
        with open("buylist.csv", mode="r") as f:
            reader = csv.reader(f)
            next(reader)
            print("ITEM | AMOUNT")
            try:
                for i in reader:
                    print(i[0], "x", i[1])
            except IndexError:
                print("shoplist is empty!")
        while True:
            x = input("press c to clear the shoplist or "
                      "e to exit without clearing:").lower()
            if x == 'c':
                with open("buylist.csv", mode="w") as f:
                    writer = csv.writer(f)
                    writer.writerow(["item", "amount"])
                    print("shoplist is cleared!")
                    break
            elif x == "e":
                print("nothing changed.")
                break
            else:
                print("c = clear , e = exit ")


sounds = sem.Sounds()
appointment = Appointment()
auth = Auth()
if __name__ == "__main__":
    print("this is the Module plz run clinic.py")




# this is just a reminder
#with open("./final_project/users.csv") as f:
   # reader = csv.reader(f)
 #   next(reader)
   # for i, line in enumerate(reader):
      #  print(f'{i+1},{line}')