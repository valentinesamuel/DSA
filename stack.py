class Stack:
      def __init__(self):
            self.items = []
      
      def is_empty(self):
            return self.items == []
      
      def push(self, item):
            self.items.append(item)
      
      def pop(self):
            return self.items.pop()
      
      def peek(self):
            return self.items[len(self.items) -1]
      
      def size(self):
            return len(self.items)
      
      def rev_string(self, string):
            return string[::-1]
      
      def show_items(self):
            for item in self.items:
                  print(item)


