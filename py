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

# Further split each record by commas into individual data fields
medical_records = []
for record in updated_medical_split:
    medical_records.append(record.split(','))
print(medical_records)  # Debug: print raw split records

# Clean up each field by removing unnecessary spaces
medical_records_clean = []
for record in medical_records:
    record_clean = []
    for item in record:
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean)
print(medical_records_clean)  # Debug: print cleaned records

# Separate each field type into individual lists for easier processing
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])

# Print just the names (first field in each record)
for record in medical_records_clean:
    print(record[0])
# Separate each field type into individual lists for easier processing
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])
# Debug: print lists
print(names)
print(ages)
print(bmis)
print(insurance_costs)

# Calculate total BMI for averaging
total_bmi = 0
for bmi in bmis:
    total_bmi += float(bmi)
print(total_bmi)

# Compute and print average BMI
average_bmi = total_bmi / len(bmis)
print(f'Average BMI: {average_bmi}')
