"""
This code sample shows Custom Model operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Form Recognizer Python client library SDKs
https://docs.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/try-v3-python-sdk
"""
# This code will call From Recognizer Compose model and return the result as tableur format

from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from tabulate import tabulate

data = []

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""

endpoint = "YOUR END POINT URL HERE"
key = "YOUR END POINT KEY HERE"

# ********************* Use the SAMPLE TESTING doc ***************************

#model_id = "Compose-Bail-ELM-Model"
model_id = "YOUR COMPOSE MODEL NAME/ID HERE"
formUrl = "YOUR TESTING DOC (STORAGE CONTAINER) URL HERE"

print("********************* Sample doc ***************************")



document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Make sure your document's type is included in the list of document types the custom model can analyze
poller = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)
result = poller.result()


# Display key value pairs
for idx, document in enumerate(result.documents):
    print()
    print("--------Analyzing document #{}--------".format(idx + 1))
    print("Document has type {}".format(document.doc_type))
    print("Document has document type confidence {}".format(
        document.confidence))
    print("Document was analyzed with model with ID {}".format(
        result.model_id))
    print()
    for name, field in document.fields.items():
        field_value = field.value if field.value else field.content
        if field.value_type != 'list':
            data.append([name, field.value, field.confidence])

data.sort()
print(tabulate(data, headers=[
    'Label', 'Value', 'Confidence'], tablefmt='fancy_grid'))

# Display table data
for i, table in enumerate(result.tables):

    row_index = 1
    hdr = []
    rows = []
    row = []

    print("\nTable {} can be found on page:".format(i + 1))
    # for region in table.bounding_regions:
    #     print("...{}".format(i + 1, region.page_number))

    for cell in table.cells:
        if cell.row_index == 0:
            hdr.append(cell.content)
        else:
            if row_index != cell.row_index:
                rows.append(row)
                row_index = cell.row_index
                row = []

            row.append(cell.content)

    rows.append(row)
    print(tabulate(rows, headers=hdr, tablefmt='fancy_grid'))

print("-----------------------------------")


