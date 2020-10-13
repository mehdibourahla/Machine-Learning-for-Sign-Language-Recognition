## Machine Learning for Sign Language Recognition: an Application on Smart Buildings

This work was done in partial fulfillment of the conditions for the award of the degree Master Software engineering in the University of Saad Dahbleb Blida and the Research Centre for Scientific and Technical Information (CERIST).

The main goal of this project is to conceive and realize a solution based on machine learning for sign language recognition that allows the control of a smart home environment through gestures.

We proposed a solution that is based on channel state information measurements present in the Wi-Fi signal, which reflect the gestures of sign language performed in the environment. We made two different architectures that meet the needs of our subject. The wordbased architecture processes the input measurements sign-by-sign with a CNN model, and then performs sentence-level recognition with an LSTM model to predict the desired action. As for the sequence-based architecture, it processes the measurements in sequences with a ConvLSTM model to directly predict the desired action. This solution is implemented using the Python programming language and the Keras deep learning framework and is evaluated using the SignFi public dataset (accessible here: https://github.com/yongsen/SignFi) , which offers pre-processed and segmented word-by-word CSI measurements.

This repository regroups the implementation of our work namely the three developed models (CNN, LSTM and ConvLSTM) with Keras. And also the demonstration application made with Flask.
