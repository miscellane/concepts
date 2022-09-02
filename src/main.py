"""
Module: main
"""
import logging
import os
import sys


def main():
    """
    Previews the LTLA & NHS Trust Codes

    :return:
    """

    logger.info('concepts')

    configurations = config.Config()

    # frame: msoa, ltla
    ltla = configurations.ltla()
    logger.info(ltla.ltla.unique())

    # frame: trust_code, trust_name
    trusts = configurations.trusts()
    logger.info(trusts.trust_code.unique())


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Configurations
    import config

    main()
