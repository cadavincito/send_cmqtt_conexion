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
    .stButton > button {
        display: block;
        margin: 10px auto;
        background-color: #3b82f6; /* Azul vibrante para botones */
        color: #ffffff; /* Texto blanco en botones */
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s, transform 0.2s;
    }
    .stButton > button:hover {
        background-color: #2563eb; /* Azul más oscuro al pasar el ratón */
        transform: scale(1.05); /* Efecto de aumento */
    }
    .stTextInput > div > div > input {
        display: block;
        margin: 0 auto;
        background-color: #2a2a3a; /* Fondo oscuro para inputs */
        color: #ffffff; /* Texto blanco */
        border: 1px solid #4b4b5b;
        border-radius: 8px;
    }
    .stMarkdown, .stWrite, h1 {
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
    }

    .stImage > img {
        display: block;
        margin: 0 auto;
        border-radius: 10px; /* Bordes redondeados para la imagen */
        width: 300px; /* Limita el ancho de la imagen */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Sombra para un efecto moderno */
    }
    </style>
""", unsafe_allow_html=True)


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

st.image("finca.jpg", caption="Finca system", width=400px)

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
    col1, col2 = st.columns([1, 1], gap="small")  # Crear dos columnas con igual ancho
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
