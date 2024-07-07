# Importing libraries
import pandas as pd, os
from sklearn.model_selection import train_test_split
# NLP Preprocessing
# from gensim.utils import simple_preprocess

def process_file(file_path, filename, dataset_type):
    with open(file_path, "r") as f1, open(f'{dataset_type}.txt', "a") as f2:
        line = f1.readline()
        print(line)
        while line:
            if dataset_type == 'train':
                line = '__label__' + filename.split(".")[0] + f" {line}"
            f2.writelines(line)
            line = f1.readline()


work_dir = os.getcwd() + "/flores101_dataset"
def create_training():
    for filename in os.listdir(work_dir+"/dev"):
        file_path = os.path.join((work_dir+"/dev"), filename)
        if os.path.isfile(file_path):
            process_file(file_path, filename, dataset_type="train")

def create_testing():
    for filename in os.listdir(work_dir+"/devtest"):
        file_path = os.path.join((work_dir+"/devtest"), filename)
        if os.path.isfile(file_path):
            process_file(file_path, filename, dataset_type="train")

def shuffle_create_test():
    with open("train.txt", "r") as f:
        lines = f.readlines()
    training, testing = train_test_split(lines, test_size=0.1, random_state=42, shuffle=True)
    with open("model_train.txt", "w") as f1:
        f1.writelines(training)
    
    

    actual_output = [line[:12]+"\n" for line in testing]
    test_lines = [line[14:] for line in testing]

    with open("model_test.txt", "w") as f1, open("actual_output.txt", "w") as f2:
        f1.writelines(test_lines)
        f2.writelines(actual_output)

create_training()
create_testing()
shuffle_create_test()

# # Importing the dataset
# dataset = pd.read_csv('train.csv')[['Body', 'Y']].rename(columns = {'Body': 'questions', 'Y': 'category'})
# ds = pd.read_csv('valid.csv')[['Body', 'Y']].rename(columns = {'Body': 'questions', 'Y': 'category'})

# # NLP Preprocess
# dataset.iloc[:, 0] = dataset.iloc[:, 0].apply(lambda x: ' '.join(simple_preprocess(x)))
# ds.iloc[:, 0] = ds.iloc[:, 0].apply(lambda x: ' '.join(simple_preprocess(x)))

# # Prefixing each row of the category column with '__label__'
# dataset.iloc[:, 1] = dataset.iloc[:, 1].apply(lambda x: '__label__' + x)
# ds.iloc[:, 1] = ds.iloc[:, 1].apply(lambda x: '__label__' + x)