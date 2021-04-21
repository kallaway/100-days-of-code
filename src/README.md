### Project Plan
What should I build:
* Metric API service

Metric Topics:
* Weight
* Exercise (Run)
* Nutritional Macros (Calories / Nutrients / Fat / Protein / Carbs)


POST /Weight 
{
	DateTime: string (ISO),
	Value: 185.5,
	Unit: string ("pounds", "kilograms", "ounces", "stones")
}

Weight:
Date Time - Measurement - Units - Person (Identifier)
Units:  Mass - Grams/Kilograms, Pounds, Ounces

Height:
Date Time - Measurement - Units - Person (Identifier)
Units: Length - Meters, Feet


API Calls:
Start Date Time - End Date Time - Measurement - Units - System - Endpoint
Units: Calls / Period


Error Incidents:
Start Date Time - End Date Time - Measurement - Units - System - Error Type
Units: Incidents / Period

Things I've Built Before:
* Credit Card Processing Platform
* Document Management System
* Games