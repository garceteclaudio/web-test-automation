import imaplib
import email

# Configurar las credenciales de acceso
username = 'mail@hotmail.com'
password = 'password'

# Conectar al servidor IMAP de Outlook.com
mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')

# Iniciar sesión en la cuenta
mail.login(username, password)

# Seleccionar la bandeja de entrada
mail.select('inbox')

# Buscar los IDs de los últimos correos electrónicos
result, data = mail.search(None, 'ALL')
latest_email_ids = data[0].split()

# Leer el último correo electrónico
latest_email_id = latest_email_ids[-1]  # Obtener el ID del último correo electrónico

result, data = mail.fetch(latest_email_id, '(RFC822)')
raw_email = data[0][1]  # Obtener el cuerpo del correo electrónico en texto sin formato
msg = email.message_from_bytes(raw_email)  # Analizar el mensaje de correo electrónico

# Mostrar el remitente, asunto y cuerpo del correo electrónico
print('From:', msg['From'])
print('Subject:', msg['Subject'])

# Verificar si hay una carga útil antes de intentar decodificarla
if msg.is_multipart():
    for part in msg.walk():
        content_type = part.get_content_type()
        if content_type == 'text/plain':
            payload = part.get_payload(decode=True)
            if isinstance(payload, bytes):
                print(payload.decode())  # Decodificar y mostrar el cuerpo del correo electrónico
            else:
                print(payload)
        elif content_type.startswith('image/') or content_type.startswith('application/'):
            filename = part.get_filename()
            print(f'Adjunto: {filename}')
else:
    print('No hay contenido de texto plano en este correo electrónico')

# Cerrar la conexión
mail.logout()