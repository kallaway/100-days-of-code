using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.Domain.UnitTests
{
    [TestClass()]
    public static class AssemblySetupTeardown
    {

        [AssemblyInitialize]
        public static void AssemblyInit(TestContext context)
        {
            Data.DbContext dbContext = new Data.DbContext();
            dbContext.Init();
        }


        [AssemblyCleanup]
        public static void AssemblyCleanup()
        {

        }
    }
}
