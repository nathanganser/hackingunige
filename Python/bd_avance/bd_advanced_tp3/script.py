import numpy
import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt
import random

# Dynamic part
DATA_INPUT_CSV = "data_for_seminars/data_input.csv"

IDV_COLUMN_NAME = "STEPS"
DV_COLUMN_NAME = "SLEEP"
TOTAL_columns = ['DAY OF STUDY', 'WEEKEND', 'SEASON', 'HOLIDAY', 'DISTANCE', 'STEPS',
                 'SLEEP', 'AWAKE', 'STEPS AWAKE', 'STRIDE', 'RHR']
ROWS_TO_READ = 128
BINARY_CUTTINGPOINT = 7*60*60
SEED_RANDOM = 1

CONTROLS = TOTAL_columns.copy()
CONTROLS.remove(IDV_COLUMN_NAME)
CONTROLS.remove(DV_COLUMN_NAME)

data_input = pandas.read_csv(DATA_INPUT_CSV, sep=';')
data_input = data_input[0:ROWS_TO_READ]

# getting DV and IDV
DV = data_input[DV_COLUMN_NAME]
IDV = data_input[IDV_COLUMN_NAME]
DV_previous_day = DV[:-1]
DV = DV.iloc[1:]

for count in range(0, len(DV), +1):
    pass
    # print(f'Today: {DV[count:count+1]}')
    # print(f'Yesterday: {DV_previous_day[count:count+1]}')
    # print('-----')


def remove_empty_cells(column):
    print('REMOVE EMPTY CELLS')
    for count in range(0, len(column), +1):
        if numpy.isnan(column[count]):
            # print(f'this row is empty: {column[count]}')
            column.at[count] = (column[count - 1] + column[count + 1]) / 2
        else:
            # print(f'this row is ok: {column[count]}')
            pass


def idv_to_binary(column):
    print('CONVERT COLUMN TO BINARY')
    for count in range(0, len(column), +1):
        if column[count] >= BINARY_CUTTINGPOINT:
            # print(f'turning this row to 1 (true): {column[count]}')
            column.at[count] = 1
        else:
            # print(f'turning this row to 0 (false): {column[count]}')
            column.at[count] = 0


def get_control_values():
    print('GET CONTROL VALUES')
    control_values = []
    for column in CONTROLS:
        # print(f'getting values from control column {column}')
        remove_empty_cells(data_input[column])
        control_values.append(column)
    return control_values


def impact_idv(X, DV_local):
    print('CALCULATE IMPACT IDV')
    IDV_positiveEffect_total = 0
    IDV_positiveEffect_numberElements = 0
    IDV_negativeEffect__total = 0
    IDV_negativeEffect__numberElements = 0
    for i in range(0, len(X) - 1):
        if X[IDV_COLUMN_NAME][i] == 1:
            IDV_positiveEffect_total += DV_local[i + 1]
            IDV_positiveEffect_numberElements += 1
        else:
            IDV_negativeEffect__total += DV_local[i + 1]
            IDV_negativeEffect__numberElements += 1

    if IDV_positiveEffect_numberElements == 0 or IDV_negativeEffect__numberElements == 0:
        print("ERROR: Check the BINARY_CUTTINGPOINT, as no negative/positive values were found for binary IDV.")
        exit()

    average_positive = IDV_positiveEffect_total / IDV_positiveEffect_numberElements
    average_negative = IDV_negativeEffect__total / IDV_negativeEffect__numberElements
    return [average_positive, average_negative]


def idv_shuffler(input):
    for i in range(len(input) - 1, 0, -1):
        random.seed(SEED_RANDOM)
        j = random.randint(1, i + 1)
        input.at[i], input.at[j] = input[j], input[i]


remove_empty_cells(IDV)
idv_to_binary(IDV)

columns_for_DataFrame = [DV_COLUMN_NAME + "-1", IDV_COLUMN_NAME] + CONTROLS
controls_data = get_control_values()
data_for_DataFrame = [DV_previous_day, IDV] + controls_data
X = pandas.DataFrame(list(zip(*data_for_DataFrame)), columns=columns_for_DataFrame)
Y = DV

impact_beforeMoTR = impact_idv(X, DV)

regression_model = linear_model.LinearRegression()
regression_model.fit(X, Y)
