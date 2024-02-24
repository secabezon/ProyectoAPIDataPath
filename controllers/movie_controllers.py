from fastapi import APIRouter, HTTPException, status
from model.models import myCollections
import mysql.connector

router=APIRouter()

conn=mysql.connector.connect(user='root',passwd='root',host='mysql',port='3306',database='my_collections')



@router.get('/my_collections')
def get_collections():
    with conn.cursor() as cursor:
        query='select * from my_collections'
        cursor.execute(query)
        respuesta=cursor.fetchall()
        return 200, respuesta
    
@router.get('/my_collections/{ID}')
def get_specific_collections(ID):
    with conn.cursor() as cursor:
        query=f'select * from my_collections where ID={ID}'
        cursor.execute(query)
        respuesta=cursor.fetchall()
        if respuesta is not None:
            return 200, respuesta
        else:
            raise HTTPException(status_code=404, detail='No se encontro el id')
        
@router.post('/my_collections',status_code=201)
def post_collections(myCollection:myCollections):
    with conn.cursor() as cursor:
        conteo='select count(*) from my_collections'
        cursor.execute(conteo)
        conteo=(cursor.fetchone()[0]+1)
        myCollection.ID=conteo
        fila = (myCollection.ID, myCollection.Autor, myCollection.Descripcion, myCollection.FechaEstreno)
        insert_collections = 'insert into my_collections(ID, Autor, Descripcion, FechaEstreno) VALUES (%s,%s,%s,%s)'
        cursor.execute(insert_collections,fila)#ejecutar esta sentencia dependiendo del numero de filas
        conn.commit()
        return {"message":"Collection agregado correctamente"}
        
@router.put('/my_collections/{ID}')
def update_collections(ID,myCollection:myCollections):
    with conn.cursor() as cursor:
        collection = (myCollection.Autor, myCollection.Descripcion, myCollection.FechaEstreno,ID)
        update_query='''update my_collections
        set Autor=%s
        , Descripcion=%s
        , FechaEstreno=%s
        where ID=%s'''
        cursor.execute(update_query,collection)
        conn.commit()
        return {"message":"Collection actualizado correctamente"}

@router.delete('/my_collections/{ID}')
def delete_collections(ID:int):
    with conn.cursor() as cursor:
        delete_query=f'''delete from my_collections
        where ID={ID}'''
        cursor.execute(delete_query)
        conn.commit()
        return {"message":"Collection eliminado correctamente"}