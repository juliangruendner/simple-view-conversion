from pathling import PathlingContext

pc = PathlingContext.create()
data = pc.read.ndjson("/input")


result = data.view(
    resource="Patient",
    select=[
        {"column": [{"path": "id", "name": "id"}]}
    ],
)
result.show(truncate=False)