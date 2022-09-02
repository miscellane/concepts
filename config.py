import os
import collections
import datetime

import numpy as np
import pandas as pd


class Config:

    def __init__(self):
        """
        https://coronavirus.data.gov.uk/details/developers-guide/main-api#query-parameters
        """

        # fields
        self.LTLA = {'date': 'date',
                     'dailyCases': 'newCasesBySpecimenDate',
                     'newDeaths28DaysByDeathDate': 'newDeaths28DaysByDeathDate',
                     'dailyFirstDoseByVaccinationDate': 'newPeopleVaccinatedFirstDoseByVaccinationDate',
                     'dailySecondDoseByVaccinationDate': 'newPeopleVaccinatedSecondDoseByVaccinationDate',
                     'dailyThirdInjectionByVaccinationDate': 'newPeopleVaccinatedThirdInjectionByVaccinationDate',
                     'VaccineRegisterPopulationByVaccinationDate': 'VaccineRegisterPopulationByVaccinationDate',
                     'newVirusTestsBySpecimenDate': 'newVirusTestsBySpecimenDate',
                     'newPCRTestsBySpecimenDate': 'newPCRTestsBySpecimenDate'}

        self.TRUSTS = {'date': 'date',
                       'covidOccupiedBeds': 'hospitalCases',
                       'covidOccupiedMVBeds': 'covidOccupiedMVBeds',
                       'estimatedNewAdmissions': 'newAdmissions'}

    @staticmethod
    def ltla() -> pd.DataFrame:
        """

        :return:
        """

        datafile = os.path.join(os.getcwd(), 'data', 'districts', '2020.csv')

        try:
            frame = pd.read_csv(filepath_or_buffer=datafile, header=0,
                                encoding='utf-8', usecols=['MSOA11CD', 'LAD20CD'])
        except RuntimeError as err:
            raise Exception(err)
        frame.rename({'MSOA11CD': 'msoa', 'LAD20CD': 'ltla'}, axis=1, inplace=True)

        return frame

    @staticmethod
    def trusts():

        uri = os.path.join('data', 'catchments', '2021 Trust Catchment Populations_Supplementary Trust Area lookup.xlsx')
        sheet_name = 'Trust Area Lookup'
        rename = {'TrustCode': 'trust_code', 'TrustName': 'trust_name'}

        try:
            frame = pd.read_excel(io=uri, sheet_name=sheet_name, header=0, usecols=['TrustCode', 'TrustName'])
        except RuntimeError as err:
            raise Exception(err)
        frame.rename(columns=rename, inplace=True)

        return frame
