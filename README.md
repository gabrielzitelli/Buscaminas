# TP Análisis de la Información: Buscaminas

Trabajo práctico de la materia Análisis de la Información de la Facultad de Ingeniería de la Universidad de Buenos Aires (FIUBA).

## Resumen

El proyecto consiste en el desarrollo del clásico juego de Buscaminas.

El juego contiene un tablero de NxM dimensiones, con K minas distribuídas de manera aleatoria sobre el mismo, el objetivo es marcar todas las minas y revelar todas las demás celdas. Las celdas que no contengan minas marcarán con un número cuántas minas se encuentran en las celdas adyacentes.

## Grupo

* **Integrante 1** - [Gabriel Zitelli](https://github.com/gabrielzitelli)
* **Integrante 2** - [Francisco Strambini](https://github.com/FranFiuba)
* **Integrante 3** - [Julio Piñango](https://github.com/julioPinango)
* **Integrante 4** - [Walter Mamani](https://github.com/wjma)
* **Integrante 5** - [Gian Keberlein](https://github.com/GianK128)

## Tecnologías

Para este proyecto se decidió usar [Python](https://www.python.org) 3.9+

En principio la interfaz gráfica se realizará en la terminal, de tener todo funcionando a término se sumará una interfaz gráfica utilizando [Pygame](https://www.pygame.org/tags/framework)


## Cómo correr el juego

El juego deberá ser lanzado desde una terminal tipeando:

> python buscaminas.py

## El juego y sus reglas

Buscaminas es un juego de computadora que se originó en la década de 1960 y se popularizó con la inclusión en el sistema operativo Windows. El objetivo del juego es despejar un campo de minas evitando detonar las mismas. El campo se representa como una cuadrícula de celdas cuadradas, algunas de las cuales contienen minas ocultas. El jugador hace clic en las celdas para descubrir qué hay debajo. Cada celda revela un número que indica la cantidad de minas adyacentes (en un radio de 1 casilla a la redonda). Utilizando esta información, el jugador debe deducir la ubicación de las minas y marcarlas con banderas.
El juego se basa en la lógica y la deducción, y los jugadores deben evitar hacer clic en celdas minadas. Hacer clic en una mina resulta en la pérdida del juego. El desafío radica en utilizar la información proporcionada por los números para tomar decisiones estratégicas y evitar las minas. El juego tiene diferentes niveles de dificultad, ajustando el tamaño del campo y la cantidad de minas para aumentar la complejidad. El objetivo final es revelar todas las celdas no minadas sin detonar ninguna mina, demostrando habilidad y paciencia.
