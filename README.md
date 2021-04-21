# NETS213 Final Project - Glam Guru
Jones Pearlman, Anthony Kupecz, Anannya Shandilya, Anne Chen, Jordan Wong, and Samuel Kamien

# Raw Data
The raw data we used for our sample runs comes from a publically available dataset on Kaggle that contains 5000 images of clothes. The raw data can be found under NETS213FinalProject/data/.

# Sample input/output for QC
We generated fake sample data to use as inputs for testing our quality control module. This data can be found under NETS213FinalProject/QC&AggModules/. The following is a description of files in this folder - 

(1) sample_input.csv: This csv file contains our dummy data that we generated for 2 HITs where each HIT would contain 4 images, out of which one will be a gold standard image that will be used for testing worker quality.

(2) quality_control.py: This python file contains our code for quality control. We used majority vote system for quality control. For the sake of simplicity for workers, we modified our previous HIT design such that now users enter one word responses for each image to indicate if it fashinable/trashy and casual/formal. Each HIT is filled by 3 workers, and then, we use simple majority to determine the category for the clothing. 
To asses worker quality, we created 3 categories - quality for identifying fashionable vs trashy, quality for identify casual vs. formal, and overall quality i.e. quality for both categorizations (& clause).
While currently, we have simple majority, we may adopt weighted majority if we are able to find reliable gold standard image data i.e. data from credible sources that classifies clothes. We are also considering collecting gold standard data for quality check by sending questionnaires to fashion students.
If we are unable to generate reliable gold standard image data, we may adopt EM quality check method.

(3) sample_output.csv: This csv file shows the output that was generated after we ran our quality control module on our sample_input. It shows a simple majority classification of input images into Fashionable (True)-Trashy (False) and Casual (True)-Formal (False).

(4) worker_qual.csv: This csv file shows the output that was generated after we ran our quality control module on our sample_input for worker quality.

(5) Sample input_output Aggregation.xlsx: This excel file provides an overarching reader friendly summary of file 3.

(5) Sample input_output QC.xlsx: This excel file provides an overarching reader friendly summary of file 4.
