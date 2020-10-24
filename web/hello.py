def parse_query_string(query_string):
    return '\n'.join(query_string.split('&'))

def app(environ, start_response):
    data = parse_query_string(environ['QUERY_STRING']).encode()
    start_response("200 OK", [("Content-Type", "text/plain")])
    return iter([data])
