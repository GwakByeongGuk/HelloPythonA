import teereal.empDAO as empdao

def displayMenu():
    main_menu = '''
    ========================
       - 사원 관리 프로그램 -
    ========================
        1. 사원 데이터 추가
        2. 사원 데이터 조회
        3. 사원 데이터 상세조회
        4. 사원 데이터 수정
        5. 사원 데이터 삭제
        0. 사원 관리 프로그램 종료
    ========================
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu

# 사원 데이터를 입력 받는 함수
def readEmp():
    emp = []
    cnt = empdao.getTotalEmp()
    emp.append(int(input(f'{cnt}번 사원 번호를 입력하시오: ')))
    emp.append(input(f'{cnt}번 사원 퍼스트네임을 입력하시오: '))
    emp.append(input(f'{cnt}번 사원 라스트네임을 입력하시오: '))
    emp.append(input(f'{cnt}번 사원 이메일을 입력하시오: '))
    emp.append(input(f'{cnt}번 사원 전화번호를 입력하시오: '))
    emp.append(input(f'{cnt}번 사원 고용일을 입력하시오: '))
    emp.append(input(f'{cnt}번 사원 직책을 입력하시오: '))
    emp.append(int(input(f'{cnt}번 사원 연봉을 입력하시오: ')))
    emp.append(float(input(f'{cnt}번 사원 커미션을 입력하시오: (없으면 0) ')))
    emp.append(int(input(f'{cnt}번 사원 상사 번호를 입력하시오: (없으면 0) ')))
    emp.append(int(input(f'{cnt}번 사원 부서 번호를 입력하시오: (없으면 0) ')))
    return emp

# 입력받은 사원 데이터를 처리하고 테이블에 저장
# 입력받은 수당, 매니저번호, 부서번호 적잘한 형변환 필요
def addEmp(emp):
    emp = readEmp()
    emp[8] = float(emp[8]) if emp[8] != 0 else 'null'
    emp[9] = int(emp[9]) if emp[9] != 0 else 'null'
    emp[10] = int(emp[10]) if emp[10] != 0 else 'null'
    empdao.newEmp(emp)

# 테이블에 저장된 사원 데이터들 중 기본 데이터만 모아서 출력
def showEmp():
    result = ''
    emps = empdao.readAllEmp()
    for emp in emps:
        result += f'{emp[0]} {emp[1]} {emp[3]} {emp[3]} {emp[4]}\n'
    print(result)

# 사원번호로 사원 데이터 조회 후 출력
def showOneEmp():
    empid = input('조회할 사원 번호는? ')
    result = '데이터가 존재하지 않아요!!'
    emp = empdao.readOneEmp(empid)
    if emp:   # 조회한 데이터가 존재한다면
        result = (f'{emp[0]} {emp[1]} {emp[2]} {emp[3]} {emp[4]} {emp[5]} {emp[6]} \n'
                  f'{emp[7]} {emp[8]} {emp[9]} {emp[10]}')
    print(result)

