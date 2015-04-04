#A pretend temperature sensor, for testing purposes.
import SocketServer

class HandleUDP(SocketServer.BaseRequestHandler):
    temperatue = 72
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print data
        if(data =="TYPE"):
          socket.sendto("TEMPERATURE SENSOR", self.client_address)
        elif(data =="UNITS"):
          socket.sendto("FAHRENHEIT", self.client_address)
        elif(data=="VALUE"):
          socket.sendto(temperature, self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 16512
    server = SocketServer.UDPServer((HOST, PORT), HandleUDP)
    server.serve_forever()