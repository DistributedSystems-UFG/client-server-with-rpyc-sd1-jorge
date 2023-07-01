import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print("Iniciando operações na lista")
  print (conn.root.exposed_value())
  print("Adicionando valores 5 e 6 à lista")
  conn.root.exposed_append(5)       # Call an exposed operation,
  conn.root.exposed_append(6)       # and append two elements
  print("Inserindo mais itens à lista")
  print("Adicionando valores 3 e 4 à lista")
  conn.root.exposed_append(3)       # Call an exposed operation,
  conn.root.exposed_append(4)
  print (conn.root.exposed_value())   # Print the result
  print("Removendo o valor")
  print (conn.root.exposed_remove())
  print("Lista Atual")
  print (conn.root.exposed_value())