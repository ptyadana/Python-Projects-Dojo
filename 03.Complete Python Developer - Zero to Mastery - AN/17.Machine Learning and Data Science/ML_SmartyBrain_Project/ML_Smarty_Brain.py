from imageai.Prediction import ImagePrediction
import os

#get current working directory
execution_path = os.getcwd()

#will use SqueezeNet model from 4 types of supported models
prediction = ImagePrediction()
prediction.setModelTypeAsSqueezeNet()
prediction.setModelPath(os.path.join(execution_path, "squeezeNet_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

#result count : how many predictions we want the model to give us
predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "giraffee.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)