import csv
import random
from datetime import datetime, timedelta

def get_csv_data ( csv_file_path):
    with open ( csv_file_path) as csv_file:
        yield from csv.reader(csv_file)
        
def generate_random_number(start=0, end=1000):
    return random.randint(start, end)

def generate_random_first_name():
    first_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah']
    first_name = random.choice(first_names)
    return f"{first_name}"

def generate_random_last_name():
    last_names = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
    last_name = random.choice(last_names)
    return f"{last_name}"

def generate_random_boolean():
    return random.choice([True, False])

def generate_random_date(start_date="2000-01-01", end_date="2023-12-31"):
    # Convert the input date strings to datetime objects
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Generate a random number of days between start and end
    random_days = random.randint(0, (end - start).days)
    
    # Add the random number of days to the start date
    random_date = start + timedelta(days=random_days)
    
    # Return the date as a string in "YYYY-MM-DD" format
    return random_date.strftime("%Y-%m-%d")

def generate_random_snacks_type():
    snacksType = ['Breakfast', 'Lunch', 'Dinner', 'Breakfast,Lunch,Dinner']
    snacksType = random.choice(snacksType)
    return f"{snacksType}"