# **Project Goal**
  > The goal of this project is to combine data sets from numerous companies such as Drilling Info, IHS, State and Local Governments, EPA, and COMPASS to produce a uniformed map of well locations. In order to acomplish this, we will use Arcpy, a form of Python script that works between ArcGIS Pro and Visual Source Code to incorporate and establish uniform parameters, allowing us to produce a well location map that can be used across all companies. 


# **Project Discussion**
**Return on Investment:**
  > Investment in this project will be seen shortly after implementation and has a guaranteed rate of 90% return on investment. By combining all data sets retrieved from the numerous companiesn, we will minimize time spent on data configuration across the board for future data collection and projections.

**User Interface:**
  > Users of this program can closely follow the code provided to ensure a combinded and uniform renderig of all data sets. Related software found in both Visual Studio Code and ArcGIS Pro allows the client to run Arcpy script in Visual Studio Code to successfully produce tools and maps in ArcGIS. In addition, a member of the team will be readily available to assist with any coding issues if encountered. 

**Requirements:**
  > All data and program information can be collected in any electronic form (Excel, Word, R) and delivered to us. We will use programming created with Visual Studio Code to convert all data to a source code that can be read and manipulated within ArcGIS Pro.

**Program Testing and Issue Reporting:**
  > Before this project is released to the client, all members of the team will conduct trial runs of various data sets and initiate any debugging required in the system. After program launch, the client will be able to contact the team at any time over the first 2 weeks of use to assist with any issue resolution. After the two week trial period, the development team can be reached through the company's phone or email, with a guarnteed resolution within 48 hours. 

**Maintaining Software:**
  > With the understanding of a ever-changing data set, the code produced can be rerun with new and updated information as needed. Software updates will be conducted automatically. After initial project launch, the programming and code will be stored on our back-up servers for a period of 6 months. After this time, the client will need to initiate a new project with us to reproduce any lost work or create new perameters.


# **Data Incorporation**
  >In the table below, you will find a description of each aspect needed to make this project successful. To access the example code for each section, simply click on the corresponding icon.

|**Software Development**|**Data Sets**|**Inverse Coordinates**|**Master Geodatabase**|
|   :---:   |   :---:   |   :---:   |   :---:   |
|The program that will be used to compile and manipulate the data will be [ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/get-started/get-started.htm) and [Visual Studio Code](https://code.visualstudio.com/docs/getstarted/getting-started). With extensions such as python, coding project parameters into ArcGIS pro can be made easy in Visual Studio Code.|Data for this project was collected from the S&P Glodal, IHS, EPA, your local government website, and the Department of Health and Saftey. Data sets in the form of Excel documents can be converted into GIS data sets using the provided code.|The code implemented below will ensure that all data sets collected will produce maps within the same coordinate system, ensuring that all information is displayed in a uniform map scale.|Once all necessary data points have been collected and converted to the proper map scale, we will create a master database that will store all data sorces and maps for this project.|
|[![image](https://github.com/user-attachments/assets/ccb6fab8-fa14-4b87-995b-9346a84418e9)](https://github.com/mschwartz-tamu/Schwartz_GEOG676/tree/main/Labs/Lab1)|[![image](https://github.com/user-attachments/assets/e1300240-d4ba-4fcb-8ed7-9a864bd0bd16)](https://github.com/mschwartz-tamu/Schwartz_GEOG676/tree/main/Labs/Lab3)|[![image](https://github.com/user-attachments/assets/c5de293a-5abc-4b27-9441-b4cd280a5778)](https://github.com/mschwartz-tamu/Schwartz_GEOG676/tree/main/Labs/Lab2)|[![image](https://github.com/user-attachments/assets/3c027c15-22c5-4504-8bd3-a351ec94e665)](https://github.com/mschwartz-tamu/Schwartz_GEOG676/tree/main/Labs/Lab4)|
|**Building a Buffer**|**Graduated Colors**|**Aerial Imagery**|   |
|In ArcGIS pro, buffers can be used to minimize error by incorporating data within a given distance of a source location. By following the code provided, we can institute a check to insure all well locations fall with the same area, whether the dat was projected in NAD83 or NAD27.|Another way to check how data was incorpoorated is to run a Graduated Colors tool, allowing us to set a confidence interval for each data point.|With the successful incorporation of all data sets, we will be able to run final checks by using aerial imagery to check the locations of wells by using parameters such as slope and hillshade. Each of which can be determined by using composite data from our master database.|   |
|[![image](https://github.com/user-attachments/assets/21e1ce0a-dec2-4f4f-bbb7-6c311b072823)](https://github.com/mschwartz-tamu/Schwartz_GEOG676/tree/main/Labs/Lab5)|[![image](https://github.com/user-attachments/assets/1ae63dd1-a085-4e1a-a932-20d5cebab96c)](https://github.com/mschwartz-tamu/Schwartz_GEOG676/tree/main/Labs/Lab6)|[![image](https://github.com/user-attachments/assets/b98d10be-ea44-44f0-8d2f-43ef6212dfa1)](https://github.com/mschwartz-tamu/Schwartz_GEOG676/tree/main/Labs/Lab7)|   |
