from src.data.load_dataset import LoadDataset
import logging

def run():
    logger.info('* 1 * Loading raw dataset')
    load_dataset = LoadDataset()
    train_values, train_labels, test_values = load_dataset.read_raw_data()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(name)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S ', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info('Executing model evaluator')
    run()

