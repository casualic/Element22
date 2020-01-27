# Element22

#Project Descritpion

Consolidated Audit Trail (CAT) is a regulatory reporting requirement enforced by FINRA, that obligates Broker-dealers to submit detailed information about securities trades. Required information includes details from order initiation to placement if form of "events".
In order to comply with the requirement Broker Dealers (aka industry members) are creating internal reporting platforms.
The task is to design a database capable of storing CAT report data.


Data requirements for CAT reports is described in FINRA CAT Industry Member specification and schema. For the purposes of this exercise use version 2.2.

Given JSON specification of CAT Industry member schema (IM-Schema-v2.2.json) we complete the following tasks:

1. Use python to extract data definitions for each CAT event and save it to a spreadsheet.
Format of the spreadsheet shall be as follows:

2. Review data type definitions and propose compatible MariaDB data types in a spreadsheet formatted as follows:

3. Propose a relational data model to accommodate CAT event data requirements (just entities and Primary/Foreign Keys)
Submitted high-level text description of entities and relationships between them.

More information about CAT can be found here:
https://www.catnmsplan.com/
CAT technical specs can be found here:
https://www.catnmsplan.com/technical-specifications/index.html
Note that everything you need to complete the tasks is attached:
IM-Schema-v2.2.json
Industry-Member-Tech-Specs-v2.2-Clean.pdf

Each folder contains:
A jupyter notebook that describes the working (*shorthand writing descriptions)
An output csv file
Working python code (.py file)

# Navigation
1. JSONCATParser folder contains the project for creating a parser to convert the .json to a csv. 
2. MariaDBMap folder contains the Data Definition mappings from .json to MariaDB compatibles. 
3. RelationalModelDiagram contains the Relational Model Diagram. The folder contains the readme with clarifications.
