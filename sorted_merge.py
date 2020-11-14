def sorted_merge(list1, list2):
    i = 0
    j = 0
    output = []
    length1 = len(list1)
    length2 = len(list2)
    while i  < length1 and j  < length2:
        if list1[i] < list2[j]:
            output.append(list1[i])
            i += 1
            continue
        elif list1[i] > list2[j]:
            output.append(list2[j])
            j += 1
        else:
            output.append(list1[i])
            output.append(list2[j])
            i += 1
            j += 1

    if i <= length1:
        left_over1 = list1
        left_over1 = left_over1[i: -1]
        try:
            output.extend(left_over1)
        except:
            output.append(list1[i])
    if j <= length2:
        left_over2 = list2
        left_over2 = left_over2[j]
        print(left_over2)
        try:
            output.extend(left_over2)
        except:
            output.append(list2[j])

    # Here is an alternate way to replace the code from lines 21 to 35. Both are O(n) or linear, but the current one is shorter and cleaner.
    # try:
    #     if list1[i] not in output:
    #         while True:
    #             try:
    #                 output.append(list1[i])
    #                 i += 1
    #             except IndexError:
    #                 break
    # except IndexError:
    #     pass
    #
    # try:
    #     if list2[j] not in output:
    #         while True:
    #             try:
    #                 output.append(list2[j])
    #                 j += 1
    #             except IndexError:
    #                 break
    # except IndexError:
    #     pass

    return output






