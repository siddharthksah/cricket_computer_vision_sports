import subprocess
import sys
import logging
import unittest
from unittest.mock import patch
from io import StringIO

class TestTracking(unittest.TestCase):
    
    def setUp(self):
        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        logging.getLogger().addHandler(console_handler)
        logging.getLogger().handlers[0].setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_tracking(self, mock_stdout):
        cmd = [
            'python', 'track.py', 
            '--tracking-method', 'deepocsort', 
            '--yolo-weights', '/home/sidd/Desktop/cricket_analysis/yolov5/runs/train/exp3/weights/best.pt', 
            '--source', '0',
            '--classes', '1'
        ]
        result = subprocess.run(cmd, input='q\n', stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        logging.info(result.stdout)
        logging.info('Command finished with return code: ' + str(result.returncode))
        self.assertEqual(result.returncode, 0)
        self.assertIn('DeepSORT', result.stdout)
            
    @patch('sys.stdout', new_callable=StringIO)
    def test_error_handling(self, mock_stdout):
        cmd = [
            'python', 'track.py', 
            '--tracking-method', 'deepocsort', 
            '--yolo-weights', '/home/sidd/Desktop/cricket_analysis/yolov5/runs/train/exp3/weights/best.pt', 
            '--source', 'invalid_input',
            '--classes', '1'
        ]
        with self.assertRaises(subprocess.CalledProcessError) as cm:
            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
        logging.info(cm.exception.output)
        self.assertIn('Error', cm.exception.output)

if __name__ == '__main__':
    unittest.main()
