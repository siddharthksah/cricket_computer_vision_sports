import subprocess
import sys
import logging

# configure logging
logging.basicConfig(filename='track.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

cmd = [
    'python', 'track.py', 
    '--tracking-method', 'deepocsort', 
    '--yolo-weights', '/home/sidd/Desktop/cricket_analysis/yolov5/runs/train/exp3/weights/best.pt', 
    '--source', '0',
    '--classes', '1' # ball class
]

try:
    with subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            sys.stdout.buffer.write(line.encode('utf-8'))
            logging.info(line.strip())
            
        p.communicate(input='q')  # send 'q' to terminate the command
        
        logging.info('Command finished with return code: ' + str(p.returncode))
except subprocess.CalledProcessError as e:
    logging.error('Command failed with return code ' + str(e.returncode))
    logging.error(e.output.decode('utf-8'))
    print('Error: ' + e.output.decode('utf-8'))

print('Done.')
