using System;

namespace Metriks.Domain.UnitTests.Common
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