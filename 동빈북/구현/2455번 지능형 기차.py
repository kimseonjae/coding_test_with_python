max_people = stay_people = 0

for _ in range(4):
    out_people, ride_people = map(int, input().split())
    stay_people = stay_people - out_people + ride_people
    max_people = max(stay_people, max_people)

print(max_people)