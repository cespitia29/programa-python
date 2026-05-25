# Sistema de Auditoría de Inventario y Reabastecimiento 📦

Este repositorio contiene la solución al **Problema 3** de la actividad práctica del curso **Fundamentos de Programación**. El objetivo principal es automatizar el proceso de auditoría de inventario de una organización y determinar las cantidades exactas de artículos que requieren ser solicitados a los proveedores.

---

## 🚀 Características del Proyecto

El programa está desarrollado en **Python** y aplica conceptos clave de la programación estructurada y modular:
* **Estructura de Datos Bidimensional:** Uso de una matriz (lista de listas) para almacenar de forma organizada la información de al menos 5 artículos.
* **Programación Modular:** Implementación de una función (módulo) encargada exclusivamente de evaluar la lógica de negocio para cada producto de forma independiente.
* **Formateo de Salida:** Generación de un reporte de auditoría limpio, legible y alineado en consola utilizando f-strings.

---

## 📊 Lógica de Negocio Aplicada

Para determinar el reabastecimiento, el módulo evalúa las siguientes condiciones por cada artículo:

> 🔹 **Caso 1:** Si el `Stock Actual` es menor al `Stock Mínimo Requerido`, la cantidad exacta a solicitar se calcula como:
> $$\text{Cantidad a Pedir} = \text{Stock Mínimo} - \text{Stock Actual}$$
>
> 🔸 **Caso 2:** Si el `Stock Actual` es suficiente (mayor o igual al mínimo), la cantidad a pedir es **cero (0)**.

---

## 📂 Formato de la Matriz de Datos

La información de los productos se almacena respetando el siguiente orden de columnas:
`[Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]`

### Ejemplo de Datos Cargados:
| Código | Nombre | Stock Actual | Stock Mínimo | Pedido Calculado |
| :--- | :--- | :---: | :---: | :---: |
| ART01 | Teclado Mecánico | 12 | 20 | **8** |
| ART02 | Mouse Óptico | 35 | 30 | **0** |
| ART03 | Monitor 24 Pulg | 4 | 10 | **6** |

---

## 🛠️ Cómo Ejecutar el Programa

1. Asegúrate de tener instalado **Python 3.x** en tu equipo.
2. Clona este repositorio o descarga el archivo `inventario.py`.
3. Abre una terminal en la carpeta del proyecto y ejecuta el siguiente comando:

```bash
python inventario.py
