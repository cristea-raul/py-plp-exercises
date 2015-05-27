from apis import Logger


def try_float(val):
    try:
        return float(val)
    except:
        return None


def try_int(val):
    try:
        return int(val)
    except:
        return None


class ConfigReader:
    store = {}

    def __init__(self, filename=''):
        self.logger = Logger(ConfigReader)
        if filename:
            self.read_config(filename)

    def read_config(self, filename):
        self.logger.info('Reading config file.')
        try:
            f = open(filename, 'r')
        except:
            self.logger.log('File not found.')
            return False

        for line in f:
            kv = line.split('=')
            if len(kv) != 2:
                continue
            kv[0] = kv[0].strip()
            kv[1] = kv[1].strip()
            intn = try_int(kv[1])
            if intn is not None:
                self.store[kv[0]] = intn
            else:
                floatn = try_float(kv[1])
                self.store[kv[0]] = floatn if floatn is not None else kv[1]
        return True

    def get_val(self, key):
        try:
            return self.store[key]
        except:
            self.logger.log('Key not found.')
            return None

    def contains(self, key):
        return key in self.store

    def clear(self):
        self.store = {}

    def __repr__(self):
        return str(self.store)