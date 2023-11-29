---
layout: archive
title: "Talks"
permalink: /Talks/
author_profile: False
classes: wide
sidebar:
  nav: "docs"
---
## Invited Talks 
* San Jose State University SAVI GIS Talk: urban and environmental research with using GIS, drones, and data science [[Video]](https://fb.watch/96xkDk5bua/)
* 2021 California DroneCamp2021 "Using UAV high-resolution mapping, participatory training, and citizen science for coastal ecosystem monitoring and modeling" [[link]](https://dronecampca.org/timetable/event/flexible-afternoon-sessions-for-arcgis-pro-preparation-tbd/)
* 2021 [Esri](https://www.esri.com/en-us/about/events/remote-sensing-educators-summit/save-date?date=2021-04-28) Imagery and Remote Sensing Educators Summit [[Video]](https://www.youtube.com/watch?v=eS7WIOc1W7w&list=PLaPDDLTCmy4aV8wApg_O-5cNua4-0bGah&index=5&t=7s)
* 2021 Esri higher education web meeting "Teaching with Drones" [[Link]](https://community.esri.com/t5/education-blog/teaching-with-drones/ba-p/1038437)
* “Drone Mapping for Coastal Seagrass Monitoring and Citizen Science” in Department of Geography colloquium, University of Florida, Gainesville, FL, October 10, 2019. [PDF](/UF_Colloquium_Yang_20191009/)
*  “Multi-spectral drone mapping over Indian River Lagoon” in UCF research week kick-off event, University of Central Florida, Orlando, FL, 2018, April 5, 2019.[PDF](/UCF_Poster_Yang/)
* “Spatio-temporal Cokriging Method for Blending and Downscaling Multi-scale Data” in UC geography colloquium series, University of Cincinnati, Cincinnati, OH, October 13, 2017 [PDF](/UC_Seminar2017_Yang/)

## Conference Proceedings
* Bo Yang, Timothy Hawthorne, (2021) Accessing the spatial variation of seagrass beds along the west coast of North America using high-resolution UAV data. In, American Association of Geography (AAG) Annual Meeting. 
* Kayla Toohy, Tim Hawthorne, Bo Yang, Lain Graham, Elise Lorenzo, Morgan McDonald, Kirsten Bouck, Fernando Rivera, Hannah Torres, (2021) Mapping Sense of Place with Volunteered Geographic Information to Create Human Systems-Based Coastal Restoration Priority Zones in Indian River Lagoon, Florida. In, American Association of Geography (AAG) Annual Meeting.
* Bo Yang, Timothy Hawthorne, Emmett Duffy, Hunter Searson, (2020). Drone mapping of eelgrass meadow extent and dynamics along the US west coast. In 2020 IEEE International Geoscience and Remote Sensing Symposium (IGARSS)  
* Bo Yang, Timothy Hawthorne, Michael Feinman, Hunter Searson, (2020) High-resolution UAV mapping for investigating eelgrass wasting disease over the west coast of North America. In, American Geophysical Union (AGU) Ocean Sciences Meeting. San Diego, CA
* Hunter Searson, Bo Yang, Timothy Hawthorne, (2020). Implementing drone mapping along the US west coast for eelgrass meadow extent and dynamics. In 2020 IEEE International Geoscience and Remote Sensing Symposium (IGARSS)  
* Bo Yang, Timothy Hawthorne, (2019) A spatio-temporal geostatistical approach for sharpening multi-spectral satellite imagery using high-resolution UAV data. In, American Association of Geography (AAG) Annual Meeting. Washington, D.C.
* Hongjie Yu, Lin Liu, Bo Yang, (2019) Crime Prediction with Historical Crime and Potential Offender Data Using a Spatio-temporal Cokriging Method. In, AAG Annual Meeting. Washington, D.C.
* Hongxing Liu, Bo Yang, Emily Kang, (2018) Assessment of Heat island effect of traffic volume from space observations. In, AAG Annual Meeting. New Orleans, LA
* Hongxing Liu, Bo Yang, Emily Kang, Bailang Yu, Changchun Feng, Min Liu, Jianping Wu (2016) Analysis of impact of traffic regulation on spatial extent and intensity of urban heat islands with satellite thermal remote sensing. In, International Geographical Congress. Beijing, China
* Bo Yang, Hongxing Liu, Emily Kang, Richard A. Beck, Kenneth M. Hinkel, Lei Wang (2016) Spatio-temporal Cokriging: A multi-scale assimilation method for downscaling, hindcasting, and forecasting. In, AAG Annual Meeting. San Francisco, CA
* Bo Yang, Hongxing Liu, Emily Kang (2015) Spatio-temporal Assimilation of Multi-scale Data Sets within a Cokriging Framework. In, AAG Annual Meeting Spatial Analysis and Modeling (SAM) paper competition. Chicago, IL
* Hongxing Liu, Bo Yang, Kenneth Hinkel, Richard Beck, (2015) Change detection for thermokarst lakes in the Arctic Coastal Plain of Alaska using multi-temporal satellite radar images, In, AAG Annual Meeting. Chicago, IL
* Hongxing Liu, Bo Yang, Emily Kang, (2015). Cokriging method for spatio-temporal assimilation of multi-scale satellite data. In 2015 IEEE International Geoscience and Remote Sensing Symposium (IGARSS) (pp. 3314-3316). IEEE. 
* Heather Barrett, Mark Krekeler, Josh Crumbaker, Bo Yang, Angie Bittner (2015) Preliminary materials investigations to support search and recovery using hyperspectral remote sensing: Initial geomaterials and clothing results. In, Geological Society of America (GSA) Annual Meeting in Baltimore, MD
* Bo Yang, Hongxing Liu, Emily Kang (2014) Assimilation of multi-scale thermal remote sensing data using spatio-temporal cokriging method. In, AAG Annual Meeting. Tampa, FL
* Bo Yang, Emily Kang, Hongxing Liu (2013) Spatiotemporal (ST) cokriging to Fuse Images of Multi-Sensor Land Surface Temperature. In, Statistics 2013. Columbus, OH
* Hongxing Liu, Bo Yang, Song, Shu, K KM Hinkel, RA Beck, EL Kang, (2013). Spatio-temporal analysis of surface temperature and water level variability of thermokarst lakes on the Arctic Coastal Plain of northern Alaska using multiscale satellite thermal images and ICESat laser altimetry. In, AGU Fall Meeting. San Francisco, CA
* Bo Yang, Hongxing Liu, Emily Kang, Qiusheng Wu (2013). Spatiotemporal cokriging (ST) for multi-sensor images fusion of daily surface temperature over thaw lakes on north Alaska. In, AAG Annual Meeting. Los Angeles, CA
* Bo Yang, Hongxing Liu, Qiusheng Wu, Richard Beck, Ken Hinkel, Emily Kang (2012). Derivation of daily surface temperature and emissivity measurements over the Maumee River watershed by integrating multi-scale thermal remote sensing data. In, AAG Annual Meeting. New York City, NY
* Richard Beck, Hongxing Liu, Bo Yang, Qiusheng Wu (2012). Aircraft Sensing of Microcystis In, Workshop for Remote Sensing of Coastal & Inland Waters, University of Wisconsin-Madison
* Bo Yang, Weigong Zhang. (2011). Intelligent learning system based on HMM model. In 2011 Fourth International Symposium on Knowledge Acquisition and Modeling (pp. 490-492). IEEE. 







{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
