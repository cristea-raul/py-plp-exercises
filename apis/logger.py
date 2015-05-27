import datetime


class Logger:

    log_file = ''

    def __init__(self, parent=''):
        self.class_name = parent.__name__

    @staticmethod
    def setup(log_file):
        Logger.log_file = log_file

    def log(self, message, level='error'):
        if self.class_name:
            message = self.class_name + ' - ' + message
        message = '[' + str(datetime.datetime.now()) + '] ' + level.upper() + ' - ' + message
        if Logger.log_file:
            f = open(Logger.log_file, 'a')
            print(message, file=f)
            f.close()
        else:
            print(message)

    def info(self, message):
        self.log(message, level='INFO')

    def warn(self, message):
        self.log(message, level='WARNING')