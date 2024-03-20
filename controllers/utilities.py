import random

def generate_random_number():
    return random.randint(10000000, 99999999)

def get_all_columns(cursor):
    columns = [desc[0] for desc in cursor.description]

    return columns


def get_dictionary_from_query(result, cursor):
    data_list = []
    columns = get_all_columns(cursor)

    for row in result:
        dict = {columns[i]: row[i] for i in range(len(columns))}
        data_list.append(dict)

    return data_list