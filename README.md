# Elaboración de un SOC Doméstico (Homelab)
Proyecto final de Administración de Sistemas Informáticos en Red

**Índice**

1. [Introducción](#introducción)
2. [Objetivos](#objetivos)
3. [Descripción del proyecto](#descripción-del-proyecto)
4. [Hardware empleado](#hardware-empleado)
   1. [Equipo anfitrión](#equipo-anfitrión)
   2. [Router](#router)
   3. [Otros elementos](#otros-elementos)
5. [Aplicaciones utilizadas](#aplicaciones-utilizadas)
   1. [Sistemas Operativos](#sistemas-operativos)
   2. [Aplicaciones](#aplicaciones)
6. [Diseño de red](#diseño-de-red)
   1. [Topología](#topología)
   2. [Planteamiento de subredes](#planteamiento-de-subredes)
   3. [Tabla de direccionamiento](#tabla-de-direccionamiento)
   4. [Ficheros de configuración (EN DESARROLLO)](#ficheros-de-configuración)
7. [Despliegue del homelab](#despliegue-del-homelab)
   1. [Configuración de hardware de las máquinas virtuales](#configuración-de-hardware-de-las-máquinas-virtuales)
8. [Escenarios (EN DESARROLLO)](#escenarios)
9. [Licencia (EN DESARROLLO)](#licencia)

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

El equipo anfitrión es un portátil MSI GP73 Leopard de 17,3''. Las características técnicas son:

* Procesador Intel Core i7-8750H
* Tarjeta gráfica NVIDIA GeForce GTX1060 6GB
* Un disco duro HDD de 1TB y un disco duro SSD de 256GB
* Conexión WLAN de 2.4GHz y 5GHz, BlueTooth y un puerto LAN de 1GB/s

El enlace del portátil es el siguiente (https://es.msi.com/Laptop/GP73-Leopard-8RD)

<img src="https://asset.msi.com/resize/image/global/product/product_10_20180212162153_5a814ea172445.png62405b38c58fe0f07fcef2367d8a9ba1/1024.png" style="zoom: 33%;" />

## Router

El router usado es un router LiveBox+ suministrado por Orange. El modelo exacto es Arcadyan R02. Las características técnicas son:

* Modo de operación FTTH (a través de puerto Gigabit Ehternet WAN)
* 3 puertos RJ45 Gigabit Ethernet
* 2 puertos RJ11 para telefonía
* 1 puerto USB 2.0 tipo A
* Wi-Fi de Doble Banda 11ac y 11n

![](https://s.cexfactory.net/p/ayuda/images/orange/4/9/2849_botones-livebox-plus-1.png)

## Otros elementos

A parte de estos dos elementos principales contamos con los siguientes elementos complementarios que mejoran el desarrollo del proyecto:

*AVISO: Estos elementos no son necesarios para el funcionamiento del proyecto.*

* Pantalla AOC de 32''
* Pantalla ASUS de 20''
* SmartTV Hitachi
* Repetidor TP-Link Range Extender RE300
* Telefono móvil Huawei P Smart 2019

# Aplicaciones utilizadas

Las aplicaciones utilizadas se van a dividir en dos categorías que son las propias aplicaciones y los sistemas operativos empleados.

## Sistemas Operativos

* Microsoft Windows 10 versión Home de 64 bits.

  * Este sistema será el usado en el equipo anfitrión para la virtualización.
  * URL: https://www.microsoft.com/es-es/windows
* Ubuntu Server 18.04.4. LTS.

  * Este sistema será el principal que contendrá todos los servidores a excepción de **HADES**, **TESEO** y **ZEUS**. No contiene interfaz gráfica.
  * URL: https://ubuntu.com/download/server
* Kali Linux 2020.1b.

  * Este sistema operativo se compone de una suite de herramientas para realizar labores de pentesting y auditorías de red&blue team.
  * URL: https://www.kali.org/downloads/
* Metasploitable 2.0.

  * Este sistema operativo desarrollado por Rapid7 y basado en Linux está diseñado para que sea lo más vulnerable posible y poder entrenar a cualquier usuario en las técnicas de seguridad informática. Se aplicará en el servidor **HADES**.
  * URL: https://metasploit.help.rapid7.com/docs/metasploitable-2
* pfSense

  * Este sistema operativo es una distribución basada en FreeBSD para ser usado como firewall y router. Se controla a través de una interfaz web. Se aplicará en el servidor **ZEUS**.
  * URL: https://www.pfsense.org/

## Aplicaciones

Las aplicaciones que vamos a usar son:

* Visual Studio Code
  * Entorno de programación desarrollado por Microsoft.
  * URL: https://code.visualstudio.com/
* VMware Workstation 15
  * Entorno de virtualización en el que ejecutaremos las máquinas virtuales.
  * URL: https://www.vmware.com/es/products/workstation-pro.html
* Packet Tracert
  * Simulador de redes de Cisco Systems
  * URL: https://www.netacad.com/es/courses/packet-tracer
* nmap y zenmap
  * Escáner de red y puertos. Viene por defecto en Kali Linux. NMAP corresponde a la aplicación en sí y ZENMAP corresponde a la interfaz gráfica.
  * URL: https://nmap.org
* Wireshark
  * Sniffer de red para capturar y analizar el tráfico. Viene por defecto en Kali Linux.
  * URL: https://www.wireshark.org
* Metasploit Framework
  * Framework desarrollado por Rapid7 que permite detectar vulnerabilidades y explotarlas. Viene por defecto en Kali Linux.
  * URL: https://www.metasploit.com
