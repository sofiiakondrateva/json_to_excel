import json
import csv

file_read = input("Укажите путь к файлу json: ")

with open(file_read, 'r', encoding="utf-8") as file:
    data = json.load(file)

df_cards = data["cards"]
df_lists = data["lists"]

rows = ["Название списка", "Название карточки", "Описание", "Срок выполнения", "Выполнение сроков", "Название метки",
        "Цвет метки", "Наименование вложения", "url на вложение", "Короткий url"]

file_write = input("Укажите путь для сохранения csv: ")

with open(file_write, "w", newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, rows)
    writer.writeheader()

def write_csv(FILE, FIELDNAME):
    writer = csv.DictWriter(FILE, FIELDNAME)
    writer.writeheader()

with open(file_write, "a", newline='', encoding="utf-8") as file:
        for lists in df_lists:
                for card in df_cards:
                    if card["idList"] == lists["id"]:
                        for attach in card["attachments"]:
                            for lab in card["labels"]:
                                fieldnames = [lists["name"], card["name"], card["desc"], card["due"], card["dueComplete"],
                                      lab["name"], lab["color"], attach["name"], attach["url"], card["shortUrl"]]
                                write_csv(file, fieldnames)
                            if card["labels"] == []:
                                fieldnames = [lists["name"], card["name"], card["desc"], card["due"], card["dueComplete"],
                                      lab["name"] == None, lab["color"] == None, attach["name"], attach["url"],
                                              card["shortUrl"]]
                                write_csv(file, fieldnames)
                        if card["attachments"] == []:
                            for lab in card["labels"]:
                                fieldnames = [lists["name"], card["name"], card["desc"], card["due"], card["dueComplete"],
                                              lab["name"], lab["color"], attach["name"] == None, attach["url"] == None,
                                              card["shortUrl"]]
                                write_csv(file, fieldnames)
                            if card["labels"] == []:
                                fieldnames = [lists["name"], card["name"], card["desc"], card["due"], card["dueComplete"],
                                              lab["name"] == None, lab["color"] == None, attach["name"] == None,
                                              attach["url"] == None, card["shortUrl"]]
                                write_csv(file, fieldnames)