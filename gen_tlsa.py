import os

def process_tlsa_files():
    # 현재 디렉토리에서 파일 목록 가져오기
    file_list = [f for f in os.listdir() if "TLSA" in f and os.path.isfile(f)]
    textnum = 0
    for file_name in file_list:
        # 각 파일을 읽어오기
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.readlines()

        # 16줄씩 나누어서 조각으로 처리
        chunks = [content[i:i + 16] for i in range(0, len(content), 16)]

        # 결과 파일 이름 설정
        output_file_name = f"{file_name[:-4]}_grouped.txt"
        output_file_path = os.path.join(os.getcwd(), output_file_name)

        # 결과를 파일에 저장
        with open(output_file_path, 'w', encoding='utf-8') as f:
            for chunk in chunks:
                # 각 조각에 "_443._udp.ns1.{hostname}." 형태 추가
                f.write('_443._udp.ns1.{}.{textnum}          IN      TLSA    3 0 0\n'.format(file_name[:-9]))
                f.write(''.join(chunk))
                f.write(')\n\n')  # 두 칸 띄우기
                textnum = textnum+1

# 사용 예시: 현재 디렉토리에서 실행
process_tlsa_files()
