The RelDiagramV2.pdf contains the Diagram for the relational database model.

The ID for the primary key can be generated artificially as a string of 'eventName' + 'name' strings, as these form a uniqe entity. 

PK : Primary Key

FK : Foreign Key

FK1 Maps Choices, matched by name. This connection will excist if dataType is 'choice'.
FK2 Maps name to NameValue Pair in NameValuePairDefinitions, 
FK3 Maps dataType to dataType (from NameValuePairs and CATs to DataTypes tables)
Array Elements is mapped by Primary Key.


