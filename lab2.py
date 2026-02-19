import os

def input_k():
    while True:
        try:
            k = int(input("Введите целое число K (0 < K < 10): "))
            if 0 < k < 10:
                return k
            else:
                print("Ошибка! K должно быть от 1 до 9.")
        except ValueError:
            print("Ошибка! Введите целое число.")

def check_file(name):
    if not os.path.exists(name):
        print("Файл не существует!")
        return False
    if os.path.getsize(name) == 0:
        print("Файл пуст!")
        return False
    return True

def z1():
    k = input_k()
    infile = input("Введите имя исходного файла (.txt): ")
    
    if not check_file(infile):
        return
    
    with open(infile, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    if not lines:
        print("Файл не содержит строк!")
        return
    
    outfile = input("Введите имя нового файла (.txt): ")
    
    with open(outfile, "w", encoding="utf-8") as f:
        f.writelines(lines[-k:])
    
    print("Готово!")


def z2():
    filename = input("Введите имя файла (.txt): ")
    
    if not check_file(filename):
        return
    
    students = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2 and parts[1].isdigit():
                students.append((parts[0], int(parts[1])))
    
    if not students:
        print("Нет корректных данных!")
        return

    min_age = min(age for _, age in students)
    print("Студенты с минимальным возрастом:")
    for name, age in students:
        if age == min_age:
            print(name)

def main():
    print("1 - К последних строк файла")
    print("2 - Студенты с минимальным возрастом")
    choice = input("Выберите вариант: ")    
    if choice == "1":
        z1()
    elif choice == "2":
        z2()
    else:
        print("Неверный выбор!")

main()