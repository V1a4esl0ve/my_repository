# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher
from aiogram.types import  Message
from aiogram.filters import Command
from aiogram import F

#Сначала функции для списка валют и далее для конвертации
lst_cur=['ARS', 'AUD', 'AZN', 'BGN', 'BYN', 'BRL', 'HUF', 'VES', 'HKD', 'GEL', 'USD', 'DKK', 'EUR', 'ISK', 'ILS', 'INR', 'KGS', 'KZT', 'CAD', 'CNY', 'MDL', 'MXN', 'NZD', 'NOK', 'AED', 'PKR', 'PLN', 'RON', 'RUB', 'SGD', 'SAR', 'TJS', 'THB', 'TMT', 'TWD', 'TRY', 'UAH', 'UZS', 'PHP', 'CZK', 'CHF', 'SEK', 'ZAR', 'JPY']
lst_cur2=['DZD', 'AMD', 'AWG', 'AFN', 'BSD', 'BHD', 'BBD', 'BMD', 'BOB', 'BZD', 'BND', 'BIF', 'PAB', 'VED', 'KRW', 'VUV', 'XCD', 'GIP', 'GNF', 'GYD', 'HTG', 'PYG', 'GHS', 'SBD', 'KYD', 'DOP', 'FJD', 'GMD', 'NAD', 'VND', 'TTD', 'MKD', 'STN', 'ZWL', 'EGP', 'COU', 'NIO', 'ZMW', 'IRR', 'IQD', 'JOD', 'YER', 'MMK', 'COP', 'KMF', 'CRC', 'HRK', 'CUP', 'GTQ', 'KES', 'KWD', 'PGK', 'QAR', 'CUC', 'AOA', 'CDF', 'ВАМ', 'HNL', 'LAK', 'LBP', 'LSL', 'LRD', 'LYD', 'SLL', 'SZL', 'SLE', 'MWK', 'MYR', 'MUR', 'MAD', 'MZN', 'MGA', 'BTN', 'ERN', 'NPR', 'ANG', 'NGN', 'OMR', 'BWP', 'MOP', 'TOP', 'KHR', 'IDR', 'MVR', 'RUB', 'SVC', 'KPW', 'PEN', 'SCR', 'SOS', 'SYP', 'SDG', 'RSD', 'XDR', 'SRD', 'BDT', 'MNT', 'TND', 'TZS', 'WST', 'UGX', 'UYU', 'MRU', 'UYI', 'FKP', 'DJF', 'RWF', 'SHP', 'GBR', 'XAF', 'XOF', 'XPF', 'CLP', 'LKR', 'CVE', 'ETB', 'SSP', 'JMD']


dic_cur={'ARS': 'Аргентинское песо', 'AUD': 'Австралийский доллар', 'AZN': 'Азербайджанский манат', 'BGN': 'Болгарский лев', 'BYN': 'Белорусский рубль', 'BRL': 'Бразильский реал', 'HUF': 'Венгерский Форинт', 'VES': 'Венесуэлла Боливар Соберано', 'HKD': 'Гонконгский доллар', 'GEL': 'Грузинский Лари', 'USD': 'Доллар США', 'DKK': 'Датская крона', 'EUR': 'Евро', 'ISK': 'Исландская крона', 'ILS': 'Израильский шекель', 'INR': 'Индийская рупия', 'KGS': 'Киргизский Сом', 'KZT': 'Казахский Тенге', 'CAD': 'Канадский доллар', 'CNY': 'Китайский Юань', 'MDL': 'Молдавский лей', 'MXN': 'Мексиканское песо', 'NZD': 'Новозеландский доллар', 'NOK': 'Норвежская крона', 'AED': 'ОАЭ Дирхам ', 'PKR': 'Пакистанская рупия', 'PLN': 'Польский Злотый', 'RON': 'Румынский лей', 'RUB': 'Российский рубль', 'SGD': 'Сингапурский доллар', 'SAR': 'Саудовский риял', 'TJS': 'Таджикский Сомони', 'THB': 'Тайский Бат', 'TMT': 'Туркменский манат', 'TWD': 'Тайваньский доллар', 'TRY': 'Турецкая лира', 'UAH': 'Украинская Гривна', 'UZS': 'Узбекский сум', 'PHP': 'Филиппинское песо', 'CZK': 'Чешская крона', 'CHF': 'Швейцарский франк', 'SEK': 'Шведская крона', 'ZAR': 'Южноафриканский Рэнд', 'JPY': 'Японская Иена'}



def convertator(cur1,cur2, count):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    response=requests.get(url=f'https://ru.investing.com/currencies/{cur1.lower()}-{cur2.lower()}',  headers= headers)
    soup=BeautifulSoup(response.text,'lxml')
    num=float(soup.find('span',{'data-test':'instrument-price-last'}).text.replace(',','.'))
    return str(count)+' '+ dic_cur[cur1.upper()]+ ' = ' +str(num*count)+' '+str(dic_cur[cur2.upper()])



#Сам телеграмм бот

BOT_TOKEN: str = '6678054142:AAF5VMAPJaH4kAGmmptKjF5nqQfBFD5WyBw'
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()
user:dict={}
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет! Я бот, который конвертирует любую валюту.\n'
                         '1) Сначала выбери валюту, которую хочешь конвертировать.\n'
                         '2) Потом напиши количество этой валюты.\n'
                         '3) И наконец, выбери в какую валюту ты хочешь ковертировать.\n'
                         'Я беру данные с валютной биржи.\n'
                         'Если ты забыл(а) как пишется интересующая тебя валюта, выбери команду /help.\n'
                         'Итак, напиши валюту, которую ты хочешь конвертировать:')
    user[message.from_user.id]={'in_count':True,
                                'cur1':None,
                                'count':0,
                                'cur2':None,
                                'nums':0}
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('ARS - Аргентинское песо\nAZN - Азербайджанский манат\nAUD - Австралийский доллар\nBGN - Болгарский лев\nBRL - Бразильский реал\nBYN - Белорусский рубль\nHUF - Венгерский Форинт\nVES - Венесуэлла Боливар Соберано\nHKD - Гонконгский доллар\nGEL - Грузинский Лари\nUSD - Доллар США\nDKK - Датская крона\nEUR - Евро\nISK - Исландская крона\nINR - Индийская рупия\nILS - Израильский шекель\nKGS - Киргизский Сом\nKZT - Казахский Тенге\nCAD - Канадский доллар\nCNY - Китайский Юань\nMXN - Мексиканское песо\nMDL - Молдавский лей\nNOK - Норвежская крона\nNZD - Новозеландский доллар\nAED - ОАЭ Дирхам \nPLN - Польский Злотый\nPKR - Пакистанская рупия\nRUB - Российский рубль\nRON - Румынский лей\nSGD - Сингапурский доллар\nSAR - Саудовский риял\nTRY - Турецкая лира\nTJS - Таджикский Сомони\nTMT - Туркменский манат\nTHB - Тайский Бат\nTWD - Тайваньский доллар\nUZS - Узбекский сум\nUAH - Украинская Гривна\nPHP - Филиппинское песо\nCZK - Чешская крона\nSEK - Шведская крона\nCHF - Швейцарский франк\nZAR - Южноафриканский Рэнд\nJPY - Японская Иена\n')


@dp.message(lambda message: (message.text and message.text.isalpha() and message.text.upper() in lst_cur) or (message.text and message.text.isdigit()))
async def process_numbers_answer(message: Message):
    if message.text.isalpha():
       if user[message.from_user.id]['cur1'] is None:
            user[message.from_user.id]['cur1']=message.text.lower()
          #  print(user[message.from_user.id]['cur1'])
            user[message.from_user.id]['nums']+=1
            await message.answer('Отлично, теперь введи число - сколько этой валюты ты хочешь конвертировать.')
         #   print(user[message.from_user.id])
       elif  user[message.from_user.id]['cur1'] is not None and user[message.from_user.id]['cur2'] is None:
            user[message.from_user.id]['cur2']=message.text.lower()
          #  print(user[message.from_user.id]['cur2'])
            user[message.from_user.id]['nums'] += 1
         #   print(user[message.from_user.id])

    elif message.text.isdigit():
        if user[message.from_user.id]['count']==0:
            user[message.from_user.id]['count']=int(message.text)
            user[message.from_user.id]['nums'] += 1
            await message.answer('Прекрасно, теперь выбери в какую валюту ты хочешь конвертировать.')
          #  print(user[message.from_user.id])
    if user[message.from_user.id]['nums']==3:
        await message.answer(convertator(user[message.from_user.id]['cur1'],user[message.from_user.id]['cur2'],user[message.from_user.id]['count']))
        user[message.from_user.id] = {'in_count': False,
                                      'cur1': None,
                                      'count': 0,
                                      'cur2': None,
                                      'nums': 0}
@dp.message(lambda message: message.text in lst_cur2)
async def process_other_answers(message: Message):
    await message.answer('Упс, данная валюта не торгуется на бирже.')

@dp.message()
async def process_other_answers(message: Message):
    await message.answer('Мой создатель создал меня только для конвертации валюты.')





if __name__ == '__main__':
    dp.run_polling(bot)








