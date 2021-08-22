try:
    print(3 / 1)
except:
    print("0으로 나눌수 없음")
else:
    print("예외 없이 성공적으로 실행")
finally:
    print("실행 끝")



try:
    print(3/0)
except Exception as e:
    print(e)