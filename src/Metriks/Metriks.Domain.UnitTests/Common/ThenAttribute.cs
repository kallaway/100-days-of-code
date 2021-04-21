using System;

namespace Metriks.Domain.UnitTests.Common
{
    internal class ThenAttribute : Attribute
    {
        public string Outcome { get; set; }

        public ThenAttribute(string outcome)
        {
            Outcome = outcome;
        }
    }
}