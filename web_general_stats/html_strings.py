# Avatar Image using a url
avatar1 ="https://www.w3schools.com/howto/img_avatar1.png"

intro = """
        # General Moodle Reports Analytics v1.0 (Analíticas generales de reportes de Moodle)
        Analíticas de aprendizaje de informes de Moodle en Python, para visualizarlos en web con 
        Streamlit (Learning analytics from Moodle reports in Python, web Vizualised with Streamlit)
        Este proyecto está en desarrollo y abierto a colaboración (This project is in development process 
        and is open to collaboration)
        ## Donde descargar los CSV 
        En la página principal del curso en Moodle, vaya al menú que aparece en la rueda dentada y 
        siga la ruta "Aún más/Informes/Registros", luego haga clic en "Conseguir estos registros" y 
        descarguelos como CSV.
        Este fichero .csv lo puede subir en este sitio para su análisis.
        ## Objetivo
        El objetivo de este proyecto es crear algoritmos, aplicaciones Web y otros servicios en 
        Python para analizar informes de Moodle (CSV) tanto generales como de actividades como 
        foros de discusión, de manera que un profesor que imparta un curso en Moodle y desee hacer 
        análisis de su curso, independientemente de si el servidor tenga plugins instalados para 
        esta función, pueda hacerlo utilizando los recursos libres que en este proyecto se brindan.
        Este proyecto está en desarrollo y está abierto a colaboración en Github: \
        https://github.com/ravellom/moodle-py 
        """

html_temp = """
        <div style="background-color:{};padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">Disease Mortality Prediction </h1>
        <h5 style="color:white;text-align:center;">Hepatitis B </h5>
        </div>
        """
result_temp ="""
        <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
        <h4 style="color:white;text-align:center;">Algorithm:: {}</h4>
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
        <br/>
        </div>
        """
descriptive_message_temp ="""
        <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
            <h3 style="text-align:justify;color:black;padding:10px">Definition</h3>
            <p>Description bla bla. descriptive_message TExto dde prueba</p>
        </div>
        """