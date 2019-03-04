# Contador Binario 0 a 4
Para compender el uso de los pines de una Raspberry Pi, se realizó un contador binario para remplazar el DIP Switch utilizado en el proyecto 2 de la clase de Organización de Computadoras y Assembler de la Universidad del Valle de guatemala, donde nos toco realizar el tema número 14

#### Proyecto 2: Convertidor binario a letras vocales
Diseñar y simular un circuito que muestre las vocales A, E, I, O, U. Un número binario de 3 bits representa cada vocal y se representará usando un **dip-switch** y la vocal será representada mediante una pantalla LED de 7 segmentos.

**NOTA:** No pueden utilizarse el integrado SN74LS47 o SN74LS48 para la conversión de binario a 7 segmentos.

## Scritp Python al iniciar la Raspberry Pi
El sistema operativo que se esta utilizando en la Raspberry Pi es [Raspbian](https://www.raspberrypi.org/downloads/raspbian/), por lo que realizaremos los siguientes pasos para que nuestro script de Python pueda ejecutarse al cargar el sistema operativo.

1. Ejecutamos el siguiente comando en nuestra Terminal de Raspbian, como super usuario, para copiar el archivo. O podemos crearlo y escribir el script 

```bash
# cp _path-ubicación-archivo_/cbinario-init /etc/init.d/
```

2. Se da permiso de ejecución a nuestro archivo con el siguiente comando

```bash
# chmod 755 /etc/init.d/cbinario-init
```

3. Para verificar si los cambios fueron realizados de forma correcta, ejecutamos nuestro archivo cbinario-init, con el siguiente comando:

```bash
# /etc/init.d/detector-init start
```
4. Al estar funcionando nuestro script, procedemos a agregarlo al archivo para que se ejecute al cargar el sistema operativo

```bash
# update-rc.d detector-init defaults
```

Al momento de que se reinicie, o se apague y se encienda nuestra Raspberry Pi, nuestro script de Python sera ejecutado al cargar el sistema operativo

## Configuración de Pines

![Pines de Raspberry Pi](/img/headers.png)

## Prerequisitos

* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)
* [Raspberry Pi B+](https://www.raspberrypi.org/products/raspberry-pi-1-model-b-plus/)

## Autores

* **Pablo Sao** - [psao](https://github.com/psao)
* **Mirka Monzón** - [mirkanicolle](https://github.com/mirkanicolle)
