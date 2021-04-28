# NETS213 Final Project - Glam Guru
Jones Pearlman, Anthony Kupecz, Anannya Shandilya, Anne Chen, Jordan Wong, and Samuel Kamien

# Raw Data
The raw data we used for our sample runs comes from a publically available dataset on Kaggle that contains 5000 images of clothes. The raw data can be found under NETS213FinalProject/data/. The link to the Kaggle dataset is https://www.kaggle.com/agrigorev/clothing-dataset-full

# Sample input/output for QC and Aggregation
We generated fake sample data to use as inputs for testing our quality control module. This data can be found under NETS213FinalProject/QC&AggModules/. The following is a description of files in this folder - 

(1) sample_input.csv: This csv file contains our dummy data that we generated for 2 HITs where each HIT would contain 4 images, out of which one will be a gold standard image that will be used for testing worker quality.

(2) quality_control.py: This python file contains our code for quality control and aggregation. 

* We used majority vote system for quality control and aggregation. For the sake of simplicity for workers and to avoid survey response issues like regression to mean or ambiguity in responses, we modified our previous HIT design (which was that users enter a number on scale of 1 to 4 to indicate how fashionable, formal, casual, or trashy a clothing item is) such that now users enter one word responses for each image to indicate if the clothing item shown is fashinable/trashy and casual/formal. Each HIT is filled by 3 workers, and then, we use simple majority to determine the category for the clothing. 

* To asses worker quality, we compare their response with majority response. We created 3 categories - quality for identifying fashionable vs trashy, quality for identifying casual vs. formal, and overall quality i.e. quality for both categorizations (implement using an & clause).

* While currently, we have simple majority, we plan to adopt weighted majority aggregation and quality check, if we are able to find reliable gold standard image data i.e. data from credible sources that classifies clothes into fashionable/trashy and casual/formal. We are planning to collect this gold standard data for quality check by sending questionnaires to fashion students and potentially, professors.

* If we are unable to generate reliable gold standard image data, we may adopt EM quality check method.

(3) sample_output.csv: This csv file shows the output that was generated after we ran our quality control module on our sample_input. It shows a simple majority classification of input images into Fashionable (True)-Trashy (False) and Casual (True)-Formal (False).

(4) worker_qual.csv: This csv file shows the output that was generated after we ran our quality control module on our sample_input for worker quality.

(5) Sample input_output Aggregation.xlsx: This excel file provides an overarching reader-friendly summary of file 3.

(5) Sample input_output QC.xlsx: This excel file provides an overarching reader-friendly summary of file 4.

# How to Contribute to Data Classification

1. Access the HIT [here](https://workersandbox.mturk.com/requesters/A31L69C4K3T6Z6/projects?ref=w_pl_prvw&fbclid=IwAR2ZTe2LYdVOBxuyV8o1O6KxypPhNYvzv-BlUTy_6PWPZjiZkfeXUHQYKQA)

2. You will be shown 12 images of clothes, and you will be tasked with classifying them as the following:
   - Fashionable & Casual
   - Fashionable & Formal
   - Not Fashionable & Casual
   - Not Fashionable & Formal

3. Then, after classifying each of the pictures, hit submit.
4. If you have any questions or comments, feel free to contact Anthony Kupecz at anthonykupecz@gmail.com -- Or call me at (732) 213-7558 -- Prank calls are welcomed. 


# Next Steps
Our next steps for this project will focus on - 

(1) gathering actual data

(2) refining our quality control and aggregation algorithm to incorporate gold standard labels

(3) implementing the machine learning algorithm

(4) testing and further analysis (with our preliminary analysis plans discussed below)

# Analysis Plan
We aim to primarily tackle the two questions of analyzing how accurate the subjective tastes of the crowd are and how well this method could scale in terms of time and money. 

To tackle the first question, we currently have a couple fashion major friends from Drexel manually labelling a handful of images (until they get tired), and we will use these as gold standard labels. Of course fashion is subjective, but surely there exists some creedence in the ability of a fashion major to accurately identify fashion. We will then compare the results of our MTurk hits to these gold standards and evaluate there quality from that.

To tackle the second question, we will see how well the responses from MTurk are, and of course throw out responses that were clearly incorrect. After seeing how much we had to pay to get X labels of images, we can approximate how much it would cost to get Y labels of images. We would need to see how the X labels of images do with training our model -- if the model's accuracy is good on the gold standard images, then we clearly don't need more labels. however, if the quality of the model is terrible on these gold standard labels, then we will try to estimate how many more pieces of training data we need to bump the accuracy up (which isn't simple/ necessarily possible to exactly determine), based on some assumptions that would be necessary for the calculation. 
