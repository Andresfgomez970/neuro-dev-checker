import json
import os


# Crear un solo JSON con todos los bloques ya completados
asconi_full = {
    "edad_0_3": {
        "hitos": [
            {"área": "Motor grueso", "descripcion": "Gira la cabeza a los lados en prono."},
            {"área": "Motor fino", "descripcion": "Reflejo de prensión palmar presente."},
            {"área": "Alimentación", "descripcion": "Succión adecuada. Deglución sin dificultad."},
            {"área": "Lenguaje expresivo", "descripcion": "Llanto diferencial."},
            {"área": "Lenguaje comprensivo", "descripcion": "Reacciona a sonidos."},
            {"área": "Social - Cognitivo", "descripcion": "Reconoce la voz del cuidador. Sonríe dormido."}
        ],
        "banderas": [
            {"área": "Motor grueso", "descripcion": "No gira la cabeza lateralmente en prono."},
            {"área": "Motor fino", "descripcion": "Manos siempre cerradas. Pulgar incluido."},
            {"área": "Alimentación", "descripcion": "Dificultades de succión o deglución."},
            {"área": "Lenguaje expresivo", "descripcion": "Ausencia de llanto diferencial."},
            {"área": "Lenguaje comprensivo", "descripcion": "No reacciona a sonidos."},
            {"área": "Social - Cognitivo", "descripcion": "No sonríe ni fija la mirada."}
        ]
    },
    "edad_4_6": {
        "hitos": [
            {"área": "Motor grueso", "descripcion": "Se apoya sobre antebrazos en prono. Sedente con apoyo."},
            {"área": "Motor fino", "descripcion": "Pasa objetos de una mano a otra. Agarre simétrico."},
            {"área": "Alimentación", "descripcion": "Inicia alimentación complementaria."},
            {"área": "Lenguaje expresivo", "descripcion": "Balbucea. Sílabas aisladas."},
            {"área": "Lenguaje comprensivo", "descripcion": "Dirige la mirada al sonido."},
            {"área": "Social - Cognitivo", "descripcion": "Ríe a carcajadas. Reconoce personas."}
        ],
        "banderas": [
            {"área": "Motor grueso", "descripcion": "No sostiene la cabeza. No se voltea."},
            {"área": "Motor fino", "descripcion": "No toma objetos ni los traslada de mano."},
            {"área": "Alimentación", "descripcion": "No inicia alimentación blanda. Rechazo oral."},
            {"área": "Lenguaje expresivo", "descripcion": "No balbucea."},
            {"área": "Lenguaje comprensivo", "descripcion": "No busca el origen de sonidos."},
            {"área": "Social - Cognitivo", "descripcion": "No reconoce al cuidador principal."}
        ]
    },
    "edad_7_9": {
        "hitos": [
            {"área": "Motor grueso", "descripcion": "Sedente sin apoyo. Gateo inicial. Se mantiene de pie con ayuda."},
            {"área": "Motor fino", "descripcion": "Pinza lateral con pulgar e índice. Sostiene biberón."},
            {"área": "Alimentación", "descripcion": "Come galletas sólidas. Usa manos para llevar comida a la boca."},
            {"área": "Lenguaje expresivo", "descripcion": "Sílabas redobladas como 'mamama' y 'papapa'."},
            {"área": "Lenguaje comprensivo", "descripcion": "Responde al nombre. Comprende gestos simples."},
            {"área": "Social - Cognitivo", "descripcion": "Busca objetos escondidos. Juega a esconderse."}
        ],
        "banderas": [
            {"área": "Motor grueso", "descripcion": "No se sienta sin apoyo. No intenta gatear."},
            {"área": "Motor fino", "descripcion": "No transfiere objetos entre manos. No hace pinza."},
            {"área": "Alimentación", "descripcion": "No lleva comida a la boca. Dificultades con alimentos sólidos."},
            {"área": "Lenguaje expresivo", "descripcion": "No balbucea. No emite sílabas duplicadas."},
            {"área": "Lenguaje comprensivo", "descripcion": "No responde al nombre. No mira a lo que se señala."},
            {"área": "Social - Cognitivo", "descripcion": "No muestra interés por juegos sociales."}
        ]
    },
    "edad_10_12": {
        "hitos": [
            {"área": "Motor grueso", "descripcion": "Camina con apoyo. Se pone de pie solo."},
            {"área": "Motor fino", "descripcion": "Pinza fina completa. Mete objetos en recipientes."},
            {"área": "Alimentación", "descripcion": "Come alimentos blandos con las manos. Usa vaso con ayuda."},
            {"área": "Lenguaje expresivo", "descripcion": "Dice palabras como mamá o papá con significado."},
            {"área": "Lenguaje comprensivo", "descripcion": "Obedece órdenes sencillas. Señala objetos conocidos."},
            {"área": "Social - Cognitivo", "descripcion": "Imita gestos y sonidos. Muestra interés por otros niños."}
        ],
        "banderas": [
            {"área": "Motor grueso", "descripcion": "No se pone de pie con apoyo. No camina con ayuda."},
            {"área": "Motor fino", "descripcion": "No hace pinza fina. No mete objetos en recipientes."},
            {"área": "Alimentación", "descripcion": "No mastica ni traga alimentos blandos."},
            {"área": "Lenguaje expresivo", "descripcion": "No dice ninguna palabra con significado."},
            {"área": "Lenguaje comprensivo", "descripcion": "No obedece órdenes sencillas. No señala objetos."},
            {"área": "Social - Cognitivo", "descripcion": "No imita gestos. No interactúa con otros niños."}
        ]
    },
    "edad_13_18": {
        "hitos": [
            {"área": "Motor grueso", "descripcion": "Camina solo. Sube escaleras gateando."},
            {"área": "Motor fino", "descripcion": "Hace torres con dos cubos. Garabatea."},
            {"área": "Alimentación", "descripcion": "Usa cuchara con ayuda. Come con menos derrames."},
            {"área": "Lenguaje expresivo", "descripcion": "Usa de 5 a 10 palabras."},
            {"área": "Lenguaje comprensivo", "descripcion": "Identifica partes del cuerpo. Sigue órdenes simples."},
            {"área": "Social - Cognitivo", "descripcion": "Señala lo que quiere. Juega imitando."}
        ],
        "banderas": [
            {"área": "Motor grueso", "descripcion": "No camina solo. No gatea escaleras."},
            {"área": "Motor fino", "descripcion": "No apila bloques. No sostiene lápiz o crayón."},
            {"área": "Alimentación", "descripcion": "No sostiene utensilios. No lleva alimentos a la boca."},
            {"área": "Lenguaje expresivo", "descripcion": "No usa palabras. Solo balbucea."},
            {"área": "Lenguaje comprensivo", "descripcion": "No sigue instrucciones. No reconoce partes del cuerpo."},
            {"área": "Social - Cognitivo", "descripcion": "No señala ni hace juego simbólico."}
        ]
    },
    "edad_19_24": {
        "hitos": [
            {"área": "Motor grueso", "descripcion": "Corre con dificultad. Sube y baja escaleras con apoyo."},
            {"área": "Motor fino", "descripcion": "Hace torre de 4 cubos. Pasa páginas de un libro."},
            {"área": "Alimentación", "descripcion": "Come solo con cuchara. Bebe en vaso sin ayuda."},
            {"área": "Lenguaje expresivo", "descripcion": "Dice frases de 2 palabras. Vocabulario de 20-50 palabras."},
            {"área": "Lenguaje comprensivo", "descripcion": "Reconoce objetos por nombre. Sigue instrucciones simples."},
            {"área": "Social - Cognitivo", "descripcion": "Imita acciones cotidianas. Juega al lado de otros niños."}
        ],
        "banderas": [
            {"área": "Motor grueso", "descripcion": "No camina de forma estable. No sube escaleras con ayuda."},
            {"área": "Motor fino", "descripcion": "No construye torre de 2 cubos. No pasa páginas."},
            {"área": "Alimentación", "descripcion": "No come solo. Dificultad para usar utensilios."},
            {"área": "Lenguaje expresivo", "descripcion": "No combina dos palabras. Vocabulario muy limitado."},
            {"área": "Lenguaje comprensivo", "descripcion": "No reconoce objetos ni sigue instrucciones."},
            {"área": "Social - Cognitivo", "descripcion": "No muestra juego simbólico. No se interesa por otros niños."}
        ]
    },
        "edad_25_30": {
        "hitos": [
            {"área": "Motor grueso", "descripcion": "Salta en el lugar. Sube y baja escaleras solo."},
            {"área": "Motor fino", "descripcion": "Hace torre de 6 cubos. Comienza trazos verticales."},
            {"área": "Alimentación", "descripcion": "Usa cuchara y vaso sin derrames."},
            {"área": "Lenguaje expresivo", "descripcion": "Forma frases de 3 palabras. Usa pronombres."},
            {"área": "Lenguaje comprensivo", "descripcion": "Sigue instrucciones complejas. Entiende acciones."},
            {"área": "Social - Cognitivo", "descripcion": "Juego simbólico. Nombra objetos en libros."}
        ],
        "banderas": [
            {"área": "Motor grueso", "descripcion": "No sube escaleras solo. No salta."},
            {"área": "Motor fino", "descripcion": "No apila 3 cubos. No dibuja líneas."},
            {"área": "Alimentación", "descripcion": "Derrames frecuentes al comer o beber."},
            {"área": "Lenguaje expresivo", "descripcion": "No forma frases. Vocabulario muy limitado."},
            {"área": "Lenguaje comprensivo", "descripcion": "No sigue instrucciones dobles."},
            {"área": "Social - Cognitivo", "descripcion": "No imita tareas del entorno. No nombra objetos conocidos."}
        ]
    },
    "edad_31_36": {
        "hitos": [
            {"área": "Motor grueso", "descripcion": "Corre con agilidad. Se mantiene en un solo pie por 1 segundo."},
            {"área": "Motor fino", "descripcion": "Hace torre de 8 cubos. Copia un círculo."},
            {"área": "Alimentación", "descripcion": "Se alimenta solo completamente."},
            {"área": "Lenguaje expresivo", "descripcion": "Hace preguntas. Usa tiempos verbales."},
            {"área": "Lenguaje comprensivo", "descripcion": "Comprende conceptos espaciales como dentro/fuera."},
            {"área": "Social - Cognitivo", "descripcion": "Juego cooperativo simple. Se reconoce por nombre y edad."}
        ],
        "banderas": [
            {"área": "Motor grueso", "descripcion": "No corre. No se sostiene en un pie."},
            {"área": "Motor fino", "descripcion": "No dibuja formas. No usa crayones correctamente."},
            {"área": "Alimentación", "descripcion": "Dificultad para comer solo."},
            {"área": "Lenguaje expresivo", "descripcion": "No hace frases de más de 2 palabras."},
            {"área": "Lenguaje comprensivo", "descripcion": "No identifica conceptos espaciales."},
            {"área": "Social - Cognitivo", "descripcion": "No participa en juegos con otros niños."}
        ]
    },
    "edad_3_4_anios": {
        "hitos": [
            {"área": "Motor grueso", "descripcion": "Sube escaleras alternando pies. Pedalea triciclo."},
            {"área": "Motor fino", "descripcion": "Copia figuras básicas. Usa tijeras con ayuda."},
            {"área": "Alimentación", "descripcion": "Se alimenta y limpia solo tras comer."},
            {"área": "Lenguaje expresivo", "descripcion": "Habla en oraciones. Usa plurales y pronombres correctamente."},
            {"área": "Lenguaje comprensivo", "descripcion": "Entiende preguntas complejas y secuencias."},
            {"área": "Social - Cognitivo", "descripcion": "Juega con roles. Comparte con pares."}
        ],
        "banderas": [
            {"área": "Motor grueso", "descripcion": "No sube escaleras alternando pies. No mantiene equilibrio en movimiento."},
            {"área": "Motor fino", "descripcion": "No copia líneas. No maneja tijeras."},
            {"área": "Alimentación", "descripcion": "Requiere ayuda para comer y limpiarse."},
            {"área": "Lenguaje expresivo", "descripcion": "No habla en oraciones."},
            {"área": "Lenguaje comprensivo", "descripcion": "No responde a preguntas con lógica."},
            {"área": "Social - Cognitivo", "descripcion": "No juega con otros niños ni sigue reglas simples."}
        ]
    },
    "edad_4_6_anios": {
        "hitos": [
            {"área": "Motor grueso", "descripcion": "Salta en un pie. Corre y se detiene con facilidad."},
            {"área": "Motor fino", "descripcion": "Copia letras. Dibuja personas con cuerpo."},
            {"área": "Alimentación", "descripcion": "Independencia total para comer y usar utensilios."},
            {"área": "Lenguaje expresivo", "descripcion": "Cuenta historias. Usa tiempos verbales con corrección."},
            {"área": "Lenguaje comprensivo", "descripcion": "Comprende explicaciones y responde adecuadamente."},
            {"área": "Social - Cognitivo", "descripcion": "Juego cooperativo complejo. Entiende normas sociales."}
        ],
        "banderas": [
            {"área": "Motor grueso", "descripcion": "No salta con un pie. Torpeza al correr o girar."},
            {"área": "Motor fino", "descripcion": "No dibuja formas o figuras humanas."},
            {"área": "Alimentación", "descripcion": "No maneja cubiertos o requiere ayuda constante."},
            {"área": "Lenguaje expresivo", "descripcion": "Dificultad para narrar o conversar."},
            {"área": "Lenguaje comprensivo", "descripcion": "No entiende preguntas ni sigue historias."},
            {"área": "Social - Cognitivo", "descripcion": "No comprende normas ni se integra a grupos."}
        ]
    }
}

output_dir = "data/asconi_json_por_rango"
os.makedirs(output_dir, exist_ok=True)

for nombre, datos in asconi_full.items():
    file_path = os.path.join(output_dir, f"{nombre}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

output_dir
