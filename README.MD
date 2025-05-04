## 📘 Machine Learning from Beginning ##

| **SN** | **Work Done**                     | **Details**                                                                                                                                         |
|--------:|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **1**   | Tensor Details                   | Learned about different types of tensors: 0D, 1D, 2D, etc.                                                                                           |
| **2**   | Working with CSV Files           | Explored CSV (Comma Separated Values) files using both **Pandas** and Python's built-in **`csv`** module.                                          |
| **3**   | Working with JSON Files          | Worked with JSON (JavaScript Object Notation) files: reading, writing, and parsing structured data.                                                |
| **4**   | Worked on API (Application Programming Interface) | Fetched data from APIs and formatted the responses into **DataFrames** using Pandas.                                                                |
| **5**   | Web Scraping and BeautifulSoup   | Used **Selenium** for web automation and scraping. Created a bot that:<br>1. Navigates to YouTube<br>2. Opens a specific channel<br>3. Scrolls down<br>4. Extracts all video descriptions into a DataFrame. |
| **6** | UNIVARIENT ANALYSIS | Done the univareint analysis in the **`advertisment.csv`** data |
| **7**| MULTIVARIENT ANALYSIS| Multivarient analysis on <br>1. **`flight dataset`** <br>2. **`tips dataset`** <br>3. **`iris dataset`**|
| **8**| FEATURE STANDRADIZATION | <br> 1. Introduction of the feature engineering <br> 2. Componentes of the feature engineering <br> 3. Detail of the feature scaling <br> 4. Feature Standradization <br> 5. Z-score noramalization of **`adverstisment.csv`** <br>6. Min max scaling |
|**9**| FEATURE ENCODING (CONTINUE OF FEATURE ENGINEERING)|<br> 1. Encoding and its defination <br> 2. Types of encoding <br>3. Ordinal Encoding <br>4. Label encoding <br> All the works were done on **`Student_performance_10k.csv`**| |
|**10**| ONEHOTENCODING| Deatails of the one hot encoding. OnehotEncoding using <br> 1.```pd.get_dummies()```<br>2. ```pd.get_dummies(dropfirst=True)``` <br>3. ```sklearn.preprocessing.OneHotEncoder()```|    
|**11**| COLUMN TRANSFOMER|A way of putting all the preprocessing tasks such as encoding, imputation and other tasks in a single transformer. code is like this:<br> ```from sklearn.compose import ```<br>```ColumnTransformertransformer=ColumnTransformer(transformers=[],reminder=(column to be left after the transfomation where we can mostly use the keyword 'passthrough' ))```<br>```transformer.fit_transform()```|
|**12**| SklearnPipelines| First fitted the decision tree classifier on the titanic dataset which had missing and the non numeric categorical variables. Thus the imputation was done then the encoding.<br> After that sklearn pipelines was used for the series of the imputation, encoding and fitting the model| 
|**13**| Function transfomer| Used the log tranformation on the data to see the impact of the transformation on distributiona and the machine learning models|
|**14**| Power transfomer| Used the box-cox and yeo-jhoson tranform which are used to make the distributions gaussian|
|**15**| BINNING AND BINARIZATION| Descrition and types of binning. Did the binning and binarization titatnic dataset but it is not the best example to work with so it is not fully reliable example|
|**16**| HANDELLING MIXED DATA| Columns with the numerica and non numric values and a single data with both numbers and strings|
<br>
Note:pickle notebook is to open the models that are exported using the pickle
