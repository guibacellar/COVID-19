# Download, Parse, Generate Features and Save by CountryCode

import os
import cv19_downloader
import cv19_parser
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def main() -> None:

    # Download and Parse Data
    if cv19_downloader.download_timeline_data():
        cv19_parser.parse_timeline_raw_data_to_csv()

    # Run Feature Generation Notebook
    print('Running Feature Generation Notebook: ', end='')
    nb = nbformat.read(open('feature_generation.ipynb'), as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': os.path.abspath(os.getcwd())}})
    print('DONE')


if __name__ == '__main__':
    main()
