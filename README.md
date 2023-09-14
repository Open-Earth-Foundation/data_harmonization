# data_harmonization
Transform data between different data schemas


**POC scripts for transformation**

IFRS -> EFRAG
Python code to transform between a simulated and abbreviated IFRS schema to a simulated and abbreviated EFRAG schema

https://github.com/Open-Earth-Foundation/data_harmonization/blob/main/ifrs_to_efrag_poc.py

Matching

IFRS periodOfReport.yearOfReport            -->  EFRAG reportingScope.reportingYear  
IFRS periodOfReport.yearOfBaseline          -->  EFRAG reportingScope.baselineYear  
IFRS periodOfReport.yearOfTarget            -->  EFRAG reportingScope.targetYear  

IFRS scope1and2GHGEmissions.grossScope1GHGEmissions.value           -->  EFRAG greenHouseGas(GHG)Reporting.ghgEmissions(CO2e)  

IFRS scope1and2GHGEmissions.grossLocationBasedScope2GHGEmissions.value   -->  EFRAG indirectGHGEmissionCalculationMethods.locationBasedCalculation.ghgEmissions(CO2e)  

IFRS scope1and2GHGEmissions.grossMarketBasedScope2GHGEmissions.value   -->  EFRAG indirectGHGEmissionCalculationMethods.marketBasedCalculation.ghgEmissions(CO2e)  

IFRS grossScope3GHGEmissions.value     -->  EFRAG scope3GHGEmissionCategories.totalScope3GHGEmissions.ghgEmissions(CO2e)  




EFRAG -> IFRS
Python code to transform between a simulated and abbreviated EFRAG schema to a simulated and abbreviated IFRS schema

https://github.com/Open-Earth-Foundation/data_harmonization/blob/main/efrag_to_ifrs_poc.py

Matching

EFRAG                                          IFRS
-----                                          ----

E1 - DR E1- 07.0-Scope 1 GHG Emissions    ->    greenhouseGasEmissions.scope1and2GHGEmissions.grossScope1GHGEmissions
E1 - DR E1-08.0 - Scope 2 GHG Emissions (location-based) -> greenhouseGasEmissions.scope1and2GHGEmissions.grossLocationBasedScope2GHGEmissions
E1 - DR E1-08.0 - Scope 2 GHG Emissions (market-based)  -> greenhouseGasEmissions.grossMarketBasedScope2GHGEmissions
E1 - DR E1-09.0 - Scope 3 GHG Emissions  ->    greenhouseGasEmissions.grossScope3GHGEmissions
E1 - DR E1- 07.0-Scope 1 + E1 - DR E1-08.0 - Scope 2 GHG Emissions (location-based) -> greenhouseGasEmissions.scope1and2GHGEmissions.grossScope1and2GHGEmissions






