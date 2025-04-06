# -*- coding: utf-8 -*-
import time
import requests
import os
import platform

url = "http://192.168.56.101:7070/"

def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500)
    else:
        os.system('echo -e "\a"')

def restart_docker_container():
    print("[알림] 웹 서비스 재시작 중...")
    os.system("docker stop web")
    time.sleep(2)
    os.system("docker start web")
    print("[알림] docker 컨테이너 재시작 완료.")

def check_service():
    while True:
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print("[{}] 서비스 정상 작동".format(now))
            else:
                print("[{}] 상태 코드 이상: {}".format(now, response.status_code))
                beep()
                restart_docker_container()
        except requests.RequestException as e:
            print("[{}] 요청 실패: {}".format(now, e))
            beep()
            restart_docker_container()
        
        time.sleep(10)

check_service()
