def state_def(name, index):
    tp = (name, index)
    states.append(tp)
    return states


machine = {}
states = []

for i in range(3):
    name = input()
    index = int(input())
    state_def(name, index)


machine = dict(states)
print(machine)
