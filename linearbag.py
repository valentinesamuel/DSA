class Bag:

      def __init__(self):
            self._theItems = []

      def __len__(self):
            return len(self._theItems)
      
      def __contains__(self, item):
            return item in self._theItems
      
      def add(self, item):
            self._theItems.append(item)
      
      def remove(self, item):
            assert item in self._theItems, "The item must be in the bag."
            ndx = self._theItems.index(item)
            return self._theItems.pop(ndx)

      def __iter__(self):
            return _BagIterator(self._theItems)


class _BagIterator:
      def __init__(self, theList):
            self._bagItems = theList
            self._currentItem = 0

      def __iter__(self):
            return self

      def __next__(self):
            if self._currentItem < len(self._bagItems):
                  item = self._bagItems[self._currentItem]   
                  self._currentItem += 1
                  return item
            else:
                  raise StopIteration

shoppingBag = Bag()
shoppingBag.add(20)
shoppingBag.add(89)
shoppingBag.add(39)

for item in shoppingBag:
      print(item)