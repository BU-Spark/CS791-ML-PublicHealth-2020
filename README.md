This repository contains all code and information for the ML for Public Health class ,Spring 2020

# Project: Understanding the Determinants of Health

BU School of Public Health has access to clinician notes collected during routine medical visits at the Boston Medical Center. These notes are written free-text reports of visits capturing the clinician’s findings, observations, and diagnoses.
We need to predict a diagnosis of substance abuse, alcohol use and tobacco smoking from the data in the notes by using techniques such as NLP and machine learning methods. 

<br/>
<br/>

# PROBLEM / OBJECTIVE:  
Using the patients records, predict diagnosis of:  
. substance abuse   
. alcohol use   
. tobacco smoking  

Different patients with different background can have different response to diseases. So, information extraction for above 3 phenotypes would help in cohort studies in HIV and Hepatitis C.  
 
<br/>
<br/>

# Methods:
## Method 1 - MedCAT (Medical Annotation Tool)  
## Method 2 - 3 machine learning models (kNN, Naive Bayes, Linear SVC) 

<br/>
<br/>

# Results (Logician Notes):

## 1. ALCOHOL ABUSE

### Linear SVC: ###
Accuracy: 88.89%,
F1 score: 90.0%,
Precision: 81.82%,
Recall: 100.0 % 

### kNN: ###
Accuracy: 83.33%,
F1 score: 84.21%,
Precision: 72.73%.
Recall: 100.0% 

### Naive Bayes: ###
Accuracy: 88.89%,
F1 score: 90.0%,
Precision: 81.82%,
Recall: 100.0% 

## 2. DRUG ABUSE

### Linear SVC: ###
Accuracy: 80.85%,
F1 score: 84.75%,
Precision: 100.0%,
Recall: 73.53% 

### kNN: ###
Accuracy: 82.98%,
F1 score: 84.0%,
Precision: 84.0%,
Recall: 84.0% 

### Naive Bayes: ###
Accuracy: 80.85%,
F1 score: 84.75%,
Precision: 100.0%,
Recall: 73.53% 

## 3. TOBACCO SMOKING

### Linear SVC: ###
Accuracy: 83.93%,
F1 score: 90.72%,
Precision: 100.0%,
Recall: 83.02%  

### kNN: ###
Accuracy: 87.5%,
F1 score: 92.31%,
Precision: 95.45%,
Recall: 89.36% 

### Naive Bayes: ###
Accuracy: 78.57%,
F1 score: 88.0%,
Precision: 100.0%,
Recall: 78.57% 


<br/>
<br/>

# Results (Epic Notes):

## 1. ALCOHOL ABUSE

### Linear SVC: ###
Accuracy: 80.23%,
F1 score: 56.41%,
Precision: 44.0%,
Recall: 78.57% 

### kNN: ###
Accuracy: 82.56%,
F1 score: 61.54%,
Precision: 48.0%,
Recall: 85.71% 

### Naive Bayes: ###
Accuracy: 75.58%,
F1 score: 36.36%,
Precision: 24.0%,
Recall: 75.0% 

## 2. DRUG ABUSE

### Linear SVC: ###
Accuracy: 84.27 %
F1 score: 90.54 %
Precision: 100.0 %
Recall: 82.72 % 

### kNN: ###
Accuracy: 77.53 %
F1 score: 83.87 %
Precision: 77.61 %
Recall: 91.23 % 

### Naive Bayes: ###
Accuracy: 83.15%,
F1 score: 89.93%,
Precision: 100.0%,
Recall: 81.71% 

## 3. TOBACCO SMOKING

### Linear SVC: ###
Accuracy: 93.18%,
F1 score: 96.39%,
Precision: 100.0%,
Recall: 93.02% 

### kNN: ###
Accuracy: 87.5%,
F1 score: 92.62%,
Precision: 86.25%,
Recall: 100.0% 

### Naive Bayes: ###
Accuracy: 90.91%,
F1 score: 95.24%,
Precision: 100.0%,
Recall: 90.91% 

