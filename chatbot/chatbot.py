#diccionario de respuestas
import csv
respuestas = {
    "hola": "¡Hola! ¿En que puedo ayudarte?",
    "como estas": "Estoy bien, gracias por preguntar",
    "adiós": "¡Hasta luego! Que tengas un buen día"
}

#funcion para obtener la respuesta
def obtener_respuesta(mensaje):
    mensaje = mensaje.lower()
    if mensaje in respuestas:
        return respuestas[mensaje]
    else:
     with open("salida.csv", "a", newline="")as archivo:
       escritor = csv.writer(archivo)
       escritor.writerow([mensaje,"pregunta por responder"])
     return "lo siento, no entiendo esa pregunta"
    
#Bucle de conversación
print("¡Hola! Soy un chatbot, Escribe 'salir' para terminar la conversación.")
while True:
    usuario = input("Tú: ")
    if usuario.lower() == "salir":
        print("Chatbot: ¡Adiós!")
        break
    respuesta = obtener_respuesta(usuario)
    print("Chatbot:", respuesta)