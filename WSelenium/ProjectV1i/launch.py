import os
import time


print("Choose the job of the person to create : \n")
print("-Type 1 for doctor")
print("-Type 2 for nurse")
print("-Type 3 for secretary\n")

choice = input("Choice : ")

job =''
if choice == '1':
    job = 'doctor'
elif choice == '2':
    job = 'nurse'
elif choice == '3':
    job = 'secretary'

print("\nThe job is : ",job)

time.sleep(3)

os.chdir('./run')
if job == 'doctor':
    os.system('./rundoctor.sh')
    
    
elif job == 'nurse':
    os.system('./runnurse.sh')
elif job == 'secretary':
    os.system('./runsecretary.sh')


