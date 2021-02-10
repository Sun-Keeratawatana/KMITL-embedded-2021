import threading
import queue
q = queue.Queue()
for i in range(10):
    q.put(i)
    
def Queue():
    while q:
        print("Queue: {}".format(q.get()))
        
t1 = threading.Thread(target = Queue)
t1.start()
