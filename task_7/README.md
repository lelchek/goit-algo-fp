# Comparison of Monte Carlo and Analytic Results

This task evaluates the correctness of probability calculations obtained using the Monte Carlo method by comparing them with exact analytic probabilities for the sums of two fair dice.

## Monte Carlo vs Analytic Comparison

To demonstrate convergence, the simulation was executed with a small number of trials and with a large number of trials.

When the number of simulations is small, Monte Carlo estimates show noticeable random deviations.  
As the number of simulations increases, the estimated probabilities approach the analytic values.

## Results for N = 100

Sum | MC % | Analytic % | Abs err %
----|------|------------|----------
2  | 3.000 | 2.778 | 0.222
3  | 4.000 | 5.556 | 1.556
4  | 5.000 | 8.333 | 3.333
5  | 17.000 | 11.111 | 5.889
6  | 10.000 | 13.889 | 3.889
7  | 24.000 | 16.667 | 7.333
8  | 9.000 | 13.889 | 4.889
9  | 16.000 | 11.111 | 4.889
10 | 3.000 | 8.333 | 5.333
11 | 5.000 | 5.556 | 0.556
12 | 4.000 | 2.778 | 1.222

RMSE: 4.21%

## Results for N = 1,000,000

Sum | MC % | Analytic % | Abs err %
----|------|------------|----------
2  | 2.807 | 2.778 | 0.029
3  | 5.534 | 5.556 | 0.022
4  | 8.317 | 8.333 | 0.017
5  | 11.100 | 11.111 | 0.011
6  | 13.883 | 13.889 | 0.005
7  | 16.630 | 16.667 | 0.037
8  | 13.932 | 13.889 | 0.043
9  | 11.147 | 11.111 | 0.036
10 | 8.292 | 8.333 | 0.042
11 | 5.586 | 5.556 | 0.030
12 | 2.772 | 2.778 | 0.005

RMSE: 0.03%

## Conclusion

The comparison shows that Monte Carlo simulation produces probability estimates consistent with analytic calculations.  
For small numbers of trials, deviations are caused by randomness.  
With a large number of simulations, these deviations decrease significantly, confirming the correctness of the implemented algorithm and illustrating the law of large numbers.
