from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from message.api import MessageService
import time

# Make socket
transport = TSocket.TSocket('localhost', 8800)
# Buffering is critical. Raw sockets are very slow
transport = TTransport.TBufferedTransport(transport)
# Wrap in a protocol
protocol = TBinaryProtocol.TBinaryProtocol(transport)


client = MessageService.Client(protocol)
transport.open()
print(client.send_sendEmailMessage())
time.sleep(100)
transport.close()



