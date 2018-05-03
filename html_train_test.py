#Creating the Training & Testing Sets
import pandas as pd

from sklearn.model_selection import train_test_split

#Create the groups the html data will be split into
courses = ['course'] * 930
departments = ['department'] * 182
faculty = ['faculty'] * 1124
others = ['other'] * 3764
projects = ['project'] * 504
staff = ['staff'] * 137
students = ['student'] * 1641

#Combine into one large group the same size as the clean_html data
labels = courses + departments + faculty + others + projects + staff + students

#Plots of the Testing Categories
# data to plot
label_df = pd.DataFrame(labels)

label_df.columns = ['Category']

label_df['Category'].value_counts().plot('bar')

#Generate the random training and testing sets
html_tr, html_te, categories_tr, categories_te = train_test_split(clean_html,
                                                                  labels,
                                                                  test_size=0.30,
                                                                  random_state=42,
                                                                  stratify=labels)

#Review the head of each
html_tr[0:5]
categories_tr[0:5]
html_te[0:5]
categories_te[0:5]
