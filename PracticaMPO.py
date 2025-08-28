
# ------------------------------------------------------------------------------------------------------------------
#  PREGUNTAS: Aqui hacemos una variable llamada cargar_preguntas y redactamos todas las preguntas que queremos hacer
# ------------------------------------------------------------------------------------------------------------------
def cargar_preguntas():
    return [
        {
            "pregunta": "¿Cuánto es 2 + 2?",
            "opciones": {"A": "3", "B": "4", "C": "5", "D": "6"},
            "respuesta_correcta": "B",
        },
        {
            "pregunta": "¿De qué color es el cielo en un día despejado?",
            "opciones": {"A": "Rojo", "B": "Azul", "C": "Verde", "D": "Amarillo"},
            "respuesta_correcta": "B",
        },
        {
            "pregunta": "¿Cuál es la inicial de la palabra Python?",
            "opciones": {"A": "P", "B": "Y", "C": "T", "D": "N"},
            "respuesta_correcta": "A",
        },
    ]


# -------------------------------------------------------------------------
#  Esta parte del codigo muestra la pregunta con sus 4 diferentes opciones.
# -------------------------------------------------------------------------
def mostrar_pregunta(p):
    print("\n" + p["pregunta"])
    for letra in ("A", "B", "C", "D"):
        print(f"  {letra}) {p['opciones'][letra]}")

# En el caso de que pongas una letra que no sea una de las 4 (A-D), envia el mensaje de error Opcion no valida.

def obtener_respuesta():
    while True:
        r = input("Tu respuesta (A/B/C/D): ").strip().upper()
        if r in {"A", "B", "C", "D"}:
            return r
        print("⚠️  Opción no válida. Escribe A, B, C o D.")


# ---------------------------------
#  Esta es la parte logica del test
# ---------------------------------

# Comprueba si la respuesta del usuario es correcta
def corregir_respuesta(respuesta, correcta):
    return respuesta == correcta

#Aqui iniciamos el contador de aciertos
def ejecutar_test(preguntas):
    aciertos = 0
    total = len(preguntas)
# Podemos ver como aqui recorre todas las preguntas y si la respuesta es correcta suma 1.
# Al final devuelve el numero de aciertos totales y el numero de preguntas.
    for p in preguntas:
        mostrar_pregunta(p)
        r = obtener_respuesta()
        if corregir_respuesta(r, p["respuesta_correcta"]):
            print("✅ ¡Correcta!")
            aciertos += 1
        else:
            correcta = p["respuesta_correcta"]
            print(f"❌ Incorrecta. La correcta era {correcta}) {p['opciones'][correcta]}")

    return aciertos, total

# con esta funcion calculamos el total de preguntas, el total de aciertos y el porcentaje de aciertos.
def mostrar_resultados(aciertos, total):
    porcentaje = round((aciertos / total) * 100, 2)
    print("\n### RESULTADOS ###")
    print(f"Total de preguntas: {total}")
    print(f"Aciertos: {aciertos}")
    print(f"Porcentaje: {porcentaje}%")
# Dependiendo del porcentaje de aciertos lanza un comentario distinto.
    if porcentaje == 100:
        valoracion = "¡Excelente!"
    elif porcentaje >= 60:
        valoracion = "¡Bien hecho!"
    else:
        valoracion = "Necesitas practicar."

    print("Valoración:", valoracion)


# ----------------------------
#  MENÚ PRINCIPAL: este es el menu basico para empezar el test
# ----------------------------
def menu():
    while True:
        print("\n### MENÚ ###")
        print("1 - Empezar cuestionario")
        print("2 - Salir")
# Da 3 opciones: empezar test, terminar test o en su defecto si no selecionas la opcion 1 o 2 da un mensaje de error.
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            preguntas = cargar_preguntas()
            aciertos, total = ejecutar_test(preguntas)
            mostrar_resultados(aciertos, total)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Prueba otra vez.")


if __name__ == "__main__":
    menu()
