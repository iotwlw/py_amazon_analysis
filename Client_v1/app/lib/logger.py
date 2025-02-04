# coding:utf-8

import sys,os
curPath = os.path.abspath(os.path.dirname(__file__))
appPath = os.path.split(curPath)[0].replace("\\", "/").rstrip("\\") + "/../var/logs/"

import logging,time

class Log:
    def __init__(self, level='DEBUG', filePre="system_"):
        #创建日志文件夹
        if (not os.path.exists(appPath)):
            os.makedirs(appPath)

        # 文件的命名
        self.logname = os.path.join(appPath + filePre+'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        if(level == 'DEBUG'):
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

        # 日志输出格式
        # self.formatter = logging.Formatter('[%(asctime)s]-[%(process)d-%(thread)d]-%(levelname)s: %(message)s')
        self.formatter = logging.Formatter('[%(asctime)s]-%(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        #创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        #这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

if __name__ == "__main__":
   log = Log( 'info', 'system_')