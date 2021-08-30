# 녹화는 motion을 사용합니다.
# motion 설치
sudo apt install motion -y

# motion 설치 후 setconfig.py를 실행 해주세요
# 이 스크립트는 녹화 위치와 녹화파일을 아래와 같이 설정 해줍니다.
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
# 
# 오늘 녹화중인 녹화파일은 기본 위치에 생성 (예: "/home/motion_records/2021-08-12-15-30")
# 오늘 이전 녹화파일 위치는 디렉토리에 옮김 (예: "/home/motion_records/2021-08-11/2021-08-11-10-15")
nohup python3 motion_manager.py &

# 스케줄링
# crontab -e 로 수정, 아래 내용 추가 (매일 00시 1분 실행)
# crontab -l 로 스케줄 내용 확인
1 00 * * * python3 /home/chanseulkim/momo/linux/motion_manager.py

# cron 서비스 실행, 확인
sudo service cron start
service cron status
