# NETS213FinalProject
Jones Pearlman, Anthony Kupecz, Anannya Shandilya, Anne Chen, Jordan Wong, and Samuel Kamien NETS213 Final Project

1. Gather training data (4 points)

Out plan is to gather the training data from various fashion websites. We will scrape these websites for images of outfits. We will also use google and other search engine tools to find pictures of un-fashionable outfits. This will be a farily involved process which we will put a lot of work into in order to ensure we have good quality training data.

DATA FORMAT:
  The raw data will be stored in a git directory as jpg files. The repository will also hold some pre designed CSV files which will serve as input to the HIT. The HIT we design will take one of the premade CSV files and display the images requiring labels to the workers. From here, the results will be downloaded and also stored in the GitHub repository.

2. Design the HIT (3 points)

The hit design will also be of utmost importance. In order to ensure that the data is labeled "properly" and efficiently, the HIT will need to be well designed. Furthermore, in order to keep the cost of this labeling relatively low, we will need to find a balance between loading as many images as possible in the hit and allowing for Turkers to give meaningful lables.

3. Have crowd workers label data (2 points)

Once the hit is complete, we will deploy as many batches as necessary in order to label all of the data.

4. Use gold-standard lables and dummy-questions for quality control (1 point)

In order to ensure the quality of our labels, we will have some of the data labeled in a gold-standard method by asking fashion majors to label some of the data beforehand. Additionally, we will add one or two "dummy" questions per hit. For example, it might show a picture and say "Please enter the number 0." That way, if a particular Turker doesn't answer that question correctly, we can reasonably throw out all of their responses.

5. Aggregate data in Python (3 points)

Once the data is labeled and downloaded we will write Python scripts in order to aggragate the data to our needs. This will involve determining the correct labels for data using a majority voting process, regrouping, and reorganizing the data into structures that will allow our model to be trained easily.

6. Train classifier(s) using the training data labeled by the cloud (3 points)

Once our data is succesfully aggregated, we will use the various Python machine learning libraries to train our classifier.

7. Build UI for users to submit images (3 points)

After the model is trained, we will begin working on the user interface for our application. This will likely be done in Python or possibly JavaScript. The UI will allow the users to upload images of their outfits and will give them a response letting them know how stylish it is as well as what kind of outfit it is.

8. Classify the image and return the results (1 point)

Once the user uploads their image, it will get passed over to our model to be evaluated. After the evaluation is complete, the results will be parsed and returned to the user in a nice, easy to read format.
