using message.api;
using System;
using Thrift.Protocol;
using Thrift.Transport;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            using (TSocket socket = new TSocket("localhost", 8800))
            using (TTransport transport = new TBufferedTransport(socket))
            using (TProtocol protocol = new TBinaryProtocol(transport))
            using (var client = new MessageService.Client(protocol))
            {
                transport.Open();
                Console.WriteLine(client.sendEmailMessage());

                ;
            }

            //using (TTransport transport = new TSocket("127.0.0.1", 8800))
            //using (TProtocol protocol = new TBinaryProtocol(transport))
            //using (var clientUser = new MessageService.Client(protocol))
            //{
            //    transport.Open();

            //    Console.WriteLine(clientUser.sendEmailMessage());
            //}

            Console.ReadKey();
        }
    }
}
