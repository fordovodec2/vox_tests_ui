import os

new_out_scenario = 'New out scenario'
new_inb_scenario = 'New inb scenario'

""" Системные переменные, которые нельзя передавать в гитхаб"""
url = os.getenv('preprod_url')
domain = os.getenv('preprod_domain')
mail = os.getenv('preprod_mail')
password = os.getenv('preprod_password')
number_ru = os.getenv('preprod_number_ru')
number_us = os.getenv('preprod_number_us')
number_sip = os.getenv('preprod_number_sip')
number_sp = os.getenv('preprod_number_sp')
host = os.getenv('preprod_host')

url_softphone = os.getenv('url_softphone')
username_softphone = os.getenv('username_softphone')
password_softphone = os.getenv('password_softphone')
app_name_softphone = os.getenv('app_name_softphone')
acc_name_softphone = os.getenv('acc_name_softphone')