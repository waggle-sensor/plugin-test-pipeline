import waggle.plugin as plugin
from random import random
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG)

plugin.init()

while True:
    sleep(10)
    print('uploading data', flush=True)
    plugin.upload(b'my binary data')

    print('uploading file', flush=True)
    with open('mydata.txt', 'w') as f:
        f.write('this is a large data file to be sent to beehive')
    plugin.upload_file('mydata.txt', labels={
        'label1': 'value1',
        'label2': 'value2',
        'label3': 'value3',
    })

    value = 25.0 + 5*random()
    print('publishing', value, flush=True)
    plugin.publish('test', value)
