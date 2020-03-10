from tap_pipedrive.stream import PipedriveStream


class ActivityTypesStream(PipedriveStream):
    endpoint = "activityTypes"
    schema = "activity_types"
    key_properties = [
        "id",
    ]
    state_field = "add_time"
