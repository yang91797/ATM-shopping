import logging


def logger(user_id, path):

    logg = logging.getLogger(user_id)

    if not logg.handlers:
        fh = logging.FileHandler(path)
        logg.setLevel(logging.DEBUG)
        fm = logging.Formatter('%(asctime)s-user_id:%(name)s-%(levelname)s-%(message)s')
        logg.addHandler(fh)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(fm)

    return logg




