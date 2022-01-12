import requests
import re
from .models import Printer


def crawling_printers():
    print('Crawling printers ...')
    for printer in Printer.objects.all():
        try:
            response = requests.get(f'http://{printer.ip}/cgi-bin/config_periodic_data.cgi')

            # set_status(0, 10001, 86.330915, 41, 41, 'ff', 'ff', 'ff', 1, 58, 201, 'odroid-case.gcode')
            parameters = re.match(r'^set_status\((.+)\)$', response.text).group(1)
            estimate_time, print_job_status, print_job_processing, \
                filament_remain, fliament_sub, r, g, b, material, \
                bed_temp, nozzle_temp, filename = map(lambda param: param.strip(), parameters.split(','))

            printer.filament_remain = int(filament_remain)
            printer.state = '비활성화' if int(print_job_processing) == 100 else '활성화'
            printer.process = int(print_job_processing)

        except:
            print(f'Printer {printer.ip} seems not working. please check.')
