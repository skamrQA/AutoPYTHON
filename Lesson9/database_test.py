from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"

def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[1] == 'company'

def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[0]

    assert row1['id'] > 2928
    assert row1['name'] == "SkyPro"

def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 5162).fetchall()

    assert len(rows) == 1
    assert rows[-1]['name'] == "Барбершоп 'ЦирюльникЪ'"

def test_insert_company():
    db = create_engine(db_connection_string)
    sql = text("insert into company (\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = 'SkyPro')
    
def test_insert_employee():
    db = create_engine(db_connection_string)
    sql = text("insert into employee (first_name, last_name, middle_name, phone, email, birthdate, avatar_url, company_id) values (:new_first_name, :new_last_name, :new_middle_name, :new_phone, :new_email, :new_birthdate, :new_avatar_url, :company_id)")
    rows = db.execute(sql, new_first_name = 'Ivan', new_last_name = 'Travkin', new_middle_name = 'Petrovich', new_phone = '89038095578', new_email = 'travkinivan@mail.ru', new_birthdate = '1985-01-30', new_avatar_url = 'string', company_id = 5162)

def test_update_company():
    db = create_engine(db_connection_string)
    sql = text("update company set description = :descr where id = :company_id")
    rows = db.execute(sql, descr = 'Муж на час', company_id = 3379)

def test_update_employee():
    db = create_engine(db_connection_string)
    sql = text("update employee set last_name = :last_name, phone = :phone, email = :mail, avatar_url = :url, is_active = :is_active  where id = :employee_id")
    rows = db.execute(sql, last_name = 'Kukushkin', phone = '89959872563', mail = 'kukushkin@yandex.ru', url = 'wow', is_active = False, employee_id = 1835)

def test_delete_emloyee():
    db = create_engine(db_connection_string)
    sql = text("delete from employee where id = :employee_id")
    rows = db.execute(sql, employee_id = 1965)

def test_delete_company():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :id")
    rows = db.execute(sql, id = 2446)