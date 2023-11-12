.. plotter clustering documentation master file, created by
   sphinx-quickstart on Thu Nov  9 16:29:23 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to plotter clustering's documentation!
==============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Funciones de la Biblioteca
==========================

GraficoCluster
--------------

.. autoclass:: plotterclassprogra.plotter.GraficoCluster
   :members:
   :undoc-members:
   :show-inheritance:

   El objeto `GraficoCluster` se utiliza para crear gráficos básicos y configurar opciones comunes.

   **Uso básico:**

   .. code-block:: python

      from plotterclassprogra.plotter import GraficoCluster

      # Crear instancia de GraficoCluster con datos
      grafico = GraficoCluster(datos)

      # Configurar colores
      grafico.configurar_colores(['#FF0000', '#00FF00', '#0000FF'])

      # Configurar título
      grafico.configurar_titulo("Distribución de la Variable")

      # Configurar tamaño de la figura
      grafico.configurar_figsize((12, 4))

      # Mostrar el gráfico
      grafico.mostrar()

GraficoHistograma
-----------------

.. autoclass:: plotterclassprogra.plotter.GraficoHistograma
   :members:
   :undoc-members:
   :show-inheritance:

   El objeto `GraficoHistograma` hereda de `GraficoCluster` y se utiliza para crear histogramas.

   **Uso básico:**

   .. code-block:: python

      from plotterclassprogra.plotter import GraficoHistograma

      # Crear instancia de GraficoHistograma con datos
      histograma = GraficoHistograma(datos)

      # Configurar colores
      histograma.configurar_colores(['#FF0000', '#00FF00', '#0000FF'])

      # Configurar título
      histograma.configurar_titulo("Histograma de la Variable")

      # Mostrar el histograma para una columna específica
      histograma.mostrar('nombre_de_la_columna')

GraficoDeBarras
---------------

.. autoclass:: plotterclassprogra.plotter.GraficoDeBarras
   :members:
   :undoc-members:
   :show-inheritance:

   El objeto `GraficoDeBarras` hereda de `GraficoCluster` y se utiliza para crear gráficos de barras.

   **Uso básico:**

   .. code-block:: python

      from plotterclassprogra.plotter import GraficoDeBarras

      # Crear instancia de GraficoDeBarras con datos
      grafico_barras = GraficoDeBarras(datos)

      # Configurar colores
      grafico_barras.configurar_colores(['#FF0000', '#00FF00', '#0000FF'])

      # Configurar título
      grafico_barras.configurar_titulo("Gráfico de Barras de la Variable")

      # Mostrar el gráfico de barras para una columna específica
      grafico_barras.mostrar('nombre_de_la_columna')

GraficoHistogramaCluster
------------------------

.. autoclass:: plotterclassprogra.plotter.GraficoHistogramaCluster
   :members:
   :undoc-members:
   :show-inheritance:

   El objeto `GraficoHistogramaCluster` hereda de `GraficoCluster` y se utiliza para crear histogramas agrupados por cluster.

   **Uso básico:**

   .. code-block:: python

      from plotterclassprogra.plotter import GraficoHistogramaCluster

      # Crear instancia de GraficoHistogramaCluster con datos
      histograma_cluster = GraficoHistogramaCluster(datos)

      # Configurar colores
      histograma_cluster.configurar_colores(['#FF0000', '#00FF00', '#0000FF'])

      # Configurar título
      histograma_cluster.configurar_titulo("Histograma por Cluster de la Variable")

      # Mostrar el histograma para una columna específica y agrupado por cluster
      histograma_cluster.mostrar('nombre_de_la_columna')

GraficoDeBarrasCluster
----------------------

.. autoclass:: plotterclassprogra.plotter.GraficoDeBarrasCluster
   :members:
   :undoc-members:
   :show-inheritance:

   El objeto `GraficoDeBarrasCluster` hereda de `GraficoCluster` y se utiliza para crear gráficos de barras agrupados por cluster.

   **Uso básico:**

   .. code-block:: python

      from plotterclassprogra.plotter import GraficoDeBarrasCluster

      # Crear instancia de GraficoDeBarrasCluster con datos
      grafico_barras_cluster = GraficoDeBarrasCluster(datos)

      # Configurar colores
      grafico_barras_cluster.configurar_colores(['#FF0000', '#00FF00', '#0000FF'])

      # Configurar título
      grafico_barras_cluster.configurar_titulo("Gráfico de Barras por Cluster de la Variable")

      # Mostrar el gráfico de barras para una columna específica y agrupado por cluster
      grafico_barras_cluster.mostrar('nombre_de_la_columna')

GraficoDispersion
-----------------

.. autoclass:: plotterclassprogra.plotter.GraficoDispersion
   :members:
   :undoc-members:
   :show-inheritance:

   El objeto `GraficoDispersion` hereda de `GraficoCluster` y se utiliza para crear gráficos de dispersión.

   **Uso básico:**

   .. code-block:: python

      from plotterclassprogra.plotter import GraficoDispersion

      # Crear instancia de GraficoDispersion con datos
      scatter_plot = GraficoDispersion(datos)

      # Configurar colores
      scatter_plot.configurar_colores(['#FF0000', '#00FF00', '#0000FF'])

      # Configurar título
      scatter_plot.configurar_titulo("Gráfico de Dispersión")

      # Mostrar el gráfico de dispersión para dos columnas, con opcional agrupación por cluster
      scatter_plot.mostrar('columna_x', 'columna_y', hue_col='cluster')




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
