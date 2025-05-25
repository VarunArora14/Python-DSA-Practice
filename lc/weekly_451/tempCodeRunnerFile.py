, present, future, hierarchy, budget):
        # Build parent-child relationships
        parent = [0] * (n + 1)  # parent[i] = parent of employee i
        children = [[] for _ in range(n + 1)]  # children[i] = list of direct children of employee i

        for boss, subordinate in hierarchy:
            parent[subordinate] = boss
            children[boss].append(subordinate)

        max_profit = 0

        # Try all possible combinations using bitmask (2^n combinations)
        for mask in range(1 << n):
            total_cost = 0
            total_profit = 0
            valid = True

            # For each employee, check if they're selected in this combination
            for i in range(n):
                if mask & (1 << i):  # Employee (i+1) is selected
                    employee_id = i + 1
                    cost = present[i]

                    # Check if this employee's direct parent is also selected
                    parent_id = parent[employee_id]
                    if parent_id > 0 and (mask & (1 << (parent_id - 1))):
                        # Parent is selected, so this employee gets discount
                        cost = cost // 2

                    total_cost += cost
                    if total_cost > budget:
                        valid = False
                        break

                    profit = future[i] - cost
                    total_profit += profit

            if valid:
                max_profit = max(max_profit, total_profit)

        return max_profit
