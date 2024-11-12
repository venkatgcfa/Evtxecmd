# Evtxecmd
This project provides a Python-based automation script that integrates Eric Zimmerman's forensic utility, EvtxECmd, into a streamlined workflow for processing Windows Event Log (.evtx) files.
The script performs the following tasks:
Syncs the latest event log maps from GitHub using EvtxECmd.exe --sync.
Processes .evtx files from the specified input directory using EvtxECmd.
Generates both CSV and JSON outputs in the specified output directory.
Names the output files according to SOF-ELK standards (e.g., CASE_NUMBER.csv for CSV and CASE_NUMBER-evtx_eventlogs.json for JSON).
Automatically creates the output directory if it does not exist.
The tool is designed to simplify digital forensic investigations by automating repetitive tasks such as syncing maps and generating structured reports in formats compatible with SOF-ELK.
