# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

from __future__ import absolute_import
from os.path import exists

SUFFIX = '_'


def get_safe_path(dst):
    if not exists(dst):
        return dst
    if not dst.endswith(SUFFIX):
        dst += SUFFIX
        if not exists(dst):
            return dst
    n = 0
    test_dst = dst + str(n)
    while exists(test_dst):
        n += 1
        test_dst = dst + str(n)

    return test_dst
