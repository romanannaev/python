import requests
from bs4 import BeautifulSoup
import psycopg2
import re




def get_response(url):
    """create object soup"""

    response = requests.get(url)
    return response.text


def get_total_info(html):
    """parsing site"""

    soup = BeautifulSoup(html, 'lxml')

    regexp = r'\d{1}'  
    kurs = soup.find('tbody').find('tr').find_all(text = re.compile(regexp))
    #total_kurs = [i.__str__().replace('td', '').replace('>', '').replace('<', '').replace('/', '') for i in kurs]
    return kurs


def insert_table(info):
    """insert total_kurs in table"""
    con = psycopg2.connect(
    database = 'postgres',
    user = 'postgres',
    password = '20021992',
    host = '127.0.0.1',
    port = '5432'
    )
    print ('database opened successufully')

    cur = con.cursor()

    cur.execute('insert into all_currency(usd_client, usd_bank, euro_client, euro_bank, rub_client, rub_bank) \
    values(%s,%s,%s,%s,%s,%s)', info)

    con.commit()
    print('record inserted successfully')
    con.close()


def main():
    url = 'https://select.by/kurs/'
    total_gen = get_total_info(get_response(url))
    print(total_gen)
    insert_table(total_gen)
    


if __name__ == "__main__":
    main()