from math import ceil
def solution(fees, records):
    answer = []

    car_charge = [0] * 10000
    is_car_here = [False] * 10000
    cars_id = []

    for i in range(len(records)):
        number = int(records[i][6:10])

        if records[i][11:13] == "IN":
            car_charge[number] -= int(records[i][0:2]) * 60 + int(records[i][3:5])
            is_car_here[number] = True
            cars_id.append(number)
        else:
            car_charge[number] += int(records[i][0:2]) * 60 + int(records[i][3:5])
            is_car_here[number] = False

    cars_id = list(set(cars_id))
    cars_id.sort()

    for i in cars_id:
        if is_car_here[i] == True:
            car_charge[i] += 23 * 60 + 59

        result = fees[1] + int(ceil((car_charge[i] - fees[0]) / fees[2])) * fees[3]
        result = fees[1] if result <= fees[1] else result

        answer.append(result)

    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
