import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):  # Callback para publicación
    print("El dato ha sido publicado\n")
    pass

def on_message(client, userdata, message):  # Callback para mensajes recibidos
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

# Configuración del cliente MQTT
broker = "broker.hivemq.com"
port = 1883
client1 = paho.Client("fincaSystem")
client1.on_message = on_message
client1.on_publish = on_publish
client1.connect(broker, port)

st.title("Finca System Control por Texto")

# Campo de texto para ingresar comandos
controlTexto = st.text_input("Control por texto", key="control_texto")

# Verificar si se ingresó un comando y mostrar mensaje de confirmación
if controlTexto:
    message = json.dumps({"Act1": controlTexto})
    ret = client1.publish("finca/puerta", message)
    st.success(f"Comando enviado: **{controlTexto}**")  # Mensaje de confirmación

st.header("Lista de Comandos")
st.write('Escriba el comando y presione "ENTER" para enviar')

# Lista de comandos con sus descripciones
comandos = [
    ("abrir", "Abre puerta"),
    ("cerrar", "Cierra la puerta"),
    ("luzInterna", "Prende luz interna"),
    ("luzInternaOff", "Apaga la luz interna"),
    ("luzExterna", "Prende luz Externa"),
    ("luzExternaOff", "Apaga la luz Externa"),
    ("alarmaInterna", "Enciende la alarma Interna"),
    ("alarmaExterna", "Enciende la alarma Externa")
]

# Mostrar cada comando como un elemento de lista
for comando, descripcion in comandos:
    st.write(f"**{comando}** -> {descripcion}")

# Opcional: Suscripción a un tópico (descomentar si es necesario)
# client1.subscribe("Sensores")
