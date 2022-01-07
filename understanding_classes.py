class Dog:
      def __init__(self, name, month, day, year, speakText):
            self.name = name
            self.month = month
            self.day = day
            self.year = year
            self.speakText = speakText

      def speak(self):
            return self.speakText
      
      def getName(self):
            return self.name
      
      def birthDate(self):
            return str(self.month) + "/" + str(self.day) + "/" + str(self.year)

      def changeBark(self,bark):
            self.speakText = bark
      
      def __add__(self, otherDog):
            return Dog("puppy of " + self.name + " and " + otherDog.name, self.month, self.day, self.year + 1, self.speakText + otherDog.speakText)

boyDog = Dog("Mesa", 5, 15, 2004, "Woof")
girlDog = Dog("Sequoia", 5,6, 2004, "barkbark")
gayDog = Dog("Bobrisky", 3,9, 1994, "osheyyy")
puppy = boyDog+girlDog+gayDog

print(puppy.birthDate())
