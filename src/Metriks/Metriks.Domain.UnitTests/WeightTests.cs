using Metriks.Domain.Models;
using Metriks.Domain.UnitTests.Common;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;

namespace Metriks.Domain.UnitTests
{
    [TestClass]
    public class WeightTests
    {
        [TestMethod]
        [Scenario("Create weight should populate an empty ID")]
        [Given("a weight measurement has an empty Id")]
        [When("Create is executed")]
        [Then("the weight measurement is added to the datastore and the ID is populated")]
        public void Create_weight_should_populate_an_empty_ID()
        {
            // Arrange
            var expectedId = Guid.Empty;
            WeightMeasurement expected = new WeightMeasurement();
            expected.EntryDate = DateTime.UtcNow;
            expected.Id = expectedId;
            expected.Unit = "Pounds";
            expected.Weight = 185.5f;

            // Act
            Weight bizLogic = new Weight();
            var actual = bizLogic.Create(expected);

            // Assert
            Assert.AreEqual(expected.EntryDate, actual.EntryDate, "EntryDate does not match.");
            Assert.AreNotEqual(expectedId, actual.Id, "Id is still empty.");
            Assert.AreEqual(expected.Unit, actual.Unit, "Unit does not match.");
            Assert.AreEqual(expected.Weight, actual.Weight, "Weight does not match.");
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
            WeightMeasurement expected = new WeightMeasurement();
            expected.EntryDate = DateTime.UtcNow;
            expected.Id = expectedId;
            expected.Unit = "Pounds";
            expected.Weight = 185.5f;

            // Act
            Weight bizLogic = new Weight();
            var actual = bizLogic.Create(expected);

            // Assert
            Assert.AreEqual(expected.EntryDate, actual.EntryDate, "EntryDate does not match.");
            Assert.AreEqual(expectedId, actual.Id, "Id does not match.");
            Assert.AreEqual(expected.Unit, actual.Unit, "Unit does not match.");
            Assert.AreEqual(expected.Weight, actual.Weight, "Weight does not match.");

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

            WeightMeasurement original = new WeightMeasurement();
            original.EntryDate = DateTime.UtcNow;
            original.Id = originalId;
            original.Unit = "Pounds";
            original.Weight = 185.5f;

            WeightMeasurement expected = new WeightMeasurement();
            expected.EntryDate = DateTime.UtcNow;
            expected.Id = originalId;
            expected.Unit = "Pounds";
            expected.Weight = 150.0f;

            // Act
            Weight bizLogic = new Weight();
            _ = bizLogic.Create(original);
            var actual = bizLogic.Create(expected);

            // Assert
            // TODO: Should we return a tuple <bool, WeightMeasurement> or should we throw or return null
            Assert.IsNull(actual);            
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
            var actual = bizLogic.Create(null);

            // Assert
           
        }

      
    }
}
