import requests
import re
from printers.models import Printer
import urllib.request
import os
from pathlib import Path


def crawling_printers():
    print('Crawling printers ...')

    for printer in Printer.objects.all():
        try:

            response = requests.get(f'http://{printer.ip}:8101/cgi-bin/config_periodic_data.cgi')

            # set_status(0, 10001, 86.330915, 41, 41, 'ff', 'ff', 'ff', 1, 58, 201, 'odroid-case.gcode')
            parameters = re.match(r'^set_status\((.+)\)$', response.text).group(1)
            estimate_time, print_job_status, print_job_processing, \
                filament_remain, fliament_sub, r, g, b, material, \
                bed_temp, nozzle_temp, filename = map(lambda param: param.strip(), parameters.split(','))

            printer.filament_remain = int(filament_remain)
            printer.state = '비활성화' if int(print_job_processing) == 100 else '활성화'
            printer.process = int(print_job_processing)
            print(printer.filament_remain, printer.state, printer.process)
            printer.save()

            BASE_DIR = Path(__file__).resolve().parent.parent

            url = f"http://deu818.kro.kr:8101/?action=snapshot"

            # 이미지 요청 및 다운로드
            downloaded_file = open(os.path.join(BASE_DIR, f'media/Image/{printer.ip}.png'), "wb")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            file_on_web = urllib.request.urlopen(req)
            while True:
                buf = file_on_web.read(65536)
                if len(buf) == 0:
                    break
                downloaded_file.write(buf)
            downloaded_file.close()
            file_on_web.close()

        except:
            print(f'Printer {printer.ip} seems not working. please check.')
