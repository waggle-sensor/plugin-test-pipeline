import waggle.plugin as plugin
from random import random
import time


def randvalue():
    return 25.0 + 5*random()


plugin.init()

while True:
    print('publishing measurement', flush=True)

    plugin.publish('test', randvalue(), meta={
        "mytag": "abc123",
    })

    print('uploading file', flush=True)

    with open('test-data.txt', 'w') as f:
        f.write(f'this is a test data file which includes value {randvalue()}.')
    
    plugin.upload_file('test-data.txt', labels={
        'label1': 'value1',
        'label2': 'value2',
        'label3': 'value3',
    })

    time.sleep(10)
