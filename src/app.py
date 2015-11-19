# -*- coding: utf-8 -*-

import time

import schedule

from cmds import update_weights_in_mongo
from logger import project_logger


schedule.every().day.at("03:00").do(update_weights_in_mongo)


def main():
    for job in schedule.jobs:
        project_logger.info(job)

    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__ == '__main__':
    main()