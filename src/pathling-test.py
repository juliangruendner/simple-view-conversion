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


pc = PathlingContext.create()
data = pc.read.ndjson("../input")
run_view_def("pat-view-def.json")
run_view_def("cond-view-def.json")
