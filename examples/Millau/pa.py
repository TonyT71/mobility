import sys
sys.path.insert(0,"../..")

from mobility.radiation_departments import *

from mobility.radiation_model import radiation_model


dep =["19"]
Age=2

(
    sources_territory,
    sinks_territory,
    costs_territory,
    coordinates,
    raw_flowDT,
) = get_data_for_model_school_map(dep, Age)


# test = radiation_model(sources_territory, sinks_territory, costs_territory, alpha=0, beta=1)[0]

# flowsRM, flowDT, coordinates_res, plot_sources=run_model_for_territory(sources_territory, sinks_territory, costs_territory, coordinates, raw_flowDT)
# print (compute_similarity_index(flowsRM, flowDT))

run_model_for_territory(sources_territory, sinks_territory, costs_territory, coordinates, raw_flowDT)