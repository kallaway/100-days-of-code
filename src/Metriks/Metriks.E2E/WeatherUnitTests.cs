using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Diagnostics;

namespace Metriks.E2E
{
    [TestClass]
    public class WeatherUnitTests
    {
        [TestMethod]
        public void GetWeatherShouldReturn5Items()
        {
            // Arrange
            var expectedCount = 5;
            var client = Metriks.Sdk.Authentication.GetClient("Metriks E2E Tests", "https://localhost:44379/");

            // Act
            var weatherTask = client.GetWeatherAsync().ConfigureAwait(false).GetAwaiter();
            var weather = weatherTask.GetResult();

            // Assert
            Assert.IsNotNull(weather);
            Assert.AreEqual(expectedCount, weather.Count);

        }
    }
}
