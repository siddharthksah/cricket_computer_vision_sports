import os
import re
import subprocess
import unittest

class TestTraining(unittest.TestCase):

    def setUp(self):
        # Load environment variables from shell script
        env_cmd = '. ./env_vars.sh && env'
        env_output = subprocess.check_output(env_cmd, shell=True)
        env_vars = env_output.decode('utf-8').strip().split('\n')

        # Parse environment variables
        self.dir_path = ''
        self.data_path = ''
        self.log_path = ''
        for var in env_vars:
            key, value = var.split('=', 1)
            if key == 'DIR_PATH':
                self.dir_path = value
            elif key == 'DATA_PATH':
                self.data_path = value
            elif key == 'LOG_PATH':
                self.log_path = value

    def test_directory_exists(self):
        self.assertTrue(os.path.exists(self.dir_path))

    def test_changing_directory(self):
        os.chdir(self.dir_path)
        self.assertEqual(os.getcwd(), self.dir_path)

    def test_training_model(self):
        train_cmd = [
            'python', 'train.py', 
            '--img', '416', 
            '--batch', '128', 
            '--epochs', '100', 
            '--data', self.data_path, 
            '--weights', 'yolov5x.pt'
        ]
        result = subprocess.run(train_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1800, universal_newlines=True)
        self.assertEqual(result.returncode, 0)

    def test_log_file(self):
        self.assertTrue(os.path.exists(self.log_path))
        with open(self.log_path, 'r') as f:
            contents = f.read()
            self.assertIn('runs/train/exp', contents)
            self.assertIn('.', contents)

        with self.assertLogs() as cm:
            with open(self.log_path, 'r') as f:
                contents = f.read()
                start_idx = contents.find('runs/train/exp')
                end_idx = contents.find('.', start_idx) + 1
                sentence = contents[start_idx:end_idx]
                exp_num = re.findall(r'exp(\d+)', sentence)[0]
                results_location = os.path.join(self.dir_path, 'yolov5', 'runs', 'train', 'exp' + exp_num)
                self.assertIn('Results saved in: ' + results_location, cm.output[0])

if __name__ == '__main__':
    unittest.main()
