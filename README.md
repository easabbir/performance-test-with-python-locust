# performance-test-with-python-locust-user-managed-csv-file
This project is done to do performance testing with couple of api in locust and user is provided with csv file using python as a language.

### Prerequisites and set-up:
To run a Locust performance testing project, you’ll need to ensure you have the following prerequisites set up:

    1. Python Installation: Locust is a Python-based tool, Python (version 3.7 or later).
    2. Install Locust: pip install locust -> verify installation: locust --version.
    3. Install Additional Packages (if needed): pip install requests

---

### How to run the project
Step-1: To run Locust, navigate to the project directory and execute locust command as shown in below section


Step-2: Open a browser and go to http://localhost:8089 to access the Locust web interface, where you can start and control the test.

    1. terminal/cmd/bash -> locust -r 10 -u 3 --host=base_url
    2. go to browsers url -> http://localhost:8089/ -> start/advance options to add test duration 
    3. Click start.
    4. Explore the UI to see the results and charts as shown below.

---

### locust command Explanation:
For Example:

`locust -r 10 -u 100 --host=base_url`

 Details:

`-r: The hatch rate, which is the number of users hatching per second.` 

In this example, it's set to 10.

`-u: The total number of users to simulate during the test. In this example, it's set to 100`

---

### Tasks
Create a list of user in the application and add those users info in the `resouces>users`
csv file in the below format.

username,password

admin,password123

easabbir,Abbl_234

easabbir,Abbl_234

**Users list can be reused, if provided in the csv file. 

**In the run command, make sure not to give `-u` value, more than the users count of the csv file.

---

### API used in this projects are 
Auth - CreateToken
https://restful-booker.herokuapp.com/auth

Booking - GetBooking
https://restful-booker.herokuapp.com/booking/:id

Booking - CreateBooking
https://restful-booker.herokuapp.com/booking

Booking - UpdateBooking using put
https://restful-booker.herokuapp.com/booking/:id

Booking - PartialUpdateBooking
https://restful-booker.herokuapp.com/booking/:id

Booking - DeleteBooking
https://restful-booker.herokuapp.com/booking/1

---

### Report Analysis on a different project which will help user to do analysis
This video explains things to check for performance testing using locust and python. 
Do give some time and watch and let me know in the comment section how you feel about these short videos. 

Bengali version
https://youtu.be/GfX0_uyTlg4

English version
https://youtu.be/DcTwbkUAiTo

---

### Running in docker
    1. terminal/cmd/bash -> docker-compose up --scale worker=3
    2. go to browsers url -> http://localhost:8089/ -> start/advance options to add test duration 
    3. Click start.
    4. Explore the UI to see the results and charts as shown below.
---

