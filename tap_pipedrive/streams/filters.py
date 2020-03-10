from tap_pipedrive.stream import PipedriveStream


class FiltersStream(PipedriveStream):
    endpoint = "filters"
    schema = "filters"
    key_properties = [
        "id",
    ]
    state_field = "add_time"
