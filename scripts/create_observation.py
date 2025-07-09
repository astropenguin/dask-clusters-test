# standard library
from pathlib import Path


# dependencies
import dask.array as da
import numpy as np
import xarray as xr
from dask.distributed import Client, LocalCluster


# constants
DATA = Path("data")
DIMS = ("time", "chan")
SHAPE = (1000000, 10000)
CHUNKS = (1000, 1000)


def main() -> None:
    with LocalCluster() as cluster, Client(cluster) as client:
        array = xr.DataArray(
            da.random.normal(size=SHAPE, chunks=CHUNKS),
            dims=DIMS,
            coords={
                "time": np.arange(SHAPE[0]),
                "chan": np.arange(SHAPE[1]),
            },
        )
        array.to_zarr(DATA / "observation.zarr", mode="w")


if __name__ == "__main__":
    main()
