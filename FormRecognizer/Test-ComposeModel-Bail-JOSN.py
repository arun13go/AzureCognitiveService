"""
This code sample shows Custom Model operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Form Recognizer Python client library SDKs
https://docs.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/try-v3-python-sdk
"""

import json
import sys
from pygments import highlight, lexers, formatters

from azure.ai.formrecognizer import DocumentAnalysisClient, AnalyzeResult
from azure.core.credentials import AzureKeyCredential
from tabulate import tabulate
from azure.core.serialization import AzureJSONEncoder

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = "https://capitaformrecogdemo.cognitiveservices.azure.com/"
key = "f0d07a3dbf3c41719b57756e5f7d1e80"

# ********************* Use the Bail doc ***************************
model_id = "ComposeBailELMONBModel"
#model_id = "ELMONBModel"
formUrl = "https://docforcomposemodel.blob.core.windows.net/composedoc/test-doc/Bail 206 - all_tests_passing-Testing.pdf"
print("********************* Bail doc ***************************")


document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Make sure your document's type is included in the list of document types the custom model can analyze
poller = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)
result = poller.result()

# parse and format the model response json 
# convert the received model to a dictionary
analyze_result_dict = result.to_dict()

# save the dictionary as JSON content in a JSON file, use the AzureJSONEncoder
# to help make types, such as dates, JSON serializable
with open('JSONResponseData.json', 'w') as f:
        json.dump(analyze_result_dict, f, cls=AzureJSONEncoder,indent=4)

# convert the dictionary back to the original model
model = AnalyzeResult.from_dict(analyze_result_dict)
print("--------------JSON Response from Model Starts---------------------")
# use the model as normal
print("Model ID: '{}'".format(model.model_id))
print("Number of pages analyzed {}".format(len(model.pages)))
print("API version used: {}".format(model.api_version))
print(json.dumps(analyze_result_dict,cls=AzureJSONEncoder,indent=4))
#print(analyze_result_dict)

print("--------------JSON Response from Model Ends---------------------")


