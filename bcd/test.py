import sys


def bcd(value, length=0, pad='\x00'):
    ret = ""
    while value:
        value, ls4b = divmod(value, 10)
        value, ms4b = divmod(value, 10)
        ret = chr((ms4b << 4) + ls4b) + ret
    return pad * (length - len(ret)) + ret


def bcd_str(value, length=0, pad='\x00'):
    value_str = str(value)
    value_str = ("0" if len(value_str) % 2 else "") + value_str
    ret = ""
    for i in range(0, len(value_str), 2):
        ms4b = ord(value_str[i]) - 0x30
        ls4b = ord(value_str[i + 1]) - 0x30
        ret += chr((ms4b << 4) + ls4b)
    return pad * (length - len(ret)) + ret


def main():
    values = [
        145,
        5,
        123456,
    ]
    for value in values:
        print("{0:d} - [{1:s}] - [{2:s}]".format(value, repr(bcd(value, length=6)), repr(bcd_str(value, length=6))))

    # Bonus
    speed_test = 1
    if speed_test:
        import timeit  # Anti pattern: only import at the beginning of the file
        print("\nTesting speed:")
        stmt = "bcd({0:d})".format(1234567890 ** 32)
        count = 100000
        for func_name in ["bcd", "bcd_str"]:
            print("    {0:s}: {1:.03f} secs".format(func_name, timeit.timeit(stmt, setup="from __main__ import {0:s} as bcd".format(func_name), number=count)))


if __name__ == "__main__":
    print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip() for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    main()
    print("\nDone.")