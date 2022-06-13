# descargarCanciones 

##### Select Language
[English](#English)  

   * [Why](#why) 
   * [Disclaimer](#disclaimer)
   * [How to use the script](#how)
   * [Configuration for executing](#configuration)
    
[Español](#Spanish)  

   * [Por qué](#porque)
   * [Descargo de responsabilidad](#descargo)
   * [Cómo usar el script](#ejecutar)
   * [Configuración para ejecutar](#configuracion)

<a name="English"/>

# descargarCanciones - English

<a name="why"/>

## Why

My wedding is in a few months and the restaurant I'm celebrating, needs me to give them a usb drive with all the songs whose I want to party. 
So, after years of paying for Spotify subscription, i decided to use "my right to listen to music" with this little script after I've tryed to download it from all over internet and not been able to download any music.

<a name="disclaimer"/>

## Disclaimer

This script does not want to let people do any illegal actions, but to give them some tools to work with YouTube. 
Any illegal use of my script is not my responsibility.

<a name="how"/>

## How to use it

First, and logically, you need to have python installed.
Later, make sure you have pip installed.

To make sure you have all seted up, execute this two commands on a CDM

`pyton -version`

You should have an output like this

`Python 3.8.10`

Any version above this is also valid.

---

To make sure you have pip installed, try this command

`pip -V` (make sure the V is uppercase)

You should have an output like this. 

`pip 22.1.2 from (...)`

---

After this, you can install the two libraries needed with this two commands:

`pip install youtube_dl`

`pip install easygui`

`pip install colorama`

<a name="configuration"/>

## Configuration for executing

You'll need:
* One folder to save all your songs
* CSV file with any header, only one column and all the urls, listed and separated with \r\n

The csv file must have only 1 column and have a header with any name on it

The urls must have only the url to make it work

<a name="Spanish"/>

# descargarCanciones - Español

<a name="porque"/>

## Por qué

Me caso en unos meses y el restaurante donde vamos a celebrar el combite, me pedía un pincho usb para poder poner la música. 
Así que después de haber pagado durante años una suscripción a Spotify, decidí que podía descargarme toda la música por la que estoy pagando para este día, porque me pasé una tarde entera intentando descargar música de internet sin haberlo conseguido. 

<a name="descargo"/>

## Descargo de responsabilidad

Este script no pregente dejar a la gente hacer nada ilegal, sino darles herramientras para trabajar con YouTube.
Cualquier acción ilegal que se haga con este script no será mi responsabilidad.

<a name="ejecutar"/>

## Cómo ejecutar

Proimero, y lógicamente, necesitarás instalar python.
Después, asegurate de instalar pip

Para asegurarte de que todo está correcto, puedes ejecutar esto:

`pyton -version`

Deberías tener algo así

`Python 3.8.10`

Cualquier versión sobre esta, será válida

---

Para asegurarte de que tienes pip instalado, ejecuta este comando:

`pip -V` (asegurate de que la V es mayúscula)

Deberías ver algo así

`pip 22.1.2 from (...)`

---

Después de esto, ya puedes instalar las dos librerías necesarias para el programa con los siguientes comandos:

`pip install youtube_dl`

`pip install easygui`

`pip install colorama`

<a name="configuracion"/>

## Configuración para ejecutar

Necesitarás:
* Una carpeta para descargar todas tus canciones
* Un fichero CSV con una cabecera cualquiera y las canciones separadas por saltos de carro o \r\n

El fichero CSV debe tener únicamente una columna y esa columna solo contener las url

Las url únicamente pueden tener eso, no pueden tener otro valor

