class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.old = None
        self.next_oldest = None
        self.data = []

    def append(self, item):
        if self.old is None:
            self.old = 0
            return self.data.append(item)
    
        elif len(self.data) + 1 <= self.capacity:
            self.next_oldest = 1
            return self.data.append(item)

        else:
            self.data[self.old] = item
            self.old += 1 
        if self.old + 1  > self.capacity:
            self.old = 0

    def get(self):
        return self.data