# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: N/A
# date: 2 Oct, 2023
# Comments: Happy Birthday Lal Bahadur Shastri and Mahatma Gandhi

import enum
import hashlib
import os.path
import stat
import sys
import zlib
from .check_repo import internal_repo_name_check
from .read_file import read_binary_file
from .write_file import write_binary_file


class ObjectType(enum.Enum):
    """Object type enum. There are other types too, but we don't need them.
    See "enum object_type" in git's source (git/cache.h).
    """
    commit = 1
    tree = 2
    blob = 3
    
    
def hash_object(data, obj_type, write=True):
    """Compute hash of object data of given type and write to object store
    if "write" is True. Return SHA-1 object hash as hex string.
    """
    vcs = internal_repo_name_check()
    object_header = f"{obj_type} {len(data)}".encode()
    complete_data = object_header + b'\x00' + data
    sha1 = hashlib.sha1(complete_data).hexdigest()

    if write:
        path = os.path.join(f'{vcs}', 'objects', sha1[:2], sha1[2:])

        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            write_binary_file(path, zlib.compress(complete_data))

    return sha1


def find_object(sha1_prefix):
    """Find object with given SHA-1 prefix and return path to object in object
    store, or raise ValueError if there are no objects or multiple objects
    with this prefix.
    """
    vcs = internal_repo_name_check()
    if len(sha1_prefix) < 2:
        raise ValueError('hash prefix must be 2 or more characters')

    obj_dir = os.path.join(f'{vcs}', 'objects', sha1_prefix[:2])
    rest = sha1_prefix[2:]
    objects = [name for name in os.listdir(obj_dir) if name.startswith(rest)]

    if not objects:
        raise ValueError(f'object {sha1_prefix!r} not found')
    if len(objects) >= 2:
        raise ValueError(f'multiple objects ({len(objects)}) with prefix {sha1_prefix!r}')

    return os.path.join(obj_dir, objects[0])


def read_object(sha1_prefix):
    """Read object with given SHA-1 prefix and return tuple of
    (object_type, data_bytes), or raise ValueError if not found.
    """
    path = find_object(sha1_prefix)
    complete_data = zlib.decompress(read_binary_file(path))
    nul_index = complete_data.index(b'\x00')
    header = complete_data[:nul_index]
    obj_type, size_str = header.decode().split()
    size = int(size_str)
    data = complete_data[nul_index + 1:]
    assert size == len(data), f'expected size {size}, got {len(data)} bytes'

    return obj_type, data


def cat_file(mode, sha1_prefix):
    """Write the contents of (or info about) object with given SHA-1 prefix to
    stdout. If mode is 'commit', 'tree', or 'blob', print raw data bytes of
    object. If mode is 'size', print the size of the object. If mode is
    'type', print the type of the object. If mode is 'pretty', print a
    prettified version of the object.
    """
    obj_type, data = read_object(sha1_prefix)

    if mode in ['commit', 'tree', 'blob']:
        if obj_type != mode:
            raise ValueError(f'expected object type {mode}, got {obj_type}')
        sys.stdout.buffer.write(data)
    elif mode == 'size':
        print(len(data))
    elif mode == 'type':
        print(obj_type)
    elif mode == 'pretty':
        if obj_type in ['commit', 'blob']:
            sys.stdout.buffer.write(data)
        elif obj_type == 'tree':
            for mode, path, sha1 in read_tree(data=data):
                type_str = 'tree' if stat.S_ISDIR(mode) else 'blob'
                print(f'{mode:06o} {type_str} {sha1}\t{path}')
        else:
            assert False, 'unhandled object type {!r}'.format(obj_type)
    else:
        raise ValueError('unexpected mode {!r}'.format(mode))


def read_tree(sha1=None, data=None):
    """Read tree object with given SHA-1 (hex string) or data, and return list
    of (mode, path, sha1) tuples.
    """
    if sha1 is not None:
        obj_type, data = read_object(sha1)
        assert obj_type == 'tree'
    elif data is None:
        raise TypeError('must specify "sha1" or "data"')
    i = 0
    entries = []
    for _ in range(1000):
        end = data.find(b'\x00', i)
        if end == -1:
            break
        mode_str, path = data[i:end].decode().split()
        mode = int(mode_str, 8)
        digest = data[end + 1:end + 21]
        entries.append((mode, path, digest.hex()))
        i = end + 1 + 20
    return entries
