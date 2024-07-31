import csv
import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

class Tarea:
    def __init__(self, id, descripcion, prioridad, fecha_vencimiento, categoria="General"):
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, '%Y-%m-%d')
        self.completada = False
        self.categoria = categoria

class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.id_actual = 1

    def esta_vacia(self):
        return self.cabeza is None
    
    def tarea_existe(self, descripcion):
        actual = self.cabeza
        while actual is not None:
            if actual.tarea.descripcion.lower() == descripcion.lower():
                print(f"Tarea con descripción '{descripcion}' ya existe.")  # Debug print
                return True
            actual = actual.siguiente
        return False

    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento, categoria):
        if self.tarea_existe(descripcion):
            print("La tarea con esta descripción ya existe.")
            return
        tarea = Tarea(self.id_actual, descripcion, prioridad, fecha_vencimiento, categoria)
        nuevo_nodo = Nodo(tarea)
        self.id_actual += 1

        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

        print("Tarea agregada con éxito.")

    

    
    def buscar_tarea_descripcion(self,texto)->bool:
        actual = self.cabeza
        while actual is not None:
            if texto.lower() in actual.tarea.descripcion.lower():
                estado = "Completada" if actual.tarea.completada else "Pendiente"
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}")
            actual = actual.siguiente

    def completar_tarea(self, id):
        actual = self.cabeza
        while actual is not None:
            if actual.tarea.id == id:
                actual.tarea.completada = True
                print(f"Tarea con ID {id} marcada como completada.")
                return
            actual = actual.siguiente
        print(f"Tarea con ID {id} no encontrada.")


    def eliminar_tarea(self, id):
        actual = self.cabeza
        previo = None
        while actual is not None:
            if actual.tarea.id == id:
                if previo is None:
                    self.cabeza = actual.siguiente
                else:
                    previo.siguiente = actual.siguiente
                print(f"Tarea eliminada: {actual.tarea.descripcion}")
                return
            previo = actual
            actual = actual.siguiente
        print(f"Tarea con ID {id} no encontrada.")

    def mostrar_tareas(self):
        actual = self.cabeza
        while actual is not None:
            estado = "Completada" if actual.tarea.completada else "Pendiente"
            fecha_vencimiento = actual.tarea.fecha_vencimiento.strftime('%Y-%m-%d')
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}, Fecha de vencimiento: {fecha_vencimiento}")
            actual = actual.siguiente

    def mostrar_tareas_pendientes(self):
        actual = self.cabeza
        tareas_pendientes = False
        while actual is not None:
            if not actual.tarea.completada:
                fecha_vencimiento = actual.tarea.fecha_vencimiento.strftime('%Y-%m-%d')
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: Pendiente, Fecha de vencimiento: {fecha_vencimiento}")
                tareas_pendientes = True
            actual = actual.siguiente
        if not tareas_pendientes:
            print("No hay tareas pendientes.")
        
    def mostrar_tareas_descripcion(self,texto)->None:
        actual = self.cabeza
        tareas_encontradas = False
        while actual is not None:
            if texto.lower() in actual.tarea.descripcion.lower():
                estado = "Completada" if actual.tarea.completada else "Pendiente"
                fecha_vencimiento = actual.tarea.fecha_vencimiento.strftime('%Y-%m-%d')
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}, Fecha de vencimiento: {fecha_vencimiento}")
                tareas_encontradas = True
            actual = actual.siguiente
        if not tareas_encontradas:
            print("No se encontraron tareas con esa descripción.")

    # Funciones estadisticas:
    def contar_tareas_pendientes(self)->int:
        actual = self.cabeza
        contador = 0
        while actual is not None:
            if not actual.tarea.completada:
                contador += 1
            actual = actual.siguiente
        return contador
    def mostrar_estadisticas(self)->None:
        total = 0
        completadas = 0
        actual = self.cabeza
        while actual is not None:
            total += 1
            if actual.tarea.completada:
                completadas += 1
            actual = actual.siguiente
        pendientes = total - completadas
        print(f"Total de tareas: {total}")
        print(f"Tareas completadas: {completadas}")
        print(f"Tareas pendientes: {pendientes}")
        
        
    # Carga y guardado de archivos
    def guardar_en_csv(self, archivo):
        with open(archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            actual = self.cabeza
            while actual is not None:
                fecha_vencimiento = actual.tarea.fecha_vencimiento.strftime('%Y-%m-%d')
                writer.writerow([actual.tarea.id, actual.tarea.descripcion, actual.tarea.prioridad, fecha_vencimiento, actual.tarea.categoria, actual.tarea.completada])
                actual = actual.siguiente
        print(f"Tareas guardadas en {archivo} con éxito.")

    def cargar_desde_csv(self, archivo):
        if not os.path.exists(archivo):
            print(f"Archivo {archivo} no encontrado.")
            return
        with open(archivo, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    id, descripcion, prioridad, fecha_vencimiento, categoria, completada = int(row[0]), row[1], int(row[2]), row[3], row[4], row[5] == 'True'
                    if not self.tarea_existe(descripcion):
                        tarea = Tarea(id, descripcion, prioridad, fecha_vencimiento, categoria)
                        tarea.completada = completada
                        self.agregar_tarea_existente(tarea)
                    else:
                        print(f"Error: La tarea con la descripción '{descripcion}' ya existe en el archivo CSV.")
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}, {e}")
            print(f"Tareas cargadas desde {archivo} con éxito.")

    def agregar_tarea_existente(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

        if tarea.id >= self.id_actual:
            self.id_actual = tarea.id + 1

        print(f"Tarea con descripción '{tarea.descripcion}' agregada desde CSV.")

    def generar_informe_progreso(self):
        categorias = {}
        ahora = datetime.now()
        proximos_7_dias = ahora + timedelta(days=7)

        actual = self.cabeza
        while actual:
            tarea = actual.tarea
            categoria = tarea.categoria
            if categoria not in categorias:
                categorias[categoria] = {
                    "total": 0,
                    "completadas": 0,
                    "pendientes": 0,
                    "vencen_proximos_7_dias": 0,
                }
            categorias[categoria]["total"] += 1
            if tarea.completada:
                categorias[categoria]["completadas"] += 1
            else:
                categorias[categoria]["pendientes"] += 1
                if ahora <= tarea.fecha_vencimiento <= proximos_7_dias:
                    categorias[categoria]["vencen_proximos_7_dias"] += 1

            actual = actual.siguiente

        for categoria, datos in categorias.items():
            print(f"Categoría: {categoria}")
            print(f"  Total de tareas: {datos['total']}")
            print(f"  Tareas completadas: {datos['completadas']}")
            print(f"  Tareas pendientes: {datos['pendientes']}")
            print(f"  Tareas que vencen en los próximos 7 días: {datos['vencen_proximos_7_dias']}")

    def mostrar_tareas_vencen_proximos_7_dias(self):
        ahora = datetime.now()
        proximos_7_dias = ahora + timedelta(days=7)
        actual = self.cabeza
        tareas_encontradas = False
        while actual is not None:
            if ahora <= actual.tarea.fecha_vencimiento <= proximos_7_dias:
                estado = "Completada" if actual.tarea.completada else "Pendiente"
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}, Fecha de vencimiento: {actual.tarea.fecha_vencimiento.strftime('%Y-%m-%d')}")
                tareas_encontradas = True
            actual = actual.siguiente
        if not tareas_encontradas:
            print("No hay tareas que venzan en los próximos 7 días.")

    def mostrar_grafico_tareas_completadas_por_categoria(self):
        categorias = {}
        actual = self.cabeza
        while actual:
            tarea = actual.tarea
            categoria = tarea.categoria
            if categoria not in categorias:
                categorias[categoria] = {
                    "completadas": 0,
                    "pendientes": 0,
                }
            if tarea.completada:
                categorias[categoria]["completadas"] += 1
            else:
                categorias[categoria]["pendientes"] += 1

            actual = actual.siguiente

        categorias_list = list(categorias.keys())
        completadas_list = [categorias[c]["completadas"] for c in categorias_list]
        pendientes_list = [categorias[c]["pendientes"] for c in categorias_list]

        x = range(len(categorias_list))

        plt.bar(x, completadas_list, width=0.4, label="Completadas", align="center")
        plt.bar(x, pendientes_list, width=0.4, label="Pendientes", align="edge")
        plt.xlabel("Categorías")
        plt.ylabel("Número de Tareas")
        plt.title("Tareas Completadas y Pendientes por Categoría")
        plt.xticks(x, categorias_list, rotation=45)
        plt.legend()
        plt.show()

            
def mostrar_menu():
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
    print("0. Salir")

def main():
    lista_tareas = ListaEnlazada()
    archivo_csv = 'tareas.csv'

    # Cargar tareas desde CSV si el archivo existe
    lista_tareas.cargar_desde_csv(archivo_csv)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = int(input("Ingrese la prioridad de la tarea (1-10): "))
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
            categoria = input("Ingrese la categoría de la tarea: ")
            lista_tareas.agregar_tarea(descripcion, prioridad, fecha_vencimiento, categoria)

        elif opcion == "2":
            descripcion = input("Ingrese el texto a buscar en la descripción de la tarea: ")
            lista_tareas.buscar_tarea_descripcion(descripcion)

        elif opcion == "3":
            id = int(input("Ingrese el ID de la tarea a completar: "))
            lista_tareas.completar_tarea(id)

        elif opcion == "4":
            id = int(input("Ingrese el ID de la tarea a eliminar: "))
            lista_tareas.eliminar_tarea(id)

        elif opcion == "5":
            lista_tareas.mostrar_tareas()

        elif opcion == "6":
            lista_tareas.mostrar_tareas_pendientes()

        elif opcion == "7":
            descripcion = input("Ingrese el texto a buscar en la descripción de la tarea: ")
            lista_tareas.mostrar_tareas_descripcion(descripcion)

        elif opcion == "8":
            lista_tareas.mostrar_estadisticas()

        elif opcion == "9":
            lista_tareas.guardar_en_csv(archivo_csv)

        elif opcion == "10":
            lista_tareas.cargar_desde_csv(archivo_csv)

        elif opcion == "11":
            lista_tareas.generar_informe_progreso()

        elif opcion == "12":
            lista_tareas.mostrar_tareas_vencen_proximos_7_dias()

        elif opcion == "13":
            lista_tareas.mostrar_grafico_tareas_completadas_por_categoria()

        elif opcion == "0":
            print("Saliendo del sistema de gestión de tareas")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")


if __name__ == "__main__":
    main()
