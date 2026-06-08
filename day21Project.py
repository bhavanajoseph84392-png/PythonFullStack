    class Person:
    university_name = "Codegnan University"
    def __init__(self,name,age,department,gender,education_background):
        self.name = name
        self.age = age
        self.department = department
        self.gender =gender
        self.education_background = education_background
    def display_info(self):
        pass
class Student(Person):
    student_count = 0
    def __init__(self,name,age,student_id,department,gender,year,education_background):
        super().__init__(name,age,education_background,gender,department)
        self.student_id = student_id
        self.year = year
        Student.student_count+=1
    def display_info(self):
        print(f"Name:{self.name}\nAge:{self.age}\nStudent_id:{self.student_id}\nDepartment:{self.department}\nGender:{self.gender}\nYear:{self.year}\nEducation_background:{self.education_background}")
class Faculty(Person):
    faculty_count = 0
    def __init__(self,name,age,faculty_id,department,gender,experience):
        super().__init__(name,age,experience,gender,department)
        self.faculty_id = faculty_id
        self.experience = experience
        Faculty.faculty_count +=1
    def display_info(self):
        print(f"Name:{self.name}\nAge:{self.age}\nFaculty_id:{self.faculty_id}\nDepartment:{self.department}\nGender:{self.gender}\nExperience:{self.experience}")
        print("Enter student details:")
class Security(Person)        
    

    
        
        
        
        
