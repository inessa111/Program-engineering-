import typing


def sum_polinom(
    a: typing.Dict[str, int], b: typing.Dict[str, int]
) -> typing.Dict[str, int]:
    c = dict()
    # складываем в c
    for i in a.keys() | b.keys():
        c[i] = 0
        if i in a:
            c[i] += a[i]
        if i in b:
            c[i] += b[i]
    return c
