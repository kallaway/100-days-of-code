using System;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Threading;

namespace Metriks.E2E.Common
{
    internal class IisExpress : IDisposable
    {
        private bool _isDisposed;

        private Process _process;

        public void Dispose()
        {
            Dispose(true);
        }

        public void Start(string configPath, string workingDirectory)
        {
            var iisExpressPath = DetermineIisExpressPath();
            var arguments = string.Format(CultureInfo.InvariantCulture, "/config:\"{0}\"", configPath);

            var info = new ProcessStartInfo(iisExpressPath)
            {
                WindowStyle = ProcessWindowStyle.Normal,
                ErrorDialog = true,
                //LoadUserProfile = false,
                CreateNoWindow = false,
                WorkingDirectory = workingDirectory,
                UseShellExecute = false,
                Arguments = arguments
            };

            info.EnvironmentVariables.Add("ASPNETCORE_ENVIRONMENT", "Development");
            info.EnvironmentVariables.Add("LAUNCHER_PATH", @"bin\Debug\net5.0\Metriks.Service.exe");

            var startThread = new Thread(() => StartIisExpress(info))
            {
                IsBackground = true
            };

            startThread.Start();
        }

        protected virtual void Dispose(bool disposing)
        {
            if (_isDisposed)
            {
                return;
            }

            if (disposing)
            {
                if (_process.HasExited == false)
                {
                    _process.Kill();
                }

                _process.Dispose();
            }

            _isDisposed = true;
        }

        private static string DetermineIisExpressPath()
        {
            string iisExpressPath;

            iisExpressPath = Environment.GetFolderPath(Environment.Is64BitOperatingSystem
                ? Environment.SpecialFolder.ProgramFilesX86
                : Environment.SpecialFolder.ProgramFiles);

            iisExpressPath = Path.Combine(iisExpressPath, @"IIS Express\iisexpress.exe");

            return iisExpressPath;
        }

        private void StartIisExpress(ProcessStartInfo info)
        {
            try
            {
                _process = Process.Start(info);
                _process.WaitForExit();
            }
            catch (Exception)
            {
                Dispose();
            }
        }
    }
}
