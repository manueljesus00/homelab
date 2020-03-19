# Elaboración de un SOC Doméstico (Homelab)
Proyecto final de Administración de Sistemas Informáticos en Red

**Índice**

1. [Introducción](#introducción)
2. [Objetivos](#objetivos)
3. [Descripción del proyecto](#descripción-del-proyecto)
4. [Diseño de red (EN DESARROLLO)](#diseño-de-red)
   1. [Ficheros de configuración (EN DESARROLLO)](#ficheros-de-configuración)
   2. [Tabla de direccionamiento (EN DESARROLLO)](#tabla-de-direccionamiento)
5. [Aplicaciones utilizadas (EN DESARROLLO)](#aplicaciones-utilizadas)
   1. [Sistemas Operativos (EN DESARROLLO)](#sistemas-operativos)
   2. [Aplicaciones (EN DESARROLLO)](#aplicaciones)
6. [Escenarios (EN DESARROLLO)](#escenarios)
7. [Licencia (EN DESARROLLO)](#licencia)
8. [To do List](#to-do-list)

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

# Diseño de red
   ## Ficheros de configuración
   Los ficheros de configuración se encuentran en [ficheros_cisco](./ficheros_cisco)
   ## Tabla de direccionamiento
   EN DESARROLLO
