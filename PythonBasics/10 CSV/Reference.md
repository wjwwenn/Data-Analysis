To create/retrieve a file on your local system, use the `open` command. 
Open has a few different "modes".

## 1 Create a file with the `w` mode
`w` = write-mode. First define a random path to a filename yet to exist.
```python
to_save_dir = "/path/to/save/in/"
filename = "myfilename.txt"
full_path = to_save_dir + filename
```
`open()` that path so we can save it.

```python
with open(full_path, 'w') as file_object:
    file_object.write("Hello world")
```

If we don't want to use `with`, we have to explicitly `close` the `open` call.

```python
file_object = open(full_path, 'w')
file_object.write("Hello World")
file_object.save()
```

## 2 Open a file with the `r` mode
`r` = read-mode. Define a random path to a filename that already exists.
```python
to_save_dir = "/path/to/save/in/"
filename = "myfilename.txt"
full_path = to_save_dir + filename
```

```python
with open(full_path, 'r') as file_object:
    contents = file_object.read()
    print(contents)
```

If we don't want to use `with`, we have to explicitly `close` the `open` call.

```python
file_object = open(full_path, 'r')
contents = file_object.read()
print(contents)
contents.close()
```

## 3 Download files

```python
def download_file(url, directory, fname=None):
    if fname == None:
        fname = os.path.basename(url)
    dl_path = os.path.join(directory, fname)
    with requests.get(url, stream=True) as r:
        with open(dl_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return new_dl_path
```
