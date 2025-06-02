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

st.title("Finca Control System")

# Lista de botones con sus comandos asociados
botones = [
    ("Abrir Puerta", "abrir"),
    ("Cerrar Puerta", "cerrar"),
    ("Prender Luz Interna", "luzInterna"),
    ("Apagar Luz Interna", "luzInternaOff"),
    ("Prender Luz Externa", "luzExterna"),
    ("Apagar Luz Externa", "luzExternaOff"),
    ("Prender Alarma Interna", "alarmaInterna"),
    ("Prender Alarma Externa", "alarmaExterna")
]

# Contenedor para el mensaje de confirmación
mensaje_confirmacion = st.empty()

# Organizar botones en pares paralelos
for i in range(0, len(botones), 2):  # Iterar de 2 en 2
    col1, col2 = st.columns(2)  # Crear dos columnas
    with col1:
        if st.button(botones[i][0], key=botones[i][1]):
            act1 = botones[i][1]
            message = json.dumps({"Act1": act1})
            ret = client1.publish("finca/puerta", message)
            mensaje_confirmacion.success(f"Comando enviado: **{act1}**")
    
    # Verificar si hay un segundo botón en el par
    if i + 1 < len(botones):
        with col2:
            if st.button(botones[i + 1][0], key=botones[i + 1][1]):
                act1 = botones[i + 1][1]
                message = json.dumps({"Act1": act1})
                ret = client1.publish("finca/puerta", message)
                mensaje_confirmacion.success(f"Comando enviado: **{act1}**")

# Opcional: Suscripción a un tópico (descomentar si es necesario)
# client1.subscribe("Sensores")
