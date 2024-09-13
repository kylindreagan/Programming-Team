from queue import Queue

class Move:
    def __init__(self, x, y, next) -> None:
        self.x = x
        self.y = y
        self.next = next # next move: 0 = press, 1 = right, 2 = down
    
    def __eq__(self, other):
        return isinstance(other, Move) and self.x == other.x and self.y == other.y and self.next == other.next

    def __hash__(self):
        return hash((self.x, self.y, self.next))
    
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.next})"
        

keypad = [["1","2","3"],["4","5","6"],["7","8","9"],[None,"0",None]]

def ratInAMicrowave(target, len_target):
    closest_time = float('inf')
    Q = Queue()
    visited = set()  # Keep track of visited states
    Q.put(("", Move(0,0,0)))
    Q.put(("", Move(0,0,1)))
    Q.put(("", Move(0,0,2)))
    while not Q.empty():
        curr = Q.get()
        currvalue, currmove = curr

        if currvalue != "" and int(currvalue) == target:
            return currvalue
        
        currx, curry = currmove.x, currmove.y

        match currmove.next:
            #PRESS
            case 0:
                new_value = currvalue + keypad[curry][currx]
                intval = int(new_value)

                if abs(target-intval)<=abs(target-closest_time):
                    closest_time = intval
                
                if len(new_value) <= len_target:
                    if (new_value, (currx, curry)) not in visited:
                        visited.add((new_value, (currx, curry)))
                        Q.put((new_value, Move(currx,curry,0)))
                        Q.put((new_value, Move(currx,curry,1)))
                        Q.put((new_value, Move(currx,curry,2)))
            #RIGHT
            case 1:
                if keypad[curry][currx] != "0" and currx + 1 < len(keypad[0]):
                    if (new_value, (currx + 1, curry)) not in visited:
                        Q.put((currvalue, Move(currx+1,curry,0)))
                        Q.put((currvalue, Move(currx+1,curry,1)))
                        Q.put((currvalue, Move(currx+1,curry,2)))
            #DOWN
            case 2:
                if keypad[curry][currx] != "0":
                    if keypad[curry+1][currx] != None:
                        if (new_value, (currx, curry+1)) not in visited:
                            Q.put((currvalue, Move(currx,curry+1,0)))
                            Q.put((currvalue, Move(currx,curry+1,1)))
                            Q.put((currvalue, Move(currx,curry+1,2)))

    return closest_time

def main():
    for _ in range(int(input())):
        target = int(input())
        len_target = len(str(target))
        if len_target == 1:
            print(target)
        else:
            print(ratInAMicrowave(target, len_target))

if __name__ == "__main__":
    main()