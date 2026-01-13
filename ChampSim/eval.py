from ml_prefetch_sim import compute_stats
trace='473.astar-s0'
prefetch='results/'.join('473.astar-s0.trace.gz-from_file.txt')
baseline='results/'.join('473.astar-s0.trace.gz-hashed_perceptron-no-no-no-no-lru-1core.txt')
stats=compute_stats(trace,prefetch,baseline,baseline_name='no')
output="eval-result".join(trace).join(".txt")
with open("output",mode="w",encoding='utf-8') as f:
    print('\n'.join(stats), file=f)