#!/usr/bin/env python

import argparse
import json
import sys

requiredArgs = {
    'api_key': 'Sms77.io API key',
    'to': 'Receiver(s) separated by comma',
    'text': 'Message text'
}


def bool_arg(obj):
    return dict(obj, **{
        'action': 'store_const',
        'const': 1,
    })


optionalArgs = {
    'debug': bool_arg({
        'help': 'Disable dispatching'
    }),
    'delay': {
        'help': 'Dispatch at yyyy-mm-dd hh:ii or timestamp'
    },
    'details': bool_arg({
        'help': 'Append details'
    }),
    'flash': bool_arg({
        'help': 'Show directly on the recipients display'
    }),
    'foreign_id': {
        'help': 'Custom foreign id'
    },
    'from': {
        'help': 'Sender identifier',
    },
    'json': bool_arg({
        'help': 'Return JSON'
    }),
    'label': {
        'help': 'Custom label'
    },
    'no_reload': bool_arg({
        'help': 'Disable reload lock'
    }),
    'performance_tracking': bool_arg({
        'help': 'Enable performance tracking'
    }),
    'return_msg_id': bool_arg({
        'help': 'Append msg id'
    }),
    'ttl': {
        'help': 'Custom time to live',
        'type': int
    },
    'udh': {
        'help': 'Custom user data header'
    },
    'unicode': bool_arg({
        'help': 'Force unicode'
    }),
    'utf8': bool_arg({
        'help': 'Force UTF8'
    }),
}

parser = argparse.ArgumentParser()
for k in requiredArgs:
    parser.add_argument(k, help=requiredArgs[k])
for k in optionalArgs:
    parser.add_argument('--%s' % k, **optionalArgs[k])


def terminate(msg, status_code):
    print(msg)
    sys.exit(status_code)


if __name__ == '__main__':
    version = int(sys.version[:1])
    if 2 == version:
        from urllib2 import Request, urlopen
        from urllib import urlencode
    elif 3 == version:
        from urllib.request import Request, urlopen
        from urllib.parse import urlencode
    else:
        terminate('Unsupported python version %d' % version, 2)

    try:
        args = vars(parser.parse_args())
    except argparse.ArgumentError as e:
        terminate(e.message, 3)

    for k in requiredArgs:
        if not len(requiredArgs[k]):
            terminate('Argument %s must be lengthy!' % k, 3)

    req = urlopen(Request('https://gateway.sms77.io/api/sms', method='POST', headers={
        'Authorization': 'Basic %s' % args.pop('api_key'),
        'SentWith': 'Zabbix'
    }, data=urlencode(args).encode()))
    res = req.read()

    if args.get('json'):
        res = json.loads(res)
        code = res['success']
    else:
        res = str(res.decode(req.headers.get_content_charset() or 'utf-8')).strip()
        code = res.splitlines()[0]

    terminate(res, int(100 != int(code)))
