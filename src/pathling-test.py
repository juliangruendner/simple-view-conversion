from pathling import PathlingContext
import json



def get_view_def(file_path):

    with open(file_path, "r") as f:
        return json.load(f)


def run_view_def(view_def_name):
    view_def = get_view_def(f"../viewDefinitions/{view_def_name}")

    view_def_resource = view_def["resource"]["resource"]
    view_def_select = view_def["resource"]["select"]

    result = data.view(
        resource=view_def_resource,
        select=view_def_select,
    )

    result.show(truncate=False)

    #result.write.mode("overwrite").option("header", True).csv("patientstest")

    print(result.toPandas().to_csv(index=False))

    print(result.toPandas().dtypes)




#pc = PathlingContext.create()
#pc = PathlingContext.create(enable_extensions=True, enabled_open_types=(
#    'boolean', 'code', 'date', 'dateTime', 'decimal', 'integer', 'string',
#    'Coding', 'CodeableConcept', 'Address', 'Identifier', 'Reference',
#    'Quantity', 'uri',  # added
#))


pc = PathlingContext.create(enable_extensions=True, enabled_open_types=(
    'oid', 'boolean', 'string', 'code', 'decimal', 'integer', 'integer64',
    'unsignedInt', 'positiveInt', 'uri', 'canonical', 'url', 'markdown',
    'xhtml', 'date', 'dateTime', 'instant', 'time', 'uuid', 'base64Binary',
    'Coding', 'CodeableConcept', 'Identifier', 'Period', 'Ratio', 'Range',
    'Quantity', 'Age', 'Count', 'Duration', 'Distance', 'SimpleQuantity',
    'MoneyQuantity', 'Reference', 'TriggerDefinition', 'Timing', 'Attachment',
    'Contributor', 'ContactDetail', 'SampledData', 'Expression', 'ContactPoint',
    'Address', 'UsageContext', 'DataRequirement', 'Annotation', 'Dosage', 'Meta',
))

data = pc.read.ndjson("../input")
run_view_def("pat-view-broken.json")
#run_view_def("cond-view-def.json")
#run_view_def("lab-view-def.json")
#run_view_def("med-view-def.json")
