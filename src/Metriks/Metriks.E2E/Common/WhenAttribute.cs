using System;

namespace Metriks.E2E.Common
{
    internal class WhenAttribute : Attribute
    {
        public string Action { get; set; }

        public WhenAttribute(string action)
        {
            Action = action;
        }
    }
}