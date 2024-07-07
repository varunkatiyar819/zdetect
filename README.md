Received accuracy of about ~ 90%
- Install few libraries like sklearn, pandas and fasttext.
- Clone the repository.
- Assuming flores101.tar.gz would also had been cloned along with it, if not in case, download it first.
- untar the flors101.tar.gz file **tar -xzvf flores101_dataset.tar.gz** ensure to have hirerachy as : /flores101_dataset/* (make sure to extract dev and devtest folder other files and folders are not required.) 
    Note : Also if you want to apply it on different dataset modify the logic accordingly. Aim was trying to keep it generic.
- Run **python3 dataset_creation.py**, all the dataset file required for training and evaluation would be created
- Run **fasttext supervised -input model_train.txt -output model -lr 1.0 -epoch 30 -wordNgrams 2  -loss hs**, for training your own fasttext model for language detection purpose.
- Run **fasttext predict-prob model.bin - -1 0.5 < model_test.txt > output.txt**, for the inference from your dataset. 
- Run **python3 language_detect.py** file, to compute accuracy of your model on your test dataset.
    Note: You can manually compare the accuracy by checking (model_test.txt -> as test input sentence corresponding to it output.txt (for model's output) and actual_output.txt)

Points to Remember:
    - For more accuracy try to have a very large training dataset, may be you can go for flores200.
    - Tweak the Hyperparameters like learning rate, wordsNgram etc. to achieve better results.
    - Dont modify or delete any files during complete process.
    - Better to have conda environment to avoid any version confilcts.