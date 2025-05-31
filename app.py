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



st.title("MQTT Control")

if st.button('Abrir Puerta'):
    act1="abrir"
    client1= paho.Client("fincaSystem")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("finca/puerta", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('Cerrar Puerta'):
    act1="cerrar"
    client1= paho.Client("fincaSystem")                          
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("finca/puerta", message)

if st.button('Prender Luz Interna'):
    act1="luzInterna"
    client1= paho.Client("fincaSystem")                          
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("finca/puerta", message)

if st.button('Apagar Luz Interna'):
    act1="luzInternaOff"
    client1= paho.Client("fincaSystem")                          
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("finca/puerta", message)

if st.button('Prender Luz Externa'):
    act1="luzExterna"
    client1= paho.Client("fincaSystem")                          
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("finca/puerta", message)

if st.button('Apagar Luz Externa'):
    act1="luzExternaOff"
    client1= paho.Client("fincaSystem")                          
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("finca/puerta", message)
  
    
else:
    st.write('')

values = st.slider('Selecciona el rango de valores',0.0, 100.0)
st.write('Values:', values)

if st.button('Enviar valor analógico'):
    client1= paho.Client("GIT-HUB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Analog": float(values)})
    ret= client1.publish("cmqtt_a", message)
    
 
else:
    st.write('')




