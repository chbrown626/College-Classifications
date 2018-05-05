#Creating the dataframe and reviewing the data
import pandas as pd

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

#Creating the HTML Document Dataframe
from io import StringIO
html_df = pd.DataFrame({'Categories':labels, 'HTML': clean_html})
html_df.columns = ['Categories', 'HTML']
html_df['CatID'] = html_df['Categories'].factorize()[0]
catid_df = html_df[['Categories', 'CatID']].drop_duplicates().sort_values('CatID')
cat_to_id = dict(catid_df.values)
id_to_cat = dict(catid_df[['CatID', 'Categories']].values)

html_df.head()

#Plotting the Categories
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
html_df.groupby('Categories').HTML.count().plot.bar(color = 'green', ylim=0)
plt.show()

#Ordered plot of the document categories
html_df['Categories'].value_counts().plot('bar', color = 'purple')

#Creating wordclouds of the data by category
from wordcloud import WordCloud

#Course word cloud
course_wc = WordCloud(max_font_size=75,
                      max_words=500).generate_from_text(' '.join(html_df['HTML'][:929]))
plt.figure()
plt.imshow(course_wc, interpolation='bilinear')
plt.axis("off")
plt.show()

#Department word cloud
department_wc = WordCloud(max_font_size=75,
                          max_words=500).generate_from_text(' '.join(html_df['HTML'][929:1111]))
plt.figure()
plt.imshow(department_wc, interpolation='bilinear')
plt.axis("off")
plt.show()

#Faculty word cloud
faculty_wc = WordCloud(max_font_size=75,
                       max_words=500).generate_from_text(' '.join(html_df['HTML'][1111:2235]))
plt.figure()
plt.imshow(faculty_wc, interpolation='bilinear')
plt.axis("off")
plt.show()

#Other word cloud
other_wc = WordCloud(max_font_size=75,
                     max_words=500).generate_from_text(' '.join(html_df['HTML'][2235:5999]))
plt.figure()
plt.imshow(other_wc, interpolation='bilinear')
plt.axis("off")
plt.show()

#Project word cloud
project_wc = WordCloud(max_font_size=75,
                       max_words=500).generate_from_text(' '.join(html_df['HTML'][5999:6503]))
plt.figure()
plt.imshow(project_wc, interpolation='bilinear')
plt.axis("off")
plt.show()

#Staff word cloud
staff_wc = WordCloud(max_font_size=75,
                     max_words=500).generate_from_text(' '.join(html_df['HTML'][6503:6640]))
plt.figure()
plt.imshow(staff_wc, interpolation='bilinear')
plt.axis("off")
plt.show()

#Student word cloud
student_wc = WordCloud(max_font_size=75,
                       max_words=500).generate_from_text(' '.join(html_df['HTML'][6640:8281]))
plt.figure()
plt.imshow(course_wc, interpolation='bilinear')
plt.axis("off")
plt.show()
