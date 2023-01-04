import sys


# TODO: Redirect all prints (including stdout from libbinaryen) to kitchen_sink.txt,
#  so we can compare it w/ original c-kitchen-sink.txt from the same release (critical)
def printf(fmt: str, *values):
    fmt = fmt.replace('%zd', '%d').replace('\n', '')
    print(fmt % values)


puts = print


def abort():
    sys.exit(1)


def free(*args, **kwargs):
    pass


def sizeof(*args, **kwargs):
    raise NotImplementedError


def strcmp(str1: str, str2: str) -> int:
    if str1 == str2:
        return 0
    # TODO: Do we want to emulate this?
    return -1
