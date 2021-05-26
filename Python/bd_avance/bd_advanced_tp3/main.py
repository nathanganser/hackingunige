import numpy
import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt

import random

DATA_INPUT_CSV = "data_for_seminars/data_input.csv"
DV_COLUMN_NAME = "SLEEP"  # inverted SLEEP and STEPS
NUM_ROWS_TO_READ = 128
IDV_COLUMN_NAME = "STEPS"  # inverted SLEEP and STEPS
BINARY_CUTTINGPOINT = 13415  # use get_average_IDV()
TOTAL_columns = ['DAY OF STUDY', 'WEEKEND', 'SEASON', 'HOLIDAY', 'DISTANCE', 'STEPS', 'SLEEP', 'AWAKE', 'STEPS AWAKE',
                 'STRIDE', 'RHR']
SEED_RANDOM = 1
N_REPETITIONS = 3000
NAME_OUTPUT_TXT = "results.txt"
NAME_OUTPUT_GRAPH = "results_graph.png"


def remove_empty_cells(input):
    for i in range(1, len(input)):
        if numpy.isnan(input[i]):
            input.at[i] = ((input[i - 1] + input[i + 1]) / 2)


def get_average_IDV():
    total = 0
    counter = 0
    for row in IDV:
        total += row
        counter += 1

    return total / counter


def idv_to_binary(input):
    for i in range(0, len(input)):
        if input[i] >= BINARY_CUTTINGPOINT:
            input.at[i] = 1
        else:
            input.at[i] = 0


def get_control_values():
    control_values = []
    for element in CONTROLS:
        data = data_input[element]
        remove_empty_cells(data)
        data_without_empty_cells = data
        control_values.append(data_without_empty_cells)
    return control_values


def impact_idv(X, DV_local):
    # for the greens
    IDV_positiveEffect_total = 0
    IDV_positiveEffect_numberElements = 0
    # for the reds
    IDV_negativeEffect__total = 0
    IDV_negativeEffect__numberElements = 0
    for i in range(0, len(X) - 1):
        if X[IDV_COLUMN_NAME][i] == 1:
            IDV_positiveEffect_total += DV_local[i + 1]

            IDV_positiveEffect_numberElements += 1
        else:
            IDV_negativeEffect__total += DV_local[i + 1]
            IDV_negativeEffect__numberElements += 1
    if (IDV_positiveEffect_numberElements == 0 or IDV_negativeEffect__numberElements == 0):
        print("ERROR: Check the BINARY_CUTTINGPOINT, as no negative/positive values were found for binary IDV.")
        exit()

    average_positive = IDV_positiveEffect_total / IDV_positiveEffect_numberElements
    average_negative = IDV_negativeEffect__total / IDV_negativeEffect__numberElements

    return [average_positive, average_negative]


def idv_shuffler(input):
    for i in range(len(input) - 1, 0, -1):
        # Pick a random index from 0 to 1
        random.seed(SEED_RANDOM)
        j = random.randint(1, i)

        # Swap arr[i] with the element at random index
        input.at[i], input.at[j] = input[j], input[i]


def simulate_after_randomization(X, IDV_randomized, regression_model):
    predicted_DV = []
    for i in range(0, len(X)):
        X._set_value(i, IDV_COLUMN_NAME, IDV_randomized[i + 1])
        controls_partial = []
        for element in CONTROLS:
            controls_partial.append(X[element][i])

        parameters_to_predict = [[X[DV_COLUMN_NAME + "-1"][i], IDV_randomized[i + 1]] + controls_partial]
        predicted_value = regression_model.predict(parameters_to_predict)
        X._set_value(i + 1, (DV_COLUMN_NAME + "-1"), predicted_value)
        predicted_DV.append(predicted_value)

    DV_output = pandas.Series((i[0] for i in predicted_DV))
    DV_output.index = numpy.arange(1, len(DV_output) + 1)

    return [X, DV_output]


def charts():
    positive = [impact_beforeMoTR[0] for i in
                range(0, NUM_ROWS_TO_READ)]
    negative = [impact_beforeMoTR[1] for i in range(0, NUM_ROWS_TO_READ)]
    plt.plot(positive, color='green', label='POS effect before MoTR')
    plt.plot(negative, color='red', label='NEG effect before MoTR')
    positive_aft = [numpy.average(sum_positive) for i in range(0, NUM_ROWS_TO_READ)]
    negative_aft = [numpy.average(sum_negative) for i in range(0, NUM_ROWS_TO_READ)]
    plt.plot(positive_aft, color='green', linestyle='dotted', label='POS effect after MoTR')
    plt.plot(negative_aft, color='red', linestyle='dotted', label='NEG effect after MoTR')
    plt.plot(DV)
    plt.xlabel('Day of study')
    plt.ylabel("log10 based " + DV_COLUMN_NAME)
    plt.title("Impact of " + IDV_COLUMN_NAME + " (>= " + str(BINARY_CUTTINGPOINT) + ") on " + DV_COLUMN_NAME)
    plt.legend()
    plt.savefig(NAME_OUTPUT_GRAPH, dpi=300)


def write_results():
    file_output = open(NAME_OUTPUT_TXT, "w")
    file_output.write("RESULTS: influence of {} on {}.\n".format(
        IDV_COLUMN_NAME, DV_COLUMN_NAME))
    file_output.write("Source of data: {}.\n".format(
        DATA_INPUT_CSV))
    file_output.write("Number of rows used, since file start: {}.\n".format(NUM_ROWS_TO_READ))
    file_output.write("Binary cutting point for the IDV: {}.\n".format(BINARY_CUTTINGPOINT))
    file_output.write("Control variables: {}.\n".format(CONTROLS))
    file_output.write("Initial seed for random method: {}.\n".format(SEED_RANDOM - N_REPETITIONS + 1))
    file_output.write("Number of MoTR simulations: {}.\n".format(N_REPETITIONS))
    file_output.write("Coefficient of IDV influence on DV: {}.\n".format(regression_model.coef_[1]))
    file_output.write("Positive Effect of IDV on DV, before MoTR: {}.\n".format(impact_beforeMoTR[0]))
    file_output.write("Negative Effect of IDV on DV, before MoTR: {}.\n".format(impact_beforeMoTR[1]))
    file_output.write("Positive Effect of IDV on DV, after MoTR: {}.\n".format(numpy.average(sum_positive)))
    file_output.write("Negative Effect of IDV on DV, after MoTR: {}.\n".format(numpy.average(sum_negative)))
    file_output.write("Impact of IDV on DV, before MoTR: {}.\n".format(impact_beforeMoTR[0] - impact_beforeMoTR[1]))
    file_output.write("Impact of IDV on DV, after MoTR: {}.\n".format(numpy.average(sum_dif_impact)))
    file_output.close()


CONTROLS = TOTAL_columns.copy()
CONTROLS.remove(IDV_COLUMN_NAME)
CONTROLS.remove(DV_COLUMN_NAME)

data_input = pandas.read_csv(DATA_INPUT_CSV, sep=';')

data_input = data_input[0:NUM_ROWS_TO_READ]

DV = data_input[DV_COLUMN_NAME]

DV_previous_day = DV

DV_previous_day = DV_previous_day[:-1]

DV = DV.iloc[1:]

IDV = data_input[IDV_COLUMN_NAME]

remove_empty_cells(IDV)
remove_empty_cells(DV)  # added this as we have empty rows in the DV

idv_to_binary(IDV)
IDV_original = IDV

CONTROLS = TOTAL_columns.copy()
CONTROLS.remove(IDV_COLUMN_NAME)
CONTROLS.remove(DV_COLUMN_NAME)

#DV = numpy.log10(DV)
#DV_previous_day = numpy.log10(DV_previous_day)

columns_for_DataFrame = [DV_COLUMN_NAME + "-1", IDV_COLUMN_NAME] + CONTROLS
controls_data = get_control_values()
data_for_DataFrame = [DV_previous_day, IDV] + controls_data
X = pandas.DataFrame(list(zip(*data_for_DataFrame)), columns=columns_for_DataFrame)

X_original = X.copy()

Y = DV

impact_beforeMoTR = impact_idv(X, DV)
print(impact_beforeMoTR)

regression_model = linear_model.LinearRegression()
regression_model.fit(X, Y)

sum_dif_impact = []
sum_positive = []
sum_negative = []

for i in range(SEED_RANDOM, N_REPETITIONS + SEED_RANDOM):
    SEED_RANDOM = i
    X_local = X_original.copy()
    IDV_local = IDV_original.copy()

    idv_shuffler(IDV_local)
    simulation_output = simulate_after_randomization(X_local, IDV_local, regression_model)
    impact_afterMoTR = impact_idv(simulation_output[0], simulation_output[1])

    sum_dif_impact.append((impact_afterMoTR[0] - impact_afterMoTR[1]))
    sum_positive.append(impact_afterMoTR[0])
    sum_negative.append(impact_afterMoTR[1])
    print("\rDone " + str(i) + " / " + str(N_REPETITIONS), end='', flush=True)

write_results()

charts()
