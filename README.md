# Bigdata_with_AWS
This project leverages EC2, Docker, and Elasticsearch to process NYC Fire Incident Dispatch data. A Docker-contained Python script ingests the dataset from NYC Open Data, streaming it to an AWS OpenSearch cluster. The concluding step involves crafting visualizations for better data understanding, offering insights into extensive fire incident data.

BACKGROUND 
The Fire Incident Dispatch Data for New York City is a valuable resource that provides detailed information about emergency incidents reported to the Fire Department. With 8.6 million records spanning from 2005 to 2022 and 29 data fields, this dataset offers a comprehensive view of the nature and distribution of fire incidents in the city.

To make sense of this vast dataset, I focused on a subset of 11 data fields that I deemed most relevant for providing insights into the incidents. 

By visualizing this subset of data, I was able to uncover patterns and trends that shed light on emergency response in New York City. Using a variety of charts, such as pie charts, bar charts, word maps, heat maps, and time series, I was able to identify key insights from the data.
The project dives into each chart in detail, providing a deeper understanding of the data and its implications for emergency response in the city. Ultimately, this project contributes to our understanding of emergency incidents in New York City with the help of data visualizations.

![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/d2f30d67-2d03-428a-be1d-ca0336423295)
![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/efaeff31-9f0c-4921-9db5-25851ae9fcd3)

# VISUALIZATIONS 
### 1.	Timeseries of NYC Fire Incidents:
#### Ques: Illustrate a time series on number of fire incidents over last 20 years and explain the spikes and drops. 
![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/24d36434-8386-4c8f-882c-c06a77dca0c6)

The time series visualization provides a comprehensive overview of the fire incidents reported to the Fire Department in New York City from 2005 to 2021. The visualization highlights spikes in fire incidents in the years 2013 and 2018, and a sharp drop in in fire incidents in the first half of 2021. Overall, the data shows that fire incidents in New York City range from 35,000 to 55,000 per year.
One peculiar observation in the time series visualization is a sharp drop in fire incidents reported in the first half of 2021, which appears abnormal compared to previous years. Upon closer examination of the original dataset, it was discovered that the sharp decline was due to data anomaly in the 'starfire_incident_id' field. One can observe duplicates in the 'starfire_incident_id' field for the first half of 2021. Additionally, the values appeared corrupted, with multiple trailing zeros, as shown in the screenshot below. This discovery reveals the importance of data quality and accuracy, and how it can impact the analysis and interpretation of the data.
Screenshot of the dataset with ‘Data Anomaly’ highlighted - 
![image](https://github.com/PoulomiTarania/Bigdata_with_AWS/assets/60750648/5191f1d7-892a-49c2-b753-6b17c43e980b)



 
 


