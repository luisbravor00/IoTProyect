import random
import datetime

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


def calculate_next_dosages(prescriptions):
    current_datetime = datetime.datetime.now()
    upcoming_doses = []

    for prescription in prescriptions:
        times_per_day = prescription['TIMES_PER_DAY']
        intervals = 24 // times_per_day
        for i in range(times_per_day):
            time_of_day = datetime.time(hour=(intervals * i))
            dose_datetime = datetime.datetime.combine(current_datetime.date(), time_of_day)
            if dose_datetime < current_datetime:
                dose_datetime += datetime.timedelta(days=1)
            if dose_datetime.date() == current_datetime.date():
                upcoming_doses.append({
                    'medication_name': prescription['MEDICATION_NAME'],
                    'active_ingredient': prescription['MEDICATION_ACTIVE_INGREDIENT'],
                    'dose_time': dose_datetime.time()
                })

    # Ordenar las dosis por hora
    upcoming_doses.sort(key=lambda x: x['dose_time'])
    return upcoming_doses