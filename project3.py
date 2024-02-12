

class employee:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.pos = c

Michael = employee("Machael", 45, "Manager")
Dwight =  employee("Dwight",40, "Assistant to the Manager")
Jim = employee("Jim", 35, "Manager") 
Pam = employee("Pam",30, "Receptionist") 
Angela = employee("Angela",32, "Accountant") 
Kevin = employee("Kevin", 42, "Accountant") 
Oscar = employee("Oscar", 40, "Accountant") 
Stanley = employee("Stanley", 55, "Salesperson") 
Phyllis = employee("Phyllis", 45, "Salesperson") 
Andy = employee("Andy", 38, "Salesperson") 
Ryan = employee("Ryan", 30, "Salesperson") 
Creed = employee("Creed", 55, "Salesperson")

empl_lst = [Michael, Dwight, Jim, Creed, Pam, Angela, Kevin, Oscar, Stanley, Phyllis, Andy, Ryan]

'''Goes through each object in a list and displays each atribute'''
def display_employees(lst):
    print("Employees in Dunder Mifflin are: ")
    for i in lst:
        print(i.name, i.age, i.pos)


'''sorts each employee's position and puts it in the respective list then returns the lists as one single list'''
def allocate_department(lst):
    managers = [[i.name, i.age, i.pos] for i in lst if i.pos == "Manager" or i.pos == "Assistant to the Manager"]
    sales = [[i.name, i.age, i.pos] for i in lst if i.pos == "Salesperson"]
    accounts = [[i.name, i.age, i.pos] for i in lst if i.pos == "Accountant"]
    res = [managers, sales, accounts]
    return res

'''displayus each emplyee in their respective department'''
def display_department_employees(lst): 
    print("Management")
    count = 0
    for i in range(len(lst)):
        for j in lst[i]:
            print(j)
            count += 1
            if count == 3:
                print("Salespersons:")
            elif count == 8:
                print("Accountants:")

print(allocate_department(empl_lst))
#display_department_employees(allocate_department(empl_lst))

'''sorts the employees from ages oldest to youngest'''
def head_of_department(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])-1):
            if lst[i][j][1] < lst[i][j+1][1]:
                temp = lst[i][j] 
                lst[i][j]= lst[i][j + 1] 
                lst[i][j + 1]= temp
    return lst



display_department_employees(head_of_department(allocate_department(empl_lst)))


