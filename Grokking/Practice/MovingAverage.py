

class MovingAverage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        self.sum = 0

    def next(self, ele):
        popped = 0
        if len(self.arr) == 3:
            popped = self.arr.pop(0)
            self.sum += -popped + ele
            self.arr += ele,
            return self.sum/len(self.arr)
        else:
            self.arr += ele,
            self.sum = sum(self.arr)
            return self.sum/len(self.arr)

def main():
    m = MovingAverage(3)
    print (m.next(3))
    print (m.next(5))
    print (m.next(7))
    print (m.next(6))

main()
