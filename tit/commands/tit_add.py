# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: tit use
# date: 2 Oct, 2023
# Comments: Happy Birthday Lal Bahadur Shastri and Mahatma Gandhi

import os
import operator
from typer import Typer
from rich import print
from tit.read_file import read_binary_file
from tit.check_repo import current_datetime
from tit.object_operations import hash_object
from tit.index_operations import write_index, IndexEntry, read_index

# create a typer app using required data.
app = Typer(
    help="tit add: Add file contents to the index (Files that will be committed)",
    context_settings={"help_option_names": ["-h", "--help"]}
)


@app.callback(invoke_without_command=True)
def add(paths: str, verbose: bool = False) -> None:
    """Add all file paths to git index."""
    if os.name == 'nt':
        paths = [p.replace('\\', '/') for p in paths]
        if verbose:
            print(f"{current_datetime()}: Replacing '//' with '\\' for compatibility purposes.")

    if verbose:
        print(f"{current_datetime()}: Reading Index...")
    all_entries = read_index()
    entries = [e for e in all_entries if e.path not in paths]
    for path in paths:
        if verbose:
            print(f"{current_datetime()}: Creating Index entry...")
        sha1 = hash_object(read_binary_file(path), 'blob')
        st = os.stat(path)
        flags = len(path.encode())
        assert flags < (1 << 12)
        entry = IndexEntry(
            int(st.st_ctime), 0, int(st.st_mtime), 0, st.st_dev,
            st.st_ino, st.st_mode, st.st_uid, st.st_gid, st.st_size,
            bytes.fromhex(sha1), flags, path)
        entries.append(entry)
        if verbose:
            print(f"{current_datetime()}: Added {path} to the index.")
    entries.sort(key=operator.attrgetter('path'))
    write_index(entries)


if __name__ == "__main__":
    app()
