# Agregado en esta versión

## Concepto
- Para que OR-Tools pueda conocer las distancias entre las direcciones, trabaja con una matriz de distancias.
- La matriz de distancias la vamos a obtener de una consulta a la api de [OSRM](https://project-osrm.org/docs/v26.5.0/http#table-service).
- Para el armado de la matriz de distancias, OSRM necesita las coordenadas de las ubicaciones en formato (longitud, latitud), para esto utilizamos la API de Geopy que nos permite obtener las coordenadas de una dirección.
- Además, damos un código que nos permite tanto leer como guardar direcciones junto a sus coordenadas en archivos .csv para evitar peticiones a la API de Geopy.