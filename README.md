# get_Perm

get_Perm is a python script, used for graduation project task, to facilitate the process of gathering data in an indoor localization system.

## Installation

Python latest version should be installed.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements which in requirements.txt file.

```bash
pip install -r requirements.txt
```

## Options

```bash
# to display help page
python get_Perm -h
```

-h, --help            show this help message and exit

-d, --devices DEVICES number of devices

-t, --test-cases CASES number of test cases

-l, --meridians LENGth number of length lines

-w, --latitudes WIDTH number of width lines

## Usage

An example for 6 devices, 5000 test cases needed and location has 6 meridians and 4 latitudes.

```bash
python get_Perm -d 6 -t 5000 -l 6 -w 4
```

The result will be in **results** directory in two files:

1. .csv file.

2. .xlsx (excel) file.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)