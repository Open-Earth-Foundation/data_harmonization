def efrag_to_ifrs(efrag_data):
    # Extracting the necessary data from EFRAG
    scope1 = efrag_data["E1 - DR E1- 07.0-Scope 1 Green House Gas (GHG) Emissions"][0]
    scope2 = efrag_data["E1 - DR E1-08.0 - Scope 2 Green House Gas (GHG) Emissions"][0]
    scope3 = efrag_data["E1 - DR E1-09.0 - Scope 3 Green House Gas (GHG) Emissions"][0]

    # Transforming the data to IFRS
    ifrs_data = {
        "greenhouseGasEmissions": {
            "periodOfReport": {
                "yearOfReport": scope1["reportingScope"]["reportingYear"],
                "yearOfBaseline": scope1["reportingScope"]["baselineYear"],
                "yearOfTarget": scope1["reportingScope"]["targetYear"]
            },
            "scope1and2GHGEmissions": {
                "grossScope1GHGEmissions": {
                    "value": scope1["greenHouseGas(GHG)Reporting"]["ghgEmissions(CO2e)"],
                    "description": "Absolute gross scope 1 greenhouse gas emissions generated during the reporting period...",
                    "unit": "Metric tons (t) CO₂-e"
                },
                "grossLocationBasedScope2GHGEmissions": {
                    "value": scope2["indirectGHGEmissionCalculationMethods"]["locationBasedCalculation"]["ghgEmissions(CO2e)"],
                    "description": "Absolute gross location-based scope 2 greenhouse gas emissions generated...",
                    "unit": "Metric tons (t) CO₂-e"
                },
                "grossScope1and2GHGEmissions": {
                    "value": scope1["greenHouseGas(GHG)Reporting"]["ghgEmissions(CO2e)"] + scope2["indirectGHGEmissionCalculationMethods"]["locationBasedCalculation"]["ghgEmissions(CO2e)"],
                    "description": "The sum of gross scope 1 and location-based scope 2 greenhouse gas emissions generated...",
                    "unit": "Metric tons (t) CO₂-e"
                }
            },
            "grossScope3GHGEmissions": {
                "value": scope3["scope3GHGEmissionCategories"]["totalScope3GHGEmissions"]["ghgEmissions(CO2e)"],
                "scope3CategoriesIncluded": ",".join(scope3["scope3GHGEmissionCategories"].keys()),
                "description": "Absolute gross scope 3 greenhouse gas emissions generated...",
                "unit": "Metric tons (t) CO₂-e"
            },
            "grossMarketBasedScope2GHGEmissions": {
                "value": scope2["indirectGHGEmissionCalculationMethods"]["marketBasedCalculation"]["ghgEmissions(CO2e)"],
                "description": "Absolute gross market-based scope 2 greenhouse gas emissions generated...",
                "unit": "Metric tons (t) CO₂-e"
            }
        }
    }

    return ifrs_data

efrag_sample = {
    #... [Your EFRAG data sample]
}
transformed_data = efrag_to_ifrs(efrag_sample)
print(transformed_data)
