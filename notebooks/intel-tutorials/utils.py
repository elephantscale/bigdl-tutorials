import numpy as np
from bigdl.util import common
from bigdl.dataset import mnist

def get_mnist(sc, mnist_path):
    # target is start from 0,
    (train_images, train_labels) = mnist.read_data_sets(mnist_path, "train")
    (test_images, test_labels) = mnist.read_data_sets(mnist_path, "test")
    training_mean = np.mean(train_images)
    training_std = np.std(train_images)
    rdd_train_images = sc.parallelize(train_images)
    rdd_train_labels = sc.parallelize(train_labels)
    rdd_test_images = sc.parallelize(test_images)
    rdd_test_labels = sc.parallelize(test_labels)

    rdd_train_sample = rdd_train_images.zip(rdd_train_labels).map(lambda fl:
                                        common.Sample.from_ndarray(
                                        (fl[0] - training_mean) / training_std,
                                        fl[1] + 1))
    rdd_test_sample = rdd_test_images.zip(rdd_test_labels).map(lambda fl:
                                        common.Sample.from_ndarray(
                                        (fl[0] - training_mean) / training_std,
                                        fl[1] + 1))
    return (rdd_train_sample, rdd_test_sample)

COLUMNS = ["age", "workclass", "fnlwgt", "education", "education_num",
           "marital_status", "occupation", "relationship", "race", "gender",
           "capital_gain", "capital_loss", "hours_per_week", "native_country",
           "income_bracket"]

NUM_COLUMNS=15

LABEL_COLUMN = "label"

AGE, WORKCLASS, FNLWGT, EDUCATION, EDUCATION_NUM, MARITAL_STATUS, OCCUPATION, \
RELATIONSHIP, RACE, GENDER, CAPITAL_GAIN, CAPITAL_LOSS, HOURS_PER_WEEK, NATIVE_COUNTRY, \
LABEL = range(NUM_COLUMNS)

EDUCATION_VOCAB = ["Bachelors", "HS-grad", "11th", "Masters", "9th",
  "Some-college", "Assoc-acdm", "Assoc-voc", "7th-8th",
  "Doctorate", "Prof-school", "5th-6th", "10th", "1st-4th",
  "Preschool", "12th"] # 16
MARITAL_STATUS_VOCAB = ["Married-civ-spouse", "Divorced", "Married-spouse-absent",
    "Never-married", "Separated", "Married-AF-spouse", "Widowed"]
RELATIONSHIP_VOCAB = ["Husband", "Not-in-family", "Wife", "Own-child", "Unmarried",
    "Other-relative"]  # 6
WORKCLASS_VOCAB = ["Self-emp-not-inc", "Private", "State-gov", "Federal-gov",
    "Local-gov", "?", "Self-emp-inc", "Without-pay", "Never-worked"] # 9
GENDER_VOCAB = ["Female", "Male"]
AGE_BOUNDARIES = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65]

def hashbucket(sth, bucketsize = 1000, start = 0):
    return (id(sth) % bucketsize + bucketsize) % bucketsize + start

def categorical_from_vocab_list(sth, vocab_list, default = -1, start = 0):
    if sth in vocab_list:
        return vocab_list.index(sth) + start
    else:
        return default + start
    
def get_boundaries(numage, boundaries, default = -1, start = 0):
    if numage == '?':
        return default + start
    else:
        for i in range(len(boundaries)):
            if numage < boundaries[i]:
                return i + start
        return len(boundaries) + start
    
def get_label(label):
    if label == ">50K" or label == ">50K.":
        return 2
    else:
        return 1
    
def read(file, sc):
    lines=sc.textFile(file).map(lambda line: list(map(lambda word: word.strip(), line.split(',')))).filter(lambda line: len(line) == NUM_COLUMNS)
    return lines
