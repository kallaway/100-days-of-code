using System;

namespace Metriks.Domain.UnitTests.Common
{
    public class ScenarioAttribute : Attribute
    {
        public string Description { get; set; }

        public ScenarioAttribute(string description)
        {
            Description = description;
        }
    }
}