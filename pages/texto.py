import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Inyectar CSS para dark mode y centrar elementos
st.markdown("""
    <style>
    .stApp {
        background-color: #1e1e2e; /* Fondo oscuro */
        color: #ffffff; /* Texto blanco */
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .stTextInput > div > div > input {
        display: block;
        margin: 0 auto;
        background-color: #2a2a3a; /* Fondo oscuro para input */
        color: #ffffff; /* Texto blanco */
        border: 1px solid #4b4b5b;
        border-radius: 8px;
        padding: 10px;
        width: 300px; /* Ancho fijo para el input */
    }
    .stMarkdown, .stWrite, h1, h2 {
        color: #ffffff; /* Texto blanco */
        text-align: center;
    }
    .stSuccess {
        background-color: #166534; /* Fondo verde oscuro para mensajes de éxito */
        color: #ffffff; /* Texto blanco */
        border-radius: 8px;
        padding: 10px;
        margin: 10px auto;
        text-align: center;
        max-width: 400px; /* Ancho máximo para el mensaje */
    }
    .stMarkdown > div > p {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

# Muestra la versión de Python
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
    ("luzExterna", "Prende luz Ex
