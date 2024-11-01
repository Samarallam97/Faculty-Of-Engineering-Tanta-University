class Queue:
    def __init__(self):
        # Initialize an empty list to store queue items
        self.items = []

    def isEmpty(self):
        # Check if the queue is empty by verifying if the list is empty
        return self.items == []

    def enqueue(self, item):
        # Add a new item to the front of the list, effectively adding it to the queue
        self.items.insert(0, item)

    def dequeue(self):
        # Remove and return the last item in the list, mimicking a FIFO (First-In-First-Out) behavior
        return self.items.pop()

    def size(self):
        # Return the number of items in the queue
        return len(self.items)
