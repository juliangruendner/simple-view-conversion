from pathling import PathlingContext

pc = PathlingContext.create()
data = pc.read.ndjson("/input")


result = data.view(
    resource="Patient",
    select=[
        {"forEach": "address", "select": [{"column": [{"name": "zip", "path": "postalCode"}]}]}
    ],
)
result.show(truncate=False)
