#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pylab, math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import signal

#Esta funcion modula y decodifica una cadena de bits para cierto AWGN
def tarea4(P_ruido, frec, muestras, bits):

    #Onda portadora. Referencia para la demodulación
    tp=np.linspace(0, 1/frec, muestras, endpoint=False)
    seno=np.sin(2*np.pi*frec*tp)

    #Guardar figura de la onda
    pylab.plot(tp, seno)
    pylab.xlabel('t')
    pylab.ylabel('Amplitud')
    pylab.title('Onda Portadora')
    pylab.savefig('onda_portadora'+str(frec)+'Hz.png')
    pylab.close()

    #Señal modulada
    sig=[]
    for bit in bits:
        for sin in seno:
            sig.append((-1+2*bit)*sin)

    #Se grafican los primeros 5 bits de la onda modulada
    pylab.plot(sig[0:5*muestras])
    pylab.xlabel('t')
    pylab.ylabel('Amplitud')
    pylab.title('Onda modulada primeros 5 bits')
    pylab.savefig('onda_modulada_5bits_'+str(frec)+'Hz.png')
    pylab.close()

    #tiempo
    tiempo=np.linspace(0, len(bits)*(1/frec), muestras*len(bits), endpoint=False)

    #Densidad espectral antes del ruido
    freqs, psd = signal.welch(sig, frec*muestras)
    pylab.loglog(freqs, psd)
    pylab.title('PSD señal sin ruido')
    pylab.xlabel('Frecuencia')
    pylab.ylabel('Potencia')
    pylab.savefig('PSD_sin_ruido_'+str(frec)+'Hz.png')
    pylab.close()

    #Potencia promedio
    pot=frec*integrate.trapz([x**2 for x in sig], tiempo)/len(bits)

    #Relación señal a ruido
    sigma=math.sqrt(pot/(10**(P_ruido/10)))

    #Señal de ruido
    sig_ruido=[]
    ruido=np.random.normal(0, sigma, len(sig))
    for i in range(len(sig)):
        sig_ruido.append(sig[i]+ruido[i])

    #Se grafican los primeros 5 bits con el ruido
    pylab.plot(sig_ruido[0:5*muestras])
    pylab.xlabel('t')
    pylab.ylabel('Amplitud')
    pylab.title('Onda modulada primeros 5 bits con ruido blanco de ' + str(P_ruido) + 'dB')
    pylab.savefig('onda_ruido_5bits_'+str(frec)+'Hz_' +str(P_ruido)+'dB.png')
    pylab.close()

    #Densidad espectral después del ruido
    freqs, psd = signal.welch(sig_ruido, frec*muestras)
    pylab.loglog(freqs, psd)
    pylab.title('PSD con ruido blanco de '+ str(P_ruido) + 'dB')
    pylab.xlabel('Frecuencia')
    pylab.ylabel('Potencia')
    pylab.savefig('PSD_con_ruido'+str(P_ruido)+'dB_'+str(frec)+'Hz.png')
    pylab.close()

    #Demodulacion
    bits_dem=[]
    for i in range(len(bits)):
        E=frec*integrate.trapz(sig_ruido[i*muestras:(i+1)*muestras]*seno, tp)
        #print(Es, E)
        if E>0:
            bits_dem.append(1)
        else:
            bits_dem.append(0)

    #error
    error=0
    for i in range(len(bits)):
        error+=abs(bits[i]-bits_dem[i])

    return error/len(bits), bits_dem, pot

#Nombre del archivo que contiene los datos.
archivo='bits10k.csv'

#Abrimos el archivo de texto
datos = open(archivo, 'r')

#Se guarda cada dato como un entero en el vector bits
Bits=[]
for dato in datos:
    Bits.append(int(dato))

#Cerramos el archivo de texto
datos.close()

#Frecuencia en la portadora
f=5000

#Numero de muestras
m=100
ber, srn=[], []

#Se calcula la cantidad de errores de -15dB a 5dB
for i in range(-15, 6):
    BER, dem, Pot=tarea4(i, f, m, Bits)
    srn.append(i)
    ber.append(BER)

print('La potencia promedio es ', Pot, 'watts')

#Se grafiva SRN vs BER
pylab.plot(srn, ber)
pylab.xlabel('SNR (dB)')
pylab.ylabel('BER')
pylab.title('Cantidad de errores vs el nivel de ruido')
pylab.savefig('ber.png')
plt.show()
