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

### Reviewing the Data

