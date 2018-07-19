from message.api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class MessageServiceHandler:
    def sendMobileMessage(self):
        print("sendMobileMessage")
        return True

    def sendEmailMessage(self):
        print("sendEmailMessage")
        return True


if __name__ == "__main__":
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket(host="0.0.0.0", port=8800)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("python thrift server start")
    server.serve()
    print("python thrift server exit")
