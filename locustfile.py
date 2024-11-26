from locust import FastHttpUser, task, between, events
from api.api_requests import ApiRequests
from utils.helper import get_csv_data

@events.init.add_listener
def set_users(**kwargs):
    global users
    users = list (get_csv_data('./resources/users.csv'))[1:]
    
class LoadTestUser(FastHttpUser):
    wait_time = between (1, 5)
    
    
    def on_start(self):
        self.user_name, self.password = users.pop()
        self.api_requests = ApiRequests(self.client)
        
        access_token = self.api_requests.login(self.user_name, self.password)['token']
        print('Access Token###', access_token)
        self.headers = {
            'Accept': '*/*',
            #'Content-Length': 0,
            'Content-Type': 'application/json',
            'Cookie': f'token={access_token}',
            'Connection': 'keep-alive'
        }
        
    @task
    def user_task (self):
        
        bookingId = self.api_requests.createBooking(self.headers)['bookingid']
    
        self.api_requests.getBooking(self.headers, bookingId)
        
        self.api_requests.updateBookingByPut(self.headers,bookingId)
        
        self.api_requests.updateBookingByPatch(self.headers,bookingId)
        
        self.api_requests.deleteBooking(self.headers, bookingId)