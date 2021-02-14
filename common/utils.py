#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Mon 01 Feb 2021 09:16:16 AM CST

# File Name: utils.py
# Description:

"""
import logging
import os
import subprocess
import sys
from threading import Thread

def create_logger(logger_name, log_path=None):
    if log_path is None:
        log_path = check_home
    os.system('mkdir -p {0}'.format(log_path))

    # create formatter
    fmt = '%(asctime)s.%(msecs)d %(levelname)s %(process)d %(thread)d %(message)s (%(filename)s:%(lineno)d)'
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt)

    # create file handler
    log_file = log_path + '/' + logger_name + '.log'
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    # create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    return logger


# the default timeout is 1 day
def exec_cmd(cmd, timeout=10):
    global logger

    def execute(cmd):
        # execute cmd
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        ret = p.returncode
        out = out.strip()
        err = err.strip()
        result = {'ret': ret, 'out': out, 'err': err}
        return result

    class MyThread(Thread):
        def __init__(self, cmd):
            Thread.__init__(self)
            self.cmd = cmd
            self.result = None
            self.error = None

        def run(self):
            try:
                # get the result in one execute
                self.result = execute(self.cmd)
            except Exception, e:
                self.error = e

        def stop(self):
            self._Thread__stop()

    t = MyThread(cmd)
    t.start()
    # block the main thread, until the sub thread (t) is finished or timeout
    t.join(timeout)

    if t.error is not None:
        e = t.error
        ret = 1
        out = ''
        err = 'execute the command error!'
        result = {'ret': ret, 'out': out, 'err': err}
        logger.error('Execute the command [{0}] got exception [{1}]!'.format(cmd, e))
    elif t.result is None:
        ret = 1
        out = ''
        err = 'execute the command timeout!'
        result = {'ret': ret, 'out': out, 'err': err}
        logger.error('Execute the command [{0}] timeout [{1}]s!'.format(cmd, timeout))
    else:
        result = t.result
        ret = result['ret']
        logger.info('The command [{0}] is executed with returncode [{1}]'.format(cmd, ret))
        logger.info('The command [{0}] is executed with the result [{1}].'.format(cmd, result))

    # stop the thread
    if t.isAlive():
        t.stop()

    return result


# the default timeout is 1 day
def safe_exec_cmd(cmd, timeout=10):
    global logger

    result = exec_cmd(cmd, timeout)
    if result['ret'] != 0:
        # exit the process
        # exit thread if it is in a sub thread
        exit(1)

    return result
