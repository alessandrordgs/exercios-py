import sqlite3
con = sqlite3.connect('agenda.sqlite')

cursor = con.cursor()

# cursor.execute("""
# CREATE TABLE contatos (
#   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#   nome TEXT NOT NULL,
#   cel TEXT NOT NULL,
#   tel TEXT NOT NULL,
#   email TEXT NOT NULL,
#   aniver TEXT NOT NULL
# );
# """)
# print('tabela criada com sucesso')


opçao = input("""
1 - Cadastrar um novo contato 
2 - editar o celular, telefone e o email
3 - Apagar um contato
""")

if opçao == '1':
  nome = input('Nome: ')
  cel = input('Celular: ')
  tel = input('Telefone: ')
  email = input('Email: ')
  aniver = input('Aniversario ')
  cursor.execute(""" 
  INSERT INTO contatos (nome, cel, tel, email, aniver) VALUES (?, ?, ?, ?, ?)
""", (nome, cel, tel, email, aniver))
  con.commit()
elif opçao == '2':
  cel = input('Celular: ')
  tel = input('Telefone: ')
  email = input('Email: ')
  id_pessoa = input('Id ')

  cursor.execute("""
    UPDATE contatos SET cel = ?, tel = ?, email = ? WHERE id = ?
  """, (cel, tel, email, id_pessoa))
  con.commit()
elif opçao == '3':
  id_pessoa = input('Id ')

  cursor.execute("""
  DELETE FROM contatos WHERE id = ?
  """, (id_pessoa))
  con.commit()



