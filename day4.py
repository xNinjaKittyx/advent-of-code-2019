# time import is not needed, just for measuring timings.
# No imports or regex was used.
import time

# part 1

t = time.time()
counter = 0

for x in range(353096, 843212):
    y = str(x)
    # at least 1 number is repeated.
    if len(set(y)) == 6:
        continue

    prev_value = y[0]
    for value in y[1:]:
        if value >= prev_value:
            prev_value = value
            continue
        break
    else:
        counter += 1

print(time.time() - t)
print(counter)

# part 2
t = time.time()
counter = 0
violation_count = (1, 6)

for x in range(353096, 843212):
    y = str(x)
    # at least 1 number is repeated.
    if len(set(y)) in violation_count:
        continue

    prev_value = y[0]
    flag = False
    biggroup_flag = False
    repeated = 0
    for value in y[1:]:
        if value > prev_value:
            if repeated == 1:
                flag = True
            elif repeated > 1:
                biggroup_flag = True
            repeated = 0
            prev_value = value
            continue
        if value == prev_value:
            repeated += 1
            prev_value = value
            continue
        break
    else:
        if repeated == 1:
            flag = True
        if repeated > 1:
            biggroup_flag = True

        if biggroup_flag and not flag:
            continue
        counter += 1

print(time.time() - t)
print(counter)
