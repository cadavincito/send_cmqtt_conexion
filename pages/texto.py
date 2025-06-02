import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="broker.hivemq.com"
port=1883
client1= paho.Client("fincaSystem")
client1.on_message = on_message



st.title("Finca system control por texto")

controlTexto = st.text_input("Control por texto")
client1= paho.Client("fincaSystem")                           
client1.on_publish = on_publish                          
client1.connect(broker,port)  
message =json.dumps({"Act1":controlTexto})
ret= client1.publish("finca/puerta", message)


if st.button('Enviar Valor'):
    act1="controlTexto"
    client1= paho.Client("fincaSystem")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":controlTexto})
    ret= client1.publish("finca/puerta", message)


 
    #client1.subscribe("Sensores")
    

    
else:
    st.write('')





