# Elaboración de un SOC Doméstico (Homelab)
Proyecto final de Administración de Sistemas Informáticos en Red

**Índice**

1. [Introducción](#introducción)
2. [Objetivos](#objetivos)
3. [Descripción del proyecto](#descripción-del-proyecto)
4. [Hardware empleado](#hardware-empleado)
   1. [Equipo anfitrión](#equipo-anfitrión)
   2. [Router](#router)
5. [Aplicaciones utilizadas (EN DESARROLLO)](#aplicaciones-utilizadas)
   1. [Sistemas Operativos (EN DESARROLLO)](#sistemas-operativos)
   2. [Aplicaciones (EN DESARROLLO)](#aplicaciones)
6. [Diseño de red (EN DESARROLLO)](#diseño-de-red)
   1. [Topología](#topología)
   2. [Planteamiento de subredes](#planteamiento-de-subredes)
   3. [Tabla de direccionamiento (EN DESARROLLO)](#tabla-de-direccionamiento)
   4. [Ficheros de configuración (EN DESARROLLO)](#ficheros-de-configuración)
7. [Escenarios (EN DESARROLLO)](#escenarios)
8. [Licencia (EN DESARROLLO)](#licencia)
9. [To do List](#to-do-list)

---

# Introducción

¡Buenas! Soy Manuel Jesús Flores y soy estudiante de Administración de Sistemas Informáticos en Red.

Este repositorio contiene el proyecto integrado de dicho módulo y trata acerca de un homelab enfocado a seguridad, es decir, montar un centro de operaciones de seguridad en miniatura.

A lo largo del repositorio puedes encontrar los avances realizados y por donde va. Se admiten mejoras a través de los *issues* o *pull requests* pero seguramente se implemente una vez finalizado el proyecto. Para cualquier duda no dudes en abrirme un *issue* y te respondo en cuando pueda, ¡nos vemos!

# Objetivos
Es imposible negar que la seguridad se está convirtiendo a pasos cada vez mayores en un punto a reforzar tanto de empresas como de administraciones públicas pues, como se ha ido desarrollando a lo largo de la crisis mundial originada por el CoVid-19, varios hospitales extranjeros han sido infectados mediante un ransomware.

Este ataque se podía haber evitado o haber disminuido su gravedad si se contaran con expertos en seguridad informática y por ello, el objetivo principal de este proyecto es el crear un entorno desde cero de aprendizaje o de simulación de un centro de operaciones de seguridad (SOC) para poder adquirir habilidades tanto en seguridad como configuración de redes así como proporcionar un entorno seguro donde ejecutar malware conocido y saber que vulnerabilidades aprovecha para realizar su posterior explotación.

Para lograr este objetivo global se necesitan desarrollar y alcanzar objetivos individuales que se entrelazan entre sí. Los objetivos individuales o específicos del siguiente proyecto son:

* Configurar una red interna virtual donde incluir equipos clientes, servidores y dispositivos IoT.

* Entender los logs ofrecidos por aplicaciones acerca del tráfico generado por todos los dispositivos de la red.

* Desplegar un sistema que garantice la alta disponibilidad mediante aplicaciones de terceros con las que se pueda analizar el tráfico, el rendimiento y adaptar el funcionamiento del sistema según los valores devueltos.

* Conocer los diferentes factores de amenaza, saber analizarlos, enfrentarlos y adoptar medidas para evitar posibles nuevos ataques.

* Analizar las aplicaciones especializadas en el mercado e intentar, en la mayor medida posible, usar aplicaciones de software libre.

Finalmente, como objetivos opcionales se plantean los siguientes:

* Desarrollar un bot en Telegram que sea capaz de analizar los ficheros log del sistema y notificar al administrador del sistema.

# Descripción del proyecto

El proyecto “Elaboración de un SOC Doméstico” nace con la finalidad de, como se indicaba anteriormente, dar una solución de aprendizaje práctico a cualquier persona en el ámbito de la ciberseguridad sin necesidad de invertir una gran cantidad de capital en material (routers, switches, cableado, SAIs…) ya que se trabajará todo a través de la virtualización y, en la medida de lo posible, empleando aplicaciones de software libre aunque es cierto que en muchas empresas se aplican soluciones de software privativo que, en caso de ser necesarias, se usarán promociones de las empresas desarrolladoras que tienen para estudiantes del sector (principalmente el programa Github Students).

Las tecnologías que se van a usar, nombrando por encima, serán como sistemas operativos Ubuntu Server y Desktop, Metasploitable, Kali Linux y Windows Server 2019. Si hablamos de nivel de aplicación se va a usar PfSense, Metasploit Framework, Ettercap o Wireshark entre otros y, a nivel de metodología, se empleará una metodología que conocemos como Red&Blue Team. Esta metodología está en alza y la forman titulados en el campo de seguridad informática que tratarán de atacar (Red team) y defender (Blue team) el sistema de la empresa. Lo interesante de esta metodología es que, aplicándolo en un entorno real, un auditor es capaz de aprender desde ambos puntos de vista y, por tanto, poder proponer y ejecutar soluciones a medida al sistema administrado en cuestión.

# Hardware empleado

El proyecto se va a realizar entero en máquinas virtuales por lo que se necesitará dos equipos principales para el desarrollo de este proyecto. Dichos equipos son:

## Equipo anfitrión



## Router



# Diseño de red

## Topología

La topología de la red será jerárquica, es decir, tendremos un router principal (**HOME_ROUTER**) el cual se conectará al servidor de seguridad (**ZEUS**) que se encargará de filtrar los paquetes e implementar un servidor proxy.  **ZEUS** tendrá otra interfaz que se conectará a un switch (**CORE**) que dividirá entre DMZ (que se encontrará el servidor de acceso público (**HERACLES**) con servicios WEB y FTP) y la noDMZ que será donde se encuentren los hosts y dos tipos de servidores que son:

* Servidores de uso normal
  * Son servidores que se usan normalmente dentro de una empresa y que se encargan de albergar bases de datos, proporcionar un servicio de correo interno, un servicio de DNS interno y un servidor de copias de seguridad. Estos servidores son:
    * **ATENEA**: Servicios de correo interno, DNS interno y base de datos.
    * **TESEO**: Servicio de copias de seguridad.
* Servidor de aprendizaje de seguridad
  * Es un servidor crítico ya que contiene un sistema operativo (*metasploitable*) el cual cuenta con numerosas vulnerabilidades. Este servidor será **HADES**.

Por tanto, la topología final que se presenta es la siguiente:

<img src="/home/manuel/.config/Typora/typora-user-images/image-20200319144642031.png" alt="image-20200319144642031" style="zoom: 67%;" />

## Planteamiento de subredes

La red principal será la **192.168.1.0/24**.

Dada la topología anteriormente descrita se deberán crear las siguientes subredes:

| Nombre             | Equipos | Red              | Broadcast     |
| ------------------ | ------- | ---------------- | ------------- |
| noDMZ - USUARIOS   | 126     | 192.168.1.0/25   | 192.168.1.127 |
| DMZ                | 14      | 192.168.1.128/28 | 192.168.1.143 |
| noDMZ - SEGURIDAD  | 6       | 192.168.1.144/29 | 192.168.1.151 |
| ACCESO             | 2       | 192.168.1.152/30 | 192.168.1.155 |
| CORE               | 2       | 192.168.1.156/30 | 192.168.1.159 |
| noDMZ - SERVIDORES | 2       | 192.168.1.160/30 | 192.168.1.163 |

Además se deja un remante de 91 direcciones IP cuyo rango comprende desde la **192.168.1.164/24** a **192.168.1.255/24**.

   ## Tabla de direccionamiento
|   Device    |  Port  |  IP Address   | Mask |    Gateway    |
| :---------: | :----: | :-----------: | :--: | :-----------: |
| HOME_ROUTER | G0/0/1 | 192.168.1.153 |  29  |       -       |
|    ZEUS     |   G0   | 192.168.1.154 |  29  | 192.168.1.153 |
|             |   G1   | 192.168.1.157 |  30  | 192.168.1.153 |
|    CORE     | VLAN1  | 192.168.1.158 |  30  | 192.168.1.153 |
|  HERACLES   |  NIC   | 192.168.1.129 |  28  | 192.168.1.153 |
|   ATENEA    |  NIC   | 192.168.1.161 |  30  | 192.168.1.153 |
|    HADES    |  NIC   | 192.168.1.145 |  29  | 192.168.1.153 |
|    TESEO    |  NIC   | 192.168.1.162 |  30  | 192.168.1.153 |

   ## Ficheros de configuración

   Los ficheros de configuración se encuentran en [ficheros_cisco](./ficheros_cisco)