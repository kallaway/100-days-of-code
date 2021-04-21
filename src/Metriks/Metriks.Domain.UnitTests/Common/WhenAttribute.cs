using System;

namespace Metriks.Domain.UnitTests.Common
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