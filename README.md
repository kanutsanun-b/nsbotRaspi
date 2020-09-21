﻿# nsbotRaspi
Using Selenium read MEATR ,SPECI and TAF from NSWEB for ...RASPBERRY PI...

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nsbot.
```bash
pip install nsbotRaspi
```

## Usage
```python
from nsbotRaspi import MetarSpeciTaf, LoopNsweb
line_token=""
time_stop="04" #UTC time
object1 = MetarSpeciTaf()
object2 = LoopNsweb(line_token, time_stop)
object2.run_loop()
```
## License
[MIT](https://choosealicense.com/licenses/mit/)

| ...... | ...... |
| ------ | ------ |
| email | kanutsanun.b@gmail.com |
| Build README | https://dillinger.io/ |