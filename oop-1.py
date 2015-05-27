
class Elem:
    def __init__(self, data=0, _next=None):
        self.data = data
        self.next = _next


class Queue:
    def __init__(self, init_data=None):
        if init_data:
            self.first = Elem(init_data)
        else:
            self.first = None
        self.last = self.first

    def add(self, data):
        if not self.first:
            self.first = Elem(data)
            self.last = self.first
        else:
            self.last.next = Elem(data)
            self.last = self.last.next

    def peek(self):
        if not self.first:
            return None
        return self.first.data

    def pop(self):
        if not self.first:
            return None
        ret = self.first.data
        self.first = self.first.next
        return ret

    def __repr__(self):
        i = self.first
        array = []
        while i:
            array += [i.data]
            i = i.next
        return str(array)


def main():
    empty_q = Queue(3)
    print(empty_q.peek())

    empty_q.add(1)
    print(empty_q)

    empty_q.add(5)
    print(empty_q)
    print(empty_q.peek())

    empty_q.add(3)
    print(empty_q)

    print(empty_q.pop())
    print(empty_q)


if __name__ == "__main__":
    main()
