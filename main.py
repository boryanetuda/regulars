from pprint import pprint
import csv
import re
from collections import defaultdict
from itertools import groupby, chain
from collections import OrderedDict


def csv_open():
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def united(temp):
    for cont in temp:
        fn = cont[0]
        ln = cont[1]
        for new_cont in temp:
            new_fn = new_cont[0]
            new_ln = new_cont[1]
            if fn == new_fn and ln == new_ln:
                if cont[2] == "":
                    cont[2] = new_cont[2]
                if cont[3] == "":
                    cont[3] = new_cont[3]
                if cont[4] == "":
                    cont[4] = new_cont[4]
                if cont[5] == "":
                    cont[5] = new_cont[5]
                if cont[6] == "":
                    cont[6] = new_cont[6]
    final_list = []
    for i in temp:
        if i not in final_list:
            final_list.append(i)
    return final_list


def changes(contacts):
    pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
    new_list = []
    for item in contacts:
        name = ' '.join(item[:3]).split(' ')
        result = [name[0], name[1], name[2], item[3], item[4],
                  re.sub(pattern, r'+7(\2)-\3-\4-\5 \6\7', item[5]),
                  item[6]]
        new_list.append(result)
    return united(new_list)


def csv_write():
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(changes(csv_open()))


if __name__ == '__main__':
    csv_write()