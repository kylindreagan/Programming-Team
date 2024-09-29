import itertools

colors = ['R','G','B']
MOD = 10**9+7
memory = {}

def initialize():
    # Initialize a grid to keep track of valid configurations
    dp = [[[0] * 18 for _ in range(C)] for _ in range(R)]
    
    # Fill in the dp for the first square
    for i in range(18):
        dp[0][0][i] = 1  # Each valid configuration is initially a separate valid arrangement
    
    return dp


def count_colorings(R, C, dp, valid_squares):
    
    
    # Calculate valid configurations for the entire grid
    for r in range(R):
        for c in range(C):
            for square_index in range(len(valid_squares)):
                current_square = valid_squares[square_index]

                if r > 0:  # Square above
                    for top_square_index in range(len(valid_squares)):
                        top_square = valid_squares[top_square_index]
                        if is_valid_transition(top_square, current_square, True):
                            dp[r][c][square_index] += dp[r-1][c][top_square_index]
                            dp[r][c][square_index] %= MOD

                if c > 0:  # Square to the left
                    for left_square_index in range(len(valid_squares)):
                        left_square = valid_squares[left_square_index]
                        if is_valid_transition(left_square, current_square, False):
                            dp[r][c][square_index] += dp[r][c-1][left_square_index]
                            dp[r][c][square_index] %= MOD

    # Sum all configurations in the last cell
    total_configurations = sum(dp[R-1][C-1]) % MOD
    return total_configurations

def generate_valid_configs():
    # Generate all valid edge combinations (2 edges colored)
    configs = []
    for color_comb in itertools.combinations(colors, 2):
        for orientation in itertools.product(color_comb, repeat=4):
            # Only keep combinations where exactly two edges are colored
            if len(set(orientation)) == 2 and orientation.count(orientation[0]) == 2:
                configs.append(orientation)
    return configs

def is_valid_transition(square1, square2, isVert):
    # Check if the transition between two squares is valid
    # Check shared edges: bottom edge of square1 must match top edge of square2
    if isVert:
        return square1[0] == square2[2]  # Assuming orientation: [left, top, right, bottom]
    else:
        return square1[3] == square2[1]

# Step 1: Generate all valid configurations for one square
valid_squares = generate_valid_configs()
dp = initialize()

for _ in range(int(input())):
    R, C = map(int, input().split())
    print(count_colorings(R,C,valid_squares,dp))