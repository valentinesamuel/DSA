import Node

class OrderedList:
      def __init__(self):
            self.head = None
      
      def search(self, item):
            curernt = self.head
            found = False
            stop = False
            while curernt != None and not found and not stop:
                  if current.get_data() == item:
                        found = True
                  else:
                        if curernt.get_data() > item:
                              stop = True
                        else:
                              current = current.get_next()
            return found

      def add(self, item):
            current = self.head
            previous = None
            stop = False
            while current != None and not stop:
                  if current.get_data() > item:
                        stop = True
                  else:
                        previous = current
                        current = current.get_next()
            
            temp = Node(item)
            if previous == None:
                  temp.set_next(self.head)
                  self.head = temp
            else:
                  temp.set_next(current)
                  previous.set_next(temp)