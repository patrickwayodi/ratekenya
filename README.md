Ratekenya
=========


Ratekenya is a program that extracts all Chess Kenya players from a FIDE rating list. The
output is in CSV and XML formats.

The problem it solves is that the FIDE rating lists are usually very large in size
(approximately 150 MB) and so it's easier to deal with a file that only includes players
from a single country.

Ratekenya is written in [Python](https://www.python.org).

Note that this project is still in a pre-alpha state so use it with care.


## Run

Ensure that your computer has Python installed.

Fetch the FIDE rating list that you're going to process. The rating files are available
on the FIDE website, for example by using this URL: http://ratings.fide.com/download/standard_nov25frl_xml.zip

Run this command:
```
python3 getkenya.py
```

The output will be the files players_kenya.csv and players_kenya.xml.

Note that this program uses about 1 GB of RAM to process the data.


## Bugs

The tag "<playerslist>" does not get included in the XML outup file.


## TODO

Implement the use of arguments when running the program:
```
python3 getkenya.py standard_jan25frl_xml.xml

python3 getkenya.py standard_jan25frl_xml.zip
```


## Terms of Use

Copyright (C) 2025 The Ratekenya contributors (see AUTHORS file)

This program is free software; you can redistribute it and/or modify it under the terms
of version 3 of the GNU Affero General Public License as published by the Free Software
Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this
program; if not, see <https://www.gnu.org/licenses/>.


