import glob
import re
import rpyc


def main():
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()


class MyService(rpyc.Service):
    def exposed_line_counter(self, fileobj, function):
        print('Client has invoked exposed_line_counter()')
        for linenum, line in enumerate(fileobj.readlines()):
            function(line)
        return linenum + 1

    def exposed_ls(self, splitInp):
        try:
            a = glob.glob(splitInp[2])
            out = ''
            for i in a:
                out += i + "\n"
        except:
            out = splitInp[0]
        return out

    def exposed_count(self, splitInp):
        try:
            out = len(glob.glob(splitInp[2]))
        except:
            out = 'Error'
        return out

    def exposed_put(self, splitInp):
        out = ''
        try:
            fileFrom = open(splitInp[2], 'r')
            fileTo = open(splitInp[3], 'a')
            for line in fileFrom:
                fileTo.write(line)
            fileTo.write('\n')
            fileFrom.close()
            fileTo.close()
        except:
            out = 'Error'
        return out

    def exposed_get(self, splitInp):
        out = ''
        try:
            file = open(splitInp[2], 'r')
            lookFor = splitInp[3]
            for line in file:
                if re.search(lookFor, line):
                    out += line
            file.close()
        except:
            out = 'Error'
        return out


if __name__ == '__main__':
    main()
