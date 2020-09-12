import os
!pip install adafruit-io

x = "narendra_kumar"  #ADAFRUIT_IO_USERNAME
y = "aio_Qsfq51AgxCoqEiET9Sr0uAVN54UG"  #ADAFRUIT_IO_KEY

from Adafruit_IO import Client, Feed
aio = Client(x,y)

from Adafruit_IO import Data

!pip install python-telegram-bot

from telegram.ext import Updater,CommandHandler
import requests  # Getting the data from the cloud

def light_on(bot,update):
  value = Data(value=1)
  value_send = aio.create_data('bot',value)
  chat_id = update.message.chat_id
  bot.send_message(chat_id,text='The light is on now')
  bot.send_photo(chat_id,photo='https://cdn5.vectorstock.com/i/1000x1000/60/94/cartoon-glowing-yellow-light-bulb-vector-18016094.jpg')
  
def light_off(bot,update):
  value = Data(value=0)
  value_send = aio.create_data('bot',value)
  chat_id = update.message.chat_id
  bot.send_message(chat_id,text='The light is off now')
  bot.send_photo(chat_id,photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTV6dJmnfFxyqSVMcjmh-FWb0H3oNkFTxp3mw&usqp=CAU')
  
u = Updater('1249178916:AAGlRXqs_fSXNiZyjdLzWwq42VB0V4SHCvY')
dp = u.dispatcher
dp.add_handler(CommandHandler('light_on',light_on))
dp.add_handler(CommandHandler('light_off',light_off))
u.start_polling() 
u.idle()
 
