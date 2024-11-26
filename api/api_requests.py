import json
from utils import helper 

class ApiRequests:
    
    def __init__(self, client):
        self.client = client
        
    def login ( self, user_name, password):
        api_url = 'https://restful-booker.herokuapp.com/auth'
        payload = {
            'username' : user_name,
            'password' : password
        }
        headers = { 'Content-Type': 'application/json', 'Accept': '*/*' }
        response = self.client.post(api_url,json=payload, headers=headers, name= 'Login')
        print ('login response code###', response.status_code)
        return json.loads(response.text)
        
    def createBooking ( self, headers):
        api_url= f'https://restful-booker.herokuapp.com/booking'
        payload = {
            "firstname": helper.generate_random_first_name(),
            "lastname": helper.generate_random_last_name(),
            "totalprice": helper.generate_random_number(),
            "depositpaid": helper.generate_random_boolean(),
            "bookingdates": {
            "checkin": helper.generate_random_date(),
            "checkout": helper.generate_random_date()
            },
            "additionalneeds": "Breakfast"
        }
        response = self.client.post(api_url, json=payload, headers=headers, name='Create Booking')
        print('Create Booking response code:', response.status_code)
        print("Create Booking Response:", response.text)
        return json.loads(response.text)
        
    def getBooking (self, headers, booking_id):
        api_url = f'https://restful-booker.herokuapp.com/booking/{booking_id}'
        response = self.client.get(api_url, headers=headers, name='Get Booking')
        print('Get Booking:', response.status_code)
        print("Get Booking Response:", response.text)
        
    def updateBookingByPut (self, headers, booking_id):
        api_url = f'https://restful-booker.herokuapp.com/booking/{booking_id}'
        payload = {
            "firstname": helper.generate_random_first_name(),
            "lastname": helper.generate_random_last_name(),
            "totalprice": helper.generate_random_number(),
            "depositpaid": helper.generate_random_boolean(),
            "bookingdates": {
            "checkin": helper.generate_random_date(),
            "checkout": helper.generate_random_date()
            },
            "additionalneeds": "Breakfast"
        }
        response= self.client.put(api_url, json=payload, headers=headers, name='Update Booking By PUT')
        print('Update Booking By PUT:', response.status_code)
        print("Update Booking By PUT Response:", response.text)
        
    def updateBookingByPatch (self, headers, booking_id):
        api_url = f'https://restful-booker.herokuapp.com/booking/{booking_id}'
        payload = {
            "firstname": helper.generate_random_first_name(),
            "lastname": helper.generate_random_last_name()
        }
        response= self.client.patch(api_url, json=payload, headers=headers, name='Update Booking By PATCH')
        print('Update Booking By PATCH:', response.status_code)
        print("Update Booking By PATCH Response:", response.text)
        
    def deleteBooking (self, headers, booking_id):
        api_url= f'https://restful-booker.herokuapp.com/booking/{booking_id}'
        response = self.client.delete(api_url, headers=headers, name='Delete Booking')
        print('Delete Booking:', response.status_code)
        print("Delete Booking:", response.text)