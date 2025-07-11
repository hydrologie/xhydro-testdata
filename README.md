# xhydro-testdata

Testing data to support the xHydro and xDatasets projects.

## Contributing

In order to add a new dataset to the `xHydro`/`xDatasets` testing data, please ensure you perform the following:

1. Create a new branch: `git checkout -b my_new_testdata_branch`
2. Place your dataset within an appropriate subdirectory (or create a new one: `mkdir data`).
3. Run the md5 checksum generation script: `python report_check_sums.py`
4. Commit your changes: `git add * && git commit -m "added my_new_testdata"`
5. Open a Pull Request.

If you wish to perform preliminary tests against the dataset on a particular branch/commit, this can be done with the following procedure:

* To gather a single file:
```python
import pooch

GITHUB_URL = "https://github.com/hydrologie/xhydro-testdata"
BRANCH_OR_COMMIT_HASH = "my_development_branch"

test_data_path = pooch.retrieve(
    url=f"{GITHUB_URL}/raw/{BRANCH_OR_COMMIT_HASH}/data/my_test_data.nc",
    known_hash="sha256:1234567890abcdef",
)

# If your testing data is `xarray`-readable, you can then use the following:
import xarray as xr

ds = xr.open_dataset(test_data_path)
```

## Loading data

If you wish to load data from this repository, this can be done with the following procedure:

* To gather a single file (using the `streamflow_BCC-CSM1.1-m_rcp45.nc` file as an example):
```python
import pooch
import xarray as xr

GITHUB_URL = "https://github.com/hydrologie/xhydro-testdata"
BRANCH_OR_COMMIT_HASH = "main"

test_data_path = pooch.retrieve(
    url=f"{GITHUB_URL}/raw/{BRANCH_OR_COMMIT_HASH}/data/cc_indicators/streamflow_BCC-CSM1.1-m_rcp45.nc",
    known_hash="sha256:8699f40153abdea098d580f73b1f8ad64875823f0d8479fdc4f8a40b4adcaf5e",
)
ds = xr.open_dataset(test_data_path)
```

* To open multiple files stored within a zip archive (using the `reference.zip` file as an example):
```python
import pooch
import xarray as xr

GITHUB_URL = "https://github.com/hydrologie/xhydro-testdata"
BRANCH_OR_COMMIT_HASH = "main"

files = pooch.retrieve(
    url=f"{GITHUB_URL}/raw/{BRANCH_OR_COMMIT_HASH}/data/cc_indicators/reference.zip",
    known_hash="md5:192544f3a081375a81d423e08038d32a",
    processor=pooch.Unzip(),
)

# Exactly how you open the files depends on the structure of the data. This will work for the reference.zip file:
ds = xr.open_mfdataset(files, combine="nested", concat_dim="platform")
```

* You can also simply extract the files to a directory:
```python
from pathlib import Path
from zipfile import ZipFile

import pooch

GITHUB_URL = "https://github.com/hydrologie/xhydro-testdata"
BRANCH_OR_COMMIT_HASH = "main"

test_data_path = pooch.retrieve(
    url=f"{GITHUB_URL}/raw/{BRANCH_OR_COMMIT_HASH}/data/cc_indicators/reference.zip",
    known_hash="sha256:80e21de39a78da49f809ddf35bd2d21271828450ea2da71eac08aab13c7b846e",
)

directory_to_extract_to = Path(
    test_data_path
).parent  # To extract to the same directory as the zip file
with ZipFile(test_data_path, "r") as zip_ref:
    zip_ref.extractall(directory_to_extract_to)
    files = zip_ref.namelist()
```

[//]: # (Code below this line is autogenerated by `report_check_sums.py`)
## Available datasets

### Files

| File | Size | Checksum |
| ---- | ---- | -------- |
| use_case/deltas.zip | 57.9 kiB | sha256:70eb2da69550c1b839749cb5552bcd7b44196ff4d8ab7951c2e5254638a7b598 |
| ravenpy/ERA5_Riviere_Rouge_global.nc | 150.7 kiB | sha256:341ac746130a0d3e3189d3a41dc8528d6bd22869a519b68e134959407ad200a3 |
| ravenpy/Debit_Riviere_Rouge.nc | 343.5 kiB | sha256:d0a27de5eb3cb466e60669d894296bcbc4e9f590edc1ae2490685babd10b2d22 |
| pmp/CMIP.CCCma.CanESM5.historical.r1i1p1f1.fx.gn.zarr.zip | 12.7 kiB | sha256:dc7c92fc098ca5adf43e76b25e3f79b70815ed961e945952983bb68b3c380cf1 |
| pmp/CMIP.CCCma.CanESM5.historical.r1i1p1f1.day.gn.zarr.zip | 758.5 kiB | sha256:d5775b2f09381f2f3a7cc06af76f62fb216b60252aab3a602280a513554d59ad |
| optimal_interpolation/OI_data_corrected.zip | 3.2 MiB | sha256:48ee08325bd35c6bce5c0e52e3ee25df27c830720929060f607fb0417c476941 |
| optimal_interpolation/OI_data.zip | 2.9 MiB | sha256:9cd881a19fc82bda560e636d3f6a2c40718b82f5bce1e31aedce6d1b2e41d7d8 |
| hydro_modelling/ERA5_testdata.nc | 100.9 kiB | sha256:7051f696f30d9772511cfbae81a0be0bd2898f25d123227f5f5fa4869138fa4e |
| extreme_value_analysis/sea-levels_fremantle.zarr.zip | 5.6 kiB | sha256:af6abf274bf8809eca7fa0d33540979203fa4d9833e13c8e6adf3f4d15966a40 |
| extreme_value_analysis/rainfall_excedance.zarr.zip | 7.5 kiB | sha256:ce29ea4b4b427bac0c11c0bb1ead4bb961aee2ba88ac0abffc859a155986f232 |
| extreme_value_analysis/genpareto.zip | 136.0 kiB | sha256:f6b67160dd1373ad6a9ce511788184a0bbed23e0c297315d1686ecbb88e16e0a |
| extreme_value_analysis/genextreme.zip | 228.0 kiB | sha256:8d036acca8b9a4608930c97d6cebfbf24205a20c7e43c47dcbdc14221a643b0c |
| extreme_value_analysis/NOAA_GFDL_ESM4.zip | 88.7 kiB | sha256:483a5ffd398aa60db2d2c6d41857cd02c201a7f9efcacef2610a2521f72a22b6 |
| cc_indicators/streamflow_BCC-CSM1.1-m_rcp45.nc | 730.1 kiB | sha256:8699f40153abdea098d580f73b1f8ad64875823f0d8479fdc4f8a40b4adcaf5e |
| cc_indicators/reference.zip | 23.7 kiB | sha256:80e21de39a78da49f809ddf35bd2d21271828450ea2da71eac08aab13c7b846e |
| cc_indicators/deltas.zip | 1.6 MiB | sha256:d6bff404c7e1514d819db9e46c69a3756a0a5f847586fc2fa4e573de3ee1d355 |
| LSTM_data/single_watershed.nc | 1.2 MiB | sha256:bea90106d540a7b8b6aca4013ae6c2a9f202a37620f9f265fe3d7c70bf9ff7c8 |
| LSTM_data/multiple_watersheds.nc | 3.2 MiB | sha256:acc5a9821fefbd85cda5283cdfdc00c9290662b5ff6f83ac5637ae84f730c427 |
| LSTM_data/LSTM_test_data_local.nc | 118.0 kiB | sha256:4e4a70efd9405b481556c73f700dd87d0bf2169366a89b14cd8d8f771f093da8 |
| LSTM_data/LSTM_test_data.nc | 325.1 kiB | sha256:fcac6067708cbdc7e4df6d05471e89ce562bfe8720f0324f113d17fa9d1fe87b |
