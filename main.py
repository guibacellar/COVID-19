import cv19_constants
import cv19_downloader
import cv19_parser
import gc
import pandas as pd
import matplotlib

def main() -> None:

    # Download and Parse Data
       # if cv19_downloader.download_timeline_data():
    #     cv19_parser.parse_timeline_raw_data_to_csv()
    #     gc.collect()
    # else:
    #     print('[+] Fallback: Alread Downloaded Data....')

    # Load Data
    #cv19_parser.parse_timeline_raw_data_to_csv()

    # Load Data
    df = pd.read_csv( cv19_constants.TARGET_TIMELINE_CSV_DATA)

    brazil = df[df['countrycode'] == 'BR']

    columns = [
        'date',
        'totalcases',
        'totaldeaths',
        'totalrecovered'
    ]

    brazil[columns].plot()

    print(len(df))

if __name__ == '__main__':
    main()
