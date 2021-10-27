class Logger:
    def write_to_file(*args):
        f = open('output.txt', 'a')
        for i in args:
            f.write(str(i) + ' ')
        f.write('\n')
        f.close()


class Observer:
    observers = {}

    def __init__(self, event, callback):
        self.event = event
        self.observers[event] = callback

    def update(self, action, *args):
        if action == self.event:
            self.observers[action](action, args)


class Event:
    def __init__(self):
        self.ll = []

    def add(self, obser):
        if obser not in self.ll:
            self.ll.append(obser)

    def remove(self, obser):
        if obser in self.ll:
            self.ll.remove(obser)

    def notify(self, *args):
        for i in self.ll:
            i.update(*args)
