# Linux

## cd
### cd foldername(지정경로)
- foldername으로 이동
-> 상대 경로는 내 현재 위치 기준이고, 절대 경로는 최상위 기준이다.

### cd /
- 최상위 루트로 이동(시스템 최상단 루트 디렉토리로 이동)

### cd ~
- 로그인 계정의 home 디렉토리 이동

### cd ..
- 상위 폴더 이동(바로 전 단계인 부모 폴더로 나감)

### cd -
- 직전 경로로 이동(뒤로가기)

## pwd
- print working directory로 내 위치 출력

## ls
- List 파일 및 폴더 목록 보기

### ls
- 기본 목록 출력

### ls -l
- 파일 권한, 용량, 수정 날짜 등 상세 정보 보기

### ls -a
- 숨김 파일(.으로 시작하는 파일)까지 포함해서 보기

### ls -la
- 숨김 파일 포함 전체 상세 정보 보기 (실무 표준)

## mkdir
- make directory, 새폴더 만들기

### mkdir foldername
- foldername 폴더 생성(현 위치에)

## touch
- 빈 파일 만들기

### touch filename.확장자
- filename.확장자 파일 생성

## cp
- 파일 및 폴더 복사

### cp file.txt backup.txt
- file.txt를 backup.txt라는 이름으로 복사

### cp -r folder1 copyfolder2
- 폴더 전체를 복사할때는 -r(recursive 옵션을 붙여야 한다)

## mv
- 파일 이동하기 및 이름 변경

### mv file.txt /home/user
- 해당 경로로 파일 이동

### mv old_name.py new_name.py
- 파일 이름 변경(같은 디렉토리 내 이동)

## rm
- 파일 및 폴더 삭제

### rm file.txt
- 파일하나 삭제

### rm -r folder
- 폴더와 그 안의 내용 전체 삭제(recursive)

### rm -rf folder
- 폴더/파일 강제 삭제

## cat
- concatenate 파일 내용 전체 출력

### cat file.json
- 파일 전체 내용 화면 출력

### cat file1.txt file2.txt > combined.txt
- 두 파일의 내용 합쳐서 새 파일로 저장

## chmod
- 파일 폴더 권한 변경

### chmod +x run.sh
- 해당 파일에 실행(+x) 권한 부여

### chmod 755 script.sh
- 소유자에게 읽기/쓰기/실행 권한 부여

## chown
- Change Owner 파일 폴더 소유자 변경

### chown user1:user1 file.txt
- 파일 소유자를 user1 계정과 그룹으로 변경

### chown -R user1:user1 my_folder/
- 폴더 및 하위 모든 파일의 소유자 변경

## find
- 디렉토리 전체를 뒤져서 내가 찾는 파일이 어디 있는지 검색

### find .-name".py"
- 현재폴더(.) 아래의 모든 .py 파이썬 파일 찾기

### find /home -name "model.bin"
- /home 경로 아래에서 해당파일 위치 찾기