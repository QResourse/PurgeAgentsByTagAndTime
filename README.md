# Qualys Deactivate agent based on tag

This python code is used to purge agents based on the tags and interval from the time the script run to the last time the agent on the host performed a vulenrability scan.

## Requirments

1. python 3.8+
2. [pip package manager](https://pip.pypa.io/en/stable/installation/)


### Edit config
Rename the file config.xml.sample to config.xml
Change the **BASE_URL** to the correct platfrom. See [platform-identification](https://www.qualys.com/platform-identification/)
Change the **USERNAME** and **PASSWORD** information
Change the **TAG**  information to reflect the tags you which to use for grouping the agents
Change the **TIMETOPURGE**  information to reflect the interval in hours since the agent last performed VM scanning on the asset 
Change the **PURGE**  True/False if to purge or not 


## Release Notes
1.0.0 - Innitial release;
#### For more information please see
<https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>
