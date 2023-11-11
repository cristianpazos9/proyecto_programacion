import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class GraficoCluster:
    def __init__(self, datos):
        if datos.empty:
            raise ValueError("El DataFrame está vacío. Proporcione un DataFrame con datos.")
        self.datos = datos
        self.colores = None
        self.titulo = "Distribucion variable"
        self.figsize = (12, 4)

    def configurar_colores(self, colores):
        self.colores = colores

    def configurar_titulo(self, titulo):
        self.titulo = titulo

    def configurar_figsize(self, figsize):
        self.figsize = figsize

    def mostrar(self):
        pass

class GraficoHistograma(GraficoCluster):
    def mostrar(self, col, bins=10, log=False, histtype="bar"):
        fig, ax = plt.subplots(1, 1, constrained_layout=True, figsize=self.figsize)
        ax.hist(self.datos[col], bins=bins, range=(0, self.datos[col].max()), log=log, histtype=histtype, color=self.colores)
        ax.set_title(self.titulo)
        ax.set_xlabel(col)
        ax.set_ylabel("Recuento")
        plt.show()

class GraficoDeBarras(GraficoCluster):
    def mostrar(self, col, order_df=None):
        datosg = self.datos.groupby(by=col).size().reset_index().rename(columns={0: "Recuento"})
        if isinstance(order_df, pd.DataFrame):
            datosg = datosg.merge(order_df, on=col, how="left").sort_values(by="order")
        x_coor = np.arange(datosg.shape[0])
        height = datosg["Recuento"]
        x_labels = datosg[col]

        fig, ax = plt.subplots(1, 1, constrained_layout=True, figsize=self.figsize)
        ax.bar(x_coor, height, color=self.colores)
        ax.set_title(self.titulo)
        ax.set_xlabel(col)
        ax.set_ylabel("Recuento")
        ax.set_xticks(x_coor, x_labels, rotation=20, horizontalalignment="right")
        plt.show()

class GraficoHistogramaCluster(GraficoCluster):
    def mostrar(self, col, bins=20, log=False, histtype="step"):
        if 'cluster' not in self.datos.columns:
            raise ValueError("La columna 'cluster' no existe en el DataFrame.")

        datos = self.datos
        cluster_values = datos["cluster"].unique()
        n_clusters = datos["cluster"].nunique()
        min_ = datos[col].min()
        max_ = datos[col].max()

        # Ajustamos el número de subplots según el número de clusters
        plot_ncols = min(n_clusters, 3)
        plot_nrows = (n_clusters - 1) // plot_ncols + 1

        fig, ax = plt.subplots(plot_nrows, plot_ncols, constrained_layout=True, figsize=self.figsize)

        for n, subplot_ax in zip(cluster_values, ax.flatten()):
            # Dentro del hist van los colores
            subplot_ax.hist(datos.loc[datos["cluster"] == n, col], bins=bins, range=(min_, max_), log=log, histtype=histtype, density=True, color=self.colores)
            # Dentro del set title va el titulo
            subplot_ax.set_title(f"{self.titulo} - Cluster {n}")
            subplot_ax.set_xlabel(col)
            subplot_ax.set_ylabel("Density")

        plt.show()





class GraficoDeBarrasCluster(GraficoCluster):
    def mostrar(self, col, order_df=None):
        if 'cluster' not in self.datos.columns:
            raise ValueError("La columna 'cluster' no existe en el DataFrame.")

        datosg = self.datos.groupby(by=[col, "cluster"]).size().reset_index(name="Recuento")

        # Agregar las nuevas filas al DataFrame
        if order_df is not None:
            datosg = datosg.merge(order_df, on=col, how="left").sort_values(by="order")

        bar_width = 0.8
        n_groups = datosg[col].nunique()
        n_clusters = datosg["cluster"].nunique()
        bar_ind_width = bar_width / n_clusters
        x_coor_base = np.arange(n_groups)
        x_labels = datosg[col].unique()
        offset = bar_ind_width / 2

        groups_max = datosg.groupby(by=[col, "cluster"])["Recuento"].sum().reset_index().groupby(by=col)["Recuento"].max().reset_index()
        datosg = datosg.merge(groups_max, on=col, how="left", suffixes=('_current', '_max'))
        datosg["Porcentaje"] = datosg["Recuento_current"].div(datosg["Recuento_max"])

        fig, ax = plt.subplots(1, 2, constrained_layout=True, figsize=self.figsize)
        for n in range(n_clusters):
            x_coor = x_coor_base + offset - bar_width / 2
            height = datosg.loc[datosg["cluster"] == n, "Recuento_current"].values
            height_per = datosg.loc[datosg["cluster"] == n, "Porcentaje"].values

            ax[0].bar(x_coor, height, width=bar_ind_width, label="cluster " + str(n), color=self.colores)
            ax[1].bar(x_coor, height_per, width=bar_ind_width, label="cluster " + str(n), color=self.colores)

            offset += bar_ind_width

        ax[0].set_title(self.titulo)
        ax[0].set_xlabel(col)
        ax[0].set_ylabel("Recuento")
        ax[0].legend(loc='upper center')
        ax[0].set_xticks(x_coor_base, x_labels, rotation=20, horizontalalignment="right")

        ax[1].set_title(self.titulo)
        ax[1].set_xlabel(col)
        ax[1].set_ylabel("Porcentaje")
        ax[1].legend(loc='upper center', ncols=2)
        ax[1].set_xticks(x_coor_base, x_labels, rotation=20, horizontalalignment="right")

        plt.show()


class GraficoDispersion(GraficoCluster):
    def mostrar(self, x_col, y_col, hue_col="cluster"):
        fig, ax = plt.subplots(1, 1, constrained_layout=True, figsize=self.figsize)

        # Obtener colores únicos para cada cluster
        unique_colors = plt.cm.rainbow(np.linspace(0, 1, self.datos[hue_col].nunique()))

        # Crear un diccionario que mapea cluster a color
        color_map = {cluster: color for cluster, color in zip(self.datos[hue_col].unique(), unique_colors)}

        # Asignar color a cada punto según el cluster
        colors = self.datos[hue_col].map(color_map)

        # Crear el gráfico de dispersión
        scatter = ax.scatter(self.datos[x_col], self.datos[y_col], c=colors)

        # Crear leyenda con colores y etiquetas de cluster
        handles = [plt.Line2D([0], [0], marker='o', color='w', label=str(cluster),
                              markerfacecolor=color, markersize=10) for cluster, color in color_map.items()]
        ax.legend(handles=handles, title=hue_col)

        ax.set_title(self.titulo)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)

        plt.show()