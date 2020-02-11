import hashlib


def hs(args):

    m = hashlib.md5()

    m.update(args.encode('utf8'))

    return m.hexdigest()


def open_file(path, *args, **kwargs):
    if kwargs['md'] == 'r':
        with open(path, mode='r', encoding='utf-8') as f:
            res = (line.split(',') for line in f)
            for i in res:
                yield i


def write_in(path, *args, **kwargs):
    if kwargs['md'] == 'a':
        with open(path, mode='a', encoding='utf-8') as f:
            for i in args:
                if i == args[-1]:
                    f.write(args[-1] + '\n')
                else:
                    f.write(i + ',')
    elif kwargs['md'] == 'w':
        with open(path, mode='w', encoding='utf-8') as f:
            for i in args:
                if i == args[-1]:
                    f.write(args[-1] + '\n')
                else:
                    f.write(i + ',')






