import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

print("\n\n ********** Servidor iniciado ********** \n")

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value
	
  def exposed_remove(self):
    self.value = self.value.pop()
    return self.value

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

