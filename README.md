# PDF Manager

The PDF manager is a simple command-line PDF editor developed in Python.

## How to install

Clone the repository:

```bash
  git clone git@github.com:davidspader/pdf-manager.git
```

Access the project directory:

```bash
  cd pdf-manager
```

You need the PyPDF2 library:

```bash
  pip install PyPDF2
```

## How to use

There are two main required parameters: action and fileName, and a third parameter(used in some methods, each with its own purpose).

The PDF files that will be manipulated must be located in the `./pdfs` folder. All new generated files will have the same name as the file edited with `-new` at the end.

### How to run

```bash
  python3 index.py action fileName thirdParameter
```

### GetAllPages

Each page will be transformed into a pdf file, they are in `./pdf/allPages`:

```bash
  python3 index.py GetAllPages example.pdf
```

### RemoveAllPagesFiles

Remove all files from `./pdf/allPages`:

```bash
  python3 index.py RemoveAllPagesFiles noFile
```
This method doesn't need any files, so we use `noFile`.

### GetFirstPage

Extracting only the first page:

```bash
  python3 index.py GetFirstPage example.pdf
```

### GetFirstPage

Extracting only the last page:

```bash
  python3 index.py GetLastPage example.pdf
```

### GetOnePage

Extracting any page:

```bash
  python3 index.py GetOnePage example.pdf 3
```

### GetPages

Extracting multiple pages:

```bash
  python3 index.py GetPages example.pdf 1 2 4
```

You can pass `to` as a parameter to get a sequence of pages:

```bash
  python3 index.py GetPages example.pdf 1 to 4
```

After the file name `example.pdf`, the parameters will all be interpreted as pages.

You can use this function to sort the pages too:

```bash
  python3 index.py GetPages example.pdf 5 3 4 1 2
```
Now the page order is 5 3 4 1 2.

### GetMerge

Join two pdfs:

```bash
  python3 index.py GetMerge example.pdf example2.pdf
```

### GetRotatePages

To rotate the file:

```bash
  python3 index.py GetRotatePages example.pdf 90
```
The third parameter is the number of degrees that the file will rotate, it always has to be multiples of 90.

### DeletePages

You can delete one or more pages:

```bash
  python3 index.py DeletePages example.pdf 1
```

deleting multiple pages:
```bash
  python3 index.py DeletePages example.pdf 1 3 5
```

You can also pass `to` as a parameter to get a sequence of pages to delete:

```bash
  python3 index.py DeletePages example.pdf 2 to 4
```

## Author

- [@davidspader](https://www.github.com/davidspader)