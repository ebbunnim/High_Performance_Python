from queue import Queue

eventloop=None

class Eventloop(Queue):
    """
        Concurrency: use eventloop if you want to manage target which program may execute and time
        Eventloop : list of functions to call. Collaborating with I/O asynchronous method may help improvement of  performance
    """
    def start(self):
        while True:
            function=self.get()
            function()

def do_hello():
    global eventloop
    print('Hello')
    eventloop.put(do_world)

def do_world():
    global eventloop
    print('World')
    eventloop.put(do_hello)

if __name__=="__main__":
    eventloop=Eventloop()
    eventloop.put(do_hello)
    eventloop.start()