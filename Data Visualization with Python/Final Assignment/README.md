# Peer-graded Assignment: Final Assignment
---
## A. Data Science Topic
A survey was conducted to gauge an audience interest in different data science topics, namely:
- Big Data (Spark / Hadoop)
- Data Analysis / Statistics
- Data Journalism
- Data Visualization
- Deep Learning
- Machine Learning

The participants had three options for each topic: **Very Interested**, **Somewhat interested**, and **Not interested**. **2,233** respondents completed the survey.

The survey results have been saved in a csv file and can be accessed through this link: [Topic Survey Assignment](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/Topic_Survey_Assignment.csv)

If you examine the csv file, you will find that the **first column represents the data science topics** and the **first row represents the choices for each topic**.

### Question 1
Use the _pandas_ `read_csv` method to read the csv file into a pandas dataframe, that looks like the following:
![image](https://user-images.githubusercontent.com/67453870/119421694-296bd500-bcb4-11eb-83f2-55820199e744.png)
In order to read the data into a dataframe like the above, one way to do that is to use the `index_col` parameter in order to load the first column as the index of the dataframe. 

### Question 2
Use the artist layer of Matplotlib to replicate the bar chart below to visualize the **percentage** of the respondents' interest in the different data science topics surveyed.
![image](https://user-images.githubusercontent.com/67453870/119421820-72bc2480-bcb4-11eb-8e19-75ab919f600a.png)
To create this bar chart, you can follow the following steps:
1. Sort the dataframe in descending order of **Very interested**.
2. Convert the numbers into percentages of the total number of respondents. Recall that **2,233** respondents completed the survey. Round percentages to 2 decimal places.
3. As for the chart:
   - use a figure size of (20, 8),
   - bar width of 0.8,
   - use color #5cb85c for the **Very interested** bars, color #5bc0de for the **Somewhat interested** bars, and color #d9534f for the **Not interested** bars,
   - use font size 14 for the bar labels, percentages, and legend,
   - use font size 16 for the title, and,
   - display the percentages above the bars as shown above, and remove the left, top, and right borders.

## B. San Francisco Crime
In the final lab, we created a map with markers to explore crime rate in San Francisco, California. In this question, you are required to create a Choropleth map to visualize crime in San Francisco.

Before you are ready to start building the map, let's restructure the data so that it is in the right format for the Choropleth map. Essentially, you will need to create a dataframe that lists each neighborhood in San Francisco along with the corresponding total number of crimes(_including all the 39 crime type categories_).

Based on the San Francisco crime dataset, you will find that San Francisco consists of 10 main neighborhoods, namely:  
1. Central
2. Southern
3. Bayview
4. Mission
5. Park
6. Richmond
7. Ingleside
8. Taraval
9. Northen1
10. Tenderloin

### Question 1
Convert the San Francisco dataset, which you can also find here, [San Francisco dataset](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/Police_Department_Incidents_-_Previous_Year__2016_.zip) , into a _pandas_ dataframe, like the one shown below, that represents the total number of crimes in each neighborhood.

Paste  this link in the browser and download the zip file. 

Extract the csv file from the zip file.

Later upload the csv file to skills lab and use it.
![image](https://user-images.githubusercontent.com/67453870/119425048-7ef7b000-bcbb-11eb-83de-43ac9077e896.png)

### Question 2
Now you should be ready to proceed with creating the Choropleth map.

As you learned in the Choropleth maps lab, you will need a GeoJSON file that marks the boundaries of the different neighborhoods in San Francisco. In order to save you the hassle of looking for the right file, I already downloaded it for you and I am making it available via this link: [GeoJSON](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/san-francisco.geojson)

For the map, make sure that:
- it is centred around San Francisco,
- you use a zoom level of 12,
- you use fill_color = 'YlOrRd',
 - you define fill_opacity = 0.7,
- you define line_opacity=0.2, and,
- you define a legend and use the default threshold scale.

If you follow the lab on Choropleth maps and use the GeoJSON correctly, you should be able to generate the following map:
![image](https://user-images.githubusercontent.com/67453870/119425353-06ddba00-bcbc-11eb-8054-7f4e99902276.png)





