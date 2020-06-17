# breakdown:
# 1. loop thru each file and group them by filename
# in a file_lookup dict
# 2. loop thru each query, and if the query is
# in the file_lookup, add all records under that
# key to the return result

def finder(files, queries):
    result = []
    
    # create a lookup that looks like this,
    # {
    #     ...
    #     'foo.txt': [ 'path/to/foo.txt', 'anotherpath/to/foo.txt' ]
    #     ...
    # }
    file_lookup = {}
    for filepath in files:
        # get the name of the file at the end
        # of this filepath
        filename = get_filename_from_path(filepath)
        if filename not in file_lookup:
            # create this key with an empty array
            file_lookup[filename] = []
        file_lookup[filename].append(filepath)
        
    for query in queries:
        if query in file_lookup:
            # match found!
            result.extend(file_lookup[query])

    return result

def get_filename_from_path(filepath):
    path_arr = filepath.split('/')
    # vvv gets the last part of the filepath, the filename
    filename = path_arr[-1]
    return filename


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
