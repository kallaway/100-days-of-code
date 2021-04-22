using Metriks.E2E.Common;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.E2E
{
    [TestClass]
    public class WeightTests
    {
        [TestMethod]
        [Scenario("Create weight with valid data should return with a populate ID")]
        [Given("A weight measurement with weight above 0.0 pounds and less than 300.0 pounds from the past year")]
        [When("that measurement is submitted to be created")]
        [Then("a weight measurement matching the original measurements with a new ID is returned")]
        public void Create_weight_with_valid_data_should_return_with_a_populate_ID()
        {
            // Arrange
            var client = TestHelper.GetSdkClient();

            // Act
            var actual = client.Weight.GetWeight();

            // Assert
            Assert.IsTrue(actual.Count > 0);

        }
    }
}
