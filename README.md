# Natural-Family-Planning-Creighton-Model-Chart
Credit to mkudija for creating this originally.  I was able to take his creation and modify it to run as a standard python script using modern versions.

[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](https://github.com/mkudija/Creighton-Model-Chart/blob/master/LICENSE)
[![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&maxAge=2592000)](https://twitter.com/mkudija)

> Plotting of Creighton Model charts.

---

## Example Chart
![Example](https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/charts/example_month_1.png)
![Example Combined](https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/charts/complete/example_month_1_to_example_month_2.png)

## Disclaimer
This software is not endorsed or in any way affiliated with the Pope Paul VI Institute or the "Official Creighton Model". It is intended only to facilitate electronic vizualization instead of paper charts with physical stickers. The user provides determination of what to chart via data files in [`data/`](https://github.com/jgerber53/nfp-creighton-model-chart/tree/main/data). 

## Background
According to the [United States Conference of Catholic Bishops](http://www.usccb.org/issues-and-action/marriage-and-family/natural-family-planning/what-is-nfp/), Natural Family Planning (NFP) is "the general title for the scientific, natural and moral methods of family planning that can help married couples either achieve or postpone pregnancies."

The [Creighton Model](http://www.creightonmodel.com) is one of several NFP methods which uses the observation of biomarkers (cervical mucus) to identify the natural times of fertility and infertility. Other popular methods include [the Billings Model](http://www.woomb.org/), [the Sympto-Thermal Method](https://sympto.org/data/manual_en_sympto.pdf), and [the Marquette Model](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.marquette.edu/nursing/institute-natural-family-planning/model.php&ved=2ahUKEwicldq49LeMAxX7OjQIHZJPHyYQFnoECBUQAQ&usg=AOvVaw3K0vL5LtMjgsWN_18DftTG/), with information about other methods [here](http://www.usccb.org/issues-and-action/marriage-and-family/natural-family-planning/what-is-nfp/methods.cfm) and [here](http://verilymag.com/2016/12/how-to-chart-your-cycle-creighton-billings-two-day-sympto-thermal-marquette-lactational). The [Creighton Model](http://www.unleashingthepower.info/PDFs/IA_IntroCrMS.pdf) was developed by Dr. Thomas Hilgers at Creighton University in the 1970's and 1980's and is one of the most popular NFP methods. It has been widely studied, and has also led to the development of NaProTechnology (natural procreative technology), a method of medical treatments for women that preserves fertility.

Charting is a convenient way of visually tracking the woman's cycle. Creighton Method instruction typically includes instruction in using a paper chart. Unfortunately, there does not appear to be an app or other form of electronic charting offered by any organization officially affiliated with Creighton. Electronic charting in some form would greatly improve convenience and data integrity.

### Survey of Electronic Charting Options
There are a variety of electronic (app, online, spreadsheet) charting options available offering various combinations of features and degrees of compatibility with the Creighton model. Below are links to some of the options I found online:

#### Charting Apps
* [NFP Charting (free trial)](https://itunes.apple.com/us/app/nfp-charting/id300767738?mt=8)
* [Kindara (free trial)](https://www.kindara.com/)
* [OvuView (free trial)](https://play.google.com/store/apps/details?id=com.sleekbit.ovuview&hl=en)
* [Ovia Fertility Tracker (free trial?)](https://itunes.apple.com/us/app/ovia-fertility-tracker-ovulation-calculator/id570244389?mt=8)
* [Lily (free trial?)](http://whimsicallily.com/lily/appstore.php)
* [Fertility Friend (free trial?)](https://itunes.apple.com/app/apple-store/id443919067?mt=8)

#### Online Charting
* [My Fertility Charts ($2.50/mo)](http://www.myfertilitycharts.com/)
* [NFP Charting.com ($2.99/mo)](https://www.nfpcharting.com/index.php)

## Creighton-Model-Chart
Finding nothing that meets our needs above, and wanting to make something simple in Python, I generated these scripts. This provides a simple way of visualizing biomarker observations.

### Stickers
<img src="https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/stickers/g.png" width="50"/> <img src="https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/stickers/r.png" width="50"/> <img src="https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/stickers/y.png" width="50"/> <img src="https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/stickers/gb.png" width="50"/> <img src="https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/stickers/gb1.png" width="50"/> <img src="https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/stickers/gb2.png" width="50"/> <img src="https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/stickers/gb3.png" width="50"/> <img src="https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/stickers/wb.png" width="50"/> <img src="https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/stickers/wbp.png" width="50"/>

Images to form the "stickers" are located in [`/stickers`](https://github.com/jgerber53/nfp-creighton-model-chart/tree/main/stickers). Stickers with the baby illustration are derived from the "dancing baby" by [Jeff Geerling](https://www.jeffgeerling.com/blog/2010/dancing-baby-illustration). 

### Usage

#### Installation
Clone this repo using [`https://github.com/jgerber53/nfp-creighton-model-chart.git`](https://github.com/jgerber53/nfp-creighton-model-chart.git).

#### Requirements
This very well may run on other versions.  The below versions are what is verified.

- matplotlib == 3.10.1
- pandas == 2.2.3
- pillow == 11.1.0
- numpy == 2.2.4
- openpyxl == 3.1.2

#### Generate Data
User inputs are gathered via Excel files in [`data/`](https://github.com/jgerber53/nfp-creighton-model-chart/tree/main/data). 

| Date          | Discharge     | Sticker  | Intercourse  | 
| ------------- |:-------------:| -------- | ------------ |
| MM/DD/YY      | *record using usual code* | *see below* | Record **I** for Intercourse | 

**Stickers** - use the following codes for each sticker type:
- `g` - green
- `r` - red
- `y` - yellow
- `wb` - white baby
- `wbp` - white baby (Peak Day)
- `wb1` - white baby (Peak +1)
- `wb2` - white baby (Peak +2)
- `wb3` - white baby (Peak +3)
- `gb` - green baby 
- `gb1` - green baby (Peak +1)
- `gb2` - green baby (Peak +2)
- `gb3` - green baby (Peak +3)


#### Create Single Chart
Run [`plotChart.py`](https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/plotChart.py) to generate the chart for a single cycle.

Update `file_path` as needed to the location of your data. 

Update `file_name` for the date of the start of the cycle you want to plot. 

Update `charts_path` to specify the location for your charts.

#### Merge Charts
Run [`combineCharts.py`](https://github.com/jgerber53/nfp-creighton-model-chart/blob/main/combineCharts.py) to combine multiple single cycle charts into a full chart (the group of 6 cycles you are used to seeing on paper charts). 

Update `charts_path` to specify the location for your charts.

Copy charts you want to combine from the `charts_path` to the `combine` subfolder of your charts directory.

This script will take the charts you place in the combine folder, merge them, and place the finished product in the complete folder.