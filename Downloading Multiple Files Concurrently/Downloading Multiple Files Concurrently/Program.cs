using System;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;

namespace Downloading_Multiple_Files_Concurrently
{
    class Program
    {

        static void Main()
        {
            string[] urls = { "https://tmpfiles.org/dl/17080002/sheet7.pptx", "https://tmpfiles.org/dl/17080034/lect_06.pdf" };
            string[] fileNames = { "file1.zip", "file2.zip" };

            Thread[] threads = new Thread[urls.Length];

            for (int i = 0; i < urls.Length; i++)
            {
                int index = i;  // Capture index to avoid closure issues
                threads[i] = new Thread(() => DownloadFileAsync(urls[index], fileNames[index]).Wait());
                threads[i].Start();
            }

            foreach (var thread in threads)
            {
                thread.Join(); // Wait for all downloads to finish
            }

            Console.WriteLine("All downloads completed.");
        }

        static async Task DownloadFileAsync(string url, string fileName)
        {
            using HttpClient client = new HttpClient();
            Console.WriteLine($"Starting download: {url}");

            var data = await client.GetByteArrayAsync(url);
            File.WriteAllBytes(fileName, data);

            Console.WriteLine($"Download complete: {fileName}");
        }
    }

}
