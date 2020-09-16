from faker import Faker
from faker.providers import profile
import csv
import datetime
import sys


def datagenerate(records, headers):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # To generate phone numbers
    with open("People_data.csv", 'wt', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname +"."+ Lname + domain_name
            
            writer.writerow({
                    "Email Id" : userId,
                    "Prefix" : fake.prefix(),
                    "Name": fake.name(),
                    "Birth Date" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
                    "SSN" : fake.profile('ssn')['ssn'],
                    "Phone Number" : fake1.phone_number(),
                    "Additional Email Id": fake.email(),
                    "Address" : fake.address(),
                    "Zip Code" : fake.zipcode(),
                    "City" : fake.city(),
                    "State" : fake.state(),
                    "Country" : fake.country(),
                    "Year":fake.year(),
                    "Time": fake.time(),
                    "Link": fake.url(),
                    "Text": fake.word(),
                    })

def usage():
    script = sys.argv[0]
    help = script+''' <number of records>\n'''
    example = script+''' 10000\n'''
    print("Usage: "+help)
    print("Example: "+example)

if __name__ == '__main__':

    # Manage commandline arguments
    if len(sys.argv) != 2:
        usage()
        sys.exit()
    try:
        records = int(sys.argv[1])
    except:
        print("ERROR: could not cast '"+sys.argv[1]+"' to an int...\n")
        sys.exit(1)
    start = datetime.datetime.now()
    print("Starting time: "+str(start))
    
    # Create Faker object
    fake = Faker()
    fake.add_provider(profile)

    headers = ["Email Id", "Prefix", "Name", "Birth Date", "SSN", "Phone Number", "Additional Email Id",
               "Address", "Zip Code", "City","State", "Country", "Year", "Time", "Link", "Text"]

    datagenerate(records, headers)
    end = datetime.datetime.now()
    print("Ending time: "+str(end))
    print("CSV generation complete!")
    print("Execution took: "+str((end - start).total_seconds())+" seconds")
    