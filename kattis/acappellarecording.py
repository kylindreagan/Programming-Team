n, diff = map(int, input().split())

note_pitches = [None for _ in range(n)]
for i in range(n):
    note_pitches[i] = int(input())
note_pitches.sort()

if note_pitches[-1] - note_pitches[0] <= diff:
    print(1)
    quit()

recordings = 0
prev_min = -1 - diff
for pitch in note_pitches:
    if prev_min + diff < pitch:
        recordings += 1
        prev_min = pitch

print(recordings)