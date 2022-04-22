import pandas as pd
import statistics
import csv

df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

#mean for height or weight

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

#median for height or weight

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

#mode for height or weight

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

print("Mean, Medean, modee of height is {}, {}, and {}".format(height_mean, height_median, height_mode))
print("Meen, Medan, moed of weight is {}, {}, and {}".format(weight_mean, weight_median, weight_mode))