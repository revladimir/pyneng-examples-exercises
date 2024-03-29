# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""
#import os
#from pprint import pprint
#from netmiko import ConnectHandler
#import yaml
#import netmiko
#
#
#def send_and_parse_show_command(device_dict, command, template_path):
#    os.environ["NET_TEXTFSM"]  = "/home/vagrant/venv/pyneng-py3-8/lib/python3.8/site-packages/ntc-templates/templates" 
#    with ConnectHandler(**device_dict) as ssh:
#        ssh.enable()
#        output = ssh.send_command(command, use_textfsm=True)
#    return output
#
#
#if __name__ == "__main__":
#    full_pth = os.path.join(os.getcwd(), "templates")
#    with open("devices.yaml") as f:
#        devices = yaml.safe_load(f)
#    for dev in devices:
#        result = send_and_parse_show_command(
#            dev, "sh ip int br", template_path=full_pth
#        )
#        pprint(result, width=120)

import os
from pprint import pprint
from netmiko import ConnectHandler
import yaml


def send_and_parse_show_command(device_dict, command, templates_path):
    if "NET_TEXTFSM" not in os.environ:
#        os.environ["NET_TEXTFSM"] = "/home/vagrant/venv/pyneng-py3-8/lib/python3.8/site-packages/ntc_templates/templates/" 
#        os.environ["NET_TEXTFSM"] = "/home/vagrant/pyneng-examples-exercises/exercises/21_textfsm/templates/"
        os.environ["NET_TEXTFSM"] = templates_path
#        print(os.environ["NET_TEXTFSM"])
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command, use_textfsm=True)
    return output


if __name__ == "__main__":
    full_pth = os.path.join(os.getcwd(), "templates")
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        result = send_and_parse_show_command(
            dev, "sh ip int br", templates_path=full_pth
        )
        pprint(result, width=120)

