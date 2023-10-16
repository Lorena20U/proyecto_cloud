from flask import Flask, render_template, request, url_for, redirect, session
from jinja2 import Template, FileSystemLoader, Environment
import mysql.connector
from correos import sender
import os

app = Flask(__name__)
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)
app.secret_key = "key"
conn = ""
creador = {}
proyecto_actual = {}

def openConnection():
    global conn
    # conn = mysql.connector.connect(host="localhost",user="root",password="",database="co-co")
    conn = mysql.connector.connect(
        # host="localhost",  # local
        host = os.environ['DB_HOST'], # contenedor
        user = os.environ['DB_USER'],
        password = os.environ['DB_PASSWORD'],
        # password="",
        database = os.environ['DB_NAME']
        # host = 'database-1.c9yjy3nmd8az.us-east-1.rds.amazonaws.com', # contenedor
        # user = 'proyectocoandco',
        # password = 'hola1234',
        # database = 'coandco'
    )

def verificar_credenciales(email, password):
    openConnection()
    global conn
    cursor = conn.cursor()
    select_query = "SELECT id FROM usuario WHERE mail = %s AND password = %s"
    cursor.execute(select_query, (email, password))
    id_u = cursor.fetchone()[0]
    conn.close()
    return id_u

@app.route("/")
def homePage():
    return render_template("HomePage.html")

@app.route("/signUp", methods = ["GET", "POST"])
def signup():
    if(request.method == "POST"):
        global creador
        creador = {}
        name = request.form['name']
        last_name = request.form['l_name']
        e_mail = request.form['email']
        password = request.form['password']
        # Atributos no pedidos en la página aún.
        celphone = request.form['cel']
        date_birth = request.form['birth_date']

        creador['name'] = name
        creador['last_name'] = last_name
        creador['e_mail'] = e_mail
        creador['celphone'] = celphone
        

        if name and last_name and e_mail and password and celphone and date_birth:
            #newUser = Usuario(carnet, name, last_name, e_mail, celphone, carrera, semester, date_birth, password)
            openConnection()
            global conn
            cursor = conn.cursor()
            selectquery = "SELECT * FROM usuario"
            cursor.execute(selectquery)
            records = cursor.fetchall()
            bandera = 1
            #print("entre al if grande")
            for row in records:
                print(row[0])
                print(type(row[0]))
                if(row[0] == e_mail):
                    print("entre al if grande")
                    bandera = 0
                    break
            #print(f"bandera: {bandera}")
            if(bandera == 0):
                print("warning")
                #warning
                pass
            else:
                #insert
                print(bandera)
                inquery = "INSERT INTO `usuario`(`id`, `nombre`, `apellido`, `mail`, `tel`, `birth`, `password`) VALUES (NULL,%s,%s,%s,%s,%s,%s)"
                cursor.execute(inquery, (name, last_name, e_mail, celphone, date_birth, password))
                conn.commit()

                selectquery = "SELECT id FROM usuario WHERE mail = %s"
                print(selectquery)
                cursor.execute(selectquery, (e_mail,))
                id_u = -1
                id_u = cursor.fetchone()
                print(id_u)
            cursor.close()
            conn.close()
            return redirect(url_for('autenticacion',id_u = id_u, bandera = 0), 301)
    csss = url_for('static', filename="style.css")
    logo = url_for('static', filename="logo.png")
    return render_template("sign_up.html", csss = csss, logo=logo)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("correo", "")
        password = request.form.get("password", "")
        id_u = verificar_credenciales(email, password)
        print("Esto es el idddddd")
        print(id_u)
        if id_u != None:
            print("entreeeeeee")
            session['Logged_in'] = id_u
            return redirect("/usuario", code=301)
        else:
            return redirect("/signup", code=301)
    return render_template("signup.html")

@app.route("/autenticacion")
def autenticacion():
    session['Logged_in'] = request.args.get('id_u')
    id_u = request.args.get('id_u')
    bandera = int(request.args.get('bandera'))
    if bandera == 0:
        print("usuario conectado: " + str(session['Logged_in']))
        return redirect("/especialidades", 301)
    else:
        return redirect("/usuario", 301)

@app.route("/especialidades", methods = ["GET", "POST"])
def especialidades():
    lista_intereses = []
    if(request.method == "POST"):

        if request.form.getlist('1'):
            lista_intereses.append(1)
        if request.form.getlist('2'):
            lista_intereses.append(2)
        if request.form.getlist('3'):
            lista_intereses.append(3)
        if request.form.getlist('4'):
            lista_intereses.append(4)
        if request.form.getlist('5'):
            lista_intereses.append(5)
        if request.form.getlist('6'):
            lista_intereses.append(6)

        print(lista_intereses)
        #tenemos que recibir los checkboxs  y convertirlos a int o bool en base a si fue o no seleccionado.
        #en estas variables: progra, dise, est_m, camp_p, mate, circu
        #--------------------conexión base de datos
        #insert in tags despues del post de los checkbox, necesito que esten en una lista las que si marco el usuario

        openConnection()
        global conn
        cursor = conn.cursor()
        if "Logged_in" in session:
            Logged_in = session["Logged_in"]
        for var in lista_intereses:
            query = "INSERT INTO `tag`(`id_u`, `tag_t`) VALUES (%s,%s)"
            cursor.execute(query, (Logged_in, var))
            conn.commit()
        conn.close()

        return redirect("/usuario")

    arqui = url_for('static', filename="arqui.jpg")
    med = url_for('static', filename="med.jpg")
    return render_template("especialidades.html", arqui = arqui, med = med)


@app.route("/usuario", methods = ["GET", "POST"])
def usuario():
    openConnection()
    global conn
    if "Logged_in" in session:
        Logged_in = session["Logged_in"]
    print(Logged_in)
    cursor = conn.cursor()
    query = "SELECT usuario.id, usuario.nombre, usuario.apellido, usuario.mail, usuario.tel, usuario.birth FROM usuario WHERE usuario.id = %s"
    adr = (str(Logged_in), )
    cursor.execute(query, adr)
    datos = cursor.fetchall()
    user = {}
    for row in datos:
        user['carne'] = row[0]
        user['nombre'] = row[1]
        user['apellido'] = row[2]
        user['mail'] = row[3]
        user['telefono'] = row[4]
        user['cumpleaños'] = row[5]
    user['intereses'] = []
    query = "SELECT usuario.id, intereses.descripcion FROM usuario, intereses, tag WHERE usuario.id = tag.id_u AND intereses.id = tag.tag_t AND usuario.id = %s"
    adr = (str(Logged_in), )
    cursor.execute(query, adr)
    intereses = cursor.fetchall()
    for row in intereses:
        # print("carne de usuario:", row[0]) # esta no es necesaria. solo usen la de abajo. 
        # print("descipción: nombre de interes:", row[1]) 
        user['intereses'].append(row[1])
    query = "SELECT proyectos.id_proyecto, proyectos.nombre, proyectos.objetivo, proyectos.descripcion, proyectos.fecha_cierre FROM `proyectos` WHERE `id_usuario` = %s"
    adr = (str(Logged_in), )
    cursor.execute(query, adr)
    info_proyecto = cursor.fetchall()
    proyectos = {}
    for row in info_proyecto:
        proyectos[str(row[0])] = {}
        proyectos[str(row[0])]['nombre proyecto'] = row[1]
        proyectos[str(row[0])]['objetivo'] = row[2]
        proyectos[str(row[0])]['descripción'] = row[3]
        proyectos[str(row[0])]['fecha de cierre'] = row[4]
    print(proyectos)
    conn.close()
    #record se manda al html para mostrar lo datos
    csss = url_for('static', filename="style_perfil.css")
    js = url_for('static', filename = "main.js")
    return render_template("usuario.html", csss = csss, js = js, user = user, proyectos = proyectos) 

#En este nedpoint se van a obtener todos las conferencias que al usuario le interese
@app.route("/usuario_conferencias_intereses", methods = ["GET", "POST"])
def usuario_conferencias_intereses():
    openConnection()
    global conn
    if "Logged_in" in session:
        Logged_in = session["Logged_in"]
    print(Logged_in)

    cursor = conn.cursor()
    user = {}
    query = "SELECT usuario.id, usuario.nombre, usuario.apellido, usuario.mail, usuario.tel, usuario.birth FROM usuario WHERE usuario.id = %s"
    adr = (str(Logged_in), )
    cursor.execute(query, adr)
    datos = cursor.fetchall()
    user = {}
    for row in datos:
        user['carne'] = row[0]
        user['nombre'] = row[1]
        user['apellido'] = row[2]
        user['mail'] = row[3]
        user['telefono'] = row[4]
        user['cumpleaños'] = row[5]
    user['intereses'] = []
    query = "SELECT intereses.id, intereses.descripcion FROM usuario, intereses, tag WHERE usuario.id = tag.id_u AND intereses.id = tag.tag_t AND usuario.id = %s"
    adr = (str(Logged_in), )
    cursor.execute(query, adr)
    intereses = cursor.fetchall()
    for row in intereses:
        user['intereses'].append(row[0])
    query = "SELECT proyectos.id_proyecto, proyectos.nombre, proyectos.objetivo, proyectos.descripcion, proyectos.fecha_cierre, proyectos.cupo FROM proyectos INNER JOIN proyecto_intereses ON proyecto_intereses.id_proyecto=proyectos.id_proyecto  WHERE proyecto_intereses.id_interes IN (%s) AND proyectos.id_usuario != " + str(Logged_in)

    intereses_param = ', '.join(['%s'] * len(tuple(user['intereses'])))
    query = query % intereses_param

    cursor.execute(query, tuple(user['intereses']))
    info_proyectos_intereses = cursor.fetchall()

    proyectos = {}
    for row in info_proyectos_intereses:
        proyectos[str(row[0])] = {}
        proyectos[str(row[0])]['nombre proyecto'] = row[1]
        proyectos[str(row[0])]['objetivo'] = row[2]
        proyectos[str(row[0])]['descripción'] = row[3]
        proyectos[str(row[0])]['fecha de cierre'] = row[4]
        proyectos[str(row[0])]['cupo'] = row[5]
    print(user)
    print(proyectos)
    
    conn.close()
    #record se manda al html para mostrar lo datos
    csss = url_for('static', filename="style_perfil.css")
    js = url_for('static', filename = "main.js")
    return render_template("conferencias_intereses.html", csss = csss, js = js, user = user, proyectos = proyectos) 

@app.route("/crear_proyecto", methods = ["GET", "POST"])
def proyecto():
    if "Logged_in" in session:
        Logged_in = session["Logged_in"]
        
    if(request.method == "POST"):
        global proyecto_actual
        proyecto_actual = {}
        name = request.form['name']
        objetivo = request.form['objetivo']
        descripcion = request.form['descri']
        fecha_cierre = request.form['fecha']
        cupo = request.form['cupo']
        visible = 1
        print(name, objetivo, descripcion, fecha_cierre)

        proyecto_actual['name'] = name
        proyecto_actual['objetivo'] = objetivo
        proyecto_actual['descripcion'] = descripcion
        proyecto_actual['fecha_cierre'] = fecha_cierre
        proyecto_actual['cupo'] = cupo

        if name and objetivo and descripcion and fecha_cierre:
            openConnection()
            global conn
            cursor = conn.cursor()
            inquery = "INSERT INTO `proyectos`(`id_proyecto`, `id_usuario`, `nombre`, `objetivo`, `descripcion`, `fecha_cierre`, `visible`, `cupo`) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(inquery, (Logged_in, name, objetivo, descripcion, fecha_cierre, visible, cupo))
            conn.commit()
            opquery = "SELECT proyectos.id_proyecto FROM proyectos ORDER BY proyectos.id_proyecto DESC LIMIT 1"
            cursor.execute(opquery)
            idpro = cursor.fetchall()
            idproyecto = 0
            for row in idpro:
                idproyecto = row[0]
            query = "INSERT INTO `usuario_proyecto`(`id_usuario`, `id_proyecto`) VALUES (%s,%s)"
            cursor.execute(query, (Logged_in, idproyecto))
            conn.commit()
            conn.close()
            return redirect(url_for('intereses'))
    #query = "SELECT proyectos.id_proyecto, proyectos.nombre, usuario.mail FROM proyectos, usuario, usuario_proyecto, tag, intereses, proyecto_intereses WHERE proyectos.id_proyecto = %s, AND proyectos.id_proyecto = proyecto_intereses.id_proyecto AND proyecto_intereses.id_interes = tag.tag_t AND tag.carne_u = usuario.carne"
    #query para obtener el último proyecto: SELECT proyectos.id_proyecto FROM proyectos ORDER BY proyectos.id_proyecto DESC LIMIT 1
    #logo = url_for('static', filename="logo.png")
    return render_template("crear_proyecto.html")

@app.route("/prueba", methods = ["GET", "POST"])
def perfil():
    if(request.method == "POST"):
        name = request.form['name']
        print(name)
        objetivo = request.form['objetivo']
        print(objetivo)
        descripcion = request.form['descri']
        print(descripcion)
        fecha_cierre = request.form['fecha']
        print(fecha_cierre)
        return render_template("crear_proyecto.html")
    
    return render_template("crear_proyecto.html")

@app.route("/intereses", methods = ["GET", "POST"])
def intereses():
    
    necesidades = []
    if(request.method == "POST"):

        if request.form.getlist('1'):
            necesidades.append(1)
        if request.form.getlist('2'):
            necesidades.append(2)
        if request.form.getlist('3'):
            necesidades.append(3)
        if request.form.getlist('4'):
            necesidades.append(4)
        if request.form.getlist('5'):
            necesidades.append(5)
        if request.form.getlist('6'):
            necesidades.append(6) 

        print(necesidades)
        #tenemos que recibir los checkboxs  y convertirlos a int o bool en base a si fue o no seleccionado.
        #en estas variables: progra, dise, est_m, camp_p, mate, circu
        #--------------------conexión base de datos
        #insert in tags despues del post de los checkbox, necesito que esten en una lista las que si marco el usuario
        openConnection()
        global conn
        cursor = conn.cursor()
        if "Logged_in" in session:
            Logged_in = session["Logged_in"]
        opquery = "SELECT proyectos.id_proyecto FROM proyectos ORDER BY proyectos.id_proyecto DESC LIMIT 1"
        cursor.execute(opquery)
        idpro = cursor.fetchall()
        idproyecto = 0
        for row in idpro:
            idproyecto = row[0]
        for var in necesidades:
            query = "INSERT INTO `proyecto_intereses`(`id_proyecto`, `id_interes`) VALUES (%s,%s)"
            cursor.execute(query, (idproyecto, var))
            conn.commit()
        opquery = "SELECT usuario.mail FROM usuario WHERE usuario.id = %s"
        adr = (str(Logged_in), )
        cursor.execute(opquery, adr)
        idpro = cursor.fetchall()
        mail = ""
        for row in idpro:
            mail = row[0]
        selquery = "SELECT DISTINCT proyectos.id_proyecto, proyectos.nombre, usuario.mail FROM proyectos, usuario, usuario_proyecto, tag, intereses, proyecto_intereses WHERE proyectos.id_proyecto = proyecto_intereses.id_proyecto AND proyecto_intereses.id_interes = tag.tag_t AND tag.id_u = usuario.id AND proyectos.id_proyecto = %s AND usuario.mail <> %s"
        id_proyecto = (int(idproyecto), str(mail), )
        cursor.execute(selquery, id_proyecto)
        correos = cursor.fetchall()
        listado_correos = []
        for row in correos:
            #Aqui es donde se mandan los correos
            #print(row[0])  comprobante ambos los pueden quitar
            #print(row[1])  comprobante
            #print(row[2])  este es el correo
            listado_correos.append(row[2])
        # <-- linea para mandar los correos, la lista a utilizar es listado_correos
        print(listado_correos)
        cursor.close()
        conn.close()
            # Preparación para mandar el correo
        categoria = ""
        i = 0
        nece = len(necesidades) - 2
        for n in necesidades: 
            if n == 1: 
                categoria += "programación"
            if n == 2: 
                categoria += "diseño"
            if n == 3: 
                categoria += "estudio de mercado"
            if n == 4: 
                categoria += "campañas de publicidad"
            if n == 5: 
                categoria += "matemáticas"
            if n == 6: 
                categoria += "circuitos"
            if i == nece: 
                categoria += " y "
            if i != nece or i != nece + 1:
                categoria += ", "
            i += 1
        global creador, proyecto_actual
        #sender(listado_correos, categoria, creador, proyecto_actual)

        return redirect("/usuario")

    
    
    arqui = url_for('static', filename="arqui.jpg")
    med = url_for('static', filename="med.jpg")
    return render_template("interes.html", arqui = arqui, med = med)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
