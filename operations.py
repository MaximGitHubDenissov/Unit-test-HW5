import csv


def add_record(name, second_name, phone_number, comment):
    with open ('data_base.csv', 'a', encoding= 'cp1251', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', dialect='excel', lineterminator='\n')
        csv_writer.writerow([' ', name, second_name, phone_number, comment])

def enumerate_file():
    result_list =[]
    with open('data_base.csv', 'r+', encoding= 'cp1251', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';', dialect='excel')
        for id, row in enumerate(csv_reader):
            row[0] = str(id)
            result_list.append(row)
    with open('data_base.csv', 'w+', encoding= 'cp1251', newline='') as csv_file:    
        csv_writer = csv.writer(csv_file, delimiter=';', dialect='excel', lineterminator='\n')
        csv_writer.writerows(result_list)
    return result_list[len(result_list)-1]

def search_record(column, name):
    data = []
    with open('data_base.csv', 'r+', encoding= 'cp1251', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';', dialect='excel')
        for row in csv_reader:
                if row[column] == name: 
                    data.append(row)
    return data
            

def update_record(record_pos, column, name):
    result_list =[]
    with open('data_base.csv', 'r+', encoding= 'cp1251', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';', dialect='excel')
        for row in csv_reader:
            result_list.append(row)
    result_list[record_pos][column] = name
    with open('data_base.csv', 'w+', encoding= 'cp1251', newline='') as csv_file:    
        csv_writer = csv.writer(csv_file, delimiter=';', dialect='excel', lineterminator='\n')
        csv_writer.writerows(result_list)
    return result_list[record_pos]
 
def delete_record(number):
    result_list =[]
    with open('data_base.csv', 'r+', encoding= 'cp1251', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';', dialect='excel')
        for row in csv_reader:
            result_list.append(row)
    del result_list[number]
    with open('data_base.csv', 'w+', encoding= 'cp1251', newline='') as csv_file:    
        csv_writer = csv.writer(csv_file, delimiter=';', dialect='excel', lineterminator='\n')
        csv_writer.writerows(result_list)


