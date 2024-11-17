# cook your dish here
states = ["NORMAL", "HUGE", "SMALL"]  # The order of states
x = int(input())
for i in range(x):
    a = int(input())
    final_state = states[a % 3]  # Use modulus to determine the final state
    print(final_state)