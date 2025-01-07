import pandas as pd
import random

# Function to generate random employee data
def generate_employee_data(num_employees):
    first_names = ["John", "Jane", "Alex", "Chris", "Emma", "Olivia", "Noah", "Liam", "Sophia", "James"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez"]
    departments = ["HR", "IT", "Sales", "Finance", "Marketing", "Operations", "Support"]
    positions = ["Manager", "Specialist", "Analyst", "Developer", "Engineer", "Consultant", "Coordinator"]
    locations = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio"]
    genders = ["Male", "Female", "Non-binary"]
    
    data = []
    for emp_id in range(1, num_employees + 1):
        employee = {
            "Employee_ID": f"EMP{emp_id:03}",
            "First_Name": random.choice(first_names),
            "Last_Name": random.choice(last_names),
            "Gender": random.choice(genders),
            "Age": random.randint(22, 60),
            "Department": random.choice(departments),
            "Position": random.choice(positions),
            "Salary": random.randint(40000, 120000),
            "Location": random.choice(locations),
            "Date_Of_Joining": f"{random.randint(2010, 2024)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}",
            "Email": f"employee{emp_id}@company.com",
            "Phone_Number": f"+1-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        }
        data.append(employee)
    return data

# Generate 200 employees
num_employees = 200
employee_data = generate_employee_data(num_employees)

# Create DataFrame
df = pd.DataFrame(employee_data)

# Save to CSV
file_path = "/mnt/data/employee_data.csv"
df.to_csv(file_path, index=False)

file_path
