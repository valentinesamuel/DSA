class Deque:
      def __init__(self):
            self.items = []
      
      def add_front(self, item):
            return self.items.append()
      
      def remove_front(self):
            return self.items.pop()
      
      def add_rear(self, item):
            return self.items.insert(0, item)
      
      def remove_rear(self, item):
            return self.items.pop(0)
      
      def is_empty(self):
            return self.items == []
      
      def size(self):
            return len(self.items)