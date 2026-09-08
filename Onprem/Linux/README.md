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
