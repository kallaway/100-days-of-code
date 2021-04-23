using Metriks.Sdk.Domains.Models;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Metriks.Sdk.Domains
{

    public interface IWeather
    {
        List<WeatherForecast> GetWeather();
        Task<List<WeatherForecast>> GetWeatherAsync();
    }
}
