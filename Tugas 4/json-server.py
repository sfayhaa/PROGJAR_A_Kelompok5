from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import glob
import re


def ls(splitInp):
    try:
        a = glob.glob(splitInp[2])
        out = ''
        for i in a:
            out += i + "\n"
    except:
        out = splitInp[0]
    return out


def count(splitInp):
    try:
        out = len(glob.glob(splitInp[2]))
    except:
        out = 'Error'
    return out


def put(splitInp):
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


def get(splitInp):
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


def main():
    server = SimpleJSONRPCServer(('localhost', 7002))
    server.register_function(ls)
    server.register_function(count)
    server.register_function(put)
    server.register_function(get)
    print("Starting server")
    server.serve_forever()


if __name__ == '__main__':
    main()
