**Overview**

API responsible for validating XML SciELO structures and generate python structures

**API Usage**

#. The instance of porteira.Schema(xsd) parses and validates the time of construction instance

#. Validating xml against an xsd, method: Schema.validate(xml) return boolean

#. Deserialized XML to dict object, method: Schema.deserialize(xml) return dict 

#. Serialize dict to XML, method: Schema.serialize(dict) return XML

#. Get_validation_errors return a list of syntax and schema errors otherwise empty list, method: Schema.get_validation_errors(xml) return list

Errors format returned from this method;

Output Format: [(DOMIAN, LINE, COLUMN, LEVEL, TYPE_NAME, MESSAGE),]

Ex.: [(PARSER, 3, 51, FATAL, ERR_TAG_NAME_MISMATCH, Opening and ending tag mismatch: statpage line 3 and startpage), (SCHEMASV, 2, 0, ERROR, SCHEMAV_CVC_ELT_1, Element 'wizard': No matching global declaration available for the validation root)]