import os
import rpyc


def main():
    config = {'allow_public_attrs': True}
    proxy = rpyc.connect('localhost', 18861, config=config)
    cmd = ''
    while cmd != 'quit':
        inp = os.path.basename(__file__) + ' ' + input('> ')
        splitInp = inp.split()
        cmd = splitInp[1]
        if cmd == 'ls':
            print(proxy.root.ls(splitInp))
        if cmd == 'count':
            print(proxy.root.count(splitInp))
        if cmd == 'put':
            print(proxy.root.put(splitInp))
        if cmd == 'get':
            print(proxy.root.get(splitInp))


if __name__ == '__main__':
    main()
