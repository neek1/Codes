class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    # Method to add item to tail of the list (queue)
    def enqueue(self, item):
        self.items.append(item)

    # Method to remove item from the head of the list (queue)
    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)   # Removes the item at the index 0 (the head)

    # Method to display the items in the list
    def show_queue(self):
        print(self.items)

q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")

print("Pass" if(q.size() == 3) else "Fail")
q.enqueue("d")
print("Pass" if(q.size() == 4) else "Fail")

print("Pass" if (q.dequeue() == "a") else "Fail")
print("Pass" if (q.dequeue() == "d") else "Fail")  # This line will still dequeue but the conditional statement will be false
print("Pass" if (q.size() == 2) else "Fail")
q.show_queue()
