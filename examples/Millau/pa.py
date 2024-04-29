import sys
sys.path.insert(0,"../..")

from mobility.radiation_departments import *

dep =["19"]
Age=3

(
    sources_territory,
    sinks_territory,
    costs_territory,
    coordinates,
    raw_flowDT,
) = get_data_for_model_school(dep,1)



flowsRM, flowDT, coordinates_res, plot_sources=run_model_for_territory(sources_territory, sinks_territory, costs_territory, coordinates, raw_flowDT)
# print (compute_similarity_index(flowsRM, flowDT))
