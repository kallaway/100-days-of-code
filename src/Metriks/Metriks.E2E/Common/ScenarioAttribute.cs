using System;

namespace Metriks.E2E.Common
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