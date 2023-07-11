import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "D8mFbOQnyE4dMncs0E4ZAjnf3Dtdq8zr"
consumo_combustible = 0.12  # Consumo estimado de combustible en litros por kilómetro

while True:
    orig = input("Inicio de Viaje: ")
    dest = input("Fin del Viaje: ")

    if orig.lower() == "s" or dest.lower() == "s":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    response = requests.get(url)
    data = response.json()

    if data["info"]["statuscode"] == 0:
        distancia = data["route"]["distance"]
        duracion = data["route"]["formattedTime"]

        duracion_horas, duracion_minutos, duracion_segundos = duracion.split(":")
        duracion_horas = int(duracion_horas)
        duracion_minutos = int(duracion_minutos)
        duracion_segundos = int(duracion_segundos)

        print(f"Distancia: {distancia:.1f} km")
        print(f"Duración del viaje: {duracion_horas:02d} horas, {duracion_minutos:02d} minutos, {duracion_segundos:02d} segundos")

        litros_necesarios = round(consumo_combustible * distancia, 2)
        print(f"Litros necesarios: {litros_necesarios} L")

        narrativa = f"Viaje desde {orig} hasta {dest}:\n"
        narrativa += f"- Distancia: {distancia:.2f} km\n"
        narrativa += f"- Duración del viaje: {duracion_horas:02d} horas, {duracion_minutos:02d} minutos, {duracion_segundos:02d} segundos\n"
        narrativa += f"- Litros necesarios: {litros_necesarios} L\n"

        with open("narrativa_viajes.txt", "a") as file:
            file.write(narrativa)

    else:
        print("No se pudo calcular la ruta. Por favor, intenta nuevamente.")
