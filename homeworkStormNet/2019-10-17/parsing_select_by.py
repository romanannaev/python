import requests
from bs4 import BeautifulSoup
import datetime

def get_html(url):
    resp = requests.get(url)
    return resp.text

def get_kurs_currency(html):
    
    soup = BeautifulSoup(html, 'lxml')
    kurs = soup.find_all('tr')[11]
    print(kurs)
    lst_1 = [print(i) for i in kurs]
    lst = [i.get_text() for i in kurs]
    return lst[1:-1]
    # //*[@id="curr_table"]/tbody/tr[10]/td[2]
    
def write_txt(data, lst_currency):
    with open('exchange_currency.txt', mode='w', encoding='utf-8') as f:
        index = 0
        f.write('Курс валют в банке "Дабрабыт"  на Партизансокго 46:\n')
        f.write('Запись в файл сделана: ' + str(datetime.datetime.now()) + '\n')
        for i in data:
            f.write(i + ': ' + lst_currency[index] + ';\n')
            index += 1

def main():

    url = 'https://select.by/kurs/'
    lst_currency = get_kurs_currency(get_html(url))
    data = ['euro_bank', 'euro_client', 'usd_bank', 'usd_client', 'rub_bank', 'rub_client']
    write_txt(data, lst_currency)

if __name__ == "__main__":
    main()