from turtle import *
import pandas as pd
import networkx as nx
from typing import Dict
import time

# ----------------------------------------------------------------------------------------------------------------------
# Creamos un diccionario con el nombre de las estaciones y sus respectivas coordenadas en la pantalla.
# ----------------------------------------------------------------------------------------------------------------------

Estaciones: Dict[str, tuple] = {
    'Faliro': (-373, -165),
    'Moschato': (-315, -117),
    'Kalithea': (-252, -109),
    'Tavros': (-228, -80),
    'Petralona': (-208, -62),
    'Thisio': (-175, -28),
    'Monastiraki': (-145, -19),
    'Victoria': (-122, 54),
    'Aghios Nikolaos': (-145, 122),
    'Kato Patissia': (-145, 150),
    'Aghios Eleftherios' : (-120, 189),
    'Ano Patissia': (-97, 207),
    'Perissos': (-65, 239),
    'Pefkakia': (-46, 259),
    'Nea Ionia': (-23, 282),
    'Iraklio': (20, 284),
    'Irini': (80, 286),
    'Neratziotissa': (113, 308),
    'Maroussi': (155, 350),
    'KAT': (158, 390),
    'Kifissia': (182, 432),
    'Anthoupoli': (-275, 165),
    'Peristeri': (-250, 140),
    'Aghios Antonios': (-220, 110),
    'Sepolia': (-175, 95),
    'Attiki': (-145, 85),
    'Larissa Station': (-150, 55),
    'Metaxourghio': (-150, 24),
    'Omonia': (-125, 13),
    'Panepistimio': (-105, -3),
    'Syntagma': (-110, -25),
    'Akropoli': (-120, -60),
    'Syngrou/Fix': (-143, -80),
    'Neos Kosmos': (-143, -105),
    'Aghios Ioannis': (-117, -120),
    'Dafni': (-95, -140),
    'Aghios Dimitrios/Alexandros Panagoulis': (-90, -180),
    'Ilioupoli': (-77, -250),
    'Alimos': (-78, -308),
    'Argyroupoli': (-78, -365),
    'Elliniko': (-45, -415),
    'Dimotiko Theatro': (-435, -180),
    'Piraeus': (-443, -150),
    'Maniatika': (-443, -95),
    'Nikea': (-420, -65),
    'Korydallos': (-400, -30),
    'Aghia Varvara': (-385, 5),
    'Agia Marina': (-350, 40),
    'Egaleo': (-305, 45),
    'Eleonas': (-260, 45),
    'Kerameikos': (-185, -5),
    'Evangelismos': (-56, -25),
    'Megaro Moussikis': (-30, -2),
    'Ambelokipi': (-21, 19),
    'Panormou': (-3, 50),
    'Katehaki': (50, 50),
    'Ethniki Amyna': (84, 81),
    'Holargos': (127, 105),
    'Nomismatokopio': (177, 139),
    'Aghia Paraskevi': (210, 172),
    'Halandri': (246, 196),
    'Douk Plakentias': (280, 196),
    'Pallini': (348, 42),
    'Peania-Kantza': (350, -73),
    'Koropi' : (350, -220),
    'Aeropuerto Internacional de Atenas': (473, -293)
}

# ----------------------------------------------------------------------------------------------------------------------
# Añadimos la imagen del mapa en el fondo de la pantalla.
# ----------------------------------------------------------------------------------------------------------------------

tr = Turtle()
wn = Screen()
# wn.addshape('MetroAtenas.gif')
wn.addshape("./MetroAtenas.gif")
tr.shape('./MetroAtenas.gif')

# ----------------------------------------------------------------------------------------------------------------------
# Establecemos las dimensiones de la pantalla y del puntero, y el título de la pantalla.
# ----------------------------------------------------------------------------------------------------------------------

screenTk = wn.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
wn.setup(width=1.0, height=1.0)
turtlesize(stretch_wid=2, stretch_len=2, outline=2)
title("METRO DE ATENAS")
hideturtle()

# ----------------------------------------------------------------------------------------------------------------------
# Creamos cajas input para obtener la estación de origen y destino deseadas, junto con otras dos cajas input que se
# activarán en caso de que las estaciones introducidas no sean válidas.
# ----------------------------------------------------------------------------------------------------------------------

origen = textinput("ESTACIÓN", "ORIGEN")
while origen not in Estaciones:
    origen = textinput("ESTACIÓN", "INTRODUZCA UN ORIGEN VÁLIDO")
destino = textinput("ESTACIÓN", "DESTINO")
while destino not in Estaciones:
    destino = textinput("ESTACIÓN", "INTRODUZCA UN DESTINO VÁLIDO")

# ----------------------------------------------------------------------------------------------------------------------
# Definimos el color y tamaño del trazado.
# ----------------------------------------------------------------------------------------------------------------------

color("orange")
pensize(8)
penup()

# ----------------------------------------------------------------------------------------------------------------------
# Aplicamos el algoritmo A*.
# ----------------------------------------------------------------------------------------------------------------------

df = pd.read_excel("./metro_Atenas.xlsx")
# df = pd.read_excel('metro_Atenas.xlsx')
METRO = nx.from_pandas_edgelist(df, source='Origen', target='Destino', edge_attr='Distancia')
METRO.nodes()
METRO.edges()
METRO.order()
astar_path = nx.astar_path(METRO, source=origen, target=destino, weight='Distancia')

astar_path_long = nx.astar_path_length(METRO, source=origen, target=destino, weight='Distancia')

# ----------------------------------------------------------------------------------------------------------------------
# Calculamos las líneas de metro.
# ----------------------------------------------------------------------------------------------------------------------

linea1 = ['Piraeus', 'Faliro', 'Moschato', 'Kalithea', 'Tavros', 'Petralona', 'Thisio', 'Monastiraki', 'Omonia',
          'Victoria', 'Attiki', 'Aghios Nikolaos', 'Kato Patissia', 'Aghios Eleftherios', 'Ano Patissia', 'Perissos',
          'Pefkakia', 'Nea Ionia', 'Iraklio', 'Irini', 'Neratziotissa', 'Maroussi', 'KAT', 'Kifissia']

linea2 = ['Anthoupoli', 'Peristeri', 'Aghios Antonios', 'Sepolia', 'Attiki', 'Larissa Station', 'Metaxourghio', 'Omonia',
          'Panepistimio', 'Syntagma', 'Akropoli', 'Syngrou/Fix', 'Neos Kosmos', 'Aghios Ioannis', 'Dafni',
          'Aghios Dimitrios/Alexandros Panagoulis', 'Ilioupoli', 'Alimos', 'Argyroupoli',
          'Elliniko']

linea3 = ['Dimotiko Theatro', 'Piraeus', 'Maniatika', 'Nikea', 'Korydallos', 'Aghia Varvara', 'Agia Marina', 'Egaleo',
          'Eleonas', 'Kerameikos', 'Monastiraki', 'Syntagma', 'Evangelismos', 'Megaro Moussikis', 'Ambelokipi',
          'Panormou', 'Katehaki', 'Ethniki Amyna', 'Holargos', 'Nomismatokopio', 'Aghia Paraskevi', 'Halandri',
          'Douk Plakentias', 'Pallini', 'Peania-Kantza', 'Koropi', 'Aeropuerto Internacional de Atenas']

# ----------------------------------------------------------------------------------------------------------------------
# Calculamos el número de transbordos.
# ----------------------------------------------------------------------------------------------------------------------

transbordo = 0

for estacion in range(1, len(astar_path)-1):
     if METRO.degree(astar_path[estacion]) > 2:
         if not ((astar_path[estacion-1] in linea1 and astar_path[estacion+1] in linea1 and astar_path[estacion] in
                  linea1) or (astar_path[estacion-1] in linea2 and astar_path[estacion+1] in linea2 and
                              astar_path[estacion] in linea2) or (astar_path[estacion-1] in linea3 and
                                                                  astar_path[estacion+1] in linea3 and
                                                                  astar_path[estacion] in linea3)):
            transbordo += 1

# ----------------------------------------------------------------------------------------------------------------------
# Calculamos el tiempo del trayecto.
# ----------------------------------------------------------------------------------------------------------------------

vel_speed = 80
vel_speed_mod = (80*1000)/3600
tiempo_transbordo = 7.5
bias = len(astar_path)*40

segundos = round((round(astar_path_long, 2)/vel_speed_mod) + bias)
if segundos > 60:
    minutos = segundos / 60
    segundos = round(segundos % 60)
else:
    minutos = 0

minutos = round(minutos % 60 + tiempo_transbordo*transbordo)
if minutos > 60:
    horas = round(minutos/60)
    minutos = round(minutos % 60)
else:
    horas = 0

# ----------------------------------------------------------------------------------------------------------------------
# Imprimimos los datos por la pantalla.
# ----------------------------------------------------------------------------------------------------------------------

distancia = 'Distancia total: ' + str(round(astar_path_long, 2)) + ' metros.'

nParadas = 'Número de paradas: ' + str(len(astar_path))

nTransbordos = 'Número de transbordos: ' + str(transbordo)

if horas > 0:
    Tiempo_Trayecto = f"Tiempo aproximado: {horas} hora, {minutos} minuto(s) y {segundos} segundo(s)."
elif horas == 0 and astar_path_long > 0:
    Tiempo_Trayecto = f"Tiempo aproximado: {minutos} minuto(s) y {segundos} segundo(s)."
else:
    Tiempo_Trayecto = f"Tiempo aproximado: 0 segundos."

# ----------------------------------------------------------------------------------------------------------------------
# Creamos la lista, con el camino y sus respectivas coordenadas.
# ----------------------------------------------------------------------------------------------------------------------

lista_coordenadas = []
for elem in astar_path:
    lista_coordenadas.append(Estaciones[elem])

# ----------------------------------------------------------------------------------------------------------------------
# Dibujamos el trazado entre los puntos de la ruta seleccionada.
# ----------------------------------------------------------------------------------------------------------------------

setposition(lista_coordenadas[0][0], lista_coordenadas[0][1])
dot(20, 'orange')
speed(1)
showturtle()
pendown()
for estacion in lista_coordenadas:
    seth(towards(estacion[0], estacion[1]))
    setposition(estacion[0], estacion[1])
dot(20, 'orange')

# ----------------------------------------------------------------------------------------------------------------------
# Escribimos en pantalla información extra acerca del trayecto.
# ----------------------------------------------------------------------------------------------------------------------

hideturtle()
penup()
speed(8)
color("black")
setposition(-595, 315)
time.sleep(1)
write(distancia, move=False, align='left', font=('Arial', 13, 'normal'))
setposition(-595, 285)
time.sleep(1)
write(nParadas, move=False, align='left', font=('Arial', 13, 'normal'))
setposition(-595, 255)
time.sleep(1)
write(nTransbordos, move=False, align='left', font=('Arial', 13, 'normal'))
setposition(-595, 225)
time.sleep(1)
write(Tiempo_Trayecto, move=False, align='left', font=('Arial', 13, 'normal'))

# ----------------------------------------------------------------------------------------------------------------------
# Mantenemos la ventana abierta hasta que pulsemos el ratón.
# ----------------------------------------------------------------------------------------------------------------------
exitonclick()
