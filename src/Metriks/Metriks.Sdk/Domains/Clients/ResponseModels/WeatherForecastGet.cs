using Metriks.Sdk.Domains.Models;
using System;

namespace Metriks.Sdk.Domains.Clients.ResponseModels
{
    internal class WeatherForecastGet
    {
        public DateTime Date { get; set; }

        public int TemperatureC { get; set; }

        public int TemperatureF { get; set; }

        public string Summary { get; set; }

        internal WeatherForecast MapTo()
        {
            var result = new WeatherForecast();
            result.Date = this.Date;
            result.TemperatureC = this.TemperatureC;
            result.TemperatureF = this.TemperatureF;
            result.Summary = this.Summary;

            return result;
        }
    }
}
