import allure
import requests

class EmployeesApi:
    def __init__(self, url):
        self.url = url

    @allure.step("api.Создать компанию {name}:{description}")
    def create_company(self, name: str, description=""):
        company = {
            'name': name,
            'description': description
            }
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        return resp.json()

    @allure.step("api.Получить компанию по {id}")
    def get_company(self, id: int):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    @allure.step("api.Получить сотрудника по {id}")
    def get_employee(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()

    @allure.step("api.Получить список сотрудников организации {companyId}")
    def get_employees_list(self, companyId: int):
        params = {'company': companyId}
        resp = requests.get(self.url + '/employee', params=params)
        return resp.json()

    @allure.step("API.Получить токен авторизации {user}:{password}")
    def get_token(self, user = 'bloom', password = 'fire-fairy'):
        """
        Получить токен авторизации
        :params user(str): логин пользователя
        :params password(str): пароль пользователя

        :return: str: token
        """
        creds = {
           'username': user,
           'password': password
           }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()['userToken']

    @allure.step("api.Добавить нового сотрудника {firstName}:{lastName}:{middleName}:{companyId}:{email}:{url}:{phone}:{birthdate}:{isActive}")
    def create_employee(self, firstName: str, lastName: str, middleName: str, companyId: int, email: str, url: str, phone: int, birthdate: bool, isActive: bool):
        employee = {
            'firstName': firstName,
            'lastName': lastName,
            'middleName': middleName,
            'companyId': companyId,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
            }
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.post(self.url + '/employee', json=employee, headers=my_headers)
        return resp.json()

    @allure.step("api.Редактировать данные сотрудника {new_lastName}:{new_email}:{new_url}:{new_phone}:{new_isActive}:{id}")
    def edit_employee(self, new_lastName: str, new_email: str, new_url: str, new_phone: int, new_isActive: bool, id: int):
        employee = {
           'lastName': new_lastName,
           'email': new_email,
           'url':  new_url,
           'phone': new_phone,
           'isActive': new_isActive
           }
        my_headers = {'x-client-token': self.get_token()}
        resp = requests.patch(self.url + '/employee/' + str(id), headers=my_headers, json=employee)
        return resp.json()

    @allure.step("api.Удалить сотрудника по {id}")
    def delete_employee(self, id: int):
        employee = {
           'id': id
           }
        my_headers = {'x-client-token': self.get_token()}
        resp = requests.delete(self.url + f'/employee/{id}', headers=my_headers)
        return resp.json()