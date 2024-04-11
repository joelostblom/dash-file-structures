# dash-file-structures

This repo contains a few examples of file structures for dash apps.
Select a different branch to see how you can structure your app.
The branches corresponds to the following file structures.

## Single page app single file

```bash
src
└── app.py
```

## Single page app multiple files

```bash
src
├── app.py
├── callbacks.py
├── components.py
└── data.py  # Load data so it can be imported by the other files
```

## Single page app multiple files complex

```bash
src
├── assets
│   ├── favicon.ico  # The little icon displayed in the browser tab
│   └── style.css  # Components can be styled here instead of via `style={}`
├── callbacks
│   ├── __init__.py  # The init file are only used to simplify the imports (see file for details)
│   ├── charts.py
│   └── table.py
├── components
│   ├── __init__.py
│   ├── general.py  # All short component
│   └── table.py
├── data
│   ├── __init__.py
│   └── data.py
└── app.py
```


## Multi page app multiple files

```src
src
├── pages
│   ├── about.py
│   ├── charts.py
│   ├── home.py
│   └── table.py
└── app.py
```

## Multi page app multiple files complex

There is no branch for this in the repo;
instead [see this repo for a more complex multi-page app](https://github.com/bradley-erickson/dash-app-structure).
