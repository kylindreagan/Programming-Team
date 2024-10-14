def find_awkwardness(people_list):
    language_positions = {}
    
    # Group people by language with their indices
    for index, language in enumerate(people_list):
        if language not in language_positions:
            language_positions[language] = []
        language_positions[language].append(index)

    min_distance = float('inf')
    for positions in language_positions.values():
        if len(positions) > 1:  # Only consider languages spoken by more than one person
            for i in range(1, len(positions)):
                distance = positions[i] - positions[i - 1]
                min_distance = min(min_distance, distance)

    return min_distance if min_distance != float('inf') else len(people_list)

def main():
    _ = int(input())
    people_list = input().split()
    
    print(find_awkwardness(people_list))

# Run the main function
if __name__ == "__main__":
    main()