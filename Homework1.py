class employee():
    def __init__(self, Name, Age, Job):
        self.Name = Name
        self.Age = Age
        self.Job = Job

    def details(self):
        print("Name: " + self.Name,
              "\n Age: " + str (self.Age),
              "\n Job: " + str (self.Job))

s1 = employee("Alex", 27, "Teacher")
s2 = employee("John", 28, "Mehanic")

s1.details()