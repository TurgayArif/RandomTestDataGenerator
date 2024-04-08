import json


def format_output(data, output_format):
    if output_format == 'json':
        return json.dumps(data, indent=4)
    elif output_format == 'csv':
        return ','.join(map(str, data))
    elif output_format == 'sql':
        return 'INSERT INTO table_name VALUES (' + ', '.join(map(str, data)) + ');'
    else:
        return 'Invalid output format'
