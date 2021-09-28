import mysql.connector #importa o driver mysql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("show databases;")

myresult = mycursor.fetchall()

mycursor.execute("use livraria")
mycursor.execute("select * from livros") #consulta
dados = mycursor.fetchall()

for dado in dados:
    print("Titulo", dado[1])
    print("Autor", dado[2])
    #print("????", dado[3])
    print("Genero", dado[4], "\n")


#print(dados)

if mydb.is_connected():
    print("- Uhuul ainda estou conectado!!")
    print("Desconectando...")
    print("- A não")
    mydb.close()
    mycursor.close()
    print("Desconectado!!")
