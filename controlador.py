import sqlite3


def ver_enviados(correo):
    db=sqlite3.connect("Men_Electronica.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select  m.Asunto,m.Mensaje,m.Fecha, m.Hora, u.Nombre_Usuario  from Usuario u, Mensajes m where u.Correo=m.id_Receptor and m.id_Emisor='"+correo+"' order by Fecha desc,Hora desc"
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    return resultado

def ver_recibidos(correo):
    db=sqlite3.connect("Men_Electronica.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select  m.Asunto,m.Mensaje,m.Fecha, m.Hora, u.Nombre_Usuario  from Usuario u, Mensajes m where u.Correo=m.id_Receptor and m.id_Emisor='"+correo+"' order by Fecha desc,Hora desc"
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    return resultado

def validar_usuario(usuario, password):
    db=sqlite3.connect("Men_Electronica.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select *from Usuario where Correo='"+usuario+"' and Password='"+password+"' and Estado='1'"
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    return resultado

def lista_destinatarios(usuario):
    db=sqlite3.connect("Men_Electronica.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select *from Usuario where Correo<>'"+usuario+"' "
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    return resultado


def actualizapass(password, correo):
    db=sqlite3.connect("Men_Electronica.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="update Usuario set Password='"+password+"' where Correo='"+correo+"'"
    cursor.execute(consulta)
    db.commit()
    return "1"

def registrar_mail(origen, destino, asunto, mensaje):
    db=sqlite3.connect("Men_Electronica.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="insert into Mensajes (Asunto,Mensaje,Fecha,Hora,id_Emisor,id_Receptor,Estado) values ('"+asunto+"','"+mensaje+"',DATE('now'),TIME('now'),'"+origen+"','"+destino+"','0')"
    cursor.execute(consulta)
    db.commit()
    return "1"

def registrar_usuario(nombre,correo, password,codigo):
    try:
        db=sqlite3.connect("Men_Electronica.s3db")
        db.row_factory=sqlite3.Row
        cursor=db.cursor()
        consulta="insert into Usuario (Nombre_Usuario,Correo,Password,Estado,Cod_Activacion) values ('"+nombre+"','"+correo+"','"+password+"','0','"+codigo+"')"
        print("op 1")
        cursor.execute(consulta)
        print("op 2")
        db.commit()
        print("op 3")
        return "Usuario Registrado Satisfactoriamente"
    except:
        return "ERROR!!! No es posible registrar al usuario debido a que el CORREO y/o NOMBRE DE USUARIO existen. Lo invitamos a modificar los campos pertinentes."
        
        
    
    

def activar_usuario(codigo):
    db=sqlite3.connect("Men_Electronica.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="update Usuario set Estado='1' where Cod_Activacion='"+codigo+"'"
    cursor.execute(consulta)
    db.commit()
    
    consulta2="select *from Usuario where Cod_Activacion='"+codigo+"' and Estado='1'"
    cursor.execute(consulta2)
    resultado=cursor.fetchall()
    return resultado
    
   


    