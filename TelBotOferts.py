from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import pandas as pd
import time 
   
#step 3
#from the product database creates a new dataframe 



TOKEN: Final 
#TOKEN: Final = API KEY
BOT_USERNAME: Final 
#BOT_USERNAME: Final = BOT USERNAME

#commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi, ready to find deals!')
    num = 5
    #for indexz in range(5):
        #prodNum = result_df['ProdNo#'][indexz]
        #linkFull = f'https://www.amazon.com.mx/dp/{prodNum}/ref=nosim?tag=techymas-20'
        #await update.message.reply_text(linkFull)
        #time.sleep(1)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi, ready to find deals! help')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi, ready to find deals! custom')

#responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hola' in processed:
        return 'holaaa'
    if 'adios' in processed:
        return 'adioos'
    if 'que hora es' in processed:  
        return 'que hora es'
    if '5' in processed:
        return 'por el culo te la hinco'
    
    return 'No te entiendo  '

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User:{update.message.chat.id} in {message_type} : "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip() #limpia el quita el nomre del bot
            response: str = handle_response(new_text)
        else:
            return
    else:   
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
  print(f'Update :{update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting Bot...')
    app = Application.builder().token(TOKEN).build()

    #COMMANDS
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #Errors
    app.add_error_handler(error)

    #Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)