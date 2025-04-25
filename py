# Multiline string holding messy medical data
medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Replace '#' with '$' to simplify later processing of insurance costs
updated_medical_data = medical_data.replace('#', '$')

# Initialize a counter to count the number of insurance records
num_records = 0
for i in updated_medical_data:
    if i == '$':  # Every dollar sign marks a new insurance cost
        num_records += 1

# Split the full string into individual records using ';' as separator
updated_medical_split = updated_medical_data.split(';')
print(updated_medical_split)  # Debug: print split records
