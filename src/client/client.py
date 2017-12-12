import urllib2
import json
import argparse


parser = argparse.ArgumentParser(description='Test request size.')
parser.add_argument('-f','--from_size', dest='from_size', help='from size.', type=int)
parser.add_argument('-r','--range', dest='range', help='range to test.', type=int)
parser.add_argument('-s','--server', dest='server', help='server address.')
parser.add_argument('-b','--base_size', dest='base_size', help='base size of the packet.', type=int, default=1)


args = parser.parse_args()


def get_request(params):

    for doc_size in range(params['from_size']*params['base_size'],
                          params['from_size']*params['base_size']+params['range']):
        str_val = 'x' * doc_size
        req = urllib2.Request(url=params['server'],
                              data=str_val)
        response = urllib2.urlopen(req)
        data = json.load(response)
        if data['received_bytes'] != doc_size:
            print ('''
            Sent data size: {0}
            Received data size : {1}          
            '''.format(doc_size, data['received_bytes']))


if __name__ == '__main__':

    params={}
    params['from_size'] = args.from_size
    params['range'] = args.range
    params['server'] = args.server
    params['base_size'] = args.base_size

    get_request(params)
    print "Done!"