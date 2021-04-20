using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Metriks.E2E
{
    public class ServerLauncher: IDisposable
    {
        private Boolean _isDisposed;

        private Process _process;

        public void Dispose()
        {
            Dispose(true);
        }

        public static ServerLauncher Start()
        {
            var instance = new ServerLauncher();
            instance.InternalStart();
            return instance;
        }

        private void InternalStart()
        {
            var info = new ProcessStartInfo(@"C:\WeekendProject\github\100-days-of-code\src\Metriks\Metriks.Service\e2e-launch.bat")
            {
                WindowStyle = ProcessWindowStyle.Normal,
                ErrorDialog = true,
                LoadUserProfile = false,
                CreateNoWindow = false,
                UseShellExecute = false
            };

            StartProcess(info);
            //var startThread = new Thread(() => StartProcess(info))
            //{
            //    IsBackground = true
            //};

            //startThread.Start();
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


        private void StartProcess(ProcessStartInfo info)
        {
            try
            {
                _process = Process.Start(info);

               // _process.WaitForExit();
            }
            catch (Exception)
            {
                Dispose();
            }
        }
    }
}
