s1 = "Available"
s2 = "Available"
dict = {
    "bed" :["101","102"],
    "status" : [s1 , s2] ,
    "patients" : ["null","null"]
}

def display_beds():
    for i in range(len(dict["bed"])):
        print(f"Bed {dict['bed'][i]}: {dict['status'][i]}")

def admit(bed_number,patient_name):
    for i in range(len(dict["bed"])):
        if ((dict["bed"][i] == bed_number)):
            if (dict["status"][i] == "Available"):
                dict["status"][i] = f"Occupied by {patient_name}"
                dict["patients"][i] = f"{patient_name}"
                print(f"patient {patient_name} is admitted to Bed {bed_number} successfully.")
                break
            else :
                print(f"Sorry, this bed is {dict["status"][i]}")
                break
        elif (i == len(dict["bed"])-1):
            print("Sorry, this bed is not available")

def discharge(patient_name):
    for i in range(len(dict["bed"])):
        if (dict["patients"][i] == patient_name):
            dict["status"][i] = "Available"
            dict["patients"][i] = "null"
            print(f"patient {patient_name} discharged successfully.")
            break
        elif (i == len(dict["bed"])-1):
            print("No patient found with this name")
            


    

    
while True :
    i = input("Hospital Management System Menu:\n1.Display Beds\n2.Admit patient\n3.Discharge patient\n4.Exit\n")

    if (i == '1'):
        display_beds()
    elif (i == '2'):
        bed_number = input("Enter bed number to admit into: \n")
        patient_name = input("Enter patient name: \n")
        admit(bed_number,patient_name)
    elif (i == '3'):
        patient_name = input("Enter patient name to discharge: ")
        discharge(patient_name)
    elif (i == '4'):
        exit()
    else :
        print("Invalid choice.please try again")

    print("______________________________________")