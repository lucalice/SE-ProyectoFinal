"""
** Autor: Carranza Escobar Luis Enrique
**
"""

from gpiozero import DistanceSensor

def sensor(echo=18, trigger=17):
    sensor = DistanceSensor(echo, trigger)
    dist = sensor.distance * 100
    if(dist <= 40):
        return "Hay un objeto muy cerca de tu planta. Ten cuidado!!!"