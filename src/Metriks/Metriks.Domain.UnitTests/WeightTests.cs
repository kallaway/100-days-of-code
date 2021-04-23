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

        #region Get List
        [TestMethod]
        [Scenario("Get weight list should return at least 2 items")]
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
            List<WeightMeasurement> actual = bizLogic.Read();

            // Assert
           Assert.IsTrue(actual.Count >= 2, $"Expected at least 2 items, but there was only {actual.Count} items.");
        }


        #endregion

        #region Get by ID
        [TestMethod]
        [Scenario("Get weight measurement by valid ID")]
        [Given("an end-user is trying to retrieve a weight measurement")]
        [When("a valid ID for an existing weight measurement is entered")]
        [Then("a weight measure is returned")]
        public void Get_weight_measurement_by_valid_ID()
        {
            // Arrange
            Weight bizLogic = new Weight();
            var expected = bizLogic.Create(GenerateRandomWeightMeasurement());
           
            // Act
            WeightMeasurement actual = bizLogic.Read(expected.measurement.Id);

            // Assert
            Assert.AreEqual(expected.measurement.Id, actual.Id);
        }
        #endregion

        #region Delete
        [TestMethod]
        [Scenario("Delete weight measurement by valid ID")]
        [Given("an end-user is trying to delete a weight measurement")]
        [When("a valid ID for an existing weight measurement is entered")]
        [Then("the specified weight measure is deleted and a 'true' response is returned")]
        public void Delete_weight_measurement_by_valid_ID()
        {
            // Arrange
            Weight bizLogic = new Weight();
            var expectedId = Guid.NewGuid();
            _ = bizLogic.Create(GenerateRandomWeightMeasurement(expectedId));

            // Act
            bool actual = bizLogic.Delete(expectedId);

            // Assert
            Assert.IsTrue(actual);
        }

        [TestMethod]
        [Scenario("Delete weight measurement twice should fail the second time")]
        [Given("an end-user is trying to delete a weight measurement")]
        [When("a valid ID for an existing weight measurement is deleted twice")]
        [Then("the specified weight measure is deleted the first time and fails on the second attempt")]
        public void Delete_weight_measurement_twice_should_fail_the_second_time()
        {
            // Arrange
            Weight bizLogic = new Weight();
            var expectedId = Guid.NewGuid();
            _ = bizLogic.Create(GenerateRandomWeightMeasurement(expectedId));

            // Act
            bool initialResult = bizLogic.Delete(expectedId);
            bool secondResult = bizLogic.Delete(expectedId);

            // Assert
            Assert.IsTrue(initialResult, "Expected the initial delete to succeed");
            Assert.IsFalse(secondResult, "Expected the second delete to fail");
        }
        #endregion

        private static WeightMeasurement GenerateRandomWeightMeasurement()
        {
            return GenerateRandomWeightMeasurement(Guid.NewGuid());
        }
            private static WeightMeasurement GenerateRandomWeightMeasurement(Guid id)
        {
            Random r = new Random(Guid.NewGuid().GetHashCode());

            WeightMeasurement expected = new WeightMeasurement();
            expected.EntryDate = DateTime.UtcNow.AddDays(r.Next(1, 100) * -1);
            expected.Id = id;
            expected.Unit = "Pounds";
            expected.Weight = (double)(r.Next(60, 300) + (r.Next(0, 9) / 10.0d));
            return expected;
        }
    }
}
