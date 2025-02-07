from DeepLearningOptimized import Data_DL
from DeepLearningOptimized import Model_DL

data_name = input("Data name: ")
model_name = input("Model name: ")

Model = Model_DL.model()
Model.load(model_name, activation_values=[4 for i in range(2)], min_diff=0.00001, learning_rate=0.00001, cycles=100, ignore_minimum=1, hidden_shaped=False, normaliser_depth=0)

Data_train = Data_DL.data()
Data_validate = Data_DL.data()

Data_train.extract(data_name + "TRAIN")
Data_validate.extract(data_name + "VALIDATE")

Data_train.batch_count = 100

Model.train(Data_train, Data_validate)
Model.save()