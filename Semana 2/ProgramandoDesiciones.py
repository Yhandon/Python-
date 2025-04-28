print("ENFRETARSE A UN VILLANO FUERTE")

print("Simulando la decisión del superhéroe...")

# Preguntamos al usuario si el héroe está solo
respuesta_esta_solo = input("¿Está el héroe solo? (si/no): ").lower()
esta_solo = respuesta_esta_solo == "si"

# Preguntamos al usuario si el villano es más fuerte
respuesta_villano_fuerte = input("¿Es el villano más fuerte que el héroe? (si/no): ").lower()
villano_fuerte = respuesta_villano_fuerte == "si"

# Preguntamos al usuario por el nivel de confianza del héroe
nivel_confianza = input("¿Cuál es el nivel de confianza del héroe? (alto/bajo): ").lower()

if esta_solo and villano_fuerte:
    print("\n¡Alerta! Un villano fuerte aparece y el superhéroe está solo.")
    if nivel_confianza == "alto":
        print("El superhéroe se siente confiado y decide enfrentar al villano...")
        # Aquí podríamos simular una batalla con resultados aleatorios o basados en más inputs
        resultado_batalla = input("¿Cómo terminó la batalla? (victoria/derrota): ").lower()
        if resultado_batalla == "victoria":
            print("¡Victoria! El superhéroe ha derrotado al villano.")
        elif resultado_batalla == "derrota":
            print("¡Derrota! El villano ha superado al superhéroe.")
        else:
            print("Resultado de batalla no reconocido.")
    elif nivel_confianza == "bajo":
        print("El superhéroe no se siente seguro y solicita refuerzos...")
        llega_refuerzo = input("¿Llegan los refuerzos? (si/no): ").lower()
        if llega_refuerzo == "si":
            print("¡Llegan los refuerzos! El apoyo ayudará en la misión.")
        else:
            print("Los refuerzos no pudieron llegar a tiempo. El héroe debe reconsiderar su estrategia.")
    else:
        print("Nivel de confianza no reconocido. El superhéroe duda, perdiendo tiempo valioso.")
else:
    print("\n.")
    if not esta_solo:
        print("El héroe no está solo y puede coordinar acciones con su equipo.")
    if not villano_fuerte:
        decision_alternativa = input("El villano no es tan fuerte. ¿Qué decide hacer el héroe? (enfrentar/retirar): ").lower()
        if decision_alternativa == "enfrentar":
            print("El superhéroe enfrenta al villano y (Victoria)")
        elif decision_alternativa == "retirar":
            print("El superhéroe se retira para evaluar la situación, con el riesgo de dejar la ciudad vulnerable.(Derrota)")
        else:
            print("Decisión no reconocida.")