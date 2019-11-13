# Language is armenian
# pip install pyowm
# pip install pyTelegramBotAPI
# https://t.me/exanakpaybot


import telebot
import pyowm

owm = pyowm.OWM('d85e7ac642f805a3c5213e658c821b3d')
bot = telebot.TeleBot("925990020:AAHyKE7Ho4rltUpEvIUGDRXOfOsHIy3NixQ")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '''Բարև, Ես բոտ եմ՝ 
						   ով քեզ կօգնի իմանալ 
						   քո ուզած երկրի կամ քաղաքի ջերմաստիճանը։
						   \nՊարզապես գրիր երկրի կամ քաղաքի անվանումը 
						   (օրինակ՝ Armenia կամ Yerevan ):''')


@bot.message_handler(content_types=['text'])
def send_echo(message):
    answer = ""

    try:
        # Get whole data about whether of the inputted place
        observation = owm.weather_at_place(message.text)
        # Extract the temperature only
        temperature = observation.get_weather().get_temperature('celsius')['temp']

        # Response Message to user
        answer = "Ջերմաստիճանը տվյալ հատվածում " + str(temperature) + "°C է:" + "\n\n"

        # If no errors occur, finalize the response
        if temperature < 10:
            answer += "Տաք հագնվելը պարտադիր է: "
        elif temperature < 20:
            answer += "Խորհուրդ է տրվում տաք հագնվել: "
        else:
            answer += "Նորմալ եղանակ է, կարող եք հագնել ինչ ցանկանում եք: "
    except Exception as e:
        print(e)
        # In case user input is incorrect
        answer += "Սխալ մուտքաագրում: \nՍտուգեք ուղղագրությունը!!!"

    # Sent to user
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
input()
