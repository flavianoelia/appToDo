import unittest
import os
import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from tareas import Tarea, Nodo, ListaEnlazada


class TestTarea(unittest.TestCase):  # Verifica la correcta creación de una instancia Tarea
    def test_crear_tarea(self):
        tarea = Tarea(1, "Test tarea", 5, "2024-08-05", "Trabajo")
        self.assertEqual(tarea.id, 1)
        self.assertEqual(tarea.descripcion, "Test tarea")
        self.assertEqual(tarea.prioridad, 5)
        self.assertEqual(tarea.fecha_vencimiento, datetime.strptime("2024-08-05", "%Y-%m-%d"))
        self.assertEqual(tarea.completada, False)
        self.assertEqual(tarea.categoria, "Trabajo")


class TestListaEnlazada(unittest.TestCase):
    def setUp(self):  # configura una lista enlazada con tres tareas de ejemplo
        self.lista_tareas = ListaEnlazada()
        self.lista_tareas.agregar_tarea("Ir al centro", 3, "2024-08-10", "Trabajo")
        self.lista_tareas.agregar_tarea("Ir al médico", 2, "2024-08-11", "Salud")
        self.lista_tareas.agregar_tarea("Leer apunte", 1, "2024-08-05", "Estudio")
        self.lista_tareas.agregar_tarea("Hacer resumen", 1, "2024-08-06", "Estudio")
        self.lista_tareas.agregar_tarea("Enviar mail a obra social", 1, "2024-08-09", "Salud" )
        self.lista_tareas.agregar_tarea("Resolver los cuestionarios", 1, "2024-08-08", "Trabajo")

    def test_agregar_tarea(self):  # Verifica que las tareas se agreguen correctamente a la lista enlazada
        self.assertEqual(self.lista_tareas.cabeza.tarea.descripcion, "Ir al centro")  # Utiliza self.lista_tareas.cabeza para ecceder al primer nodo
        self.assertEqual(self.lista_tareas.cabeza.siguiente.tarea.descripcion, "Ir al médico")  # Utiliza siguiente para acceder al siguiete nodo
        self.assertEqual(self.lista_tareas.cabeza.siguiente.siguiente.tarea.descripcion,"Leer apunte")
        self.assertEqual(self.lista_tareas.cabeza.siguiente.siguiente.siguiente.tarea.descripcion,"Hacer resumen")
        self.assertEqual(self.lista_tareas.cabeza.siguiente.siguiente.siguiente.siguiente.tarea.descripcion,"Enviar mail a obra social")
        self.assertEqual(self.lista_tareas.cabeza.siguiente.siguiente.siguiente.siguiente.siguiente.tarea.descripcion,"Resolver los cuestionarios")

    def test_completar_tarea(self):
        self.lista_tareas.completar_tarea(1)
        self.lista_tareas.completar_tarea(3)
        self.lista_tareas.completar_tarea(4)

        # Verificar que las tareas se han completado
        actual = self.lista_tareas.cabeza
        tareas_completadas = []
        while actual is not None:
            if actual.tarea.id in [1, 3, 4]:
                tareas_completadas.append(actual.tarea.id)
                self.assertTrue(actual.tarea.completada)  # Verificar que las tareas específicas están completadas
            actual = actual.siguiente

        # Verificar que ambas tareas han sido marcadas como completadas
        self.assertIn(1, tareas_completadas)
        self.assertIn(3, tareas_completadas)
        self.assertIn(4, tareas_completadas)

    def test_eliminar_tarea(self):
        self.lista_tareas.eliminar_tarea(1)
        self.assertEqual(self.lista_tareas.cabeza.tarea.descripcion, "Ir al médico")

    def test_mostrar_tareas(self):
        self.lista_tareas.mostrar_tareas()

    def test_buscar_tarea_descripcion(self):
        self.lista_tareas.buscar_tarea_descripcion("Ir al centro")

    def test_mostrar_tareas_pendientes(self):
        self.lista_tareas.mostrar_tareas_pendientes()

    def test_mostrar_estadisticas(self):
        self.lista_tareas.mostrar_estadisticas()

    def test_generar_informe_progreso(self):
        self.lista_tareas.generar_informe_progreso()

    def test_mostrar_tareas_vencen_proximos_7_dias(self):
        self.lista_tareas.mostrar_tareas_vencen_proximos_7_dias()

    def test_mostrar_grafico_tareas_completadas_por_categoria(self):
        # Como hay independencia entre pruebas primero tuve que completar algunas tareas para ver los cambios en el gráfico
        self.lista_tareas.completar_tarea(1)  # Marco como completada tarea con ID 1
        self.lista_tareas.completar_tarea(3)  # Marco como completada tarea con ID 3

        print("Estado de las tareas antes de generar el gráfico:")
        actual = self.lista_tareas.cabeza
        while actual is not None:
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Completada: {actual.tarea.completada}")
            actual = actual.siguiente

        # Generar el gráfico
        self.lista_tareas.mostrar_grafico_tareas_completadas_por_categoria()


if __name__ == "__main__":
    unittest.main()
