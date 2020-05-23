#!/bin/bash
# Función: Crear copias de seguridad mediante rsync a través de SSH tunneling
###################################################
## Nombre del fichero: backups.SH
## Ruta recomendada: /home/scripts/backups.SH
## Fecha creación: 13-Mayo-2020
## Fecha modificación: 17-Mayo-2020
## Equipo: TESEO
## Autor: Manuel Jesus Flores Montaño
## Github: @manueljesus00
## Twitter: @_manueljesus00
###################################################

# Establecer la variable 'fecha'
fecha=`date +%y-%m-%d-%H:%M`
# Ejecutar la copia de seguridad
# Solo copia los directorios personales
rsync -aav -e 'ssh -i /ssh_keys/atenea' -b --backup-dir = manuel@atenea.pasir1920.local:/home /backups/atenea/$fecha >> /backups/logs/atenea/$fecha.log
rsync -aav -e 'ssh -i /ssh_keys/heracles' -b --backup-dir = manuel@heracles.pasir1920.local:/home /backups/heracles/$fecha >> /backups/logs/heracles/$fecha.log