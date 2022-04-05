import datetime
import os
import threading
import time
from synrate_main.models import ParserDetail


def timer():
    # time.sleep(5)
    print("TIMER: parsers autorun is ON")
    while True:
        while True:
            dt_now = datetime.datetime.now()
            time_now = dt_now.strftime("%M")
            # print(time_now)
            if time_now == "24" or time_now == "01":
            # if time_now == "00" or time_now == "01":
                change_status_for_all()
                os.system(f"python3 /var/www/synrate_dir/synrate/PARSER_SCRIPT/main.py --m short")
                time.sleep(120)
            elif datetime.datetime.today().weekday() == 5:
                change_status_for_all()
                os.system(f"python3 /var/www/synrate_dir/synrate/PARSER_SCRIPT/main.py")
            else:
                time.sleep(2)


def change_status_for_all():
    qs = ParserDetail.objects.all()
    for parser in qs:
        parser.status = 'В работе'
        parser.save()