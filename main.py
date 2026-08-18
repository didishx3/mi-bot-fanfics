import os
import telebot
import urllib.parse
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

# 1. CONFIGURACIÓN DEL BOT
TOKEN = "8778828947:AAFWAhNJi-kTmfWtAh6ZKFXtrvBFQuKe_1I"
bot = telebot.TeleBot(TOKEN)

# 2. MINI-SERVIDOR PARA MANTENERLO VIVO
app = Flask('')

@app.route('/')
def home():
    return "¡El súper bot de fanfics 6-en-1 está vivo 24/7!"

def run():
    app.run(host='0.0.0.0', port=8080)

# 3. GENERADOR DE PANEL CON 6 BOTONES INTERACTIVOS
def buscar_fanfics_seguro(termino):
    base_buscador = "https://bing.com"
    
    url_ao3 = f"{base_buscador}?q={urllib.parse.quote_plus(f'site:archiveofourown.org/works {termino}')}"
    url_wattpad = f"{base_buscador}?q={urllib.parse.quote_plus(f'site:wattpad.com {termino}')}"
    url_fanfiction = f"{base_buscador}?q={urllib.parse.quote_plus(f'site:fanfiction.net {termino}')}"
    url_inkitt = f"{base_buscador}?q={urllib.parse.quote_plus(f'site:inkitt.com {termino}')}"
    url_sweek = f"{base_buscador}?q={urllib.parse.quote_plus(f'site:sweek.com {termino}')}"
    url_inkspired = f"{base_buscador}?q={urllib.parse.quote_plus(f'site:getinkspired.com {termino}')}"
    
    markup = InlineKeyboardMarkup()
    
    b_ao3 = InlineKeyboardButton("❤️ AO3", url=url_ao3)
    b_wattpad = InlineKeyboardButton("🧡 Wattpad", url=url_wattpad)
    b_fanfiction = InlineKeyboardButton("💙 FanFiction", url=url_fanfiction)
    b_inkitt = InlineKeyboardButton("💚 Inkitt", url=url_inkitt)
    b_sweek = InlineKeyboardButton("💜 Sweek", url=url_sweek)
    b_inkspired = InlineKeyboardButton("🖤 Inkspired", url=url_inkspired)
    
    markup.row(b_ao3, b_wattpad)
    markup.row(b_fanfiction, b_inkitt)
    markup.row(b_sweek, b_inkspired)
    
    return markup

# 4. COMANDOS DEL BOT
@bot.message_handler(commands=['start', 'help'])
def enviar_bienvenida(message):
    bot.reply_to(message, "¡Buscador Total 6-en-1 Activo! 🚀\n\nEscribe /buscar seguido de tu shipp o temática.\nEjemplo: `/buscar yoonmin mafia`")

@bot.message_handler(commands=['buscar'])
def realizar_busqueda(message):
    termino = message.text.replace("/buscar", "").strip()
    
    if not termino:
        bot.reply_to(message, "Por favor, escribe qué quieres buscar. Ejemplo: /buscar yoonmin")
        return
        
    bot.reply_to(message, f"🔍 Rastreando en las 6 plataformas para **'{termino}'**...")
    botones = buscar_fanfics_seguro(termino)
    bot.send_message(message.chat.id, f"📚 Elige la plataforma para leer **'{termino}'**:", reply_markup=botones)

# 5. ENCENDER SERVIDOR Y BOT
if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    print("¡El súper bot 6-en-1 está encendido!")
    bot.infinity_polling()
