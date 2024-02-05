import os

def process_directory():
    # 현재 디렉토리에서 파일 목록 가져오기
    file_list = [f for f in os.listdir() if f.endswith('.txt') and os.path.isfile(f)]

    total_chunks = 0

    for file_name in file_list:
        # 각 파일을 읽어오기
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()

        # 230바이트씩 나누기
        chunks = [content[i:i + 230] for i in range(0, len(content), 230)]

        # 앞 뒤로 큰 따옴표와 빈 칸 추가
        formatted_chunks = [' " {} " '.format(chunk) for chunk in chunks]

        # 결과 파일 이름 설정
        output_file_name = f"{file_name[:-4]}_output.txt"
        output_file_path = os.path.join(os.getcwd(), output_file_name)

        # 결과를 파일에 저장
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(''.join(formatted_chunks))

        total_chunks += len(chunks)
        print(f"Total chunks: {total_chunks}")

# 사용 예시: 현재 디렉토리에서 실행
process_directory()
