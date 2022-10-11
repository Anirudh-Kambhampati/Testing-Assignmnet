import pytest 
import json
import System,Staff,Student,Professor


def test_login():
    testStudent = System.System()
    testName = "hdjsr7"
    testPwd = "pass1234"

    testStudent.login(testName,testPwd)

    with open('Data/users.json') as usr:
        data = json.load(usr)

    if testName not in data:
        assert False
            
            
def test_password():
    gradSys = System.System()
    test_pwd = "augurrox"
    if not gradSys.check_password("goggins",test_pwd):
        assert False
                
            
def test_change_grade():
    name,course,assignment,g = "akend3","comp_sci","assignment1",93
    changeGrade = Staff.Staff()
    
    changeGrade.change_grade(name, course, assignment,g)
    
    with open('Data/users.json') as usr:
        data = json.load(usr)
        grade = data["akend3"]['courses']["comp_sci"]["assignment1"]["grade"]
    if grade == 0:
        assert True
    else:
        assert False    
        

def test_create_assignment():
    assignment_name,due_date,course = "new_assignmnet","10/01/2023","Algorithms"
   
    create_Assignment = Staff.Staff()
    create_Assignment.create_assignment(assignment_name, due_date, course)
    
    with open('Data/courses.json') as usr:
        data = json.load(usr)
    if course in data:
        assert True
    else:
        assert False    
    
    
def test_add_student():
    name,course = "Anirudh","Algoritms" 
    
    with open('Data/courses.json') as usr:
        all_courses = json.load(usr)
        
    with open('Data/users.json') as usr:
        all_users = json.load(usr)
            
    add_student = Professor.Professor(name,all_users,all_courses)
    add_student.add_student(name,course)
    
    with open('Data/users.json') as usr:
        users = json.load(usr)
    
    if name in users:
        assert True    
    else:
        assert False     
    
    
def test_drop_student():
    name, course = "akend3","comp_sci"    
   
    
    with open('Data/courses.json') as usr:
        all_courses = json.load(usr)
        
    with open('Data/users.json') as usr:
        all_users = json.load(usr)
        
    drop_student = Professor.Professor(name,all_users,all_courses)
    drop_student.add_student(name,course)  
    
    with open('Data/users.json') as usr:
        users = json.load(usr)
    
    if name in users:
        assert True    
    else:
        assert False 
        
        
        
def test_submit_assignment():
    name,course = "akend3","comp_sci"    
    
    with open('Data/courses.json') as usr:
        all_courses = json.load(usr)
        
    with open('Data/users.json') as usr:
        all_users = json.load(usr)
        
    submit_assignment = Student.Student(name,all_users,all_courses)
    submission_date,submission,assignment_name = "10/10/2022","Test Sub","test_assignment"
   
    submit_assignment.submit_assignment(course,assignment_name,submission,submission_date)
    
    with open('Data/courses.json') as usr:
        courses = json.load(usr)
    
    if courses[course]['assignments'][assignment_name][submission_date]:
        assert True
    else:
        assert False    
    

def test_submission_on_time(): 
    name = "akend3"    
    with open('Data/courses.json') as usr:
        all_courses = json.load(usr)
        
    with open('Data/users.json') as usr:
        all_users = json.load(usr)
    on_time = Student.Student(name,all_users,all_courses)
    submission_date, due_date = "",""
    
    if on_time.check_ontime(submission_date,due_date):
        assert True
    else:
        assert False
        
def test_check_grades():
    name,course = "akend3","comp_sci"    
    
    with open('Data/courses.json') as usr:
        all_courses = json.load(usr)
        
    with open('Data/users.json') as usr:
        all_users = json.load(usr)
        
    check = Student.Student(name,all_users,all_courses)
    grades = check.check_grades(course)
    
    if grades:
        assert True
    else:
        assert False    

def test_view_assignments():
    name,course = "akend3", "comp_sci"    
     
    with open('Data/courses.json') as usr:
        all_courses = json.load(usr)
        
    with open('Data/users.json') as usr:
        all_users = json.load(usr)
    check = Student.Student(name,all_users,all_courses)
    assignments_returned = check.view_assignments(course)
    
    with open('Data/courses.json') as usr:
        courses_data = json.load(usr)
    
    course = data['comp_sci']['assignments']
    assignments = []
    for i in course:
        assignments.append([i,course[i]['due_date']])
    
    if assignments_returned == assignments:
        assert True
    else:
        assert False   



       
# @pytest.fixture
# def login_check():
#     checkStudent = System.System()
#     checkStudent.login()
#     return checkStudent
