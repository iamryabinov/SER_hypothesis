import os
import pandas as pd

CONFIG_PATH = 'tools\\opensmile-2.3.0\\config\\gemaps\\eGeMAPSv01a.conf'
EXE_PATH = 'tools\\opensmile-2.3.0\\bin\\Win32\\SMILExtract_Release.exe'
INPUT_PATH = ''
OUTPUT_PATH = 'features\\'
FILE_NAME = '03a05Wa.wav'

class FeatureExtractor:
    def __init__(self, input_folder, exe_path, config_path, output_folder):
        self.input_folder = input_folder
        self.exe_path = exe_path
        self.config_path = config_path
        self.output_folder = output_folder

    def construct_call_functionals_over_windows(self, input_file_name):
        instance_name = input_file_name.split('.')[0]
        config_options = ' -C ' + self.config_path
        input_options = ' -I ' + self.input_folder + input_file_name
        output_options = ' -csvoutput ' + self.output_folder + 'features_functionals_over_windows.csv'
        instance_options = ' -instname ' + instance_name
        misc = ' -loglevel 1 -nologfile'
        opensmile_call = self.exe_path + config_options + input_options + output_options + instance_options + misc
        return opensmile_call

    def construct_call_framewise_llds(self, input_file_name):
        instance_name = input_file_name.split('.')[0]
        config_options = ' -C ' + self.config_path
        input_options = ' -I ' + self.input_folder + input_file_name
        output_options = ' -lldcsvoutput ' + self.output_folder + 'features_framewise_llds.csv'
        instance_options = ' -instname ' + instance_name
        misc = ' -loglevel 1 -nologfile'
        opensmile_call = self.exe_path + config_options + input_options + output_options + instance_options + misc
        return opensmile_call

    def extract(self, input_file, method):
        if method == 'framewise_llds':
            opensmile_call = self.construct_call_framewise_llds(input_file)
        elif method == 'functionals_over_windows':
            opensmile_call = self.construct_call_functionals_over_windows(input_file)
        else:
            raise ValueError('Error!')
        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)
        os.system(opensmile_call)
        print(f'Extracted from {input_file} successfully')

if __name__ == '__main__':
    fe = FeatureExtractor(INPUT_PATH, EXE_PATH, CONFIG_PATH, OUTPUT_PATH)
    fe.extract(FILE_NAME, 'functionals_over_windows')