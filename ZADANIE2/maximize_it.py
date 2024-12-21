from itertools import product



def maximize_expression(K, M, lists):
    max_sum = 0
    for comb in product(*lists):
        sum_comb = sum(x**2 for x in comb) % M
        if sum_comb > max_sum:
            max_sum = sum_comb
    return max_sum

if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
