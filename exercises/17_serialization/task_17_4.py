# -*- coding: utf-8 -*-
"""
Задание 17.4

Создать функцию write_last_log_to_csv.

Аргументы функции:
* source_log - имя файла в формате csv, из которого читаются данные (пример mail_log.csv)
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Функция write_last_log_to_csv обрабатывает csv файл mail_log.csv.
В файле mail_log.csv находятся логи изменения имени пользователя. При этом, email
пользователь менять не может, только имя.

Функция write_last_log_to_csv должна отбирать из файла mail_log.csv только
самые свежие записи для каждого пользователя и записывать их в другой csv файл.

Для части пользователей запись только одна и тогда в итоговый файл надо записать только ее.
Для некоторых пользователей есть несколько записей с разными именами.
Например пользователь с email c3po@gmail.com несколько раз менял имя:
C=3PO,c3po@gmail.com,16/12/2019 17:10
C3PO,c3po@gmail.com,16/12/2019 17:15
C-3PO,c3po@gmail.com,16/12/2019 17:24

Из этих трех записей, в итоговый файл должна быть записана только одна - самая свежая:
C-3PO,c3po@gmail.com,16/12/2019 17:24

Для сравнения дат удобно использовать объекты datetime из модуля datetime.
Чтобы упростить работу с датами, создана функция convert_datetimestr_to_datetime - она
конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
Полученные объекты datetime можно сравнивать между собой.

Функцию convert_datetimestr_to_datetime использовать не обязательно.

"""

import datetime
import csv


def convert_datetimestr_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def write_last_log_to_csv(source_log: str, output: str):
    out = dict()
    with open(source_log, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row['Email']
            name = row['Name']
            date = row['Last Changed']
            if email in out:
                date_curr_conv = convert_datetimestr_to_datetime(date)
                date_exist_conv = convert_datetimestr_to_datetime(out[email]['Last Changed'])
                if date_curr_conv < date_exist_conv:
                    continue
            out[email] = {'Name': name, 'Last Changed': date}
    out_ready = [{'Name': out[key]['Name'], 'Email': key, 'Last Changed': out[key]['Last Changed']} for key in out.keys()]
    with open(output, 'w') as fw:
        writer = csv.DictWriter(fw, fieldnames=list(out_ready[0].keys()))
        writer.writeheader()
        writer.writerows(out_ready)


if __name__ == '__main__':
    write_last_log_to_csv('mail_log.csv', 'mail_log_changed.csv')
