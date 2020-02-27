from queue import PriorityQueue

def hello():
    open_list = PriorityQueue()
    open_list.put(43,'5')
    open_list.put(42,'6')
    
    print(open_list.get())
    print("yahya")

hello()
