class student():
    def __init__(self, Name, Age, Grade, Intelligence):
        self.Name = Name
        self.Age = Age
        self.Grade = Grade
        self.Intelligence = Intelligence

    def details(self):
        print("Name:" + self.Name,
              "\n Age" + str (self.Age),
              "\n Grade" + str (self.Grade), 
              "\n Intelligence" + self.Intelligence)

s1 = student("Alex", 13, 8, "very high")
s2 = student("Joe", 27, 5, "very low")

s1.details()