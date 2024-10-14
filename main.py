import uasyncio as asyncio  # Reemplazar por `asyncio` si utiliza CircuitPython
# Reemplazar por `circuit_monitoring` si utiliza CircuitPython
import micro_monitoring

import machine as m
import time as t
import math
import network  #pt2



async def operations():
    
    global ant
    global prom
    global segcorridos, segcorridos2
    global actual
    global convertir_dB
    global num_3, num_6, num_8, num_0, num_nada
    global normal, alto, superior, normal_1, alto_1, superior_1, mediciones
    global activado
    # Definición de pines
    luz_sala = m.Pin(20, m.Pin.OUT)  # Luz LED que representa la luz de la sala.
    foco_puerta = m.ADC(m.Pin(27))   # Sensor de luz para captar la luz del foco al abrir la puerta.
    sonido = m.ADC(m.Pin(28))        # Sensor de sonido.

    # Pines para los segmentos del display (a, b, c, d, e, f, g)
    display_pins = (19, 18, 13, 15, 14, 16, 17)
    segments = [m.Pin(pin, m.Pin.OUT) for pin in display_pins]

    # Configuraciones para los números

    #b a c e d f g <- orden del arreglo 
    num_3 = [1, 1, 1, 0, 1, 0, 1]  
    num_6 = [0, 1, 1, 1, 1, 1, 1]  
    num_8 = [1, 1, 1, 1, 1, 1, 1]  
    num_0 = [1, 1, 1, 1, 1, 1, 0]  
    num_nada = [0, 0, 0, 0, 0, 0, 0]  # Nada encendido.
        ## funciones y procedimientos ##
    def mostrar_vol(number):
        for i, segment in enumerate(segments):
            segment.value(number[i])

    async def pausar_todo():
        global ant, actual, activado, prom, convertir_dB
        await asyncio.sleep (0.7)
        print("Entro alguien a la sala")
        ant = actual [0]
        activado = True
        convertir_dB (prom)
        luz_sala.on()
        total_segundos = 10
        await asyncio.sleep (0.7)
        print("Pelicula pausada, se reanudará en 10 segundos.")
        await asyncio.sleep (0.7)
        for segundos_restantes in range(total_segundos, 0, -1):
            print(f"Reanudando en {segundos_restantes} segundos...", end="\r")
            t.sleep(1)

        luz_sala.off()
        print("\n¡La película se está reanudando!")
        await asyncio.sleep (2)
        

    async def ir_avol(volumen, d,promedio,vol_act, segundos):
        vol = volumen
        global prom
        global segcorridos, segcorridos2
        global ant
        global normal, alto, superior, normal_2, alto_2, superior_2
        segcorridos = 0
        segcorridos2 = 0
        t.sleep (3)
        if actual [0] == 3 :
            actual1 = normal_2
            
        elif actual [0] == 6:
            actual1 = alto_2
            
        else:
            actual1 = superior_2
        print (f"Se detectó un constante ruido durante {segundos} segundos seguidos fuera del rango de [{actual1[1]} dB - {actual1[2]} dB] ")
        t.sleep (2)
        activado = False
        if d == "baja":
            print(f"Bajar el volumen a: {vol}")
        else:
            print(f"Subir el volumen a: {vol}")
        await asyncio.sleep (2)
        if volumen == 3:
            mostrar_vol(num_3)
            ant = 3
            await asyncio.sleep (1)
            return normal
        elif volumen == 6:
            mostrar_vol(num_6)
            ant = 6
            await asyncio.sleep (1)
            return alto
        else:
            mostrar_vol(num_8)
            ant = 8
            await asyncio.sleep (1)
            return superior
        
        



    def fin_pelicula():
        t.sleep (1.5)
        print("A los espectadores no les importa la película parece...")
        t.sleep(1)
        print("Prendemos las luces")
        t.sleep(2)
        luz_sala.on()
        t.sleep(2)
        print("Apagamos la tele")
        t.sleep(2)
        mostrar_vol(num_nada)
        return True
        

    def calibrar (info,sensor):
        calibracion = []
        for i in range (0,20) :  #para observar la calibracion
            if info == 1:
                sal = convertir_dB (sonido.read_u16())
                print (sonido.read_u16())
                print (f"Lectura numero {i+1}= {sal} dB")
                

            if sensor == 1:
                calibracion.append(sonido.read_u16())
            else:
                calibracion.append (foco_puerta.read_u16())
        
        return (sum (calibracion) // len (calibracion))

    def convertir_dB (volt):
        ent = convertir_volt (volt)
        result = (120.24 * (ent) - 132.86)  ## experimentacion con regresion lineal
        return (round (result , 1))

    def convertir_volt (analogico) :
        return ((analogico *3.3) / 65535)

    def fin_normal ():
        print ("Prendemos las luces")
        t.sleep(2)
        luz_sala.on()
        t.sleep(2)
        print ("Apagamos la television")
        t.sleep(2)
        mostrar_vol (num_nada)
        
        
    ##########################fin funciones y procedimientos #############################

    #volumen actual, valor bajo del rango, valor alto del rango
    normal = [3,33400,34500] 
    alto = [6,34501,36800]
    superior = [8,36801,38400]
    
   # rta = int (input ("Seleccione opcion \n1-Habitacion en silencio\n2-Biblioteca de la facu con un minimo bullicio\n>"))

    
        
    normal = [3,33400,34500] 
    alto = [6,34501,36800]
    superior = [8,36801,38400]
    """if rta == 2 :
        normal = [3,36200,37000] 
        alto = [6,37001,38800]
        superior = [8,38801,4000]"""
    normal_2 = [3,70,80] 
    alto_2 = [6,81,90]
    superior_2 = [8,91,98]

    mediciones = []

    # Inicio de la simulación
    luz_sala.on()
    print("Bienvenidos al CineOgata")

    t.sleep(1)
    mostrar_vol(num_0)
    mediciones_v = []

    print ("Primero veremos si el sensor de infrarrojo esta calibrado...")
    luz= calibrar (0,2)
    
    while luz < 55000:
        t.sleep (1)
        print ("Debe calibrar de nuevo el sensor KY-026")
        t.sleep (0.5)
        if luz < 55000:
            print ("Pruebe girando el tornillo en sentido antihorario")
        luz = calibrar (0,2)
    t.sleep (1)
    
    ## calibracion
    try:
        print ("Calibracion sensor KY-026 correcta")
        rta = int (input ("Desea arrancar la pelicula? \n1- SI \n2- NO \n>"))
        if rta == 1:
            print("Prendemos la televisión")
            t.sleep (1)
            pelicula = True
            print("Apagamos las luces...", end="\r")
            t.sleep(1)
            luz_sala.off()
            t.sleep(1)
            
            mostrar_vol(num_3)  # Volumen inicial.
            prom = 0
            print ("Mientras pasan los anuncions, veremos si el sensor de sonido esta calibrado, se le pide silencio al publico")
            rta = int (input ("Ver valores sensor de sonido? \n1- SI \n2- NO \n>" ))
            promcal= calibrar (rta,1)
            actual = normal
            print (normal)
            while promcal >= actual [2] or promcal <= actual [1]: #bucle se ejecuta hasta que el sensor este calibrado
                print ("Debe calibrar de nuevo el sensor KY-037")
                t.sleep (1)
                if promcal <= actual [1]:
                    print ("Pruebe girando el tornillo en sentido antihorario")
                else:
                    print ("Pruebe girando el tornillo en sentido horario")
                t.sleep (1)
                rta = int (input ("Ver valores sensor de sonido? \n1- SI \n2- NO \n>" ))
                promcal= calibrar (rta,1)
            
            dB = convertir_dB (promcal)



            print(f"Nivel de dB calibrado: {dB:.2f} dB, es correcto, indica que el publico esta en silencio, y el volumen en 3")
            t.sleep (2)
            print ("Pelicula -El Padrino- reproduciendose, disfrutela!")
            t.sleep (0.5)
            print ("Si en cualquier momento desea cortar con la pelicula, presione cualquier tecla del teclado")
            t.sleep (2)
            

            seg = 0
            segcorridos = 0
            segcorridos2 = 0
            actual = normal

            prom = 36000 
            ##IMPORTANTE = CALIBRACION SENSOR EN 33500 -34500 publico en silencio
            while pelicula and seg <= 360: ## 3 minutos de pelicula -> 3 horas de pelicula.
                mediciones = []
                band = False
                ## volumen
                if prom > actual [2]:
                    band = True
                    if actual [0] == 3: # mi volumen es normal
                        if segcorridos2 == 4:  #pasaron 4 segundos seguidos de que mi medicion supero al rango actual 
                            if prom > alto [2]: # si este rango supera al rango del alto lo mando a 8
                                actual = await ir_avol(8, "subir",prom, actual, segcorridos2)
                            
                        if segcorridos==  7: #pasaron 7 segundos seguidos de que mi medicion supero al rango actual 
                            if normal[2] <= prom <= superior [1] : #ste rango supera al valor normal pero es menor al superior
                                actual = await ir_avol(6, "subir",prom, actual, segcorridos)
                            
                    if actual [0] == 6:
                        if segcorridos == 7:
                            actual= await ir_avol(8, "subir",prom, actual, segcorridos)
                        
                    if actual [0] == 8:
                        if segcorridos == 7:
                            fin_pelicula ()
                            pelicula = False
                            break
                        
                if prom < actual [1] :
                    band = True
                    if actual [0] == 3:
                        pass
                    elif actual [0]==6:
                        if segcorridos == 1:
                            actual= await ir_avol(3, "baja",prom, actual, segcorridos)
                    else:
                        if segcorridos == 1:
                            actual = await ir_avol(6, "baja",prom,actual, segcorridos)
                    
                if not band:
                    segcorridos = 0
                    if actual [0] == 3:
                        segcorridos2 = 0
                            
                
                for i in range (0,10):  # 10 muestras en  en un segundo
                    valor_adc = sonido.read_u16 ()
                    if valor_adc <= 33000:
                        valor_adc = 34000

                    if valor_adc >= 36800:
                        valor_adc = valor_adc + 20000  

                    if valor_adc >= 34500 and valor_adc <= 36800:
                        valor_adc = valor_adc + 11000
                    
                    mediciones.append (valor_adc)

                """
                normal = [3,33400,34500] 
                alto = [6,34501,36800]
                superior = [8,36801,38400]
                """
                
                segcorridos += 1
                segcorridos2 += 1
                prom = (prom + (sum (mediciones)) // (len(mediciones))) // 2  #promedio de ruido
                
                
                
                # Sensor de movimiento
                sensor_foco = foco_puerta.read_u16() 
                if sensor_foco < 10000:
                    await pausar_todo()
                    print ("Pelicula reanudada", end= "\r")
            
                t.sleep(1)  # paso un segundo
                seg += 1
                print (f"Promedio {prom} ---- actual [{actual [1]} - {actual[2]}]")
                print (f"Segundos transcurridos {seg}")
                
            if seg > 360:    
                t.sleep (1)    
                print ("Fin de la  pelicula")
                fin_normal ()
                t.sleep (2)
                print ("La Cosa Nostra te agredece por ver su pelicula")
            
        else:
            print ("Que aburrido... ")
        t.sleep (0.5)
    except KeyboardInterrupt:
        print("\nInterrupción de teclado detectada. La pelicula se termina.")
        fin_normal()
        t.sleep (2)
        await asyncio.sleep(2)
    pass


def get_app_data():
    global actual, foco_puerta, prom, ant
 
    return {
        "volumen_actual": ant,  # El volumen actual (normal, alto o superior).
        "promedio_ruido": convertir_dB (prom),  # Promedio de las mediciones de ruido.
        "entro_alguien": activado
    }



async def main():
    # Funcionamiento del equipo y monitoreo con el maestro se ejecutan concurrentemente.
    await asyncio.gather(
        operations(),
        micro_monitoring.monitoring(get_app_data)   # Monitoreo del maestro
    )

asyncio.run(main())