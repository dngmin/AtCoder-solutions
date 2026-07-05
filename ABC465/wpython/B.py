X, Y, L, R, A, B = map(int,input().split())
core_time = {i for i in range(L, R+1)}
parking = {i for i in range(A, B+1)}

parking_time = B - A
core_time_parking_time = len(core_time & parking)
if core_time_parking_time:
    core_time_parking_time -= 1

print(X * core_time_parking_time + Y * (parking_time - core_time_parking_time))