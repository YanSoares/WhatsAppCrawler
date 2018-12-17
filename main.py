import re
from bot import wppbot

bot = wppbot('robozin')
bot.inicia('DATA SCIENCE BRAZIL 5')
ultimo_texto = ''

while True:

    texto = bot.escuta()
    
    if texto != ultimo_texto:

        ultimo_texto = texto
        print(texto)
        link = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', texto)
        if link:
             print('LINK DETECTADO: '+ link[0])
