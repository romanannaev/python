import requests
from bs4 import BeautifulSoup
import csv


def get_response(url):
    response = requests.get(url)
    return response.text

def write_csv(current_kurs):
    with open('D:/Python/myProject/select.by' , 'a') as f:
        writer = csv.writer(f)

        writer.writerow((current_kurs['usd_client'],
                        current_kurs['usd_bank'],
                        current_kurs['euro_client'],
                        current_kurs['euro_bank'],
                        current_kurs['rub_client'],
                        current_kurs['rub_bank']))




def get_total_info(html):
    soup = BeautifulSoup(html, 'lxml')
    kurs = soup.find('tbody').find('tr').find_all ('td')[2 : 8]
    total_kurs = [i.__str__().replace('td', '').replace('>', '').replace('<', '').replace('/', '') for i in kurs]
    
    current_kurs = {'usd_client' : total_kurs[0] ,
                    'usd_bank' : total_kurs[1],
                    'euro_client' : total_kurs[2],
                    'euro_bank' : total_kurs[3],
                    'rub_client' : total_kurs[4],
                    'rub_bank' : total_kurs[5]}
   
    write_csv(current_kurs)




def main():
    url = 'https://select.by/kurs/'
    get_total_info(get_response(url))


if __name__ == "__main__":
    main()