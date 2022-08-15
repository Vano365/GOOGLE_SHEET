import gspread
import time
import psycopg2
from psycopg2 import Error
from datetime import datetime, timedelta
import requests
import xmltodict
from config import *

def get_data():
    gc = gspread.service_account(filename='Emails/client1.json')
    #Открываем таблицу
    sh = gc.open_by_key(TOKEN_SHEET)
    worksheet = sh.get_worksheet(0)
    data = worksheet.get_all_values()
    return data[1:]

def db():
    try:
        connection = psycopg2.connect(user=USER_DB,
                                    password=PASSWORD_DB,
                                    host=HOST_DB,
                                    port=PORT_DB,
                                    database=NAME_DB)

        cursor = connection.cursor()
        cursor.execute("DELETE FROM main_orders")
        data = get_data()
        
        #Получение курса доллара
        now = datetime.now() - timedelta(days=2)
        now = now.strftime('%d/%m/%Y')
        response = requests.get(f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={now}&date_req2={now}&VAL_NM_RQ=R01235")
        soup = xmltodict.parse(response.content)
        print(soup)
        value = float(soup['ValCurs']['Record']['Value'].replace(",","."))
        
        for d in data:
            date = datetime.strptime(d[3], '%d.%m.%Y').date()
            rub = round(float(d[2]) * value,1)
            cursor.execute(f"INSERT INTO main_orders(id, number, total_dollar, supply, total_rub) VALUES({d[0]}, {d[1]}, {d[2]}, '{date}', {rub})")
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

def main():
    while True:
        db()
        time.sleep(600)


if __name__ == "__main__":
    main()