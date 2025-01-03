using System.Net.Sockets;
using System.Text;

namespace Client1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            const string serverAddress = "127.0.0.1";
            const int port = 5000;

            TcpClient client = new TcpClient();

            try
            {
                client.Connect(serverAddress, port);
                Console.WriteLine("Connected to the server!");

                NetworkStream stream = client.GetStream();

                while (true)
                {
                    Console.Write("You: ");
                    string message = Console.ReadLine();

                    byte[] buffer = Encoding.UTF8.GetBytes(message);
                    stream.Write(buffer, 0, buffer.Length);

                    if (message.ToLower() == "exit")
                    {
                        Console.WriteLine("Disconnected from server.");
                        break;
                    }

                    buffer = new byte[1024];
                    int bytesRead = stream.Read(buffer, 0, buffer.Length);
                    string response = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                    Console.WriteLine($"Server: {response}");

                }

                stream.Close();

            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
            finally
            {
                client.Close();
            }
        }
    }
}
