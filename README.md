# proyecto_programacion

## Libreria de Visualización para Clustering

Esta libreria proporciona un conjunto de clases en Python para crear y personalizar diversas visualizaciones de datos comúnmente utilizadas en clustering. El kit está diseñado para ser versátil y fácil de usar, permitiendo generar rápidamente visualizaciones que pueden facilitar el analisis de clustering.

### Tabla de Contenidos

1. [Instalación](#instalación)
2. [Uso](#uso)
   - [GraficoCluster](#graficocluster)
   - [GraficoHistograma](#graficohistograma)
   - [GraficoDeBarras](#graficodebarras)
   - [GraficoHistogramaCluster](#graficohistogramacluter)
   - [GraficoDeBarrasCluster](#graficodebarrascluster)
   - [GraficoDispersion](#graficodispersion)

## Instalación

Para usar este kit, asegúrese de tener instaladas las dependencias necesarias:

```bash
pip install pandas
pip install matplotlib
pip install numpy
pip install plotterclassprogra
```

## Uso

### GraficoCluster

La clase `GraficoCluster` sirve como la clase base para varias visualizaciones basadas en clústeres. Se inicializa con un DataFrame y proporciona métodos para configurar colores, título y tamaño de figura. Para mostrar el gráfico, utilice el método `mostrar`.

```python
from plotterclassprogra.plotter import GraficoCluster

# Ejemplo de Uso
datos = # proporcionar su DataFrame
grafico = GraficoCluster(datos)
grafico.configurar_colores(['azul', 'verde', 'rojo'])
grafico.mostrar()
```

### GraficoHistograma

La clase `GraficoHistograma` extiende `GraficoCluster` y se especializa en crear gráficos de histograma. Personalice el número de bins, escala logarítmica y tipo de histograma mediante el método `mostrar`.

```python
from plotterclassprogra.plotter import GraficoHistograma

# Ejemplo de Uso
grafico_hist = GraficoHistograma(datos)
grafico_hist.configurar_colores(['naranja'])
grafico_hist.mostrar('nombre_columna', bins=20, log=True, histtype='bar')
```

### GraficoDeBarras

La clase `GraficoDeBarras`, también una extensión de `GraficoCluster`, genera gráficos de barras. Proporcione opcionalmente un DataFrame de orden para personalizar el orden de las barras.

```python
from plotterclassprogra.plotter import GraficoDeBarras

# Ejemplo de Uso
grafico_barras = GraficoDeBarras(datos)
grafico_barras.configurar_colores(['morado'])
grafico_barras.mostrar('nombre_columna', order_df=None)
```

### GraficoHistogramaCluster

Esta clase extiende `GraficoCluster` y está especializada en gráficos de histograma con múltiples clústeres.

```python
from plotterclassprogra.plotter import GraficoHistogramaCluster

# Ejemplo de Uso
grafico_hist_cluster = GraficoHistogramaCluster(datos)
grafico_hist_cluster.configurar_colores(['cian', 'magenta'])
grafico_hist_cluster.mostrar('nombre_columna', bins=20, log=True, histtype='step')
```

### GraficoDeBarrasCluster

Extendiendo `GraficoCluster`, esta clase genera gráficos de barras con múltiples clústeres. Ordene las barras usando un DataFrame de orden.

```python
from plotterclassprogra.plotter import GraficoDeBarrasCluster

# Ejemplo de Uso
grafico_barras_cluster = GraficoDeBarrasCluster(datos)
grafico_barras_cluster.configurar_colores(['amarillo', 'verde'])
grafico_barras_cluster.mostrar('nombre_columna', order_df=None)
```

### GraficoDispersion

La clase `GraficoDispersion` crea gráficos de dispersión, permitiendo la visualización de dos variables numéricas coloreadas por una variable categórica.

```python
from plotterclassprogra.plotter import GraficoDispersion

# Ejemplo de Uso
grafico_dispersion = GraficoDispersion(datos)
grafico_dispersion.configurar_colores(['marrón', 'rosa'])
grafico_dispersion.mostrar('columna_x', 'columna_y', hue_col='columna_cluster')
```

Siéntase libre de personalizar y explorar diferentes configuraciones para cada clase de visualización. ¡Feliz visualización!
