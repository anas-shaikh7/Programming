import statistics

mean1 = statistics.mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

mode1 = statistics.mode([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10])

mmode = statistics.multimode([1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10])

median1 = statistics.median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

hmedian = statistics.median_high([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

Lmedian = statistics.median_low([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"mean: {mean1}")
print(f"mode: {mode1}")
print(f"Multimode: {mmode}")
print(f"Lower median: {Lmedian}")
print(f"median: {median1}")
print(f"Higher median: {hmedian}")
