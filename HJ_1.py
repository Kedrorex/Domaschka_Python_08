# Создать телефонный справочник с возможностью импорта и экспорта данных в формате 
# .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

comand = '0'
 
def show():
    with open('file.txt','r',encoding="utf-8") as f:
        for line in f:
            print(line)
    
    
def write_t():
    with open('file.txt','a',encoding='utf-8') as f:
        info_line = input("введите ИМЯ ФАМИЛИЮ НОМЕР\n")
        f.write(info_line.upper()+'\n')

def serch_t():
    with open('file.txt','r',encoding="utf-8") as f:
        serch_info = input("введите данные для поиска\n")
        for line in f:
            if serch_info.upper() in line:
                print(line)  
        

while comand != '4':
    comand  = input('\n\nвведите номер необходимой функции:\n1 - вывод данных\n2 - сохранить данныe\n3 - найти запись\n4 - закрытие программы\n')
    match comand:
        case '1':
            show()
        case '2':
            write_t()
        case '3':
            serch_t()
        case '4':
            break
        case _:
            message = 'Invalid input'
        