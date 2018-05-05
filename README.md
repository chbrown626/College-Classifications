# Classifying Colleges Creatively

### Overview

This project takes HTML website data from four colleges in the United States and classifies them into seven different categories using Python's SciKit Learn and NLTK. The [4 Universities](http://www.cs.cmu.edu/afs/cs.cmu.edu/project/theo-20/www/data/) project was originally completed using [*Rainbow*](http://www.cs.cmu.edu/afs/cs/project/theo-11/www/naive-bayes/gentle_intro.html) in 1998, but has not been attempted using new coding or data science methods. The websites come from Cornell, Texas, Washington, Wisconson, and other miscellaneous universities from around the country and will be separated into the following categories:

   * course
   * department
   * faculty
   * other
   * project
   * staff
   * student
   
### Motivation

Being that we live in an age where education is more readily available online, it would nice to have easy access to relevant web pages. Higher education being accesible to all is critical for the advancement of our society and if I can use data science to assist in making this happen, then I am willing to accept that challenge. I am extremely passionate about higher education and teaching and this project gave me an opportunity to use the skills I have learned throughout my program and apply them to something relevant to my passions.

This project also presented me with the opportunity to utilize skills that I had not yet honed. I chose to do this project in Python in order to further advance my portfolio and force myself to step out of my comfort zone.

### Importing the Data

The data used is readily available via the [4 Universities](http://www.cs.cmu.edu/afs/cs.cmu.edu/project/theo-20/www/data/) site. The file comes GNU tar'ed and gzip'ped; I chose to complete the extraction on my desktop, but this can also be accomplished using Python. Once all the files are extracted, the data can be imported using **os.walk()** and **BeautifulSoup**; **os.walk()** allows us to read all 8282 HTML files into Python quickly and **BeautifulSoup** parses the HTML files. 

Once the data is imported, it can be cleaned using the usual text processing methods. This includes removing numbers, punctuation, converting the text to lowercase, removing stopwords, and lemmatizing the text. This makes the text documents easier to process and categorize accordingly. These steps can be completed individually or via a function that loops through each step and covers the full dataset; often times a function is more efficient and can be used for multiple tasks.

### Reviewing the Data

With the data loaded and cleaned, we can now review how the data is disbursed among the categories:

![orderd category plot](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/category_plot_2.png "Category - Ordered")

From this we can see that the 'other' category contains the most files, with 'student' files in a far second. Now let's review the word clouds for the full dataset and each category:

* Full Dataset
![full wc](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/full_wc.png "Full Word Cloud")

* Course Category
![course wc](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/course_wc.png "Course Word Cloud")

* Deparment Category
![department wc](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/department_wc.png "Department Word Cloud")

* Faculty Category
![faculty wc](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/faculty_wc.png "Faculty Word Cloud")

* Other Category
![other wc](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/other_wc.png "Other Word Cloud")

* Project Category
![project wc](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/project_wc.png "Project Word Cloud")

* Staff Category
![staff wc](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/staff_wc.png "Staff Word Cloud")

* Student Category
![student wc](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/student_wc.png "Student Word Cloud")

From these clouds we can see that **computer science** is a main theme on all of the collected pages, regardless of the category that they originated from. 

In order to further understand the categories, it was useful to review the most highly correlated words and bigrams from each category. For the 'course' category, *syllabus* and *instructor* were the most highly correlated words, while the most highly correlated bigrams were *course information* and *office hour*. To review the full set of correlations for words and bigrams use either [html_tfidf_unigram_bigram.py](https://github.com/chbrown626/College-Classifications/blob/master/html_tfidf_unigram_bigram.py) code or review the [HTML Jupyter Notebook](https://github.com/chbrown626/College-Classifications/blob/master/new_html_notebook.ipynb).

### TF-IDF Vectorization

The TF-IDF helps us find relationships between words and how many times a word may appear within the documents. *Computer* appears only  10,266 times within the documents, while *syllabus* appears 55,348 times. It was also determined that the term *syllabus* appearing in the 'faculty' category only has a mean of 0.13%; this was rather surprising since the majority of faculty I know utilize the syllabus regularly to reinforce the course objectives and outcomes. 

### Multinomial NB Model

For the Multinomial Naive-Bayes model, I created training and testing sets that were then vectorized to help rate performance of the model. Unfortunately, every test I performed failed. I pulled documents from the 'course', 'faculty', and 'student' categories, but each time the model classified them as 'other'. Based on that, I decided to review the confusion matrix for the model:

![NB conf mat](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/MNB_conf_mat.png "MultiNB Confusion Matrix")

This clearly shows that the Multinomial Naive-Bayes model will not accurately classify the HTML college documents. I also wanted to review the precision of the model:

![NB precision](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/MNB_Precision.PNG "MultiNB Precision")

From this, we can see 'department', 'project', and 'staff' have precision scores of 0.00. This clearly shows that the Multinomial Naive-Bayes model is not the best fit for classifying the college data.

### Determining the Best Model

Since we have ruled out the success of the Multinomial Naive-Bayes model in classification, we will now review five other modelling methods to determine which will provide the best results. The models we will review are **Random Forest Classifier**, **LinearSVC**, **BernoulliNB**, **GaussianNB**, and **Logistic Regression**. First we will review a boxplot comparison of the different models:

![Model Comp](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/model_compare.png "Model Comparisons")

The boxplot clearly shows that **LinearSVC** will be the most accurate model for this dataset. However, we will also review the accuracy rating for the models:

![Model Accuracy](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/model_accuracy.PNG "Model Accuracy")

Once again proving that **LinearSVC** is the best model with an accuracy rating of 81%.

### LinearSVC Model

Similarly as with the Multinomial Naive-Bayes model, we will creating training and test sets from the data and run them through the LinearSVC model. We will then review the confusion matrix and the precision of the model. When looking at the confusion matrix, we can see that this model is considerably more accurate in classifying the HTML documents:

![LSVC conf mat](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/linsvc_conf_mat.png "LinearSVC Confusion Matrix")

And this model is much more precise, with precision values in the 80's and 90's for six out of the seven categories:

![LSVC precision](https://raw.githubusercontent.com/chbrown626/College-Classifications/master/Images/linsvc_precision.PNG "LinearSVC Precision Scores")

### Conclusion

In order to ensure accurate classification it is import to review multiple model types before settling on one. There are several different modeling methods available and it is important for researchers to understand what all is available. Often times we get stuck into believing that a certain model type is the only model type, because we are comfortable with its functionality and results, but it is important to recognize that different types of data need different types of models. 

Overall, this project has been rewarding and I have learned a lot about classification and Python coding. In order for the classification to be accurate it is critical that the model is examining the right terms in each document and can relate them back to the correct category. This project exposed me to several different types of classification models and allowed me to gain further insight into how HTML and web documents are classified. Ultimately, it was dertermined that the Multinomial Naive-Bayes model was unable to classify these specific documents, but the LinearSVC model classified them quickly and concisely. This is clearly a case where you cannot put your faith into only a single method or solution, but rather it is important to keep an open mind and find other ways to solve the problem.

### References

*	Brownlee, J. (2018). Deep learning for natural language processing crash course. Retrieved from https://s3.amazonaws.com/MLMastery/deep_learning_for_nlp_mini_course.pdf?__s=mso8yxpb93x84vbi3shd
*	Brownlee, J. (2017). Machine learning mastery with Python mini-course. Retrieved from https://s3.amazonaws.com/MLMastery/machine_learning_mastery_with_python_mini_course.pdf?__s=mso8yxpb93x84vbi3shd
* George, N. (2017). MSDS682_ncg_F8W2_17_for_students. Retrieved from https://www.dropbox.com/sh/1neihwzc7pm0725/AADz1KLJvNggoEbuP5ibasDLa?dl=0
*	Informatics Forum. (n.d.). Datasets for data mining. Retrieved from http://www.inf.ed.ac.uk/teaching/courses/dme/html/datasets0405.html
*	Juffi. (1998, January). The 4 universities dataset. Retrieved from http://www.cs.cmu.edu/afs/cs.cmu.edu/project/theo-20/www/data/
* languitar. (2017, April 25). Generate word cloud from single-column Pandas dataframe. Retrieved from https://stackoverflow.com/questions/43606339/generate-word-cloud-from-single-column-pandas-dataframe
* Li, S. (2018, February 19). Multi-class text classification with Scikit-Learn. Retieved from https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f
* Mueller, A. (2017, March 21). simple.py. Retrieved from https://github.com/amueller/word_cloud/blob/master/examples/simple.py
*	Python for Beginners. (2016, March 9). Beautiful Soup 4 Python. Retrieved from http://www.pythonforbeginners.com/python-on-the-web/beautifulsoup-4-python/
*	Rennie, J. (1997, April 6). Naïve Bayes algorithm for learning to classify text. Retrieved from http://www.cs.cmu.edu/afs/cs/project/theo-11/www/naive-bayes.html 
*	Richardson, L. (2015). Beautiful Soup 4.4.0 documentation. Retrieved from https://www.crummy.com/software/BeautifulSoup/bs4/doc/

