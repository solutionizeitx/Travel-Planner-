import json

from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # print("kwargs : ",kwargs)
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        request = kwargs.get('context', {}).get('request')
        # print("DynamicFieldsModelSerializer : ",str(request.GET['ex_list']))

        ex_list = json.loads(request.GET.get("exclude_list", "[]") if request else "[]")
        # ex_list = []

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        elif exclude is not None:
            # drop fields that are specified in the 'exclude' argument
            for field_name in set(exclude):
                self.fields.pop(field_name)
        for field_name in set(ex_list):
            self.fields.pop(field_name)