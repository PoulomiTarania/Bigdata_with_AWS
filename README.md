# Bigdata Pipeline with AWS & Docker

## BACKGROUND 
The Fire Incident Dispatch Data for New York City is a valuable resource that provides detailed information about emergency incidents reported to the Fire Department. With 8.6 million records spanning from 2005 to 2022 and 29 data fields, this dataset offers a comprehensive view of the nature and distribution of fire incidents in the city.

To make sense of this vast dataset, I focused on a subset of 11 data fields that I deemed most relevant for providing insights into the incidents. 

By visualizing this subset of data, I was able to uncover patterns and trends that shed light on emergency response in New York City. Using a variety of charts, such as pie charts, bar charts, word maps, heat maps, and time series, I was able to identify key insights from the data.
The project dives into each chart in detail, providing a deeper understanding of the data and its implications for emergency response in the city. Ultimately, this project contributes to our understanding of emergency incidents in New York City with the help of data visualizations.

## AWS Opensearch Dashboard Snapshot:

![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/d2f30d67-2d03-428a-be1d-ca0336423295)
![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/efaeff31-9f0c-4921-9db5-25851ae9fcd3)

# VISUALIZATIONS 
### 1.	Timeseries of NYC Fire Incidents:
#### Ques: Illustrate a time series on number of fire incidents over last 20 years and explain the spikes and drops. 
![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/24d36434-8386-4c8f-882c-c06a77dca0c6)

The time series visualization provides a comprehensive overview of the fire incidents reported to the Fire Department in New York City from 2005 to 2021. The visualization highlights spikes in fire incidents in the years 2013 and 2018, and a sharp drop in in fire incidents in the first half of 2021. Overall, the data shows that fire incidents in New York City range from 35,000 to 55,000 per year.
One peculiar observation in the time series visualization is a sharp drop in fire incidents reported in the first half of 2021, which appears abnormal compared to previous years. Upon closer examination of the original dataset, it was discovered that the sharp decline was due to data anomaly in the 'starfire_incident_id' field. One can observe duplicates in the 'starfire_incident_id' field for the first half of 2021. Additionally, the values appeared corrupted, with multiple trailing zeros, as shown in the screenshot below. This discovery reveals the importance of data quality and accuracy, and how it can impact the analysis and interpretation of the data.
Screenshot of the dataset with ‘Data Anomaly’ highlighted - 
![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/17330267-118c-4530-bdcb-24d8be5dd0bd)


### 2.	Fire Incidents per Borough – Bar Chart vs Heat Map
#### Ques: Compare and contrast two different kind of charts to provide a brief overview on fire incidents per borough.
![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/1ca8ef79-046d-4e3c-aeb2-78a3e5b60c1e)

                                                      Visual: Bar Chart

The bar chart allows us to compare the number of fire incidents per borough. It clearly shows that Brooklyn has the highest number of fire incidents, with approximately 2.4M incidents reported over the last two decades. Manhattan follows closely with 2.2M incidents, while the Bronx and Queens have reported similar numbers of incidents, with 1.7M and 1.6M incidents respectively. Staten Island has the lowest number of fire incidents, with 400K incidents reported over the same period. This information can help emergency response teams and city officials to prioritize their resources and plan accordingly to ensure the safety of residents across all five boroughs.
 ![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/ca0cd417-ff49-40c5-8a98-1d87a1d951e9)

                                                     Visual: Heat Map
This heat map also provides a visual representation of the number of fire incidents across the five boroughs of NYC over the past two decades. The darker shades of green represent higher numbers of incidents, while the lighter shades represent lower numbers. The exact number of incidents is also displayed in each borough for more clarity. Overall, the heat map provides a quick and easy-to-understand overview of the distribution and magnitude of fire incidents across the five boroughs.
While the heat map shows the relative density of fire incidents across the five boroughs, the bar chart provides a direct comparison of the total number of incidents for each borough.

### 3. Major Fire Alarm Sources in New York City - Pie Chart Analysis
#### Ques: Illustrate and explain briefly major fire alarm sources in NYC.
![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/9eae4b73-cfbf-4fc0-9e30-626591782312)

The pie chart shows the distribution of fire alarm sources in New York City over the last 2 decades. The chart highlights the top 5 alarm sources, which account for over 90% of all reported incidents.
The largest category of alarm sources is EMS/Link Medical, which accounts for 23.18% of all incidents. This suggests that medical emergencies are a major contributor to the number of fire incidents in the city. The second largest category is PD Link/Medical, at 22.44%, which could also be related to medical emergencies, but with police department involvement.
Other significant categories include phone, at 21.46%, and UCT (Unified Call Taker System)/911 at 18.03%, which suggest that a significant proportion of incidents are reported by the public through emergency phone calls. Private fire alarm sources account for 8.89% of incidents, indicating that a smaller proportion of incidents are detected through automated systems such as building fire alarms.
Overall, this pie chart provides insights into the different types of fire alarm sources in New York City and highlights the importance of medical emergencies as a major cause of incidents.

### 4. Engines Assigned per Borough- Bar Chart 
#### Ques: Throw some light on number of engines deployed so far in NYC.
 ![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/cd249b27-85e8-449a-8f96-557fe2a48f72)
This multi-dimensional bar chart provides a detailed insight into the number of fire engines used per borough, categorizing the count of fire incidents and the quantity of engines deployed.
The five bars for each borough represent the number of engines used, with each color representing a different quantity (0 to 4) of engines deployed.
The chart shows that for most fire incidents across all five boroughs, only one engine was required, and the number of incidents requiring four engines was the least. Brooklyn and Manhattan have the highest number of fire incidents that required the deployment of multiple engines, with Brooklyn having the highest number of incidents overall. In contrast, Staten Island had the lowest number of incidents across all five boroughs and therefore the least number of engines deployed.

### 5. Average Response Time per Borough in NYC- Bar Chart 
#### Ques: Explain the following Bar chart
 ![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/fceddf47-3634-475c-8b97-390a3638d7d7)
This horizontal bar chart provides a clear comparison of the average response times for each of the five boroughs of NYC. The Y-axis shows the boroughs, while the X-axis displays the average response time in seconds.
From the chart, it's apparent that Brooklyn has the fastest average response time, just over 240 seconds. Manhattan follows closely behind with an average response time of a little over 260 seconds. Staten Island has the third-fastest response time at 270 seconds, while the Bronx and Queens have slower response times of 275 and 280 seconds, respectively.
The bar chart offers a visual representation of the differences in response times across the five boroughs, making it easier to compare them directly. This information could be useful in helping emergency services to allocate their resources effectively and improve their response times in the areas where they are most needed.

### 6. Multiple Fire Incidents Categories – Word Cloud  
#### Ques: What is a word cloud, and use it depict common fire incidents categories.
 ![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/48b88b0d-77db-4b6f-98d0-623a9a9a509f)
A word cloud is a visual representation of text data where the size of each word represents its frequency or importance in the dataset. In this case, the word cloud represents the various categories of fire incidents that have occurred in NYC over the last 20 years.
As we can see, the most prominent words in the cloud are related to medical assistance, which indicates that a significant number of fire incidents involve providing medical aid to civilians. Other notable categories include assisting civilians in non-medical situations, PD and EMS link for medical assistance.
The cloud also includes a variety of other incident categories such as defective alarm systems, elevator emergencies, and automobile fires, which suggests that fire incidents in NYC are diverse and can occur for a wide range of reasons.
Overall, the word cloud provides a quick and visually appealing way to gain insights into the different types of fire incidents that have occurred in NYC over the last two decades.

### 7. FIRE INCIDENTS CATEGORIES & CLASSIFICATIONS
#### Ques: Provide some visualizations that helps viewer provide a quick overview on fire incident types in NYC.
To gain a quick overview of fire incident types in NYC, we have three visualizations to showcase the data.
Firstly, a heat map that displays the magnitude and density of the six major fire incident categories in the city. From this, we can see that medical emergencies are the highest, while medical false alarms are the lowest.
![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/e61fe20f-4cc8-4f90-abaa-cace8e3f5fd9)
Secondly, a bar graph illustrates the average response time in seconds for each of the six major categories. We can observe that non-medical emergencies have the highest response time, while medical emergencies have the lowest response time in NYC.
 ![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/2ab5918c-786a-4fe5-9a18-6dee2da6d106)
Lastly, a multi-dimensional bar chart provides an in-depth overview of fire incident categories across each borough. This chart shows the quantity of fire incidents per borough for each category, enabling us to identify patterns in the distribution of incidents across NYC.
![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/8025fae5-4411-43f5-825a-51e720cdb07a)
Overall, these visualizations provide a comprehensive and efficient way to understand fire incident types and their patterns in NYC.

### KEY TAKEAWAYS:
After analyzing the data related to fire incidents in NYC over the past 20 years, we can draw the following takeaways -

•	Fire incidents spiked in 2013 and 2018, with a sharp drop in 2021 due to the 'starfire_incident_id' column anomaly in the dataset.

•	Brooklyn and Manhattan lead in incidents, with higher engine deployment suggesting potentially more serious incidents.

•	The prevalence of EMS/Link Medical as a dominant alarm source underscores the substantial impact of medical emergencies in contributing to reported incidents.

•	Brooklyn boasts the fastest response time, while Bronx and Queens lag.




 
 


