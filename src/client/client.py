import urllib2
import json
import argparse


parser = argparse.ArgumentParser(description='Test request size.')
parser.add_argument('-f','--from_size', dest='from_size', help='from size.', type=int)
parser.add_argument('-r','--range', dest='range', help='range to test.', type=int)
parser.add_argument('-s','--server', dest='server', help='server address.')


args = parser.parse_args()


def get_request(params):


    for doc_size in range(params['from_size'],
                          params['from_size']+params['range']):
        str_val = 'x' * doc_size
        sending_data = {'a': str_val}
        try:
            req = urllib2.Request(url=params['server'],
                                  data=json.dumps(sending_data))
            response = urllib2.urlopen(req)
            data = json.load(response)
            if data['received_bytes'] != len(json.dumps(sending_data)):
                print ('''
                Sent data size: {0}
                Received data size : {1}          
                '''.format(doc_size, data['received_bytes']))
        except Exception, e:
            print e
            print ('sent data size: {0}'.format(doc_size))
            exit(-1)

if __name__ == '__main__':

    params={}
    params['from_size'] = args.from_size
    params['range'] = args.range
    params['server'] = args.server

    get_request(params)
    print "Done!"