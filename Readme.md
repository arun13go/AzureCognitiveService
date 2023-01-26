## Overview

Azure Form Recognizer is a cloud-based Azure Applied AI Service for developers to build intelligent document processing solutions. Form Recognizer applies machine-learning-based optical character recognition (OCR) and document understanding technologies to extract text, tables, structure, and key-value pairs from documents. 

Azure Form Recognizer enable to create Composed models. A composed model is created by taking a collection of custom models and assigning them to a single model built from your form types. When a document is submitted for analysis using a composed model, the service performs a classification to decide which custom model best represents the submitted document.

Sample code in this repo to provide an idea to use API Endpoint to access the Form Recognizer compose model  to extract relevent entity from the document.

There are 3 code sample avialable:

- Use REST API in python custom code to call compose model and get JSON as payload response
- Use REST API in python custom code to call compose model and get entities as key value pair
- Use REST API in python custom code to call compose model and get entities as table structure as is like source document

- Test-ComposeModel-Bail-JOSN   -> JSON response
- Test-ComposeModel-Bail        -> key value pair
- Test-ComposeModel-ELMONB      -> table structure

Sample redacted document from one of the use case where multiple custom model built and compose model used to process the doc