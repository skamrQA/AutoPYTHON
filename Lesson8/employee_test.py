import requests
from employee_API import EmployeeApi

api = EmployeeApi("https://x-clients-be.onrender.com")

def test_add_new_employee():
    
    name = "Sea products Co"
    descr = "sea products"
    result = api.create_company(name, descr)
    new_id = result["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    body = api.get_employees_list(companyId)
    len_before = len(body)
   
    firstName = "Kamil"
    lastName = "Safin"
    middleName = "Ramilevich"
    company = companyId
    email = "skamrtest@gmail.com"
    url = "string"
    phone = "89956398270"
    birthdate = "1990-09-18"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    
    body = api.get_employees_list(companyId) 
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "Kamil"
    assert body[-1]["lastName"] == "Safin"
    assert body[-1]["middleName"] == "Ramilevich"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "89956398270"
    assert body[-1]["birthdate"] == "1990-09-18"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_get_employees_id():
    name = "Aviasales"
    descr = "авиакомпания"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
  
    new_company = api.get_company(new_id)
    companyId = new_company['id']
   
    body = api.get_employees_list(companyId)
    begin_list = len(body) 
   
    firstName = "Olga"
    lastName = "Trifonova"
    middleName = "Olegovna"
    company = companyId
    email = "triа44@yandex.ru"
    url = "string"
    phone = "89951234587"
    birthdate = "1965-10-15"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
   
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1
 
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "Olga"
    assert body[-1]["lastName"] ==  "Trifonova"
    assert body[-1]["middleName"] == "Olegovna"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "89951234587"
    assert body[-1]["birthdate"] == "1965-10-15"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_patch_employee():
    name = "KFC"
    descr = "fast food"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    firstName = "Kira"
    lastName = "Romanova"
    middleName = "Fedorovna"
    company = companyId
    email = "krfedo@mail.ru"
    url = "string"
    phone = "89106547895"
    birthdate = "1990-01-05"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
   
    body = api.get_employees_list(companyId) 
   
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]

    new_email = "new@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_email, new_url, new_phone, new_isActive)
    assert edited["email"] == "new@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False
    
    

    
    