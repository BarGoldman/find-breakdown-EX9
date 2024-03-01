def find_breakdown(budget, preferences):
    num_issues = len(budget)
    num_citizens = len(preferences)
    total_budget = sum(budget)

    # Calculate each citizen's equal share of the total budget
    equal_share = total_budget / num_citizens

    total_donate = {item: 0 for item in range(num_issues)}
    citizen_donate = []

    # Calculate total support for each issue based on preferences
    total_support = {item: 0 for item in range(num_issues)}
    for citizen_prefs in preferences:
        for issue in citizen_prefs:
            total_support[issue] += 1

    print("Total support per issue:", total_support)
    print("Donation for one person:", equal_share)

    # The entire C budget is transferred only to the subjects, the number of supporters of which is
    # The largest (if there are several such subjects, then divide the budget between them arbitrarily, or equally).
    # Allocate donations based on preferences
    for i in preferences:
        max_support = 0
        temp = {}
        for key in i:
            # Identify the most preferred (supported) issues
            if total_support[key] > max_support:
                max_support = total_support[key]
                temp = {key: 0}
            elif total_support[key] == max_support:
                temp[key] = 0

        # Calculate donation per selected issue for this citizen
        one_citizenDonate = equal_share / len(temp)
        # Allocate donations and update total donations per issue
        for key in temp:
            temp[key] = one_citizenDonate
            total_donate[key] += one_citizenDonate
        citizen_donate.append(temp)

    # to check if the budget meets the conditions of being
    # a "freak" budget, we need to integrate checks that validate against the three conditions:

    # Check if the total allocation matches the budget for each issue
    if not all(total_donate[issue] == budget[issue] for issue in range(num_issues)):
        print("Condition 1 failed: Total allocation does not match the budget for each issue.")
        return None

    # Check if each citizen's allocation sums to their equal share
    if not all(sum(allocation.values()) == equal_share for allocation in citizen_donate):
        print("Condition 2 failed: Not all citizens' allocations sum to their equal share.")
        return None

    # Check if allocations are positive only for supported issues
    for i, allocation in enumerate(citizen_donate):
        for issue, donation in allocation.items():
            if issue not in preferences[i] and donation > 0:
                print("Condition 3 failed: Allocation made to an unsupported issue.")
                return None

    return citizen_donate


if __name__ == '__main__':

    # Example usage
    print("Example 1: ")
    budget = [400, 50, 50, 0]  # Budget for each issue
    preferences = [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {0}]  # Preferences of each citizen
    breakdown = find_breakdown(budget, preferences)
    if breakdown is not None:
        print("Break down found:\n", breakdown)
    else:
        print("No feasible breakdown.")

    # Example usage
    print("\nExample 2: ")
    budget2 = [0, 300]  # Budget for each issue
    preferences2 = [{0}, {1}, {1}]  # Preferences of each citizen
    breakdown2 = find_breakdown(budget2, preferences2)
    if breakdown2 is not None:
        print("Break down found:\n", breakdown2)
    else:
        print("No feasible breakdown.")

    # # Example usage
    print("\nExample 3: ")
    budget2 = [150, 150]  # Budget for each issue
    preferences2 = [{0, 1}, {0, 1}]  # Preferences of each citizen
    breakdown2 = find_breakdown(budget2, preferences2)
    if breakdown2 is not None:
        print("Break down found:\n", breakdown2)
    else:
        print("No feasible breakdown.")

