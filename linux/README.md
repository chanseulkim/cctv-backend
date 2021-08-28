# 녹화는 motion을 사용합니다.
# motion 설치
sudo apt install motion -y

# motion 설치 후 setconfig.py를 실행 해주세요
# 이 스크립트느 녹화 위치와 녹화파일을 아래와 같이 설정 해줍니다.
python3 setconfig.py
# 녹화파일 위치 : /home/motion_records
# 녹화파일 포맷 (연월일시분초) : %Y-%m-%d-%H-%M-%S.mkv

# motion파일 위치, config 위치 : config에서 데몬모드 콘솔모드 선택가능
/etc/motion

# 모션실행
sudo motion

# 매니저실행 (motion_manager.py)
# 하루가 지난 파일은 디렉토리로 만들어서 옮기고
# 2주가 지난 파일은 삭제합니다.
nohup python3 motion_manager.py &