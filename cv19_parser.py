# Parser Functions

import cv19_constants
import json
import pandas as pd

DATA_FRAME_COLUMNS_DEFINITION = [
    'date',  # MM/DD/YY
    'countrycode',
    'countrylabel',
    'showcountrylabelcases',
    'labelpositioncases',
    'showcountrylabeldeaths',
    'labelpositiondeaths',
    'showcountrylabelrecovered',
    'labelpositionrecovered',
    'casesoverride',
    'deathsoverride',
    'recoveredoverride',
    'columnsonrightshouldbeemptywhennotinuseifyouenteranumberitwillalwaysshowunlessyoudeleteit',
    'emergencycasesoverride',
    'emergencydeathsoverride',
    'totalcases',
    'totaldeaths',
    'totalrecovered'
]


def parse_timeline_raw_data_to_csv() -> None:
    """
    Parse all Data to CSV Format

    :return: None
    """

    print('[+} Parsing Timeline Raw Data to CSV: ', end='')

    print('Loading JSON', end='')
    with open(cv19_constants.TARGET_TIMELINE_RAW_DATA, 'r') as file:
        json_data: json = json.load(file)
        file.close()

    # Create DataFrame
    df: pd.DataFrame = pd.DataFrame(
        columns=DATA_FRAME_COLUMNS_DEFINITION
    )

    print(' | Parsing Data', end='')

    # Loop on Date
    for date_record in json_data:
        current_data: str = date_record['date']

        # Parse SubData
        for country_data in date_record['data']:
            # Add Data into DataFrame
            country_data['date'] = str(current_data)
            df = df.append(country_data, ignore_index=True)

    print(' | Removing Invalid Data', end='')

    # Remove Empty Data
    df = df[(df['countrycode'] != '') & (df['countrycode'] != ' ')]

    # Remove the strange \r in date column
    df.loc[:, ('date')] = df.apply(lambda row: row['date'].replace('\r', ''), axis=1)

    print(' | Dumping CSV', end='')

    df.to_csv(
        cv19_constants.TARGET_TIMELINE_CSV_DATA,
        index=False
    )

    print(' | Completed')

