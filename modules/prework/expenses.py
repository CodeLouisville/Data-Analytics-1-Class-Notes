expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = sum(expenses)

# for reference
loop_total = 0
for expense in expenses:
    # sum = sum + x
    loop_total += expense  # short hand

print("Sum Method:  You spent $", total, " on lunch this week.", sep="")

# f-string substitution method to be covered later
print(f"Loop Method:  You spent ${total} on lunch this week.")
