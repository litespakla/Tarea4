# Tarea4
# 1. Esquema de modulación BPSK
Se creó un esquema de modulación BPSK, el cual asigna una forma de onda sinusoidal a cada bit.

Para el caso de la modulación BPSK, esta onda es sin(2*pi*f) si el bit es 1 y -sin(2*pi*f) si el bit es 0. Se utilizaron 100 muestras. La onda portadora se puede observar en la imagen "onda_portadora5000Hz.png". Los primeros 5 bits de la señal modulada se pueden observar en la imagen "onda_modulada_5bits_5000Hz.png".

# 2. Potencia promedio de la señal modulada
La potencia promedio se calcula con la función "trapz". Se obtuvo una potencia promedio de 0.5 watts.

# 3. Canal ruidoso del tipo AWGN
Se creo una función, la cual recibe la relación señal a ruido deseada, y obtiene el sigma de la gaussiana que genera el ruido. Se utilizan SRN que van de los -15 dB a 5 dB.

El efecto del ruido en la señal modulada se puede observar en las imágenes "onda_ruido_5bits_5000Hz_nndb.png" donde nn es el SRN utilizado, el cual va de -15 dB a 5 dB.

# 4. Densidad de energía espectral
Se grafica la densidad de energía espectral antes y después de aplicar el canal ruidoso. Se aplica una escala doblemente logarítmica. Antes de aplicar el canal ruidoso ("PSD_sin_ruido_5000Hz.png"), se observa como el PSD es linealmente decreciente, lo que significa que la potencia de la señal se concentra principalmente a frecuencias bajas (periodos largos). Esto tiene sentido ya que la potencia de la señal va a ser muy baja a para periodos de tiempo muy cortos (frecuencias muy altas), que es exactamente lo que se observa en la figura.

Para los PSD de la señal ruidosa ("PSD_con_ruidoxxdB_5000Hz.png", donde xx es el SRN utilizado), se observa como conforme disminuye el SRN, la potencia espectral aumenta a altas frecuencias. Esto tiene sentido porque a menor SRN, mayor es el ruido que se le aplica a la senal. 

# 5. Demodulación de la señal
Se decodifica la señal. Para ello se multiplica la señal ruidosa por una señal de referencia, que en nuestro caso es la misma señal portadora. Entonces si el bit codificado es 1, en teoría se tiene un sin^2, de manera que la potencia de la señal debería ser 0,5 watt. Si el bit codificado es 0, entonces en teoría se tiene -sin^2, de manera que la potencia de la señal debería ser -0,5 watt. 

Entonces para decodificar la señal, se calcula la potencia para cada periodo y, si esta es positiva, se le asigna un 1 a la señal decodificada.

# 6. BER vs SRN
Se grafica BER vs SRN ("ber.png"), y se observa como la tasa de errores decae exponencialmente conforme se aumenta el SRN. Para el rango solicitado (-2 dB a 3 dB), no ocurrieron errores.
