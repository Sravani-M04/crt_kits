#stack
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
        print(f"Pushed: {value} | stack: {self.stack}")
    def pop(self):
        if self.isEmpty():
            return "Stack Underflow!"
        val = self.stack.pop()
        print(f"Popped : {val} | Stack: {self.stack}")
        return val
    def peek(self):
        if self.isEmpty():
            return "Stack is empty."
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    def display(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            print("TOP -> ", self.stack[::-1])
s = Stack()
s.push(10); s.push(20); s.push(30)
print("Peek:", s.peek())
s.pop()
print("Size:", s.size())
s.display()


#browser history
class BrowserHistory:
    def __init__(self, homepage):
        self.back=[homepage]
        self.forward=[]
    def visit(self,url):
        self.back.append(url)
        self.forward.clear()
    def go_back(self):
        if len(self.back)>1:
            self.forward.append(self.back.pop())
            return self.back[-1]
    def go_forward(self):
        if self.forward:
            page=self.forward.pop()
            self.back.append(page)
            return page
b=BrowserHistory("google.com")
b.visit("youtube.com")
b.visit("github.com")
print(b.back)
print(b.forward)
print(b.go_back)
print(b.forward)
print(b.go_forward)
print(b.forward)
