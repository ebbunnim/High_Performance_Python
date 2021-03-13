from functools import partial
from queue import Queue

class Eventloop(Queue):
    """
        Concurrency: use eventloop if you want to manage target which program may execute and time
        Eventloop : list of functions to call. Collaborating with I/O asynchronous method may help improvement of  performance
    """
    def start(self):
        while True:
            function=self.get()
            function()

def save_value(value,callback):
    print(f'Saving {value} to db')
    save_result_to_db(result,callback) # save_result_to_db : example of asynchronous function

def print_response(db_response):
    print(f'Response from database {db_response}')

if __name__=="__main__":
    eventloop=Eventloop()
    eventloop.put(
        partial(save_value,'Hello, world',print_response) # If result data is ready, print_response will be called
    )
