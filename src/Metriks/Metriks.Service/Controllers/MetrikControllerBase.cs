using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Metriks.Service.Controllers
{
    public class MetrikControllerBase : ControllerBase
    {
        internal UriBuilder GetBaseUri()
        {
            UriBuilder uriBuilder = new UriBuilder();
            uriBuilder.Scheme = HttpContext.Request.Scheme;
            var host = HttpContext.Request.Host.ToString();
                       
            if (host.Contains(":"))
            {
                var parts = host.Split(":");
                if (int.TryParse(parts[1], out int port))
                {
                    // There was a port in the host, update the host
                    host = parts[0];
                    uriBuilder.Port = port;
                }
            }

            uriBuilder.Host = host;
            return uriBuilder;
        }

        internal Uri AppendIdToCurrentPath(string id)
        {
            var uriBuilder = GetCurrentPathUri();
            uriBuilder.Path += "/" + id;
            return uriBuilder.Uri;
        }
        internal UriBuilder GetCurrentPathUri()
        {
            var uriBuilder = GetBaseUri();
            uriBuilder.Path = HttpContext.Request.Path.ToString();
            return uriBuilder;
        }

        internal UriBuilder GetCurrentRequestUri()
        {
            var uriBuilder = GetCurrentPathUri();
            uriBuilder.Query = HttpContext.Request.Query.ToString();
            return uriBuilder;
        }
    }
}
