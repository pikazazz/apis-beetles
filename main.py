from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.networks import stricturl
import pymysql
import json
#database connection

connection = pymysql.connect(host="us-cdbr-east-04.cleardb.com",user="bb57b95c6a1ce7",passwd="24d9a0a7",database="heroku_f3d569c7ec6d1e1" )
cursor = connection.cursor()
# some other statements  with the help of cursor


app = FastAPI()

class Beetles(BaseModel):
    name_th: str
    name_eng: str
    likes: str
    type: str
    detail: str
    skillfeed: str
    skillbreed: str
    cost: str
    pic: str

@app.get("/beetles")
def select_all():
    # queries for inserting values
    insert1 = "SELECT * FROM `list_beetles`"
    # commiting the connection then closing it.
    if cursor.execute(insert1) :
       row_headers=[x[0] for x in cursor.description] #this will extract row headers
       rv = cursor.fetchall()
       json_data=[]
       for result in rv:
            json_data.append(dict(zip(row_headers,result)))
       return json_data
    else :
       return 'false'
   

@app.get("/beetles/{beetles_id}")
def read_item(beetles_id: int):
    # queries for inserting values
    insert1 = "SELECT * FROM `list_beetles` where id='"+str(beetles_id)+"'"
    # commiting the connection then closing it.
    if cursor.execute(insert1) :
       row_headers=[x[0] for x in cursor.description] #this will extract row headers
       rv = cursor.fetchall()
       json_data=[]
       for result in rv:
            json_data.append(dict(zip(row_headers,result)))
       return json_data
    else :
       return 'false'

@app.post("/beetles")
def add_item(beetles: Beetles):
    # queries for inserting values
    insert1 = "INSERT INTO `list_beetles`(`name_th`, `name_eng`, `likes`, `type`, `detail`, `skillfeed`, `skillbreed`, `cost`,`pic`) VALUES ('"+beetles.name_th+"','"+beetles.name_eng+"',"+beetles.likes+",'"+beetles.type+"','"+beetles.detail+"',"+beetles.skillfeed+","+beetles.skillbreed+","+beetles.cost+",'"+beetles.pic+"'"+");"
    cursor.execute(insert1)
    # commiting the connection then closing it.
    if cursor.execute(insert1):
       connection.commit() 
       return 'true'
    else :
       return 'false'


@app.put("/beetles/{beetles_id}")
def update_item(beetles_id: int,beetles_ids: int):
    return {"beetles_id":beetles_id,"beetles_ids":beetles_ids}

@app.delete("/beetles/{beetles_id}")
def delete_item(beetles_id: int):
    # queries for inserting values
    insert1 = "DELETE FROM `list_beetles` where id="+str(beetles_id)
    # commiting the connection then closing it.
    if cursor.execute(insert1):
       connection.commit() 
       return 'true'
    else :
       return 'false'
    