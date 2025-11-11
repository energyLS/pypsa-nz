import pypsa
import pandas as pd
import numpy as np


def adjust_cost(n, electrolyzer_cost):


    n.links.loc[n.links.carrier == "H2 Electrolysis", "capital_cost"] = n.links.loc[n.links.carrier == "H2 Electrolysis", "capital_cost"] * (1+0.01*electrolyzer_cost)

    print(f"Adjusted cost by {electrolyzer_cost}%")

    return n


if __name__ == "__main__":

    if "snakemake" not in globals():
        from _helpers import mock_snakemake

        snakemake = mock_snakemake(
            "prepare_sensitivity",
        )

    # Get variation from config
    electrolyzer_cost = int(snakemake.wildcards.cost_var)

    n = pypsa.Network(snakemake.input.network)

    adjust_cost(n, electrolyzer_cost)

    n.export_to_netcdf(snakemake.output.network)