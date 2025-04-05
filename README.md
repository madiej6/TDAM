# Tornado Damage Assessment Model (TDAM)
:construction: In progress - check back soon. :construction:

## Roadmap

**Structure Classifier**: Provide a geospatial dataset (points or polygons) of structures or parcels with a "Structure Category" column, generate a classifier to categorioze the structures into NWS Damage Indicators.
    - In Progress
    - Planned Completion: Summer 2025  

**Damage Assessment Model**: Given a tornado path polygon with EF ratings, and structures categorized into damage indicators, generate predicted damages at the structure level.
    - Not started
    - Planned Completion: Fall 2025  
    
**Tornado Path Generator**: Generate a tornado path polygon with EF ratings from points (i.e. field surveys).
    - Not started
    - Planned Completion: End of 2025


## Resources
- 2018 American Meteoroligical Society presentation: [An Automated Tornado Damage Assessment Model: Providing Rapid Situational Awareness to the Federal Emergency Management Agency (FEMA)](https://ams.confex.com/ams/98Annual/meetingapp.cgi/Paper/326485)
- 2020 American Meteoroligical Society presentation: [A Tornado Damage Assessment Model and Lessons Learned from the 2019 Lee County, Alabama, EF4 Tornado](https://ams.confex.com/ams/2020Annual/webprogram/Paper365065.html)

## Setup
Create a Python environment from requirements.txt to run this model. Python 3.9.19 recommended.

For example, with conda:
```
> conda create --name tdam python=3.9.19
> conda activate tdam
> pip install -r requirements.txt
```

## Usage

The Tornado Damage Assessment Model works as follows:

1. Classify Structures
The TDAM damage predictions are highly dependent on the structure classifications. Each structure needs to be mapped to a Damage Indicator. You will provide the file path of your structure data and run the classifier like this:

```
python src/main.py --classify-structures <file-path> --type-col <type-col> --id <project-id>
```

i.e.
```
python src/main.py --classify-structures data/dummy_bldgs.shp --type-col Type --id test
```
Where:
- `<file-path>` is the path to your structures. This can be a point or polygon shapefile.
- `<type-col>` is the column of your structure data that contains information about structure type, land use, construction, etc. It's the primary column that you'll use to map your structures to the Damage Indicators.
- `<project-id>` is the unique identifier of your project. This ID will be used in file naming and general organization of output files.

A table gets created in `tables/` named: `structural_mappings_{id}.csv` that contains all of the unique structure types from the structural dataset. Each one of the structure types needs to be manually mapped to a Damage Indicator. Before proceeding on to the next step, you must map each of the structure types to a Damage Indicator. The Damage Indicators can be found in `tables/camage_indicators.csv` and you should use the column named 'ABBREVIATIONS'.

For example, the Classifier will create a table like this:
| Type   | DamageIndicator       |
|------|------------|
| Cabin  |       |
| Single-Family Residence  |         |
| Church  |       |
| Office Building  |         |

And then you will populate the DamageIndicator column using your best judgment, as such:

| Type   | DamageIndicator       |
|------|------------|
| Cabin  |  SBO     |
| Single-Family Residence  |    FR12     |
| Church  |   LRB    |
| Office Building  |    SPB     |

Once you've mapped all of your Structure Types to a Damage Indicator, save the csv file and run the validator (next step).

2. Validate Mappings


```
python src/main.py --validate-mappings --id <project-id>
```

3. Predict Damages

