import os
import yaml
import pandas as pd
import logging


class Saver:
    def __init__(self, config_path='config/config.yaml'):
        config = yaml.safe_load(open(config_path, encoding='utf-8'))

        self.data_dir = config['storage']['data_dir']
        self.data_format = config['storage']['data_format']

        self.visualize_dir = config['storage']['visualize_dir']
        self.picture_dir = config['storage']['picture_dir']

        logging.basicConfig(
            filename=config['storage']['log_file'],
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def save_data(self, data, filename):
        filepath = os.path.join(self.data_dir, filename + '.' + self.data_format)
        filedir = os.path.dirname(filepath)
        if not os.path.exists(filedir):
            os.makedirs(filedir)
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)
        logging.info(f'Saving data to {filepath}')
