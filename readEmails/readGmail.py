
import imaplib
import email

username = 'clautester2023@gmail.com'
password = 'xpoa zzqv peyj qnxr'

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)
mail.select("inbox")  # Conéctate a la bandeja de entrada.

# Buscar los IDs de los últimos dos correos electrónicos
result, data = mail.search(None, "ALL")
ids = data[0].split()  # Los datos son una lista de IDs separados por espacios
latest_email_id = ids[-1]  # Obtener el último ID

# Leer el cuerpo del correo electrónico más reciente
result, data = mail.fetch(latest_email_id, "(RFC822)")
raw_email = data[0][1]  # Obtener el cuerpo del correo electrónico en texto sin formato

# Analizar el mensaje de correo electrónico y extraer el cuerpo
msg = email.message_from_bytes(raw_email)
if msg.is_multipart():
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True).decode()
            print(body)
else:
    body = msg.get_payload(decode=True).decode()
    print(body)

mail.close()
mail.logout()