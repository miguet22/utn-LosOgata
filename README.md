# Laboratorio N°1 - Microcontroladores
## Grupo: Los Ogata
### INTEGRANTES:
+ Gomez, Marcelo.
+ Gomez, Christian.
+ Medina, Mariano.
+ Tourn, Miguel.


**Escenario**

Suponga que usted tiene un cine en casa y desea automatizar algunas funciones del mismo, para eso, se plantea la necesidad de un controlador tanto de volumen como de luces de la sala.
Al estar siendo reproducida la película, las voces de los espectadores deben estar calladas, por lo que no debería haber ruido de voces y las luces deberían estar apagadas, y el volumen se mantiene en un nivel normal, que es el volumen con el cual inicia una función de cine.
Los decibeles de las voces de los espectadores van fluctuando en ciertos rangos de decibeles, nunca van a quedar en un mismo rango, ya que el volumen de voces va subiendo y bajando respecto al tiempo que pasa.
El controlador realiza mediciones de los decibeles de las voces de manera constante y  tomando decisiones respecto del volumen de la película. Cabe destacar que la película originalmente inicia en un volumen de nivel normal.
+ Si el volumen está en un **nivel normal**, las decisiones a tomar son las siguientes.
    - Si las voces permanecen en un rango por debajo del volumen normal de la película, se mantiene el volumen en el filme.
    - Si las voces permanecen durante siete segundos seguidos en un rango por encima del volumen normal de la película, se sube el volumen del filme a un volumen alto.
    - Si las voces permanecen cuatro segundos seguidos en un rango por encima de el volumen alto de la película, se sube el volumen a un volumen superior.
+ Si el volumen se encuentra en un **nivel alto**, las decisiones a tomar serán las siguientes.
    - Si las voces se mantienen en un rango por debajo del volumen actual durante un segundo, se disminuye el volumen del filme a un rango anterior.
    - Si las voces permanecen en un mismo rango que el del volumen actual, el volumen se mantiene en el nivel actual.
    - Si las voces permanecen siete segundos seguidos un rango más alto que el volumen actual de la película, se sube el volumen a un volumen superior.
+ Si el volumen se encuentra en un **nivel superior**, las decisiones a tomar serán las siguientes.
    - Si las voces se mantienen en un rango por debajo del volumen actual, y permanecen un segundo en este rango, se disminuye el volumen del filme a un rango anterior.
    - Si las voces permanecen la mayor parte del tiempo en un rango igual al del volumen actual de la película, se mantiene  el volumen del filme.
    - Si las voces permanecen durante siete segundos seguidos en un rango más alto que el volumen actual de la película, esto significa que a los espectadores no les importa para nada la película, por lo que se pausa la película y se encienden las luces de la sala.


La otra función del controlador es la de manejar las luces de la sala, esto lo hace según las entradas de las personas a la sala de cine. Si se detecta que ingresa alguien, se debe pausar la película, encender las luces y darle diez segundos al espectador para que se acomode, para así luego reiniciar la película y apagar las luces. Cabe destacar que la puerta de entrada la sala, tiene un pequeño foco, cuando una persona entra, este foco se enciende, de esta manera el sensor detecta el encendido de esta luz.
Siempre que la película se pausa, las mediciones de volumen se cancelan, y una vez que se vuelve a iniciar el filme, las mediciones vuelven a ser tomadas.

> [!CAUTION]
> **LAS EXPERIMENTACIONES DE ESTE SIMULADOR FUERON REALIZADAS DENTRO DE UNA HABITACION EN COMPLETO SILENCIO, LAS CALIBRACIONES PUEDEN VARIAR SEGUN EL ESPACIO FISICO**
**DIAGRAMA DEL CIRCUITO**

![Diagrama del circuito](https://github.com/miguet22/utn-LosOgata/blob/main/LosOgata_DiagramaLab.jpg?raw=true)

**AÑO 2024**