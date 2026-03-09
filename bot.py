import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# -------------------------
# CONFIGURACIÓN
# -------------------------

TOKEN = "8752475374:AAF-_NOlXLVSM_ZxTzwSmWPkrN1bS5Ue6gU"
ADMIN_ID = 7945378542

QR_VIP = "qr_vip.jpg"
QR_PROMO = "qr_promo.jpg"

bot = telebot.TeleBot(TOKEN)

# -------------------------
# MENSAJE DE INICIO
# -------------------------

@bot.message_handler(commands=['start'])
def start(message):

    markup = InlineKeyboardMarkup()

    btn_vip = InlineKeyboardButton("🔥 Suscripción VIP", callback_data="vip")
    btn_promo = InlineKeyboardButton("💎 Promoción Especial", callback_data="promo")
    btn_soporte = InlineKeyboardButton("💬 Soporte", url="https://t.me/TU_USUARIO")

    markup.row(btn_vip)
    markup.row(btn_promo)
    markup.row(btn_soporte)

    texto = (
        "💋 *Bienvenido al contenido exclusivo de Yolen Valen* 💋\n\n"
        "Aquí encontrarás material privado que no se publica en redes.\n\n"
        "✨ Fotos exclusivas\n"
        "🔥 Videos privados\n"
        "💎 Contenido VIP\n\n"
        "Selecciona una opción para continuar."
    )

    bot.send_message(message.chat.id, texto, parse_mode="Markdown", reply_markup=markup)

# -------------------------
# BOTONES
# -------------------------

@bot.callback_query_handler(func=lambda call: True)
def botones(call):

    usuario = call.from_user.first_name
    username = f"@{call.from_user.username}" if call.from_user.username else ""
    user_id = call.from_user.id

# ---------- VIP ----------

    if call.data == "vip":

        bot.send_message(
            ADMIN_ID,
            f"🔥 Cliente interesado en VIP\n\n"
            f"Usuario: {usuario} {username}\n"
            f"ID: {user_id}"
        )

        texto = (
            "🔥 *SUSCRIPCIÓN VIP* 🔥\n\n"
            "Accede al contenido más exclusivo de *Yolen Valen*.\n\n"
            "Incluye:\n"
            "💋 Fotos privadas\n"
            "🔥 Videos sin censura\n"
            "💎 Contenido exclusivo VIP\n\n"
            "💰 *Precio:* 170 Bs\n\n"
            "Realiza el pago escaneando el QR de abajo.\n"
            "Luego envía tu captura de pago aquí para activar tu acceso."
        )

        bot.send_message(call.message.chat.id, texto, parse_mode="Markdown")

        try:
            with open(QR_VIP, "rb") as qr:
                bot.send_photo(
                    call.message.chat.id,
                    qr,
                    caption="📲 Escanea este QR para pagar la suscripción VIP"
                )
        except:
            bot.send_message(call.message.chat.id, "⚠️ No se encontró el QR VIP.")

# ---------- PROMOCIÓN ----------

    if call.data == "promo":

        bot.send_message(
            ADMIN_ID,
            f"💎 Cliente interesado en promoción\n\n"
            f"Usuario: {usuario} {username}\n"
            f"ID: {user_id}"
        )

        texto = (
            "💎 *PROMOCIÓN ESPECIAL* 💎\n\n"
            "Accede hoy al contenido exclusivo de *Yolen Valen* con precio promocional.\n\n"
            "Incluye:\n"
            "📸 Fotos privadas\n"
            "🎥 Videos exclusivos\n\n"
            "💰 *Precio especial:* 70 Bs\n\n"
            "Escanea el QR para realizar el pago.\n"
            "Luego envía tu comprobante aquí."
        )

        bot.send_message(call.message.chat.id, texto, parse_mode="Markdown")

        try:
            with open(QR_PROMO, "rb") as qr:
                bot.send_photo(
                    call.message.chat.id,
                    qr,
                    caption="📲 Escanea este QR para pagar la promoción"
                )
        except:
            bot.send_message(call.message.chat.id, "⚠️ No se encontró el QR de promoción.")

# -------------------------
# CAPTURAS DE PAGO
# -------------------------

@bot.message_handler(content_types=['photo'])
def recibir_pago(message):

    usuario = message.from_user.first_name
    username = f"@{message.from_user.username}" if message.from_user.username else ""

    bot.forward_message(
        ADMIN_ID,
        message.chat.id,
        message.message_id
    )

    bot.send_message(
        ADMIN_ID,
        f"💰 *Nuevo comprobante recibido*\n\n"
        f"👤 Usuario: {usuario} {username}\n"
        f"🆔 ID: {message.from_user.id}",
        parse_mode="Markdown"
    )

    bot.reply_to(
        message,
        "💋 Gracias por enviar tu comprobante.\n\n"
        "⏳ Estamos verificando tu pago.\n"
        "En unos minutos recibirás tu acceso exclusivo."
    )

# -------------------------
# MENSAJES DE TEXTO
# -------------------------

@bot.message_handler(content_types=['text'])
def recibir_texto(message):

    if message.text.startswith("/"):
        return

    usuario = message.from_user.first_name
    username = f"@{message.from_user.username}" if message.from_user.username else ""

    bot.send_message(
        ADMIN_ID,
        f"💬 *Nuevo mensaje recibido en el bot*\n\n"
        f"👤 Usuario: {usuario} {username}\n"
        f"📝 Mensaje:\n{message.text}",
        parse_mode="Markdown"
    )

# -------------------------
# INICIAR BOT
# -------------------------

print("Bot iniciado correctamente...")

bot.infinity_polling()