from queue import Queue

def botbfs(f, n, cmds):
    q = Queue()
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    q.put(((0,0), 0, 0, 0, None))
    
    while not q.empty():
        robot, pos, ischange, dir, changed = q.get()
        
        if pos < n:
            cmd = cmds[pos]
            if cmd == "Forward":
                robx, roby = robot
                dx, dy = directions[dir]
                q.put(((robx+dx, roby+dy), pos+1, ischange, dir, changed))
                if not ischange:
                    q.put((robot, pos+1, 1, (dir+1)%4, (pos, "Right")))
                    q.put((robot, pos+1, 1, (dir-1)%4, (pos, "Left")))
                    
            elif cmd == "Left":
                q.put((robot, pos+1, ischange, (dir-1)%4, changed))
                if not ischange:
                    q.put((robot, pos+1, 1, (dir+1)%4, (pos, "Right")))
                    robx, roby = robot
                    dx, dy = directions[dir]
                    q.put(((robx+dx, roby+dy), pos+1, 1, dir, (pos, "Forward")))
                    
            else:
                q.put((robot, pos+1, ischange, (dir+1)%4, changed))
                if not ischange:
                    robx, roby = robot
                    dx, dy = directions[dir]
                    q.put(((robx+dx, roby+dy), pos+1, 1, dir, (pos, "Forward")))
                    q.put((robot, pos+1, 1, (dir-1)%4, (pos, "Left")))
                    
        else:
            dx, dy = directions[dir]
            if robot[0]+dx == f[0] and robot[1]+dy == f[1]:
                return changed

f_x, f_y = map(int, input().split())
n = int(input())
cmds = []
for i in range(n):
    cmds.append(input())

changed = botbfs((f_x, f_y), n, cmds)
print(changed)
if changed != None:
    print(changed[0]+1, changed[1])
else:
    print("No solution found")