using System;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Threading;

namespace Metriks.E2E
{
    public class IisExpress : IDisposable
    {
        private Boolean _isDisposed;

        private Process _process;

        public void Dispose()
        {
            Dispose(true);
        }

        public static IisExpress Start(String configPath)
        {
            var instance = new IisExpress();
            instance.InternalStart(configPath);
            return instance;
        }


        private void InternalStart(String configPath)
        {
            var iisExpressPath = DetermineIisExpressPath();
            var arguments = String.Format(
                CultureInfo.InvariantCulture, "/config:\"{0}\"", configPath);

            var info = new ProcessStartInfo(iisExpressPath)
            {
                WindowStyle = ProcessWindowStyle.Normal,
                ErrorDialog = true,
                LoadUserProfile = true,
                CreateNoWindow = false,
                UseShellExecute = false,
                WorkingDirectory = @"C:\WeekendProject\github\100-days-of-code\src\Metriks\Metriks.Service\",
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

        protected virtual void Dispose(Boolean disposing)
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

        private static String DetermineIisExpressPath()
        {
            String iisExpressPath;

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
