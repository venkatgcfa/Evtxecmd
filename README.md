# Unified Forensic Tool for EVTX Log Processing with CSV and JSON Output

## Description

This project provides a Python-based automation script that integrates Eric Zimmerman's forensic utility, **EvtxECmd**, into a streamlined workflow for processing Windows Event Log (`.evtx`) files. The script allows users to specify an input directory containing `.evtx` files, an output directory where results will be saved, and a case number that is used to name the output files.

The tool automates the following tasks:
1. Syncs the latest event log maps from GitHub using `EvtxECmd.exe --sync`.
2. Processes `.evtx` files from the specified input directory using `EvtxECmd`.
3. Generates both CSV and JSON outputs in the specified output directory.
4. Names the output files according to SOF-ELK standards (e.g., `CASE_NUMBER.csv` for CSV and `CASE_NUMBER-evtx_eventlogs.json` for JSON).
5. Automatically creates the output directory if it does not exist.

This tool simplifies digital forensic investigations by automating repetitive tasks such as syncing maps and generating structured reports in formats compatible with SOF-ELK.

---

## Features

- **Automated Execution**: Automates the execution of **EvtxECmd** to process `.evtx` files.
- **CSV & JSON Output**: Generates both CSV and JSON outputs from Windows Event Log files.
- **SOF-ELK Compatibility**: Ensures compatibility with SOF-ELK by following its naming conventions for JSON outputs.
- **Auto Directory Creation**: Automatically creates the output directory if it doesn't exist.
- **Map Syncing**: Syncs event log maps before processing to ensure the latest version is used.

---

## Requirements

Before running this tool, ensure you have:
- **Windows 10 or later**
- **Python 3.x** installed
- **EvtxECmd.exe** Download Evtxecmd from (https://ericzimmerman.github.io/#!index.md) placed in a known location (ensure it's accessible from your system's PATH)

---
