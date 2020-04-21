## Code for Orphaned Triples in UF VIVO Project

## Introduction
This project involved locating orphaned (and other constraint-violating) triples in an RDF database. This is the code used for the analysis as described in the report (available in `report/report.pdf`). (The code that was unsuccessful in achieving that goal was removed from the repository.)

## Running
#### Dependencies
All code is designed for a Python 3.7 runtime. The code depends on:
- the file `data/content.nq`, which is a snapshot of the database.
-  `numpy`, for the union-find implementation
- modified version of union-find implementation available here https://github.com/deehzee/unionfind (this dependency is vendored)

#### Resources
This ran on my Macbook pretty well, but you're probably going to need **1-2GB of disk space (for pickles) and 3-4GB of RAM** (for indexes).

#### Notes
- Some scripts depend on cached objects. These objects are cached using pickles (see `utils.py:get_obj/dump_obj`). These pickles can be built with the scripts `make_*.py`.

## Results
The file `results/orphans_and_constraint_violating.zip` contains the constraint-violating triples.

## Raw Data
Available here: https://docs.google.com/spreadsheets/d/1l6c9I52a6VDYd0nxRHaiKIDRaN5LxMmbn1GpqllCLts/edit?usp=sharing
