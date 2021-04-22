using System;

namespace Metriks.E2E.Common
{
    public class GivenAttribute : Attribute
    {
        public string Condition { get; set; }

        public GivenAttribute(string condition)
        {
            Condition = condition;
        }
    }
}