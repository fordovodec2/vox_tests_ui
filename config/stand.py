import os

new_out_scenario = 'New out scenario'
new_inb_scenario = 'New inb scenario'

""" Системные переменные, которые нельзя передавать в гит"""
url = os.getenv('stand_url')
domain = os.getenv('stand_domain')
password = os.getenv('stand_password')
mail = os.getenv('stand_mail')
number_ru = os.getenv('stand_number_ru')
number_us = os.getenv('stand_number_us')
number_sip = os.getenv('stand_number_sip')
host = os.getenv('stand_host')
number_sp = os.getenv('stand_number_sp')

url_softphone = os.getenv('url_softphone')
username_softphone = os.getenv('username_softphone')
password_softphone = os.getenv('password_softphone')
app_name_softphone = os.getenv('app_name_softphone')
acc_name_softphone = os.getenv('acc_name_softphone')