using System;

namespace Metriks.E2E.Common
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