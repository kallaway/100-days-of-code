using Metriks.Sdk.ResponseModels;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Metriks.Sdk.Domains
{
    public interface IWeather
    {
        Task<List<WeatherForecast>> GetWeatherAsync();
    }
}
