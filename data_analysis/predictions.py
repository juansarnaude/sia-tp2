import plotly.graph_objects as go
import sys

from utils.Config import Config
from genetic_algorithm import genetic_algorithm

import random

if __name__ == "__main__":

    random.seed(4567)

    config1: Config = Config("./config/config.json")
    config2: Config = Config("./config/config2.json")

    generations1 = genetic_algorithm(config1)
    generations2 = genetic_algorithm(config2)

    # Calcular el mejor fitness y el promedio de fitness de la última generación
    best_fitness_prediccion = round(max(generations1[-1]).fitness, 2)
    best_fitness_mejor_config = round(max(generations2[-1]).fitness, 2)

    avg_fitness_prediccion = round(sum([ind.fitness for ind in generations1[-1]]) / len(generations1[-1]), 2)
    avg_fitness_mejor_config = round(sum([ind.fitness for ind in generations2[-1]]) / len(generations2[-1]), 2)

    # Datos
    categorias = ['Predicción', 'Mejor configuración']
    cantidad_generaciones = [len(generations1), len(generations2)]
    promedio_fitness = [avg_fitness_prediccion, avg_fitness_mejor_config]
    mejor_fitness = [best_fitness_prediccion, best_fitness_mejor_config]

    # Configuración de estilo general para el texto
    text_style = dict(size=20, family="Arial", color="black")
    number_style = dict(size=18, color="white")  # Color de los números cambiado a blanco

    # Gráfico 1: Cantidad de generaciones
    fig1 = go.Figure(data=[
        go.Bar(x=categorias, y=cantidad_generaciones, text=cantidad_generaciones, textposition='auto', textfont=number_style)
    ])

    fig1.update_layout(
        title=dict(text='Comparación de la cantidad de generaciones', font=text_style),
        xaxis_title=dict(text='Configuración', font=text_style),
        yaxis_title=dict(text='Cantidad de generaciones', font=text_style),
        xaxis=dict(tickfont=text_style),
        yaxis=dict(tickfont=text_style),
        showlegend=False
    )

    # Mostrar el gráfico de cantidad de generaciones
    fig1.show()

    # Gráfico 2: Promedio de fitness de la última generación
    fig2 = go.Figure(data=[
        go.Bar(x=categorias, y=promedio_fitness, text=promedio_fitness, textposition='auto', textfont=number_style)
    ])

    fig2.update_layout(
        title=dict(text='Comparación del promedio de fitness en la última generación', font=text_style),
        xaxis_title=dict(text='Configuración', font=text_style),
        yaxis_title=dict(text='Promedio de fitness', font=text_style),
        xaxis=dict(tickfont=text_style),
        yaxis=dict(tickfont=text_style),
        showlegend=False
    )

    # Mostrar el gráfico del promedio de fitness
    fig2.show()

    # Gráfico 3: Mejor fitness de la última generación
    fig3 = go.Figure(data=[
        go.Bar(x=categorias, y=mejor_fitness, text=mejor_fitness, textposition='auto', textfont=number_style)
    ])

    fig3.update_layout(
        title=dict(text='Comparación del mejor fitness obtenido', font=text_style),
        xaxis_title=dict(text='Configuración', font=text_style),
        yaxis_title=dict(text='Mejor fitness', font=text_style),
        xaxis=dict(tickfont=text_style),
        yaxis=dict(tickfont=text_style),
        showlegend=False
    )

    # Mostrar el gráfico del mejor fitness
    fig3.show()



