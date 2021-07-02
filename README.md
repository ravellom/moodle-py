# General Moodle Reports Analytics (Analiticas de reportes de Moodle generales)
## Analíticas de aprendizaje de informes de Moodle en Python, para visualizarlos en web con Streamlit (Learning analytics from Moodle reports in Python, web Vizualised with Streamlit)
Este proyecto está en desarrollo y abierto a colaboración (This project is in development process and is open to collaboration)
Desarrollado por:
Raidell Avello Martínez, Profesor Titular, Dpto. de Tecnología Educativa e Informática.
Coordinador del Grupo de Investigación sobre Tecnologías EMergentes para el Aprendizaje (GITEM@) https://gitema.ucf.edu.cu/
Universidad de Cienfuegos, Cuba.

## Donde descargar los CSV 
En la página principal del curso en Moodle, vaya al menú que aparece en la rueda dentada y siga la ruta "Aún más/Informes/Registros", luego haga clic en "Conseguir estos registros" y descarguelos como CSV.
Este fichero .csv lo puede subir en este sitio para su análisis.
## Estructura del fichero CSV descargado
Data columns (total 9 columns):
 #   Column                       Non-Null Count  Dtype 
---  ------                       --------------  ----- 
 0   Hora                         25948 non-null  object
 1   Nombre completo del usuario  25948 non-null  object
 2   Usuario afectado             25948 non-null  object
 3   Contexto del evento          25948 non-null  object
 4   Componente                   25948 non-null  object
 5   Nombre evento                25948 non-null  object
 6   Descripción                  25948 non-null  object
 7   Origen                       25948 non-null  object
 8   Dirección IP                 25948 non-null  object
 En la aplicación se modifican los nombres de columnas para evitar espacios:
     df = df.rename(columns={
                    'Hora': 'DT',
                    'Nombre completo del usuario': 'Name',
                    'Usuario afectado': 'User_afec',
                    'Contexto del evento': 'Context',
                    'Componente': 'Component',
                    'Nombre evento': 'Event',
                    'Descripción': 'Description',
                    'Origen': 'Origen',
                    'Dirección IP': 'IP',
                })
## Objetivo
El objetivo de este proyecto es crear algoritmos, aplicaciones Web y otros servicios en Python para analizar informes de Moodle (CSV) tanto generales como de actividades como foros de discusión, de manera que un profesor que imparta un curso en Moodle y desee hacer análisis de su curso, independientemente de si el servidor tenga plugins instalados para esta función, pueda hacerlo utilizando los recursos libres que en este proyecto se brindan.
Inicialmente está en desarrollo la aplicación de estadísticas generales:
## Estadísticas Generales
Puede ver la última versión web en (Can see the last web version at): https://moodle-py.herokuapp.com/
Esta aplicación pretende responder las siguientes preguntas:
-	¿Cuáles son las actividades más accedidas?
-	¿Cuáles son las horas de mayor acceso al curso?
-	¿Cuáles estudiantes accedieron con mayor frecuencia al curso?
-	…
Se aceptan sugerencias y colaboración en su desarrollo
## Análisis de participación en los foros
Esta aplicación analizará los reportes descargados de un foro de discusión y pretende responder las siguientes preguntas:
-	¿Cuáles estudiantes y profesores iniciaron más debates?
-	¿Cuáles estudiantes y profesores respondieron con más frecuencia a otros estudiantes?
-	¿Cuáles fueron los temas de mayor actividad?
-	¿Cuáles fueron las frases más usadas por los participantes?
-	¿Qué tipo de intervención fue más frecuente? 
-	…
Se aceptan sugerencias y colaboración en su desarrollo

Desarrollado por: 
