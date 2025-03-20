
Convolution Neural Network is used to classify the leaf dataset.

splitfolders used to split data into train(80%)and test(20%)

imported splitted images into train and test set(Not used)

Bulid model
Sequential is the model used, it takes the entire neural network at once (forward and backward propagation)
Convoltion layer used to extract information from the image and reduce the size.
BatchNormalization used to normalize data.
added dropout to prevent overfitting
pooling control overfitting and shortens the training time. Max also woks as noise suppresent.
for additional support add 1 more convoltion and pooling layer
Flatten convorts 3D image into 1D vector. Because Dense only accepts 1D.
Dense is the fully connected layer act as hidden layer and output layer. units shows the neurons used.
output has units=10(10 number of classes)
Activation used to inculate non-linearity to the model. relu can't be used for output layer, cause it faces a problem called vanishing gradient problem
where weights are getting updated. so i use softmax.

Compile model(our aim is to minimize loss function, that is error)
optimizer:Ensures every weight is updated during Back propagation. Adam smoothen the weight updation by exponential smoothing and adaptive learnig rate.
As weight reaches optimal minima it decreases the speed convergence.
loss=categorical_crossentropy is used because model contain more than one target feature.

Train test split used

Fit model using train and test.

Accuracy was not bad.

prediction
predict leaf name when path is given and that was accurate
