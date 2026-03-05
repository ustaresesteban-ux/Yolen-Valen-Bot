import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8752475374:AAF-_NOlXLVSM_ZxTzwSmWPkrN1bS5Ue6gU"
ADMIN_ID = 123456789  # TU ID DE TELEGRAM

bot = telebot.TeleBot(TOKEN)

# MENÚ PRINCIPAL
@bot.message_handler(commands=['start'])
def start(message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = KeyboardButton("🔑 Suscripción VIP")
    btn2 = KeyboardButton("🎁 Promociones")
    btn3 = KeyboardButton("💬 Hablar conmigo")

    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)

    texto = (
        "🌸 *Bienvenido a mi espacio privado* 🌸\n\n"
        "Hola cariño 💋\n"
        "Soy *Yolen Valen* y me alegra mucho tenerte aquí.\n\n"
        "Este es mi espacio exclusivo donde comparto "
        "contenido especial que no publico en ningún otro lugar 🔥\n\n"
        "✨ Aquí podrás encontrar:\n"
        "🔑 Acceso a mi contenido VIP\n"
        "🎁 Promociones especiales\n"
        "💬 Comunicación directa conmigo\n\n"
        "Explora el menú y descubre todo lo que tengo preparado para ti 👇"
    )

    bot.send_message(message.chat.id, texto, parse_mode="Markdown", reply_markup=markup)

# BOTÓN VIP
@bot.message_handler(func=lambda message: message.text == "🔑 Suscripción VIP")
def vip(message):

    texto = (
        "🔑 *Acceso VIP Exclusivo*\n\n"
        "Si quieres ver mi contenido más atrevido y exclusivo "
        "este acceso es para ti 🔥\n\n"
        "Dentro del VIP encontrarás:\n"
        "✨ Fotos privadas\n"
        "✨ Videos exclusivos\n"
        "✨ Contenido que no comparto en redes\n\n"
        "💰 *Precio de acceso:* 170 Bs\n\n"
        "📲 Realiza el pago escaneando el QR que aparece abajo.\n\n"
        "Después del pago envía tu *captura del comprobante* "
        "por este chat para activar tu acceso."
    )

    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

    with open("qr_vip.jpg", "rb") as foto:
        bot.send_photo(message.chat.id, foto, caption="📲 Escanea este QR para realizar el pago")

# BOTÓN PROMOCIONES
@bot.message_handler(func=lambda message: message.text == "🎁 Promociones")
def promo(message):

    texto = (
        "🎁 *Promoción Especial*\n\n"
        "Si quieres empezar a conocer mi contenido "
        "tengo un paquete especial para ti 💋\n\n"
        "📸 *Paquete Básico*\n"
        "Incluye una selección de mis mejores fotos exclusivas.\n\n"
        "💰 *Precio promocional:* 70 Bs\n\n"
        "📲 Realiza el pago escaneando el QR que aparece abajo.\n\n"
        "Una vez realizado el pago envía tu comprobante "
        "para validar tu acceso."
    )

    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

    with open("qr_promo.jpg", "rb") as foto:
        bot.send_photo(message.chat.id, foto, caption="📲 Escanea este QR para realizar el pago")

# BOTÓN CONTACTO
@bot.message_handler(func=lambda message: message.text == "💬 Hablar conmigo")
def contacto(message):

    bot.send_message(
        message.chat.id,
        "💬 Puedes escribirme directamente aquí:\n\n"
        "https://t.me/TUUSUARIO\n\n"
        "Te responderé lo antes posible cariño 💋"
    )

# DETECTAR CAPTURAS DE PAGO
@bot.message_handler(content_types=['photo'])
def recibir_pago(message):

    usuario = message.from_user.first_name
    username = message.from_user.username

    bot.send_message(
        ADMIN_ID,
        f"💰 *Nuevo comprobante recibido*\n\n"
        f"Usuario: {usuario}\n"
        f"Username: @{username}",
        parse_mode="Markdown"
    )

    bot.forward_message(
        ADMIN_ID,
        message.chat.id,
        message.message_id
    )

    bot.send_message(
        message.chat.id,
        "✅ Hemos recibido tu comprobante.\n\n"
        "En breve verificaremos el pago y te enviaremos el acceso."
    )

print("Bot funcionando...")
bot.infinity_polling()