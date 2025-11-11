import pypsa
import pandas as pd
import numpy as np


def adjust_cost(n, cost_var, tech):

    if tech == "offshore_cost":
        n.generators.loc[n.generators.carrier == "offwind-ac", "capital_cost"] = n.generators.loc[n.generators.carrier == "offwind-ac", "capital_cost"] * (1+0.01*cost_var)
        n.generators.loc[n.generators.carrier == "offwind-dc", "capital_cost"] = n.generators.loc[n.generators.carrier == "offwind-dc", "capital_cost"] * (1+0.01*cost_var)

    elif tech == "storage_tank_cost":

        # Add cost to export store (in case the "virtual" export store cost is set to zero)
        idx = n.stores.loc[n.stores.carrier == "H2"].index
        idx = idx[idx != "H2 export store"]
        n.stores.loc["H2 export store", "capital_cost"] = n.stores.loc[idx].capital_cost.mean()

        # Variation of cost
        n.stores.loc[n.stores.carrier == "H2", "capital_cost"] = n.stores.loc[n.stores.carrier == "H2", "capital_cost"] * (1+0.01*cost_var)

    elif tech == "electrolyzer_cost":
        n.links.loc[n.links.carrier == "H2 Electrolysis", "capital_cost"] = n.links.loc[n.links.carrier == "H2 Electrolysis", "capital_cost"] * (1+0.01*cost_var)

    print(f"Adjusted cost of {tech} by {cost_var}%")

    return n


if __name__ == "__main__":

    if "snakemake" not in globals():
        from _helpers import mock_snakemake

        snakemake = mock_snakemake(
            "prepare_sensitivity",
        )

    # Get variation from config
    cost_var = int(snakemake.wildcards.cost_var)
    tech = snakemake.wildcards.tech

    n = pypsa.Network(snakemake.input.network)

    adjust_cost(n, cost_var, tech)

    n.export_to_netcdf(snakemake.output.network)