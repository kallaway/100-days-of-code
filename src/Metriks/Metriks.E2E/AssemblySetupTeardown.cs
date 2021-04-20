using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.E2E
{
    [TestClass()]
    public static class AssemblySetupTeardown
    {
        private static IisExpress _iisExpress = null;

        [AssemblyInitialize]
        public static void AssemblyInit(TestContext context)
        {

            string solutionFolder = GetSolutionFolder(System.IO.Path.GetFullPath("."));

            var workingDirectory = System.IO.Path.Combine(solutionFolder, @"Metriks.Service");
            var configPath = System.IO.Path.Combine(solutionFolder, @".vs\Metriks\config\applicationhost.config");
            _iisExpress = new IisExpress();

            _iisExpress.Start(configPath, workingDirectory);
            // Executes once before the test run. (Optional)

        }

        private static string GetSolutionFolder(string currentPath)
        {
            // Check to see if there is a .vs folder
            var vsPath = System.IO.Path.Combine(currentPath, ".vs");

            if (System.IO.Directory.Exists(vsPath))
            {
                return currentPath;
            }

            // Find the parent folder
            var parentPath = System.IO.Directory.GetParent(currentPath);

            // Make sure the parent is not the same as the current path
            if (parentPath.FullName == currentPath)
            {
                throw new ApplicationException("Recursed through the tree and could not find a .vs folder.");
            }

            return GetSolutionFolder(parentPath.FullName);
        }

        [AssemblyCleanup]
        public static void AssemblyCleanup()
        {
            _iisExpress.Dispose();
            // Executes once after the test run. (Optional)
        }
    }
}
