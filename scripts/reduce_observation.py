# standard library
from pathlib import Path


# dependencies
import xarray as xr
from dask.distributed import Client, LocalCluster


# constants
DATA = Path("data")


def main() -> None:
    with LocalCluster() as cluster, Client(cluster) as client:
        input("Input any key to start processing.")

        array = xr.open_dataarray(DATA / "observation.zarr", chunks="auto")
        spec = array.mean("time")
        noise = array.std("time")
        spec = spec.assign_coords(noise=noise)
        spec.to_zarr(DATA / "spectrum.zarr", mode="w")


if __name__ == "__main__":
    main()
