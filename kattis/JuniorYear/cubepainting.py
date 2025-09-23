from typing import List

def all_rotations(cube:str) -> List[str]:
    rotations = []

    top_bottoms = [
        (0, 5), (5, 0),
        (1, 4), (4, 1),
        (2, 3), (3, 2),
    ]
    # For each top-bottom pair, rotate around the top face
    for top, bottom in top_bottoms:
        unflip = (top > bottom or top == 1) and top != 4
        flip = not unflip
        # Find the four other faces (sides)
        sides = [tup for tup in top_bottoms if tup != (top, bottom) and tup != (bottom, top)]
        # Generate four rotations for this top-bottom pair
        rotations.append("".join([cube[top],  cube[sides[0][0]], cube[sides[2][unflip]], cube[sides[2][flip]], cube[sides[0][1]], cube[bottom]]))
        rotations.append("".join([cube[top], cube[sides[1][0]], cube[sides[2][flip]], cube[sides[2][unflip]], cube[sides[1][1]], cube[bottom]]))
        rotations.append("".join([cube[top], cube[sides[2][0]], cube[sides[1][unflip]], cube[sides[1][flip]], cube[sides[2][1]], cube[bottom]]))
        rotations.append("".join([cube[top], cube[sides[3][0]], cube[sides[0][unflip]], cube[sides[0][flip]], cube[sides[3][1]], cube[bottom]]))

    return rotations

try:
    while True:
        cubeandrotate = input()
        cube, rotate = cubeandrotate[:6], cubeandrotate[6:]
        rotations = all_rotations(cube)
        if rotate in rotations:
            print("TRUE")
        else:
            print("FALSE")
except EOFError:
    quit()