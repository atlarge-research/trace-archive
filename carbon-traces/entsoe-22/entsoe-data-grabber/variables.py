CO2_best = {
    "Mixed":0,
    "Fossil Brown coal/Lignite":800,
    "Fossil Coal-derived gas":279,
    "Fossil Gas":128,
    "Fossil Hard coal":600,
    "Fossil Oil":530,
    "Fossil Oil shale":385,
    "Fossil Peat":126,
    "Geothermal":11,
    "Hydro Pumped Storage":0,
    "Hydro Run-of-river and poundage":2,
    "Hydro Water Reservoir":6.1,
    "Marine":0,
    "Nuclear":5.1,
    "Other renewable":0,
    "Solar":8,
    "Waste":376,
    "Wind Offshore":12,
    "Wind Onshore":7.8,
    "Other":0,
    "Biomass":8.5,
}

CO2_best_aggregated = {
   "Mixed\nActual Aggregated": 0,
    "Fossil Brown coal/Lignite\nActual Aggregated": 800,
    "Fossil Coal-derived gas\nActual Aggregated": 279,
    "Fossil Gas\nActual Aggregated": 128,
    "Fossil Hard coal\nActual Aggregated": 600,
    "Fossil Oil\nActual Aggregated": 530,
    "Fossil Oil shale\nActual Aggregated": 385,
    "Fossil Peat\nActual Aggregated": 126,
    "Geothermal\nActual Aggregated": 11,
    "Hydro Pumped Storage\nActual Aggregated": 0,
    "Hydro Run-of-river and poundage\nActual Aggregated": 2,
    "Hydro Water Reservoir\nActual Aggregated": 6.1,
    "Marine\nActual Aggregated": 0,
    "Nuclear\nActual Aggregated": 5.1,
    "Other renewable\nActual Aggregated": 0,
    "Solar\nActual Aggregated": 8,
    "Waste\nActual Aggregated": 376,
    "Wind Offshore\nActual Aggregated": 12,
    "Wind Onshore\nActual Aggregated": 7.8,
    "Other\nActual Aggregated": 0,
    "Biomass\nActual Aggregated": 8.5
}

CO2_worst = {
    "Mixed":0,
    "Fossil Brown coal/Lignite":1300,
    "Fossil Coal-derived gas":849,
    "Fossil Gas":434,
    "Fossil Hard coal":1050,
    "Fossil Oil":900,
    "Fossil Oil shale":385,
    "Fossil Peat":262,
    "Geothermal":47,
    "Hydro Pumped Storage":0,
    "Hydro Run-of-river and poundage":5,
    "Hydro Water Reservoir":11,
    "Marine":0,
    "Nuclear":6.4,
    "Other renewable":0,
    "Solar":83,
    "Waste":376,
    "Wind Offshore":23,
    "Wind Onshore":16,
    "Other":0,
    "Biomass":130,
}

EnergyTypeCat = {
    "Mixed": {"renewable": False, "green": False},
    "Biomass": {"renewable": True, "green": True},
    "Fossil Brown coal/Lignite": {"renewable": False, "green": False},
    "Fossil Coal-derived gas": {"renewable": False, "green": False},
    "Fossil Gas": {"renewable": False, "green": False},
    "Fossil Hard coal": {"renewable": False, "green": False},
    "Fossil Oil": {"renewable": False, "green": False},
    "Fossil Oil shale": {"renewable": False, "green": False},
    "Fossil Peat": {"renewable": False, "green": False},
    "Geothermal": {"renewable": True, "green": True},
    "Hydro Pumped Storage": {"renewable": True, "green": True},
    "Hydro Run-of-river and poundage": {"renewable": True, "green": True},
    "Hydro Water Reservoir": {"renewable": True, "green": True},
    "Marine": {"renewable": True, "green": True},
    "Nuclear": {"renewable": False, "green": True},
    "Other renewable": {"renewable": True, "green": True},
    "Solar": {"renewable": True, "green": True},
    "Waste": {"renewable": False, "green": False},
    "Wind Offshore": {"renewable": True, "green": True},
    "Wind Onshore": {"renewable": True, "green": True},
    "Other": {"renewable": False, "green": False},
}

graph_colors = [ '#0077BB', '#EE7733', '#009988', '#33BBEE', '#EE3377', '#CC3311', '#BBBBBB']

country_codes = [
    "AT",  # Austria - yes
    "AL",  # Albania - yes
    "BE",  # Belgium - yes
    "BA",  # Bosnia and Herzegovina - yes
    "BG",  # Bulgaria - yes
    "HR",  # Croatia - yes
    "CZ",  # Czech Republic
    "DK",  # Denmark - yes
    "EE",  # Estonia - yes
    "FI",  # Finland - yes
    "FR",  # France - yes
    "DE",  # Germany - yes
    "GR",  # Greece - yes
    "HU",  # Hungary - yes
    "IE",  # Ireland - no
    "IT",  # Italy - yes
    "LV",  # Latvia - yes
    "LT",  # Lithuania - yes
    "LU",  # Luxembourg - yes
    "MK",  # Macedonia (officially known as North Macedonia now) - yes
    "ME",  # Montenegro - no - issues "NaN"
    "NL",  # Netherlands - yes
    "NO",  # Norway - yes
    "PL",  # Poland - yes
    "PT",  # Portugal - yes
    "RO",  # Romania - yes
    "RS",  # Serbia - yes
    "SK",  # Slovakia - yes
    "SI",  # Slovenia - yes
    "ES",  # Spain - yes
    "SE",  # Sweden - yes
    "CH",  # Switzerland - yes
    "GB"   # United Kingdom - no
]
