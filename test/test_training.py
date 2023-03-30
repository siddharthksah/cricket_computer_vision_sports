import os
import re
import subprocess
import unittest

class TestTraining(unittest.TestCase):

    def test_directory_exists(self):
        dir_path = '/home/sidd/Desktop/cricket_analysis/yolov5'
        self.assertTrue(os.path.exists(dir_path))

    def test_changing_directory(self):
        dir_path = '/home/sidd/Desktop/cricket_analysis/yolov5'
        os.chdir(dir_path)
        self.assertEqual(os.getcwd(), dir_path)

    def test_training_model(self):
        train_cmd = [
            'python', 'train.py', 
            '--img', '416', 
            '--batch', '128', 
            '--epochs', '100', 
            '--data', os.path.join('/home', 'sidd', 'Desktop', 'cricket_analysis', 'data', 'raw', 'cricket_dataset', 'data.yaml'), 
            '--weights', 'yolov5x.pt'
        ]
        result = subprocess.run(train_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1800, universal_newlines=True)
        self.assertEqual(result.returncode, 0)

    def test_log_file(self):
        log_path = os.path.join('/home', 'sidd', 'Desktop', 'cricket_analysis', 'train.log')
        self.assertTrue(os.path.exists(log_path))
        with open(log_path, 'r') as f:
            contents = f.read()
            self.assertIn('runs/train/exp', contents)
            self.assertIn('.', contents)

        with self.assertLogs() as cm:
            with open(log_path, 'r') as f:
                contents = f.read()
                start_idx = contents.find('runs/train/exp')
                end_idx = contents.find('.', start_idx) + 1
                sentence = contents[start_idx:end_idx]
                exp_num = re.findall(r'exp(\d+)', sentence)[0]
                results_location = os.path.join('/home', 'sidd', 'Desktop', 'cricket_analysis', 'yolov5', 'runs', 'train', 'exp' + exp_num)
                self.assertIn('Results saved in: ' + results_location, cm.output[0])

if __name__ == '__main__':
    unittest.main()
