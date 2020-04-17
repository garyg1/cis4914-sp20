## Code for Orphaned Triples in UF VIVO Project

## Introduction
This project involved locating orphaned (and other constraint-violating) triples in an RDF database. This is the code used for the analysis as described in the report (available in `report/report.pdf`). (Much of the code that was unsuccessful in achieving that goal was removed from the repository.)

## Running
All code is designed for a Python 3.7 runtime. The code depends on:
- the file `data/content.nq`, which is a snapshot of the database.
-  `numpy`, for the union-find implementation
- modified version of union-find implementation available here https://github.com/deehzee/unionfind (this dependency is vendored)