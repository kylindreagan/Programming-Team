MOD = 10**9+7
def count_colorings(R, C):
    # Step 1: Generate all valid configurations for one row
    valid_configs = generate_valid_configs(C)
    
    # Step 2: Initialize the DP table for row 1
    dp = {config: 1 for config in valid_configs}
    
    # Step 3: Fill the DP table for each subsequent row
    for r in range(1, R):
        new_dp = {config: 0 for config in valid_configs}
        for curr_config in valid_configs:
            for next_config in valid_configs:
                if is_valid_transition(curr_config, next_config):
                    new_dp[next_config] += dp[curr_config]
        dp = new_dp
    
    # Step 4: The final answer is the sum of all valid configurations in the last row
    return sum(dp.values())

def generate_valid_configs(C):
    # Generate all valid row configurations (adjacent vertical edges must match)
    # This is problem-specific and involves enumerating valid colorings.
    pass

def is_valid_transition(curr_config, next_config):
    # Check if the transition between two rows is valid
    # i.e., the vertical edges shared between rows must match in color.
    pass

for _ in range(int(input())):
    R, C = map(int, input().split())
    
    print(count_colorings(R,C))