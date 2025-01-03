using System.Net.Sockets;
using System.Net;
using System.Text;

namespace Server1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // connection 

            TcpListener server = new TcpListener(IPAddress.Any, 5000);
            server.Start();
            Console.WriteLine($"Server started . Waiting for a connection...");

            TcpClient client = server.AcceptTcpClient();
            Console.WriteLine("Client connected!");

            // messaging

            NetworkStream stream = client.GetStream();

            while (true)
            {
                byte[] buffer = new byte[1024]; // local memory structure within the current application.
                int bytesRead = stream.Read(buffer, 0, buffer.Length); // It blocks (pauses execution) until data is available to read or the connection is closed by the remote endpoint.
                string message = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                Console.WriteLine($"Client: {message}");


                if (message.ToLower() == "exit")
                {
                    Console.WriteLine("Client disconnected.");
                    break;
                }

                Console.Write("You: ");
                string response = Console.ReadLine();
                buffer = Encoding.UTF8.GetBytes(response);
                stream.Write(buffer, 0, buffer.Length);
            }

            client.Close();
            server.Stop();
            Console.WriteLine("Server stopped.");


        }
    }
}
