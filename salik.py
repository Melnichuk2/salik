#Для всіх
#1. Запитати у користувача код регіону
#2. Отримати ЗВО з вказаного користувачем регіону
#3. Зберегти всі дані у файл universities.csv у форматі csv
#4. Збережіть ті ж дані у файл universities_<код регіону>.csv,
#наприклад universities_80.csv
#5. Якщо регіон не зі списку доступних, то повідомити про це користувачеві у консолі
#По варіантах - завдання #1
#1. Назви та контактні дані (телефон, email) в файл contacts.csv
#По варіантах - завдання #2
#Ускладніть програму з першого завдання наступним фільтром...
#1. З формою фінансування Державна
#Завдання 3
#Ускладніть програму з другого завдання можливістю фільтрування за будь-яким з
#наявних значень поля
#Підказка - сформуйте список всіх значень що зустрічають і дайте користувачеві
#обрати

import requests
import csv
region = str(input("Введіть код регіона: "))
cod_list1 = ['01', '05', '07', 12, 14, 18, 21, 23, 26, 32, 35, 44]
cod_list2 = [46, 48, 51, 53, 56, 59, 61, 63, 65, 68, 71, 73, 74, 80, 85]
region_list1 = int(region) in cod_list1
region_list2 = int(region) in cod_list2
if region_list1 is False:
    if region_list2 is False:
        print("Цей код регіона недоступний або його неіснує!")
print("Введіть інший код!")
exit(0)
r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc='+region+'&exp=json')
print('Форма фінансування: ''Державна''/Приватна''/Комунальна')
finances = str(input("Обреріть щось одне з вибірки: "))
universities: list = r.json()
filtered_data = [{k: row[k] for k in ['university_id', 'post_index']} for row in universities]
filtered_data_contacts = [{k: row[k] for k in ['university_name', 'university_email', "university_phone",
 'university_financing_type_name']}
 for k in ['university_financing_type_name'] for row in universities if row[k] == finances]
with open('universities_'+region+'.csv', mode='w', encoding='UTF-8') as f:
 writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
 writer.writeheader()
 writer.writerows(filtered_data)
with open('contacts.csv', mode='w', encoding='UTF-8') as f_c:
 writer = csv.DictWriter(f_c, fieldnames=filtered_data_contacts[0].keys())
 writer.writeheader()
 writer.writerows(filtered_data_contacts)