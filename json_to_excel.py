import json
from openpyxl import Workbook


def json_to_excel(json_file, excel_file):
    # JSON 파일 읽기
    with open(json_file, 'r', encoding='utf-8-sig') as json_file:
        data: dict = json.loads(json_file.read())

    # 엑셀 워크북 생성
    workbook = Workbook()
    sheet = workbook.active

    # JSON 데이터를 엑셀로 복사
    for k, v in data.items():
        sheet.append([k, v])

    # 엑셀 파일 저장
    workbook.save(excel_file)

    print(f"JSON 파일 '{json_file}'이 '{excel_file}'로 성공적으로 변환되었습니다.")


# 사용 예시
json_to_excel('KLMRP\\assets\irons_spellbooks\lang\ko_kr.json', 'output.xlsx')
