class StudentFileReader:
      # Create a new student reader instance
      def __init__(self, inputSrc):
            self._inputSrc = inputSrc
            self._inputFile = None
      
      # Open a connection to the input file
      def open(self):
            self._inputFile = open(self._inputSrc, "r")

      # Close the connection to the input file
      def close(self):
            self._inputFile.close()
            self._inputFile = None
      
      # Extract all student records and store them in a list
      def fetchAll(self):
            theRecords = []
            student = self.fetchRecord()
            while student != None:
                  theRecords.append(student)
                  student = self.fetchRecord()
            return theRecords
      
      # Extract the next student record from the file
      def fetchRecord(self):
            #Read the first line of the record
            line = self._inputFile.readline()
            if line == "":
                  return None
            
            student = studentRecord()
            student.idNum = int(line)
            student.firstName = self._inputFile.readLine().rstrip()
            student.lastName = self._inputFile.readLine().rstrip()
            student.classCode = int(self._inputFile.readLine())
            student.gpa = float(self._inputFile.readLine())
            return student

class studentRecord:
      def __init__(self):
            self.idNum = 0
            self.firstName =None
            self.lastName =None
            self.classCode =0
            self.gpa =0.0
