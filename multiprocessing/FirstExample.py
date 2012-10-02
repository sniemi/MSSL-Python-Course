import numpy as np
import multiprocessing
import Queue

class simpleExample(multiprocessing.Process):
    
    def __init__(self, values, work_queue, result_queue):
        #base class initialization
        multiprocessing.Process.__init__(self)
        #job management queues
        self.work_queue = work_queue
        self.result_queue = result_queue
        self.kill_received = False

    def calculate(self, value):
        "calculations go here"
        return value * 3
        
    def run(self):
        """
        This is the method that will be called when multiprocessing.
        """
        while not self.kill_received:
            # get a task from the queue
            try:
                value = self.work_queue.get_nowait()
            except Queue.Empty:
                break

            #do some calculations here
            result = self.calculate(value)
                
            # store the result
            self.result_queue.put(result)





needed = [1,2,3,4,5,6,7,8,9,10]

num_processes = 4

# load up work queue
work_queue = multiprocessing.Queue()
for number in needed:
    work_queue.put(number)

#create a queue to pass to workers to store the results
result_queue = multiprocessing.Queue()

# spawn workers with a random seeds, this is needed because
# in Unix the seed is passed when forked leading to the
# same seed and thus the same random numbers.
rds = np.random.rand(num_processes)*100.0
for value in needed:
    worker = simpleExample(value, work_queue, result_queue)
    worker.start()

# collect the results off the queue
results = []
for file in needed:
   print(result_queue.get())
