import os
from jsonrpclib import Server


def main():
    proxy = Server('http://localhost:7002')
    cmd = ''
    while cmd != 'quit':
        inp = os.path.basename(__file__) + ' ' + input('> ')
        splitInp = inp.split()
        cmd = splitInp[1]
        if cmd == 'ls':
            print(proxy.ls(splitInp))
        if cmd == 'count':
            print(proxy.count(splitInp))
        if cmd == 'put':
            print(proxy.put(splitInp))
        if cmd == 'get':
            print(proxy.get(splitInp))


if __name__ == '__main__':
    main()
