'''
주차 요금 계산

주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 차량별로 주차 요금을 계산하려고 합니다. 아래는 하나의 예시를 나타냅니다.

요금표
기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
180	            5000	        10	            600
 

입/출차 기록
시각(시:분)	    차량 번호    내역
05:34	        5961        입차
06:00	        0000	    입차
06:34	        0000	    출차
07:59	        5961	    출차
07:59	        0148	    입차
18:59	        0000	    입차
19:09	        0148	    출차
22:59	        5961	    입차
23:00	        5961	    출차
 

자동차별 주차 요금
차량 번호	    누적 주차 시간(분)      주차 요금(원)
0000	        34 + 300 = 334          5000 + ⌈(334 - 180) / 10⌉ x 600 = 14600
0148	        670	                    5000 +⌈(670 - 180) / 10⌉x 600 = 34400
5961	        145 + 1 = 146	        5000

어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다.
0000번 차량은 18:59에 입차된 이후, 출차된 내역이 없습니다. 따라서, 23:59에 출차된 것으로 간주합니다.
00:00부터 23:59까지의 입/출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 요금을 일괄로 정산합니다.
누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구합니다.
누적 주차 시간이 기본 시간을 초과하면, 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구합니다.
초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.
⌈a⌉ : a보다 작지 않은 최소의 정수를 의미합니다. 즉, 올림을 의미합니다.
주차 요금을 나타내는 정수 배열 fees, 자동차의 입/출차 내역을 나타내는 문자열 배열 records가 매개변수로 주어집니다.
차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
'''
from collections import defaultdict
from math import ceil

def hhmm2min(s):
    return 60*int(s[:2]) + int(s[3:])

def solution(fees, records):
    car_record = defaultdict(list) # car_record = {car: [time1, time2, ...]}
    for record in records:
        time, car, check = record.split()
        car_record[car].append(time)
        
    car_tot_time = [0]*len(car_record.keys()) # car_tot_time = 자동차별 총 주차시간 리스트(차 번호 오름차순)
    for j, car in enumerate(sorted(car_record.keys())):
        if len(car_record[car]) % 2 == 1:
            car_record[car].append("23:59")
        for i in range(0, len(car_record[car]), 2):
            car_tot_time[j] += hhmm2min(car_record[car][i+1]) - hhmm2min(car_record[car][i])
    answer = list(map(lambda x: fees[1] + ceil(max(0, x - fees[0])/fees[2]) * fees[3], car_tot_time))
    return answer
    