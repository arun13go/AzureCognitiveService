## Overview

[Azure Form Recognizer](https://learn.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/overview?view=form-recog-3.0.0) is a cloud-based Azure Applied AI Service for developers to build intelligent document processing solutions. Form Recognizer applies machine-learning-based optical character recognition (OCR) and document understanding technologies to extract text, tables, structure, and key-value pairs from documents. 

Azure Form Recognizer enable to create [Composed models](https://learn.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/how-to-guides/compose-custom-models?view=form-recog-3.0.0&tabs=studio). A composed model is created by taking a collection of custom models and assigning them to a single model built from your form types. When a document is submitted for analysis using a composed model, the service performs a classification to decide which custom model best represents the submitted document.

Typical sample use case for business process automation 

![image](https://user-images.githubusercontent.com/96195521/216654950-1419a347-bbda-436f-8063-be205900686a.png)


Sample code in this repo to provide an idea on how to use API Endpoint to access the Form Recognizer compose model  to extract relevent entity from the document.

There are 3 code sample avialable:

- Use REST API in python custom code to call compose model and get JSON as payload response
    - Test-ComposeModel-JSON.py
- Use REST API in python custom code to call compose model and get entities as key value pair
    - Test-ComposeModel-KeyValue.py
- Use REST API in python custom code to call compose model and get entities as table structure as is like source document 
    - Test-ComposeModel-Table.py

Use your own sample document / forms where multiple custom model to built and compose model used to process the doc. 

## Prerequsite
Above sample code requires:
- Valid Azure subscription and, storage account access to Azure Form Recognizer
- Local environement set up:
    - VS code with envi setup (requirements.txt for envi set up available here) or use another IDE with Python3.1.1 alongwith
    - azure-cli-core 2.42.0
    - azure-ai-formrecognizer 3.2.0
- Create Azure Form Recognizer project to train model and test. You need minimum 5 doc to train
- Custom model should be built using sample docs
- Compose model should be built using custom model
- Azure Form Recognizer model end point url, key, Model name (Change the code to point the model)
