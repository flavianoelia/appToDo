import csv# importamos la libreria csv para poder trabajar con archivos csv. 
import os# importamos el modulo os para poder interactuar con el sistema operativo.
from datetime import datetime, timedelta#importamos datetime y timedelta para poder trabajar con fechas.
import matplotlib.pyplot as plt#importamos matplotlib.pyplot para poder crear graficos.

class Tarea:#Esta línea define una nueva clase llamada Tarea. 
    def __init__(self, id, descripcion, prioridad, fecha_vencimiento, categoria="General"):#Esta línea define el método __init__, que es el constructor de la clase. Este método se llama automáticamente cuando se crea una nueva instancia de la clase Tarea. 
        self.id = id #asigna el parametro id al atributo id del objeto.
        self.descripcion = descripcion# asigna el parametro descripcion al atributo descripcion del objeto.
        self.prioridad = prioridad#asigna el parametro prioridad al atributo prioridad del objeto.
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, '%Y-%m-%d')#Convierte la fecha de vencimiento de string a objeto datetime.
        self.completada = False# Inicializa el atributo completada como False
        self.categoria = categoria# Asigna el parámetro categoria al atributo categoria del objeto.

class Nodo:## Define una clase llamada Nodo.
    def __init__(self, tarea):#define el Constructor de la clase.
        self.tarea = tarea# Inicializa los atributos del nodo: tarea (que almacena una instancia de la clase Tarea)
        self.siguiente = None#siguiente (que apunta al siguiente nodo en la lista enlazada, inicialmente None).

class ListaEnlazada:# Define una clase llamada ListaEnlazada.
    def __init__(self):#Define el método constructor __init__.
        self.cabeza = None#Inicializa el atributo cabeza como None.
        self.id_actual = 1# Inicializa el atributo id_actual como 1.
        self.pendientes = 0#Inicializa el atributo pendientes como 0.

    def esta_vacia(self):#Define un método para comprobar si la lista está vacía
        return self.cabeza is None#e  # Devuelve True si la lista está vacía (cabeza es None), de lo contrario devuelve False.
    
    def tarea_existe(self, descripcion):#Define un método para comprobar si una tarea con una descripción específica ya existe.
        actual = self.cabeza#Inicializa actual con la cabeza de la lista.
        while actual is not None:#Itera sobre la lista enlazada.
            if actual.tarea.descripcion.lower() == descripcion.lower():#: Itera sobre la lista enlazada para comprobar si existe una tarea con la misma descripción (ignorando mayúsculas/minúsculas
                print(f"Tarea con descripción '{descripcion}' ya existe.") # Si encuentra una coincidencia, imprime un mensaje.
                return True# devuelve true
            actual = actual.siguiente# Avanza al siguiente nodo.
        return False#Devuelve False si no se encuentra ninguna tarea con la misma descripción.

    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento, categoria):# Define un método para agregar una tarea a la lista.
        if self.tarea_existe(descripcion):#Comprueba si ya existe una tarea con la misma descripción.
            print("La tarea con esta descripción ya existe.")#Imprime un mensaje si la tarea ya existe.
            return#Termina el método si la tarea ya existe
        tarea = Tarea(self.id_actual, descripcion, prioridad, fecha_vencimiento, categoria)#Crea una nueva instancia de Tarea.
        nuevo_nodo = Nodo(tarea)#Crea un nuevo nodo con la tarea.
        self.id_actual += 1#Incrementa el contador de ID.
        self.pendientes += 1# Incrementa el contador de tareas pendientes.

        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad:# Comprueba si la lista está vacía o si la nueva tarea tiene mayor prioridad que la tarea en la cabeza.
            nuevo_nodo.siguiente = self.cabeza # Establece el siguiente del nuevo nodo como la cabeza actual.
            self.cabeza = nuevo_nodo# Actualiza la cabeza de la lista al nuevo nodo.
        else:# Si la lista no está vacía y la nueva tarea no tiene mayor prioridad que la tarea en la cabeza.
            actual = self.cabeza# Inicializa actual con la cabeza de la lista.
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad: # Itera hasta encontrar la posición correcta para insertar la nueva tarea.
                actual = actual.siguiente # Avanza al siguiente nodo.
            nuevo_nodo.siguiente = actual.siguiente# Establece el siguiente del nuevo nodo como el siguiente del nodo actual.
            actual.siguiente = nuevo_nodo # Establece el siguiente del nodo actual como el nuevo nodo.

        print("Tarea agregada con éxito.")# Imprime un mensaje indicando que la tarea se ha agregado con éxito.

    

    
    def buscar_tarea_descripcion(self,texto)->bool:# Define un método para buscar tareas por descripción.
        actual = self.cabeza# Inicializa actual con la cabeza de la lista.
        while actual is not None: # Itera sobre la lista enlazada.
            if texto.lower() in actual.tarea.descripcion.lower(): # Comprueba si el texto está en la descripción de la tarea (ignorando mayúsculas/minúsculas).
                estado = "Completada" if actual.tarea.completada else "Pendiente" # Determina el estado de la tarea.
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}")# Imprime los detalles de la tarea. 
            actual = actual.siguiente# Avanza al siguiente nodo.

    def completar_tarea(self, id): # Define un método para marcar una tarea como completada.
        actual = self.cabeza # Inicializa actual con la cabeza de la lista.
        while actual is not None:# Itera sobre la lista enlazada.
            if actual.tarea.id == id: # Comprueba si el ID de la tarea coincide con el ID especificado.
                actual.tarea.completada = True # Marca la tarea como completada.
                self.pendientes -= 1# Decrementa el contador de tareas pendientes.
                print(f"Tarea con ID {id} marcada como completada.")# Imprime un mensaje indicando que la tarea se ha completado.
                return # Termina el método.
            actual = actual.siguiente# Avanza al siguiente nodo.
        print(f"Tarea con ID {id} no encontrada.")# Imprime un mensaje si no se encuentra la tarea con el ID especificado.


    def eliminar_tarea(self, id): # Define un método para eliminar una tarea por su ID.
        actual = self.cabeza# Inicializa actual con la cabeza de la lista.
        previo = None# Inicializa previo como None.
        while actual is not None: # Itera sobre la lista enlazada.
            if actual.tarea.id == id:# Comprueba si el ID de la tarea coincide con el ID especificado
                if previo is None: # Si la tarea a eliminar es la primera de la lista.
                    self.cabeza = actual.siguiente# Actualiza la cabeza de la lista.
                else:# Si la tarea a eliminar no es la primera de la lista.
                    previo.siguiente = actual.siguiente # Actualiza el siguiente del nodo previo.
                print(f"Tarea eliminada: {actual.tarea.descripcion}")# Imprime un mensaje indicando que la tarea se ha eliminado.
                if actual.tarea.completada: # Comprueba si la tarea estaba completada
                    self.pendientes -= 1 # Decrementa el contador de tareas pendientes.
                return# Termina el método.
            previo = actual  # Actualiza previo al nodo actual.
            actual = actual.siguiente# Avanza al siguiente nodo.
        print(f"Tarea con ID {id} no encontrada.")# Imprime un mensaje si no se encuentra la tarea con el ID especificado.

    def mostrar_tareas(self):# define el metodo mostrar tareas.
        actual = self.cabeza # Inicia el recorrido desde la cabeza de la lista enlazada.
        while actual is not None:#Se inicia un bucle while que continuará mientras actual no sea None. Esto permite recorrer todos los nodos de la lista enlazada
            estado = "Completada" if actual.tarea.completada else "Pendiente" #Se utiliza una condicional para determinar el estado de la tarea. Si actual.tarea.completada es True, estado será "Completada", de lo contrario, será "Pendiente".
            fecha_vencimiento = actual.tarea.fecha_vencimiento.strftime('%Y-%m-%d')#Se formatea la fecha de vencimiento de la tarea (actual.tarea.fecha_vencimiento) a una cadena de texto en el formato AAAA-MM-DD utilizando el método strftime
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}, Fecha de vencimiento: {fecha_vencimiento}")#Se imprime un mensaje formateado con varios atributos de la tarea actual.
            actual = actual.siguiente#Se actualiza actual para que apunte al siguiente nodo en la lista enlazada

    def mostrar_tareas_pendientes(self):#Esta línea define un método llamado contar_tareas_pendientes
        actual = self.cabeza#Se inicializa una variable actual con el valor de self.cabeza, que es el primer nodo de la lista enlazada
        tareas_pendientes = False#Se inicializa una variable booleana tareas_pendientes en False. Esta variable se usará para indicar si se han encontrado tareas pendientes.
        while actual is not None:#Se inicia un bucle while que continuará mientras actual no sea None, permitiendo recorrer todos los nodos de la lista enlazada.
            if not actual.tarea.completada:#Dentro del bucle, se verifica si la tarea actual (actual.tarea) no está completada (not actual.tarea.completada)
                fecha_vencimiento = actual.tarea.fecha_vencimiento.strftime('%Y-%m-%d')#Si la tarea no está completada, se formatea la fecha de vencimiento de la tarea (actual.tarea.fecha_vencimiento) a una cadena de texto en el formato AAAA-MM-DD utilizando el método strftime
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: Pendiente, Fecha de vencimiento: {fecha_vencimiento}")#Se imprime un mensaje formateado con varios atributos de la tarea actual
                tareas_pendientes = True#Se establece tareas_pendientes a True para indicar que se ha encontrado al menos una tarea pendiente
            actual = actual.siguiente#Se actualiza actual para que apunte al siguiente nodo en la lista enlazada (actual.siguiente), continuando así con el siguiente ciclo del bucle while
        if not tareas_pendientes:#Después de que el bucle while termina, se verifica si tareas_pendientes sigue siendo False.
            print("No hay tareas pendientes.")#Si tareas_pendientes es False, se imprime un mensaje indicando que no hay tareas pendientes
        
    def mostrar_tareas_descripcion(self,texto)->None:#define el metodo mostrar_tareas_descripcion
        actual = self.cabeza# Inicializa actual con la cabeza de la lista enlazada.
        tareas_encontradas = False#variable que se crea para verificar si se encontraron tareas que coincidan con la descripción.
        while actual is not None:# Recorre la lista enlazada hasta llegar al final.
            if texto.lower() in actual.tarea.descripcion.lower():#verifica si el texto proporcionado, convertido a minúsculas, está en la descripción de la tarea actual, (también convertida a minúsculas).
                estado = "Completada" if actual.tarea.completada else "Pendiente"#Esto determina el estado de la tarea como "Completada" si el atributo completada de la tarea es True, de lo contrario, se establece como "Pendiente"
                fecha_vencimiento = actual.tarea.fecha_vencimiento.strftime('%Y-%m-%d') # Formatea la fecha de vencimiento de la tarea en el formato 'AAAA-MM-DD'.
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}, Fecha de vencimiento: {fecha_vencimiento}")#Imprime los detalles de la tarea en un formato legible
                tareas_encontradas = True#Marca que se ha encontrado al menos una tarea que coincide con la descripción proporcionada.
            actual = actual.siguiente#Avanza al siguiente nodo en la lista enlazada
        if not tareas_encontradas:# Si no se encontraron tareas que coincidan con la descripción.
            print("No se encontraron tareas con esa descripción.")# Imprime un mensaje indicando que no se encontraron tareas.

    # Funciones estadisticas:
    def contar_tareas_pendientes(self)->int:#se crea un metodo contar_tareas_pendientes que devuelve un entero.
        actual = self.cabeza # Inicializa 'actual' con la cabeza de la lista enlazada.
        contador = 0# Inicializa el contador de tareas pendientes en 0.
        while actual is not None: # Recorre la lista enlazada hasta llegar al final.
            if not actual.tarea.completada:# Verifica si la tarea actual no está completada.
                contador += 1# Incrementa el contador de tareas pendientes.
            actual = actual.siguiente # Pasa al siguiente nodo en la lista enlazada.
        return contador # Devuelve el número total de tareas pendientes.

    def contar_tareas_pendientes_cte(self)->int:#se crea el metodo contar_tareas_pendientes_cte que devuelve un entero.
        return self.pendientes# Devuelve el contador de tareas pendientes almacenado en el atributo 'pendientes' de la lista.
    
    def mostrar_estadisticas(self)->None:
        total = 0 # Inicializa el contador total de tareas en 0
        completadas = 0# Inicializa el contador de tareas completadas en 0.
        actual = self.cabeza# Inicializa 'actual' con la cabeza de la lista enlazada.
        while actual is not None: # Recorre la lista enlazada hasta llegar al final
            total += 1# Incrementa el contador total de tareas
            if actual.tarea.completada:# Verifica si la tarea actual está completada.
                completadas += 1 # Incrementa el contador de tareas completadas.
            actual = actual.siguiente# Pasa al siguiente nodo en la lista enlazada.
        pendientes = total - completadas# Calcula el número de tareas pendientes.
        print(f"Total de tareas: {total}")#imprime el total de tareas.
        print(f"Tareas completadas: {completadas}")#imprime el total de tareas completadas.
        print(f"Tareas pendientes: {pendientes}")#imprime el total de tareas pendientes.
        
        
    # Carga y guardado de archivos
    def guardar_en_csv(self, archivo):#se define el metodo guardar_en_csv
        with open(archivo, mode='w', newline='') as file:# Abre el archivo en modo escritura ('w') con nueva línea ('newline') para manejar correctamente las líneas en CSV
            writer = csv.writer(file) #se crea un escritor CSV
            actual = self.cabeza# Inicializa 'actual' con la cabeza de la lista enlazada.
            while actual is not None:# Recorre la lista enlazada hasta llegar al final.
                fecha_vencimiento = actual.tarea.fecha_vencimiento.strftime('%Y-%m-%d')#Formatea la fecha de vencimiento de la tarea en el formato 'AAAA-MM-DD'.
                writer.writerow([actual.tarea.id, actual.tarea.descripcion, actual.tarea.prioridad, fecha_vencimiento, actual.tarea.categoria, actual.tarea.completada]) # Escribe una fila en el archivo CSV con los detalles de la tarea. 
                actual = actual.siguiente# Pasa al siguiente nodo en la lista enlazada.
        print(f"Tareas guardadas en {archivo} con éxito.")# Imprime un mensaje indicando que las tareas se guardaron con éxito.

    def cargar_desde_csv(self, archivo):
        if not os.path.exists(archivo):#Verifica si el archivo existe.
            print(f"Archivo {archivo} no encontrado.") #Imprime un mensaje si el archivo no se encuentra.
            return #Sale del método si el archivo no existe.
        with open(archivo, mode='r') as file:#Abre el archivo en modo lectura ('r').
            reader = csv.reader(file)#Crea un lector CSV.
            for row in reader: #Recorre cada fila del archivo CSV
                if len(row) != 6:#Verifica si la fila tiene exactamente 6 elementos.
                    print(f"Fila incompleta o malformada: {row}")#Imprime un mensaje si la fila está incompleta o malformada.
                    continue#Pasa a la siguiente fila.
                try: # Extrae los valores de la fila y los convierte al tipo adecuado.
                    id, descripcion, prioridad, fecha_vencimiento, categoria, completada = int(row[0]), row[1], int(row[2]), row[3], row[4], row[5] == 'True'
                    if not self.tarea_existe(descripcion):#Verifica si la tarea con la descripción dada no existe.
                        tarea = Tarea(id, descripcion, prioridad, fecha_vencimiento, categoria)#Crea una nueva instancia de la tarea con los valores extraídos
                        tarea.completada = completada #Establece el estado completado de la tarea.
                        self.agregar_tarea_existente(tarea)#Agrega la tarea a la lista enlazada.
                    else:#si la tarea con la descripción dada existe.
                        print(f"Error: La tarea con la descripción '{descripcion}' ya existe en el archivo CSV.")#Imprime un mensaje si la tarea ya existe.
                except ValueError as e: #Captura cualquier error de conversión de valores
                    print(f"Error al procesar la fila: {row}, {e}") #Imprime un mensaje de error si eso ocurre.
            print(f"Tareas cargadas desde {archivo} con éxito.")#Imprime un mensaje indicando que las tareas se cargaron con éxito.

    def agregar_tarea_existente(self, tarea):
        nuevo_nodo = Nodo(tarea)#Crea un nuevo nodo con la tarea dada.
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad:#Si la lista está vacía o la tarea tiene mayor prioridad que la cabeza.
            nuevo_nodo.siguiente = self.cabeza #Apunta el nuevo nodo a la cabeza actual.
            self.cabeza = nuevo_nodo#Establece el nuevo nodo como la nueva cabeza.
        else:#Si la lista no está vacía y la prioridad de la nueva tarea no es mayor que la de la cabeza.
            actual = self.cabeza#Inicia la búsqueda en la cabeza de la lista.
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad:#Busca el lugar adecuado según la prioridad.
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente#Ajusta los enlaces para insertar el nuevo nodo.
            actual.siguiente = nuevo_nodo

        if tarea.id >= self.id_actual:#Actualiza el ID actual si la tarea importada tiene un ID mayor
            self.id_actual = tarea.id + 1#se actualiza al valor del ID de la tarea más 1.
            
        print(f"Tarea con descripción '{tarea.descripcion}' agregada desde CSV.")#Se imprime un mensaje de confirmación indicando que la tarea ha sido agregada a la lista desde un archivo CSV

    def generar_informe_progreso(self):
        categorias = {}#Inicializa un diccionario vacío que almacenará estadísticas de tareas agrupadas por categoría.
        ahora = datetime.now()#Obtiene la fecha y hora actuales, se usará para comparar fechas de vencimiento de las tareas
        proximos_7_dias = ahora + timedelta(days=7)# Calcula la fecha que es exactamente 7 días después de la fecha y hora actuales. Esto se usará para determinar qué tareas vencen en los próximos 7 días.

        actual = self.cabeza#Inicia la variable actual en la cabeza (primer nodo) de la lista enlazada de tareas. Este nodo será utilizado para recorrer la lista.
        while actual:#Inicia un bucle while que continuará mientras actual no sea None, es decir, mientras no se haya alcanzado el final de la lista.
            tarea = actual.tarea#Extrae la tarea del nodo actual para trabajar con ella.
            categoria = tarea.categoria#Obtiene la categoría de la tarea actual, que se utilizará para agrupar las estadísticas en el diccionario categorias.
            if categoria not in categorias:#Verifica si la categoría de la tarea actual ya está en el diccionario categorias.
                categorias[categoria] = {#Si la categoría no está en el diccionario, se crea una nueva entrada con un conjunto de estadísticas inicializadas en 0 (total, completadas, pendientes, vencen_proximos_7_dias).
                    "total": 0,
                    "completadas": 0,
                    "pendientes": 0,
                    "vencen_proximos_7_dias": 0,
                }
            categorias[categoria]["total"] += 1#Incrementa el contador total de tareas para la categoría actual en 1.
            if tarea.completada:#Verifica si la tarea está completada.
                categorias[categoria]["completadas"] += 1#Si la tarea está completada, incrementa el contador de tareas completadas para la categoría en 1.
            else:#Si la tarea no está completada, entra en este bloque.
                categorias[categoria]["pendientes"] += 1#Incrementa el contador de tareas pendientes para la categoría en 1.
                if ahora <= tarea.fecha_vencimiento <= proximos_7_dias:#Verifica si la fecha de vencimiento de la tarea está dentro de los próximos 7 días.
                    categorias[categoria]["vencen_proximos_7_dias"] += 1#Si la tarea vence dentro de los próximos 7 días, incrementa el contador de tareas que vencen pronto en 1.

            actual = actual.siguiente# Mueve el puntero actual al siguiente nodo en la lista, continuando así el recorrido de la lista enlazada.

        for categoria, datos in categorias.items():#Itera sobre cada categoría y sus estadísticas en el diccionario categorias.
            print(f"Categoría: {categoria}")#Imprime el nombre de la categoría.
            print(f"  Total de tareas: {datos['total']}")#Imprime el total de tareas en esa categoría.
            print(f"  Tareas completadas: {datos['completadas']}")#Imprime el número de tareas completadas.
            print(f"  Tareas pendientes: {datos['pendientes']}")#Imprime el número de tareas pendientes.
            print(f"  Tareas que vencen en los próximos 7 días: {datos['vencen_proximos_7_dias']}")#Imprime el número de tareas que vencen en los próximos 7 días.

    def mostrar_tareas_vencen_proximos_7_dias(self):#Define un método de la clase. Este método no recibe parámetros adicionales más allá de self
        ahora = datetime.now()#Obtiene la fecha y hora actuales.
        proximos_7_dias = ahora + timedelta(days=7)#Calcula la fecha que es exactamente 7 días después de la fecha actual.
        actual = self.cabeza# Inicia la variable actual en la cabeza de la lista enlazada de tareas.
        tareas_encontradas = False#Inicializa una variable para determinar si se encontraron tareas que vencen en los próximos 7 días.
        while actual is not None:#Inicia un bucle que continuará mientras actual no sea None
            if ahora <= actual.tarea.fecha_vencimiento <= proximos_7_dias:#Verifica si la fecha de vencimiento de la tarea está dentro del rango de los próximos 7 días.
                estado = "Completada" if actual.tarea.completada else "Pendiente"#Determina el estado de la tarea como "Completada" o "Pendiente" según su estado actual.
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}, Fecha de vencimiento: {actual.tarea.fecha_vencimiento.strftime('%Y-%m-%d')}")#Imprime los detalles de la tarea, incluyendo ID, descripción, prioridad, categoría, estado y fecha de vencimiento. 
                tareas_encontradas = True#Inicializa la variable tareas_encontradas a True si se encuentra al menos una tarea que cumple la condición.
            actual = actual.siguiente#Avanza a la siguiente tarea en la lista enlazada.
        if not tareas_encontradas:#Si no se encontraron tareas en el rango de los próximos 7 días
            print("No hay tareas que venzan en los próximos 7 días.")#imprime un mensaje que no hay tareas proximas a vencer.
            
    def mostrar_grafico_tareas_completadas_por_categoria(self):#Define un método que no recibe parámetros adicionales más allá de self.
        categorias = {}#Inicializa un diccionario vacío que almacenará la cantidad de tareas completadas y pendientes para cada categoría.
        actual = self.cabeza#Inicia la variable actual en la cabeza de la lista enlazada de tareas
        while actual:#Inicia un bucle while que continuará hasta que actual sea None, es decir, hasta que se haya recorrido toda la lista enlazada.
            tarea = actual.tarea#Extrae la tarea del nodo actual para trabajar con ella.
            categoria = tarea.categoria#Obtiene la categoría de la tarea actual.
            if categoria not in categorias:#Verifica si la categoría de la tarea actual ya está en el diccionario categorias.
                categorias[categoria] = {#Si la categoría no está en el diccionario, se crea una nueva entrada con contadores para tareas completadas y pendientes inicializados en 0.
                    "completadas": 0,
                    "pendientes": 0,
                }
            if tarea.completada:#Verifica si la tarea está completada.
                categorias[categoria]["completadas"] += 1#Si la tarea está completada, incrementa el contador de tareas completadas para la categoría en 1
            else:# Si la tarea no está completada, entra en este bloque.
                categorias[categoria]["pendientes"] += 1#Incrementa el contador de tareas pendientes para la categoría en 1.

            actual = actual.siguiente#Mueve el puntero actual al siguiente nodo en la lista, permitiendo que el bucle continúe su recorrido.

        categorias_list = list(categorias.keys())#Convierte las claves del diccionario categorias (es decir, las categorías) en una lista. Esto se usará para etiquetar los ejes del gráfico.
        completadas_list = [categorias[c]["completadas"] for c in categorias_list]#Crea una lista con el número de tareas completadas para cada categoría, en el mismo orden que categorias_list.
        pendientes_list = [categorias[c]["pendientes"] for c in categorias_list]#Crea una lista con el número de tareas pendientes para cada categoría, en el mismo orden que categorias_list.

        x = range(len(categorias_list))#Crea una secuencia de números que corresponde a la cantidad de categorías.Se usará como las posiciones en el eje x del gráfico.

        plt.bar(x, completadas_list, width=0.4, label="Completadas", align="center")# # Grafica las tareas completadas con barras, ubicándolas en la posición 'x', con una anchura de 0.4 y alineación centrada.
        plt.bar(x, pendientes_list, width=0.4, label="Pendientes", align="edge")
        plt.xlabel("Categorías")#Establece la etiqueta para el eje X del gráfico.
        plt.ylabel("Número de Tareas")
        plt.title("Tareas Completadas y Pendientes por Categoría")#Establece el título del gráfico.
        plt.xticks(x, categorias_list, rotation=45)#Establece las etiquetas del eje X con las categorías, rotando los nombres 45 grados para mayor claridad.
        plt.legend()#Añade una leyenda al gráfico para identificar qué representan las barras.
        plt.show()#Muestra el gráfico en la pantalla.

            
def mostrar_menu():#Esta función muestra un menú con las diferentes opciones disponibles para el usuario. Cada opción está numerada y describe una acción específica que se puede realizar en el sistema de gestión de tareas.
    print("\nMenú de opciones:")
    print("1. Agregar tarea")
    print("2. Buscar tarea por descripción")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Mostrar todas las tareas")
    print("6. Mostrar tareas pendientes")
    print("7. Mostrar tareas por descripción")
    print("8. Mostrar estadísticas de tareas")
    print("9. Guardar tareas en CSV")
    print("10. Cargar tareas desde CSV")
    print("11. Generar informe de progreso")
    print("12. Mostrar tareas que vencen en los próximos 7 días")
    print("13. Mostrar gráfico de tareas completadas por categoría")
    print("14. Mostrar cantidad de tareas pendientes")
    print("0. Salir")

def main():
    lista_tareas = ListaEnlazada()#Crea una instancia de la lista enlazada que almacenará las tareas.
    archivo_csv = 'tareas.csv'## Define el nombre del archivo CSV para guardar y cargar tareas.

    # Cargar tareas desde CSV si el archivo existe
    lista_tareas.cargar_desde_csv(archivo_csv)

    while True:
        mostrar_menu()# Muestra el menú de opciones.
        opcion = input("Seleccione una opción: ")#Solicita al usuario que elija una opción.

        if opcion == "1":#Si el usuario elige la opción 1, agregar una nueva tarea:
            descripcion = input("Ingrese la descripción de la tarea: ")#Solicita al usuario la descripción de la nueva tarea.
            prioridad = int(input("Ingrese la prioridad de la tarea (1-10): "))#Solicita la prioridad de la tarea y la convierte a un número entero.
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")#Solicita la fecha de vencimiento de la tarea
            categoria = input("Ingrese la categoría de la tarea: ")#Solicita la categoría de la tarea.
            lista_tareas.agregar_tarea(descripcion, prioridad, fecha_vencimiento, categoria)#Llama al método para agregar la tarea con los datos proporcionados.

        elif opcion == "2":#Si el usuario elige la opción 2, buscar una tarea por descripción
            descripcion = input("Ingrese el texto a buscar en la descripción de la tarea: ")#Solicita el texto a buscar en la descripción de las tareas.
            lista_tareas.buscar_tarea_descripcion(descripcion)#Llama al método para buscar y mostrar tareas que contengan el texto proporcionado en su descripción.

        elif opcion == "3":#Si el usuario elige la opción 3, completar una tarea
            id = int(input("Ingrese el ID de la tarea a completar: "))#Solicita el ID de la tarea que se desea marcar como completada.
            lista_tareas.completar_tarea(id)#Llama al método para marcar la tarea con el ID proporcionado como completada.

        elif opcion == "4":#Si el usuario elige la opción 4, eliminar una tarea.
            id = int(input("Ingrese el ID de la tarea a eliminar: "))#Solicita el ID de la tarea que se desea eliminar.
            lista_tareas.eliminar_tarea(id)#Llama al metodo para eliminar la tarea.

        elif opcion == "5":#Si el usuario elige la opción 5, mostrar todas las tareas.
            lista_tareas.mostrar_tareas()#Llama al método para mostrar todas las tareas en la lista.

        elif opcion == "6": #Si el usuario elige la opción 6, mostrar tareas pendientes.
            lista_tareas.mostrar_tareas_pendientes()#Llama al método para mostrar solo las tareas que están pendientes.

        elif opcion == "7":#Si el usuario elige la opción 7, mostrar tareas por descripción.
            descripcion = input("Ingrese el texto a buscar en la descripción de la tarea: ")#solicita al usuario que ingrese el texto.
            lista_tareas.mostrar_tareas_descripcion(descripcion) #Solicita el texto para buscar en la descripción de las tareas.

        elif opcion == "8":#Si el usuario elige la opción 8, mostrar estadísticas de tareas.
            lista_tareas.mostrar_estadisticas()#Llama al método para mostrar las estadísticas de todas las tareas (total, completadas, pendientes).

        elif opcion == "9":#Si el usuario elige la opción 9, guardar tareas en un archivo CSV.
            lista_tareas.guardar_en_csv(archivo_csv)#Llama al metodo para guardar tareas en un archivo CSV.

        elif opcion == "10":#Si el usuario elige la opción 10, cargar tareas desde un archivo CSV.
            lista_tareas.cargar_desde_csv(archivo_csv)#Llama al método para cargar tareas desde el archivo CSV especificado.

        elif opcion == "11":#Si el usuario elige la opción 11, generar un informe de progreso.
            lista_tareas.generar_informe_progreso()#Llama al método para generar un informe sobre el progreso de las tareas.

        elif opcion == "12":#Si el usuario elige la opción 12, mostrar tareas que vencen en los próximos 7 días.
            lista_tareas.mostrar_tareas_vencen_proximos_7_dias()#Llama al método para mostrar las tareas cuya fecha de vencimiento es dentro de los próximos 7 días.

        elif opcion == "13":#Si el usuario elige la opción 13, mostrar un gráfico de tareas completadas por categoría.
            lista_tareas.mostrar_grafico_tareas_completadas_por_categoria()#Llama al método para generar y mostrar un gráfico con la cantidad de tareas completadas por categoría.

        elif opcion == "14":#Si el usuario elige la opción 14, mostrar la cantidad de tareas pendientes
            print(f"La cantidad de tareas pendientes es: {lista_tareas.contar_tareas_pendientes_cte()}")#Imprime la cantidad de tareas pendientes utilizando el método correspondiente.
            
        elif opcion == "0":#Si el usuario elige la opción 0, salir del programa.
            print("Saliendo del sistema de gestión de tareas")#Imprime un mensaje indicando que el programa está saliendo.
            break#Rompe el bucle infinito y termina la ejecución del programa.

        else: #Si la opción ingresada no es válida.
            print("Opción no válida. Por favor, seleccione una opción del menú.")#Imprime un mensaje indicando que la opción seleccionada no es válida.


if __name__ == "__main__":#Verifica si el archivo se está ejecutando directamente como un script
    main() #Llama a la función main() para iniciar la ejecución del programa.
    # Esto mostrará el menú y permitirá al usuario interactuar con el sistema de gestión de tareas
