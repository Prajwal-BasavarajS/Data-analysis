import numpy as np

scores = np.array([50,55,60,65,70,75,80,300])

mean_score = np.mean(scores)

median_score = np.median(scores)

std_dev_score = np.std(scores)

print(f"Mean : {mean_score} \nMedian : {median_score} \nStandard Deviation : {std_dev_score}")

