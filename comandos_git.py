#Comandos para configurar nuestra identidad:

#git config --global user.name "nombre apellido"
#git config --global user.email "nombre@example.com"

#git init  Se usa una sola vez (crea una carpeta .git)


#Se usan cuando nosotros queramos:
#git status Muestra el estado del repo (archivos modificados, no agregados, etc.)
#git log Muestra el historial de commits

#Se repiten siempre que haya cambios:
#git add .  Agrega todos los archivos al repo
#git commit -m "mensaje"  Crea un commit con los archivos agregados (etiqueta de info)
#git push origin main Sube los cambios al repositorio remoto (Github, Gitlab, etc.)

#ramas:
#crear y movernos a rama nueva:
#git checkout -b "funciones-nuevas"

#movernos a rama existente:
#git checkout "main"

#ver ramas:
#git branch

#juntar ramas en main:
#git merge "funciones-nuevas"

#Clase 9
#Comenzamos con la instalacion de git, luego comenzamos colocando el nombre y email del proyecto actual
#Creamos la carpeta git
#hay distintos comandos para agregar, revisar el status y nombrar los cambios
#creamos un repositorio en github y los codigos de ese repositorio se colocan aqui en la terminal
#una vez que queramos subir lo que hemos hecho, lo mandamos al repositorio
#luego creamos una rama nueva, y procedemos a cerrarla tambien
#combinamos la rama nueva creada con la main
