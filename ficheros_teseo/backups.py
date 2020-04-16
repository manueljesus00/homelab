# Función: Crear copias de seguridad mediante rsync a través de SSH tunneling
###################################################
## Nombre del fichero: backups.py
## Ruta recomendada: /home/scripts/backups.py
## Fecha creación: 12-Abril-2020
## Equipo: TESEO
## Autor: Manuel Jesus Flores Montaño
## Github: @manueljesus00
## Twitter: @_manueljesus00
###################################################
import os
from datetime import date
# Creamos la variable para nombrar la carpeta con la fecha del backup en que se realiza
bk_date = date.today()
# Formateamos la fecha para concatenarla
new_bk_date = bk_date.strftime('%Y-%m-%d')
# Definimos el comando de rsync
command = "rsync -Pav -e 'ssh -i /ssh_keys/atenea' manuel@atenea.pasir1920.local:/home /backups/atenea/"
# Definimos el comando del backup
bk_command = ("tar -zcvf /backups/atenea/"+new_bk_date +".tar /backups/atenea/"+new_bk_date)
final_command = (command+new_bk_date+"/.")


# Una vez se haya comprobado que existe el directorio ATENEA y el directorio con
# la fecha de la copia de seguridad, se realiza la copia de seguridad
def ejecuta_comando(comando):
    os.system(comando)
    print("[+] Copia de seguridad realizada correctamente.")
    print("[/] Creando archivo comprimido...")
    os.system(bk_command)
    print("[+] Se ha comprimido el backup correctamente.")

# Comprueba que, una vez existiendo el directorio ATENEA, exista el directorio con
# la fecha de cuando se crea la copia de seguridad


def comprueba_actual(fecha):
    if os.path.isdir('/backups/atenea/'+fecha):
        ejecuta_comando(final_command)
    else:
        print("[!] No existe el directorio para el dia de hoy. Creando directorio...")
        os.mkdir('/backups/atenea/'+fecha)
        print("[+] Directorio creado con exito.")
        comprueba_actual(fecha)

# Comprueba si el directorio existe


def comprueba_directorio():
    if os.path.isdir('/backups/atenea'):
        comprueba_actual(new_bk_date)
    else:
        print("[!] No existe el directorio de ATENEA. Creando directorio...")
        os.mkdir('/backups/atenea')
        print("[+] Directorio creado con exito.")
        comprueba_directorio()


# Comenzamos a ejecutar el script
if __name__ == "__main__":
    comprueba_directorio()
