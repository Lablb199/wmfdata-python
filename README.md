`wmfdata` is an Python package for analyzing Wikimedia data on Wikimedia's [non-public](https://wikitech.wikimedia.org/wiki/Analytics/Data_access#Production_access) [analytics clients](https://wikitech.wikimedia.org/wiki/Analytics/Systems/Clients).

## Features
wmfdata's most popular feature is SQL data access. The `hive.run`, `spark.run`, `presto.run`, and `mariadb.run` functions allow you to run commands using these different query engines and receive the results as a Pandas dataframe in one line of code.

Other features include:
* Easy generation of Spark sessions using `spark.get_session` (or `spark.get_custom_session` if you want to fine-tune the settings)
* Loading CSV or TSV files into Hive using `hive.load_csv`
* Turning cryptic Kerberos-related errors into clear reminders to renew your Kerberos credentials

## Installation and upgrading
To install the latest version of wmfdata, use the following command:
```
pip install --upgrade git+https://github.com/wikimedia/wmfdata-python.git@release --ignore-installed
```

This works whether or not you have an older version installed.

## Support and maintenance 
Tasks related to wmfdata are tracked in Wikimedia Phabricator in the [wmfdata-python project](https://phabricator.wikimedia.org/project/profile/4627/). 

The Wikimedia Foundation's [Product Analytics](https://www.mediawiki.org/wiki/Product_Analytics) and [Data Engineering](https://wikitech.wikimedia.org/wiki/Data_Engineering) teams are joint [code stewards](https://www.mediawiki.org/wiki/Code_Stewardship) of wmfdata. Data Engineering is the ultimate steward of the data access and analytics infrastructure interface portions, while Product Analytics is ultimate steward of the analyst ergonomics and data visualization portions. The current [maintainers](https://www.mediawiki.org/wiki/Developers/Maintainers) of wmfdata are [nshahquinn](), [ottomata](https://github.com/ottomata), [milimetric](https://github.com/milimetric/), and [nettrom](https://github.com/nettrom/).

If you're a hero who would like to contribute code, we welcome [pull requests here on GitHub](/pulls).
