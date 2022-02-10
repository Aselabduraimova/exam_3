import csv
with open("classmates.csv", encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=",")
    count = 0

    for row in file_reader:
        if count == 0:
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            print(f' {row["Асель"]} - {row["backend developer"]}', end='')
            print(f' и она родилась в {row["2003"]} году.')
        count += 1
        print(f'Всего в файле  {count} строк.')