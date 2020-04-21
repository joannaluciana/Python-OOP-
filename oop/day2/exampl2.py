import statistics
temperatures = [10,14,15,10,9,5]

# temperatures_under_mean = list(filter(lambda x:x>statistics.mean(temperatures),temperatures))
# print(temperatures_under_mean)

def if_greater_then_mean (x):
    if x > statistics.mean(temperatures):
        return True
    else:
        return False

    # tworzenie sita

temperatures_under_mean = list(filter(if_greater_then_mean,temperatures))
# print(temperatures_under_mean)

# over_12 = [ x
#             for x in temperatures
#             if x>12
# ]
#
#
# over_12_s = [x
#             for x in temperatures
#             if x>statistics.mean(temperatures)]
#
# print(over_12_s)