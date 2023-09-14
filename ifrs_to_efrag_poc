def transform_ifrs_to_efrag(ifrs_data):
    # Extracting IFRS Data
    year_report = ifrs_data["greenhouseGasEmissions"]["periodOfReport"]["yearOfReport"]
    year_baseline = ifrs_data["greenhouseGasEmissions"]["periodOfReport"]["yearOfBaseline"]
    year_target = ifrs_data["greenhouseGasEmissions"]["periodOfReport"]["yearOfTarget"]

    scope1_value = ifrs_data["greenhouseGasEmissions"]["scope1and2GHGEmissions"]["grossScope1GHGEmissions"]["value"]
    location_based_scope2_value = ifrs_data["greenhouseGasEmissions"]["scope1and2GHGEmissions"]["grossLocationBasedScope2GHGEmissions"]["value"]
    market_based_scope2_value = ifrs_data["greenhouseGasEmissions"]["grossMarketBasedScope2GHGEmissions"]["value"]
    scope3_value = ifrs_data["greenhouseGasEmissions"]["grossScope3GHGEmissions"]["value"]

    # Transforming to EFRAG Schema
    efrag_data = {
        "E1 - DR E1- 07.0-Scope 1 Green House Gas (GHG) Emissions": [{
            "reportingScope": {
                "reportingYear": year_report,
                "baselineYear": year_baseline,
                "targetYear": year_target,
                "emissionScope": "Scope 1"
            },
            "greenHouseGas(GHG)Reporting": {
                "ghgEmissions(CO2e)": scope1_value
            }
        }],
        "E1 - DR E1-08.0 - Scope 2 Green House Gas (GHG) Emissions": [{
            "reportingScope": {
                "reportingYear": year_report,
                "baselineYear": year_baseline,
                "targetYear": year_target,
                "emissionScope": "Scope 2"
            },
            "indirectGHGEmissionCalculationMethods": {
                "marketBasedCalculation": {
                    "ghgEmissions(CO2e)": market_based_scope2_value
                },
                "locationBasedCalculation": {
                    "ghgEmissions(CO2e)": location_based_scope2_value
                }
            }
        }],
        "E1 - DR E1-09.0 - Scope 3 Green House Gas (GHG) Emissions": [{
            "reportingScope": {
                "reportingYear": year_report,
                "baselineYear": year_baseline,
                "targetYear": year_target,
                "emissionScope": "Scope 3"
            },
            "scope3GHGEmissionCategories": {
                "totalScope3GHGEmissions": {
                    "ghgEmissions(CO2e)": scope3_value
                }
            }
        }],
        "E1 - DR E1-10.1 - Total Green House Gas (GHG) Emissions": [{
            "reportingScope": {
                "reportingYear": year_report,
                "baselineYear": year_baseline,
                "targetYear": year_target,
                "emissionScope": "Total GHG Emissions (Scope 1, 2 and 3)"
            },
            "totalGHGEmissions": {
                "ghgEmissions(CO2e)": scope1_value + location_based_scope2_value + scope3_value
            },
            "indirectGHGEmissionCalculationMethods": {
                "marketBasedCalculation": {
                    "ghgEmissions(CO2e)": market_based_scope2_value
                },
                "locationBasedCalculation": {
                    "ghgEmissions(CO2e)": location_based_scope2_value
                }
            }
        }]
    }

    return efrag_data

ifrs_sample_data = {
  #... (as provided above)
}

efrag_transformed_data = transform_ifrs_to_efrag(ifrs_sample_data)
print(efrag_transformed_data)
