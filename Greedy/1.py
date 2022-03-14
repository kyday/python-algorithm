# 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# 거스름돈
# 거슬러 줘야 할 돈이 N원일때 거슬러 줘야 할 동전의 최소 개수
# 가장 큰 화폐 단위부터..

# ex) 1260원

n = 1260
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
  count += n // coin
  print(count)