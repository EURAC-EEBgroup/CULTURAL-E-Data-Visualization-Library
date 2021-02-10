# -*- coding: utf-8 -*-
import click
from dotenv import find_dotenv, load_dotenv
import logging
from itertools import chain
import pandas as pd
from pathlib import Path
import re
from shutil import copyfile


def clean_energy_zones(input_filepath, output_filepath):
    src = input_filepath + '/Energy_zone.BAL'
    dst = output_filepath + '/energy_zones.csv'

    bal = open(src, 'r')
    csv = open(dst, 'w')

    line = bal.readline()
    # remove forbidden characters from title row
    o = re.sub('[^ A-Za-z1-9_\n]*', '', line)
    # format row as csv
    o = re.sub(r'\|', '', o)
    o = re.sub(' +', ',', o)

    csv.write(o[1:])

    # skip second row containing units
    bal.readline()

    # format remaining rows
    for line in bal.readlines():
        o = re.sub(r'\|', '', line)
        o = re.sub(' +', ',', o)
        csv.write(o[1:])


def fix_year(input_filepath, output_filepath):
    src = output_filepath + '/energy_zones.csv'
    dst = output_filepath + '/energy_zones.csv'

    df = pd.read_csv(src, index_col=False)

    df.drop(range(0, 745), inplace=True)
    df = df.reindex(chain(range(8760, 9505), range(745, 8760)))
    df.reset_index(inplace=True)

    del df['index']
    del df['TIME']
    df['TIME'] = df.index

    df = df.reindex(columns=['TIME'] + [i for i in df.columns if i != 'TIME'])

    df.to_csv(dst, index=False)


def clean_energy_balance(input_filepath, output_filepath):
    src = input_filepath + '/SUMMARY.BAL'
    dst = output_filepath + '/summary.csv'

    bal = open(src, 'r')
    csv = open(dst, 'w')

    # skip first two rows containing the title
    bal.readline()
    bal.readline()

    line = bal.readline()
    # remove forbidden characters from title row
    o = re.sub('[^ A-Za-z1-9_\n]*', '', line)
    # format row as csv
    o = re.sub(r'\|', '', o)
    o = re.sub(' +', ',', o)

    csv.write(o[1:])

    # skip second row containing units
    bal.readline()

    # format remaining rows
    for line in bal.readlines()[:-2]:
        o = re.sub(r'\|', '', line)
        o = re.sub(' +', ',', o)
        csv.write(o[1:])


def clean_cultural_e(input_filepath, output_filepath):
    src = input_filepath + '/CULTURAL-E_TSTEP.out'
    dst = output_filepath + '/cultural-e.csv'

    bal = open(src, 'r')
    csv = open(dst, 'w')

    line = bal.readline()
    # remove forbidden characters from title row
    o = re.sub('[^ A-Za-z_1-9\n]*', '', line)
    # format row as csv
    o = re.sub(' +', ',', o)

    csv.write(o[1:-2] + '\n')

    # format remaining rows
    for line in bal.readlines():
        o = re.sub('[ \t]+', ',', line)
        csv.write(o[1:-2] + '\n')


def clean_meteo(input_filepath, output_filepath):
    src = input_filepath + '/Bolzano-metenorm-extreme.epw'
    dst = output_filepath + '/meteo.epw'

    copyfile(src, dst)


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    clean_energy_balance(input_filepath, output_filepath)
    clean_energy_zones(input_filepath, output_filepath)
    # fix months of the year
    fix_year(input_filepath, output_filepath)
    clean_cultural_e(input_filepath, output_filepath)
    clean_meteo(input_filepath, output_filepath)
    logger.info('final data set ready')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
