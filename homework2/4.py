n = int(input())
k = int(input())
photo_count = {}
for i in range(n):
    new_photo = input()
    if new_photo in photo_count.keys():
        photo_count[new_photo] += 1
    else:
        photo_count[new_photo] = 1
    if photo_count[new_photo] <= k:
        print(new_photo)