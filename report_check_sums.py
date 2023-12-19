#!/usr/bin/env python
import hashlib
import math
import os
from pathlib import Path
from typing import Union


def file_size_formatter(i: int, binary: bool = True, precision: int = 1) -> str:
    """Format byte size into an appropriate nomenclature for prettier printing.

    Notes
    -----
    Adapted from https://github.com/Ouranosinc/miranda/blob/main/miranda/storage.py
    """
    _CONVERSIONS = ["B", "k{}B", "M{}B"]

    # Determine the appropriate conversion factor
    base = 1024 if binary else 1000
    if i == 0:
        return "0 B"
    multiple = math.trunc(math.log2(i) / math.log2(base))
    value = i / math.pow(base, multiple)
    suffix = _CONVERSIONS[multiple].format("i" if binary else "")
    return f"{value:.{precision}f} {suffix}"


def file_md5_checksum(filename: Path) -> str:
    """Return md5 checksum for file."""
    hash_md5 = hashlib.md5()
    with filename.open("rb") as f:
        hash_md5.update(f.read())
    return hash_md5.hexdigest()


def valid(path: Path) -> bool:
    """Return True if path should be considered for the creation of md5 checksum.

    Parameters
    ----------
    path : Path
      Path object.
    """

    # Exclude top-level files
    if len(path.parts) == 1:
        return False

    # Exclude hidden files
    if any([p.startswith(".") for p in path.parts]):
        return False

    # Exclude md5 files
    if path.suffix == ".md5":
        return False

    if path.is_file():
        return True


def main(dry_run: bool = False, readme: Union[str, Path] = "README.md"):
    """Create checksum files."""
    cwd = Path(".")
    files: list[Path] = filter(valid, cwd.rglob("**/*"))

    file_checksums = dict()
    for file in files:
        file_checksums[file] = file_md5_checksum(file)

    # Write the checksums dictionary to the bottom of the README.md file, replacing the existing table
    readme = Path(readme)
    with readme.open() as f:
        lines = f.readlines()

    # Find the index of the existing checksum table
    start_index, end_index = None, None
    for i, line in enumerate(lines):
        if line.startswith("### Files"):
            start_index = i

    # Remove existing checksum table
    if start_index is not None:
        del lines[start_index:]

    for i, line in enumerate(lines):
        if line.startswith("## Available datasets"):
            break

    # Insert new checksum table
    lines.insert(i + 1, "\n")
    lines.insert(i + 2, "### Files\n")
    lines.insert(i + 3, "\n")
    lines.insert(i + 4, "| File | Size | Checksum |\n")
    lines.insert(i + 5, "| ---- | ---- | -------- |\n")

    for file, checksum in file_checksums.items():
        lines.insert(
            i + 6,
            f"| {file.relative_to(cwd).as_posix()} "
            f"| {file_size_formatter(file.stat().st_size)} "
            f"| {checksum} |\n",
        )

    # Remove trailing newline
    if lines[-1].startswith("\n"):
        del lines[-1]

    if dry_run:
        print("Dry run. Not writing to README.md file.")
    else:
        with readme.open("w") as f:
            f.writelines(lines)
    print(f"Successfully wrote {len(file_checksums)} checksums to {readme}.")


if __name__ == "__main__":
    args = os.getenv("DRY_RUN", False)
    main(args)
