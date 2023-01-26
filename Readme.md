## Overview

Azure Form Recognizer  https://learn.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/concept-composed-models?view=form-recog-3.0.0 is a cloud-based Azure Applied AI Service for developers to build intelligent document processing solutions. Form Recognizer applies machine-learning-based optical character recognition (OCR) and document understanding technologies to extract text, tables, structure, and key-value pairs from documents. 

Azure Form Recognizer enable to create Composed models. A composed model is created by taking a collection of custom models and assigning them to a single model built from your form types. When a document is submitted for analysis using a composed model, the service performs a classification to decide which custom model best represents the submitted document.

Sample code in this repo to provide an idea on how to use API Endpoint to access the Form Recognizer compose model  to extract relevent entity from the document.

There are 3 code sample avialable:

- Use REST API in python custom code to call compose model and get JSON as payload response
- Use REST API in python custom code to call compose model and get entities as key value pair
- Use REST API in python custom code to call compose model and get entities as table structure as is like source document

- Test-ComposeModel-JSON.py     -> JSON response
- Test-ComposeModel-KeyValue.py -> key value pair
- Test-ComposeModel-Table.py    -> table structure

Sample redacted document from one of the use case where multiple custom model built and compose model used to process the doc

## Prerequsite
Above sample code requires:
- Valid Azure subscription and access to Azure Form Recognizer
- Custom model should be built using sample docs
- Compose model should be built using custom model
- Azure Form Recognizer model end point url, key, Model name (Change the code to point the model)
