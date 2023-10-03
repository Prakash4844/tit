# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: tit use
# date: 2 Oct, 2023
# Comments: Happy Birthday Lal Bahadur Shastri and Mahatma Gandhi

import collections
import hashlib
import os
import struct
from .check_repo import internal_repo_name_check
from .read_file import read_binary_file
from .write_file import write_binary_file

# Data for one entry in the git index (.git/index)
IndexEntry = collections.namedtuple('IndexEntry', [
    'ctime_s', 'ctime_n', 'mtime_s', 'mtime_n', 'dev', 'ino', 'mode', 'uid',
    'gid', 'size', 'sha1', 'flags', 'path',
])


def read_index():
    """Read git index file and return list of IndexEntry objects."""
    vcs = internal_repo_name_check()
    try:
        data = read_binary_file(os.path.join(f'{vcs}', 'index'))
    except FileNotFoundError:
        return []
    digest = hashlib.sha1(data[:-20]).digest()
    assert digest == data[-20:], 'invalid index checksum'
    signature, version, num_entries = struct.unpack('!4sLL', data[:12])
    assert signature == b'DIRC', 'invalid index signature {}'.format(signature)
    assert version == 2, 'unknown index version {}'.format(version)
    entry_data = data[12:-20]
    entries = []
    i = 0
    while i + 62 < len(entry_data):
        fields_end = i + 62
        fields = struct.unpack('!LLLLLLLLLL20sH', entry_data[i:fields_end])
        path_end = entry_data.index(b'\x00', fields_end)
        path = entry_data[fields_end:path_end]
        entry = IndexEntry(*(fields + (path.decode(),)))
        entries.append(entry)
        entry_len = ((62 + len(path) + 8) // 8) * 8
        i += entry_len
    assert len(entries) == num_entries
    return entries


def write_index(entries):
    """Write list of IndexEntry objects to git index file."""
    vcs = internal_repo_name_check()
    packed_entries = []
    for entry in entries:
        entry_head = struct.pack('!LLLLLLLLLL20sH',
                                 entry.ctime_s, entry.ctime_n, entry.mtime_s, entry.mtime_n,
                                 entry.dev, entry.ino, entry.mode, entry.uid, entry.gid,
                                 entry.size, entry.sha1, entry.flags)
        path = entry.path.encode()
        length = ((62 + len(path) + 8) // 8) * 8
        packed_entry = entry_head + path + b'\x00' * (length - 62 - len(path))
        packed_entries.append(packed_entry)
    header = struct.pack('!4sLL', b'DIRC', 2, len(entries))
    all_data = header + b''.join(packed_entries)
    digest = hashlib.sha1(all_data).digest()
    write_binary_file(os.path.join(f'{vcs}', 'index'), all_data + digest)
