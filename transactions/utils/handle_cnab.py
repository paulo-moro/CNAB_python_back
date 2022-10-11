from datetime import date, time, datetime
import os

from transactions.models import CNABFile


def read_cnab(filepath):
    """Function that take a CNAB File and convert into a list"""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            read_file = file.read()
            splited_file = read_file.split("\n")
            return splited_file
    except (FileNotFoundError):
        return []


def transaction_transcription(cnab_reading, serializer, user):
    """Function that transcript the cnab file to a transaction and return a list"""
    response_list = []
    request = {
        "type": "",
        "transaction_date": "",
        "amount": "",
        "CPF": "",
        "card": "",
        "transaction_time": "",
        "shop_rep": "",
        "shop_name": "",
    }

    for transaction in cnab_reading:
        transaction_type = transaction[0]

        request["type"] = transaction_type

        formated_date = date(
            int(transaction[1:5]), int(transaction[5:7]), int(transaction[7:9])
        )
        formated_datetime = datetime(
            int(transaction[1:5]),
            int(transaction[5:7]),
            int(transaction[7:9]),
            int(transaction[42:44]),
            int(transaction[44:46]),
            int(transaction[46:48]),
        )

        request["transaction_date"] = formated_date
        request["amount"] = transaction[9:19]
        request["CPF"] = transaction[19:30]
        request["card"] = transaction[30:42]
        formated_time = time(
            int(transaction[42:44]), int(transaction[44:46]), int(transaction[46:48])
        )

        request["transaction_time"] = formated_time
        request["shop_rep"] = transaction[48:62]
        request["shop_name"] = transaction[62:82]
        request["user"] = user.id

        transaction_serializer = serializer(data=request)

        transaction_serializer.is_valid(raise_exception=True)
        transaction_serializer.save()
        response_list.append(transaction_serializer.data)

    return response_list


def delete_cnab(filepath, cnab_id):
    """Function that delete cnab file from database"""
    cnab_delete = CNABFile.objects.get(id=cnab_id)
    cnab_delete.delete()
    os.remove(filepath)
