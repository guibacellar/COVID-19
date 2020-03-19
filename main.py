import gc
import cv19_downloader
import cv19_parser


def main() -> None:

    # Download and Parse Data
       # if cv19_downloader.download_timeline_data():
    #     cv19_parser.parse_timeline_raw_data_to_csv()
    #     gc.collect()
    # else:
    #     print('[+] Fallback: Alread Downloaded Data....')

    # Load Data
    cv19_parser.parse_timeline_raw_data_to_csv()


if __name__ == '__main__':
    main()
