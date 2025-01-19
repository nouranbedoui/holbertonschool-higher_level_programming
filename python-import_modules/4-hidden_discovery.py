#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Use dir() to get all names in the module
    names = dir(hidden_4)

    # Filter names that do not start with '__'
    filtered_names = [name for name in names if not name.startswith('__')]

    # Sort the names in alphabetical order
    filtered_names.sort()

    # Print each name in a new line
    for name in filtered_names:
        print(name)

