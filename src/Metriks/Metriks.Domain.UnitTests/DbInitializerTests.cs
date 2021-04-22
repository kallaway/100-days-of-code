using Metriks.Domain.Data;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.Domain.UnitTests
{
    [TestClass]
    public class DbInitializerTests
    {
        [TestMethod]
        public void TestDbInit()
        {
            // Arrange
            DbContext db = new DbContext();

            // Act
            bool result = db.Init();

            // Assert
            Assert.IsTrue(result);

        }
    }
 
}
