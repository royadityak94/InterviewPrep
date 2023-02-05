"""Browser History
Implement the BrowserHistory class:
------
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the 
history number of steps or move forward in the history number of steps.

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, 
    you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. 
    If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

I/P: 
labels = ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
data = [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
O/P: [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
"""

class Node: 
    def __init__(self, data, prev= None, next= None):
        self.data = data 
        self.prev = prev 
        self.next = next 

class BrowserHistory:
    def __init__(self, homepage):
        self.head = self.tail = self.start =Node(homepage)
        self.distance_from_home = 0

    def visit(self, forward):
        new_node = Node(forward)

        # Make the new visit as the tail
        last = self.tail 
        last.next = new_node
        new_node.prev = last 
        self.tail = new_node

        # Increase the distance
        self.distance_from_home += 1
        return

    def visit_backward(self, distance):
        current_tail = self.tail 
        while distance:
            if not self.distance_from_home:
                break
            if not current_tail.prev: # When tail is behind head
                self.distance_from_home = 0
                break 
            current_tail = current_tail.prev # Visit backwards
            self.distance_from_home -= 1
            distance -= 1
        self.tail = current_tail

    def visit_forward(self, distance):
        current_head = self.head 
        while distance: 
            if not current_head.next:
                break
            current_head = current_head.next 
            distance -= 1
            self.distance_from_home += 1
        self.head = current_head
        return 

    def current_trail(self):
        current = self.start
        print (f'\tDistance from home: {self.distance_from_home}')
        print ('\t', end='->')
        while (current):
            print (current.data, end= '->')
            current = current.next
        print ()
        print (f'\tCurrent: Head Set= {self.head.data}, Tail Set= {self.tail.data}, Global Head: {self.start.data}')
        return

def main():
    labels = ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
    data = [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

    browser = BrowserHistory(*data[0])
    for idx in range(1, len(labels)):
        action = labels[idx]
        _data = data[idx]
        print (f'Action= {action}, Data= {_data}')
        if action == 'visit':
            browser.visit(*_data)
        elif action == 'back':
            browser.visit_backward(*_data)
        elif action == 'forward':
            browser.visit_forward(*_data)
        else:
            raise Exception(f'Unknown action: {action} encountered! Exiting the code')
        browser.current_trail()
main()