# PoC Uso de OR-TOOLS

El Objetivo de este tutorial es aprender a resolver problemas de logística, mediante el uso de la libreria [OR-Tools](https://developers.google.com/optimization?hl=es-419).
Comenzando por problemas simples hasta problemas más complejos que involucren capacidades limitadas y restricciones horarias.

## Navegación por el tutorial

El proyecto está diseñado como una guía evolutiva donde la idea no es leer todo el código de golpe, sino seguir la construcción logica del modelo navegando entre los commits del repositorio.

Cada commit añade una complejidad extra respecto al paso anterior:

- Comenzaremos preparando los datos para usar la libreria.
- El siguiente paso será hacer un primer ejemplo, con múltiples vehículos.
- Luego iremos introduciendo distintas restricciones (peso, volumen, tiempo).

Para moverse entre las versiones, usaremos el comando `git checkout`


## Instalación de dependencias

1. Clonar el repositorio

```bash
git clone https://github.com/Trocha4/OR-TOOLS.git
```
```bash
cd OR-TOOLS
```

2. Instalar OR-Tools

```bash
pip install ortools
```

3. Instalar Geopy para obtener coordenadas

```bash
pip install geopy
```

4. Requests para el uso de OSRM

```bash
pip install requests
```

## Secciones del tutorial

#### Sección 0: Introducción al repositorio
* Comando : `git checkout paso-0`

#### Sección 1 Preparación de datos

* Comando : `git checkout paso-1`
* Foco: La libreria OR-Tools trabaja a partir de una matriz de distancias entre las direcciones dadas. En este paso aprenderemos a crear nuestra matriz de distancias.

#### Sección 2 Ejemplo Básico con 1 vehículo

* Comando : `git checkout paso-2`
* Foco: Creamos un ejemplo sencillo donde un solo vehículo debe recorrer múltiples destinos.
    