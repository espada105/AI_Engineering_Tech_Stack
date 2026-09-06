# ssh

1. docker destop 설정
- Settings → General → Use WSL 2 based engine 활성화
- Settings → Resources → WSL Integration → Ubuntu 활성화
- Apply / Restart 적용

2.Ubuntu SSH 서버 설치
sudo apt update
sudo apt install -y openssh-server
sudo systemctl enable --now ssh

3. Window, SSH 연결 설정
$ubuntuIp = ((wsl -d Ubuntu -- hostname -I).Trim() -split '\s+')[0]

netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=2222 connectaddress=$ubuntuIp connectport=22

if (!(Get-NetFirewallRule -Name "WSL-SSH-2222" -ErrorAction SilentlyContinue)) {
    New-NetFirewallRule -Name "WSL-SSH-2222" -DisplayName "WSL SSH 2222" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 2222 -RemoteAddress LocalSubnet
}

포트는 임시로 2222 설정함

4. 외부 접속시
ssh -p 2222 우분투계정아이디@접속주소