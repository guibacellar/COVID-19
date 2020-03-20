import cv19_constants
import cv19_downloader
import cv19_parser
import gc
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('tkagg')

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
    brazil = brazil[brazil['totalcases'] > 0]

    columns = [
        'date',
        'totalcases',
        'totaldeaths',
        'totalrecovered'
    ]

    series = brazil[columns]

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.plot(
        series['date'],
        series['totalcases'],
        color='blue',
        marker='+'
    )
    ax1.plot(
       series['date'],
       series['totaldeaths'],
       color='red',
       marker='+'
    )
    # ax1.plot(
    #     series['date'],
    #     series['totalrecovered'],
    #     color='green',
    #     marker='o'
    # )
    plt.show()


if __name__ == '__main__':
    main()
