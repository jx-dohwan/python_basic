# 실습문제5.3.1
# 구구단 출력 프로그램을 만들어보자. 프로그램 사용자로부터 출력할 단을 입력받고,
# 해당하는 구구단을 출력하는 프로그램이다.

# dan = int(input("몇 단을 출력할까요?>>>"))3

# for i in range(1, 10, 1):
#     print(dan," * ",i, "=", dan*i)

# 실습문제5.3.2
# 페스트 게임즈에 인턴으로 근무하게된 종현
# 사수에게 게님 메뉴 만들기를 받았다
# 과제 내용은 다음과 같았다.

# 숫자 1 입력 : 게임을 시작합니다. 출력
# 숫자 2 입력 : 실시간 랭킹 출력
# 숫자 3 입력 : 게임을 종료합니다. 출력 후 프로그램 종료
# 단 3을 입력할때까지 프로그램은 계속 실행된다. 1~3외 다른 숫자를 입력한
# 경ㅜ 다시 입력하세요를 출력




# while True:
#     start = int(input("[메뉴를 입력하세요] \n 1.게임시작 2.랭킹보기 3.게임종료 >>"))
#     if start >= 1 and start <= 3:       
#         if start == 1:
#             print("게임을 시작합니다.")
#         elif start == 2:
#             print("실시간 랭킹")
#         else:
#             print("게임을 종료합니다.")
#             break
#     else:ㄴ
#         print("다시 입력하세요")

# 실습문제 5.3.3 -> 이거는 잘 몰라서 강의 조금 보고 품 input()를 잘 몰랐음 -> 기초개념 모름
# 성민이는 페스트 대학교에 lily라는 이름의 교환학생과 친해지게 되었다
# 영어를 잘하지 못했던 성민은
# lily에게 한국어를 가르쳐 주기 위해 한국어 연습 프로그램을 만들게 되었다.

# -learning korean-
# 1. 연습할 한국어가 담긴 리스트를 만든다.
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다.
# 3. 프로그램 사용자는 단어를 그대로 입력하고
# 4. 맞ㅊ면 다음단어를 가져온다. 틀리면 프로그램 종료

Kword = ["가지마", "안녕", "공부중", "나는 감자"]
score = 0
for i in Kword:
    print(i)
    data = input()
    if data == i:
        score += 1
    

    
#전제 문재 갯수
print("전체 문제 갯수 : ", len(Kword))
#맞힌 문제 갯수
print("맞힌 문제 갯수 : ",score)
#틀린 문제 갯수 
print("틀린 문제 갯수 : ", len(Kword)-score)