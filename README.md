# pysyntime

`pysyntime` is a python library implementing `SynTime` algorithm from paper – *Time Expression Analysis and Recognition Using Syntactic Token Types and General Heuristic Rules*.

## Features

`pysyntime` supports extracting `timex` (time expressions) from raw text. For example, given the following text:

```text
The last 6 months surviving member of the team which first conquered Everest in 6 a.m. 17 Jan 1953 has died in a Derbyshire nursing home.
```

`pysyntime` will extract `timex` from the text and produce the following annotated text in `TimeML` format:

```
<TIMEX3 tid="t1" type="DATE" value="2016-10-10">The last 6 months</TIMEX3> surviving member of the team which first conquered Everest in <TIMEX3 tid="t2" type="DATE" value="2016-10-10">6 a.m. 17 Jan 1953</TIMEX3> has died in a Derbyshire nursing home.
```

## Installation

You can install the package by easily running the `pip` command:

```bash
pip install pysyntime
```

Since `pysyntime` relies on [spaCy](https://spacy.io/) which is an NLP library, the required model needs to be downloaded:

```bash
python -m spacy download en_core_web_sm
```

**Note**: The above command will download spaCy model and create symbol link, make sure you have root permission. 
If you are working with python virtualenv, you don't need the root permission. See [spaCy documentation](https://spacy.io/usage/#symlink-privilege) for details.

## Usage

```python
from pysyntime import SynTime

# Instanciate SynTime
synTime = SynTime()

# Your raw text
text = 'The last 6 months surviving member of the team which first conquered Everest in 6 a.m. 17 Jan 1953 has died in a Derbyshire nursing home.'
date = '2016-10-10'

# Extract timex from raw text
timeMLText = synTime.extractTimexFromText(text, date)
print(timeMLText)
```

## References

[1] Xiaoshi Zhong, Aixin Sun, and Erik Cambria. Time Expression Analysis and Recognition Using Syntactic Token Types and General Heuristic Rules. In *Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics* (ACL), pages 420-429, 2017. [[pdf](http://aclweb.org/anthology/P/P17/P17-1039.pdf)] [[slides](https://drive.google.com/file/d/0B4MkuquLjWvpV2d2dmZpU0VmbGs/view)] <br>
[2] `Syntime` implementation in Java. [[github](https://github.com/xszhong/syntime)]
