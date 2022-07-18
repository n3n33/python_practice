

def solution (bridge_len, weight, *workers_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_len)]

    while bridge:
        answer += 1
        bridge.pop(0)
        if workers_weights:
            if sum(bridge) + workers_weights[0] <= weight:
                t = workers_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
            
    return answer