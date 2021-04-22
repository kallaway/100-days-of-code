using Metriks.Sdk.Common;
using Metriks.Sdk.ResponseModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.Sdk.Domains
{
    internal class Weather : ApiClient, IWeather
    {
        HttpClient _client;

        public Weather(HttpClient client)
        {
            _client = client;
        }

        public async Task<List<WeatherForecast>> GetWeatherAsync()
        {
            string path = "api/WeatherForecast";

            var stringTask = _client.GetStringAsync(path);
            var msg = await stringTask;
            var result = DeserializeResults<List<WeatherForecast>>(msg);

            return result;
        }
    }
}
