using Metriks.Domain.Models;
using Metriks.Domain.UnitTests.Common;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;

namespace Metriks.Domain.UnitTests
{
    [TestClass]
    public class WeightTests
    {

        #region Create
        [TestMethod]
        [Scenario("Create weight should populate an empty ID")]
        [Given("a weight measurement has an empty Id")]
        [When("Create is executed")]
        [Then("the weight measurement is added to the datastore and the ID is populated")]
        public void Create_weight_should_populate_an_empty_ID()
        {
            // Arrange
            WeightMeasurement expected = GenerateRandomWeightMeasurement();
            expected.Id = Guid.Empty;

            // Act
            Weight bizLogic = new Weight();
            var actual = bizLogic.Create(expected);

            // Assert
            Assert.IsTrue(actual.created);
            Assert.AreEqual(expected.EntryDate, actual.measurement.EntryDate, "EntryDate does not match.");
            Assert.AreNotEqual(Guid.Empty, actual.measurement.Id, "Id is still empty.");
            Assert.AreEqual(expected.Unit, actual.measurement.Unit, "Unit does not match.");
            Assert.AreEqual(expected.Weight, actual.measurement.Weight, "Weight does not match.");
        }

        [TestMethod]
        [Scenario("Create weight should retain the original ID")]
        [Given("a weight measurement has an non-empty ID")]
        [When("Create is executed")]
        [Then("the weight measurement is added to the datastore and the ID remains the same")]
        public void Create_weight_should_retain_the_original_ID()
        {
            // Arrange
            var expectedId = Guid.NewGuid();
            WeightMeasurement expected = GenerateRandomWeightMeasurement();
            expected.Id = expectedId;

            // Act
            Weight bizLogic = new Weight();
            var actual = bizLogic.Create(expected);

            // Assert
            Assert.IsTrue(actual.created);
            Assert.AreEqual(expected.EntryDate, actual.measurement.EntryDate, "EntryDate does not match.");
            Assert.AreEqual(expectedId, actual.measurement.Id, "Id does not match.");
            Assert.AreEqual(expected.Unit, actual.measurement.Unit, "Unit does not match.");
            Assert.AreEqual(expected.Weight, actual.measurement.Weight, "Weight does not match.");

        }

        [TestMethod]
        [Scenario("Create weight should fail when a duplicate ID is passed in")]
        [Given("a weight measurement has an ID that already exists in the data store")]
        [When("Create is executed")]
        [Then("the operation fails")]
        // TODO: Clarify what "fail" means
        public void Create_weight_should_fail_when_a_duplicate_ID_is_passed_in()
        {
            // Arrange
            var originalId = Guid.NewGuid();

            WeightMeasurement original = GenerateRandomWeightMeasurement();
            original.Id = originalId;

            WeightMeasurement expected = GenerateRandomWeightMeasurement();
            expected.Id = originalId;

            // Act
            Weight bizLogic = new Weight();
            _ = bizLogic.Create(original);
            var actual = bizLogic.Create(expected);

            // Assert
            Assert.IsFalse(actual.created);
        }

        [TestMethod]
        [Scenario("Create weight should fail when a duplicate ID is passed in")]
        [Given("a weight measurement has an ID that already exists in the data store")]
        [When("Create is executed")]
        [Then("the operation fails")]
        [ExpectedException(typeof(ArgumentNullException), "Expected ArgumentNullException because no measurement was passed in")]
        public void CreateShouldThrowWhenNullMeasurementPassedIn()
        {
            // Arrange

            // Act
            Weight bizLogic = new Weight();
            _ = bizLogic.Create(null);

            // Assert

        }

        #endregion

        #region Get
        [TestMethod]
        [Scenario("Get a list of weight measurements")]
        [Given("an end-user has at least 2 weight measurements in the system")]
        [When("retrieve weight measurements is called")]
        [Then("at least 2 weight measurements are returned")]
        public void Get_weight_list_should_return_at_least_2_items()
        {
            // Arrange
            Weight bizLogic = new Weight();
            _ = bizLogic.Create(GenerateRandomWeightMeasurement());
            _ = bizLogic.Create(GenerateRandomWeightMeasurement());

            // Act
            List<WeightMeasurement> measurements = bizLogic.Read();

            // Assert
           Assert.IsTrue(measurements.Count >= 2, $"Expected at least 2 items, but there was only {measurements.Count} items.");
        }


        #endregion

        private static WeightMeasurement GenerateRandomWeightMeasurement()
        {
            Random r = new Random(Guid.NewGuid().GetHashCode());

            WeightMeasurement expected = new WeightMeasurement();
            expected.EntryDate = DateTime.UtcNow.AddDays(r.Next(1, 100) * -1);
            expected.Id = Guid.NewGuid();
            expected.Unit = "Pounds";
            expected.Weight = (double)(r.Next(60, 300) + (r.Next(0, 9) / 10.0d));
            return expected;
        }
    }
}
