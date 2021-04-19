using Metriks.Sdk.Models;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

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
            // https://localhost:44379/WeatherForecast
            string path = "/WeatherForecast";

            var stringTask = _client.GetStringAsync("/WeatherForecast");
            string msg = await stringTask;
            string result = msg;

            throw new NotImplementedException();
        }
    }
}
