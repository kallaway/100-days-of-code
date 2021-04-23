using Metriks.E2E.Common;
using Metriks.Sdk.Domains.Models;
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
        #region Create
        [TestMethod]
        [Scenario("Create weight with valid data should return with a populate ID")]
        [Given("A weight measurement with weight above 0.0 pounds and less than 300.0 pounds from the past year")]
        [When("that measurement is submitted to be created")]
        [Then("a weight measurement matching the original measurements with a new ID is returned")]
        public void Create_weight_with_valid_data_should_return_with_a_populate_ID()
        {
            // Arrange
            var client = TestHelper.GetSdkClient();
            DateTime expectedEntryDate = TestHelper.GetRandomPastDate(1, 365);
            double expectedWeight = TestHelper.GetRandomDouble(1, 300);
            string expectedUnit = "pounds";

            // Act
            var actual = client.Weight.Create(expectedEntryDate, expectedWeight, expectedUnit);

            // Assert
            Assert.AreNotEqual(Guid.Empty, actual.Id);
            Assert.AreEqual(expectedEntryDate, actual.EntryDate);
            Assert.AreEqual(expectedWeight, actual.Weight);
            Assert.AreEqual(expectedUnit, actual.Unit);
        }

        #endregion

        #region Get List
        [TestMethod]
        [Scenario("Get weight returns at least 2 items after 2 weight measurements have been created")]
        [Given("at least 2 weight measurements have been created ")]
        [When("weight measurement lists are retrieved")]
        [Then("at least 2 weight measurements are returned in a list")]
        public void Get_weight_returns_at_least_2_items_after_2_weight_measurements_have_been_created()
        {
            // Arrange
            var client = TestHelper.GetSdkClient();
            int expectedMinimumCount = 2;

            for (int i = 0; i < expectedMinimumCount; i++)
            {
                DateTime expectedEntryDate = TestHelper.GetRandomPastDate(1, 365);
                double expectedWeight = TestHelper.GetRandomDouble(1, 300);
                string expectedUnit = "pounds";
                _ = client.Weight.Create(expectedEntryDate, expectedWeight, expectedUnit);
            }


            // Act
            var actual = client.Weight.GetList();

            // Assert
            Assert.IsTrue(actual.Count >= expectedMinimumCount, $"Expected at least {expectedMinimumCount} items, but there was only {actual.Count} items.");

        }

        #endregion

        #region Get by ID
        [TestMethod]
        [Scenario("Get weight by valid ID")]
        [Given("a weight with a known ID")]
        [When("that weight is retrieved by ID")]
        [Then("a valid weight measurement is returned")]
        public void Get_weight_by_valid_ID()
        {
            // Arrange
            var client = TestHelper.GetSdkClient();

            DateTime expectedEntryDate = TestHelper.GetRandomPastDate(1, 365);
            double expectedWeight = TestHelper.GetRandomDouble(1, 300);
            string expectedUnit = "pounds";
            var artifact = client.Weight.Create(expectedEntryDate, expectedWeight, expectedUnit);
            var expectedId = artifact.Id;

            // Act
            WeightMeasurement actual = client.Weight.Get(expectedId);

            // Assert
            Assert.AreEqual(expectedId, actual.Id);

        }
        #endregion

        #region Delete
        [TestMethod]
        [Scenario("Delete weight returns true when a valid ID is used")]
        [Given("an ID for an existing weight measurement")]
        [When("a request delete that weight ID is sent")]
        [Then("a success response is sent to the integrator")]
        public void Delete_weight_returns_true_when_a_valid_ID_is_used()
        {
            // Arrange
            var client = TestHelper.GetSdkClient();

            DateTime expectedEntryDate = TestHelper.GetRandomPastDate(1, 365);
            double expectedWeight = TestHelper.GetRandomDouble(1, 300);
            string expectedUnit = "pounds";
            var original = client.Weight.Create(expectedEntryDate, expectedWeight, expectedUnit);

            // Act
            bool actual = client.Weight.Delete(original.Id);

            // Assert
            Assert.IsTrue(actual, "Failed to delete weight given a valid ID");

        }

        #endregion



    }
}
