using Metriks.Sdk.Models;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using System.Text.Json;

namespace Metriks.Sdk
{
    public class Client
    {
        HttpClient _client;

        /// <summary>
        /// Intializes the client and sets the request header user-agent to the consumingApplicationName
        /// </summary>
        /// <param name="consumingApplicationName">The name of the application that is consuming the SDK</param>
        /// <param name="metriksApiBaseAddress">The base address of the API</param>
        internal Client(string consumingApplicationName, string metriksApiBaseAddress)
        {
            InitializeClient(consumingApplicationName, metriksApiBaseAddress);
        }

        private void InitializeClient(string consumingApplicationName, string metriksApiBaseAddress)
        {
            _client = new HttpClient();
            _client.DefaultRequestHeaders.Accept.Clear();
            _client.DefaultRequestHeaders.Accept.Add(
                new MediaTypeWithQualityHeaderValue("application/json"));
            _client.DefaultRequestHeaders.Add("User-Agent", consumingApplicationName);
            _client.BaseAddress = new Uri(metriksApiBaseAddress);          
        }

        public async Task<List<WeatherForecast>> GetWeatherAsync()
        {
            string path = "/WeatherForecast";

            var stringTask = _client.GetStringAsync(path);
            var msg = await stringTask;
            var result = DeserializeResults<List<WeatherForecast>>(msg);

            return result;
        }

        private static T DeserializeResults<T>(string msg)
        {
            JsonSerializerOptions options = new JsonSerializerOptions() { PropertyNameCaseInsensitive = true };
            var result = JsonSerializer.Deserialize<T>(msg, options);
            return result;
        }
    }
}
