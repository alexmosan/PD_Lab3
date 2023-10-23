import os
import random

def get_instances_of_class(class_label, dataset_path):
    instances = []
    for root, dirs, files in os.walk(dataset_path):
        if os.path.basename(root) == class_label:
            instances.extend([os.path.join(root, filename) for filename in files])
    random.shuffle(instances)
    return instances

def get_next_instance(class_label, dataset_path):
    instances = get_instances_of_class(class_label, dataset_path)
    for instance in instances:
        yield instance

class_label = 'good'
dataset_path = 'D:/3-rd course/PD/PD_Lab3/dataset'

next_instance_generator = get_next_instance(class_label, dataset_path)

for next_instance in next_instance_generator:
    print(f"Следующий экземпляр класса {class_label}: {next_instance}")
