import csv
import hashlib
import pandas as pd
import clinicModule as cm
import soundeffectsmodule as sem
clinic = cm.Show()

print("welcome to the online clinic!")
while True:
    clinic.show1()
    clinic.select1()
    if cm.loggedin and cm.is_admin:
        while cm.loggedin and cm.is_admin:
            clinic.showadmin()
            clinic.adminmenu()
    elif cm.loggedin and cm.is_dr:
        while cm.loggedin and cm.is_dr:
            clinic.showdr()
            clinic.drmenu()
    elif cm.loggedin:
        while cm.loggedin:
            clinic.showpatient()
            clinic.patientmenu()

