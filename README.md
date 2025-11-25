# Hospital Management System – Instructor Assessment Project

*Instructor Name:* ……………………………………… *Date:* …………………………

## PROJECT REQUIREMENTS

Create a simple *hospital management system* using standard Python features that can:

1. *Display* all beds/rooms in the hospital and their status.
2. *Admit* a patient to a specific bed/room under a *patient name*.
3. *Discharge* a patient by *patient name*.

Your code must:

* Use *dicts* to store info about beds/rooms and patients.
* Be organized into *functions*, commented, and follow a logical sequence that you can explain.
* *Handle invalid inputs* (non-existing bed, already occupied, name not found, invalid menu choice, etc.).

Any *extra additions* (e.g., patient age/diagnosis, search by name, count available beds) are bonus.

---

## EXAMPLE OUTPUT

```
Hospital Management System Menu:
1. Display Beds
2. Admit Patient
3. Discharge Patient
4. Exit

Enter your choice: 1
Bed 101: General (Available)
Bed 102: ICU (Available)

Hospital Management System Menu:
1. Display Beds
2. Admit Patient
3. Discharge Patient
4. Exit

Enter your choice: 2
Enter bed number to admit into: 101
Enter patient name: mohamed
Patient 'mohamed' admitted to Bed 101 successfully.

Hospital Management System Menu:
1. Display Beds
2. Admit Patient
3. Discharge Patient
4. Exit

Enter your choice: 2
Enter bed number to admit into: 102
Enter patient name: ahmed
Patient 'ahmed' admitted to Bed 102 successfully.

Hospital Management System Menu:
1. Display Beds
2. Admit Patient
3. Discharge Patient
4. Exit

Enter your choice: 1
Bed 101: General (Occupied by mohamed)
Bed 102: ICU (Occupied by ahmed)

Hospital Management System Menu:
1. Display Beds
2. Admit Patient
3. Discharge Patient
4. Exit

Enter your choice: 3
Enter patient name to discharge: mohamed
Patient 'mohamed' discharged successfully.

Hospital Management System Menu:
1. Display Beds
2. Admit Patient
3. Discharge Patient
4. Exit

Enter your choice: 3
Enter patient name to discharge: fathy
No patient found with this name.

Hospital Management System Menu:
1. Display Beds
2. Admit Patient
3. Discharge Patient
4. Exit

Enter your choice: 2
Enter bed number to admit into: 101
Enter patient name: sara
Sorry, this bed is not available.

Hospital Management System Menu:
1. Display Beds
2. Admit Patient
3. Discharge Patient
4. Exit

Enter your choice: 5
Invalid choice. Please try again.

Hospital Management System Menu:
1. Display Beds
2. Admit Patient
3. Discharge Patient
4. Exit

Enter your choice: 4
