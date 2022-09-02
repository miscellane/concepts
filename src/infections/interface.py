"""
Systematically reads UK SARS-CoV-2 data from coronavirus.data.gov.uk via its API

"""

import collections
import logging
import os
import sys
import time


def main():

    # Lower Tier Local Authority Level Measures
    measures = src.infections.measures.Measures(fields=LTLA, path=os.path.join('ltla', 'measures')) \
        .exc(area_codes=ltla_[:5], area_type='ltla')
    logger.info(measures)
    time.sleep(60)

    # trust Level measures
    measures = src.infections.measures.Measures(fields=TRUSTS, path=os.path.join('trusts', 'measures')) \
        .exc(area_codes=trusts_, area_type='nhsTrust')
    logger.info(measures)


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # API filter parameters
    FilterParameters = collections.namedtuple(
        typename='FilterParameters', field_names=['area_code', 'area_type', 'area_name', 'date'], defaults=None)

    # libraries
    import config
    import src.infections.measures

    # Setting-up
    configurations = config.Config()

    LTLA = configurations.LTLA
    ltla = configurations.ltla()
    ltla_ = ltla.ltla.unique()

    TRUSTS = configurations.TRUSTS
    trusts = configurations.trusts()
    trusts_ = trusts.trust_code.unique()

    main()
