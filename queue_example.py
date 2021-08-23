import queue

# # Queue() 로 큐 만들기(가장 일반적인 큐, FIFO(First-In, First-Out)
# data_queue = queue.Queue()
#
# data_queue.put("funcoding")
# data_queue.put(1)
#
# print(data_queue.qsize())
# print(data_queue.get())
# print(data_queue.qsize())
# print(data_queue.get())
#
# print("----------------------")
# # Lifo Queue() 로 큐 만들기(LIFO(Last-In, First-Out)
# data_queue11 = queue.LifoQueue()
# data_queue11.put("funcoding")
# data_queue11.put(1)
# print(data_queue11.qsize())
# print(data_queue11.get())
# print(data_queue11.qsize())
# print(data_queue11.get())
#
# print("------------------")
# #PriorityQueue()
# data_queue22 = queue.PriorityQueue()
# data_queue22.put((10, "korea"))
# data_queue22.put((5, 1))
# data_queue22.put((15, "china"))
# print(data_queue22.qsize())
# print(data_queue22.get())

print("------------------")
# enqueue dequeue
queue_list = list()


def enqueue(data):
    queue_list.append(data)


def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data


for index in range(10):
    enqueue(index)

print(len(queue_list))
print(dequeue())
print(dequeue())
print(dequeue())


