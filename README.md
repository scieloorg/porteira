Porteira
========
[![Build Status](https://secure.travis-ci.org/scieloorg/porteira.png?branch=master)](https://travis-ci.org/scieloorg/porteira)

Overview
--------
API responsible for validating XML structures and generate python structures

API Usage
---------

The instance of <b>porteira.Schema(xsd)</b> parses and validates the time of construction instance:
<pre>
<code>
>from porteira.porteira import Schema
>sch = Schema(xsd)
</code>
</pre>

Validating xml against an xsd, method: <b>Schema.validate(xml) return boolean</b>:
<pre>
<code>
>xml = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;root&gt;&lt;a&gt;bla0&lt;/a&gt;&lt;b&gt;bla1&lt;/b&gt;&lt;/root&gt;'
>xsd = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified"&gt;&lt;xs:element name="root"&gt;&lt;xs:complexType&gt;&lt;xs:sequence&gt;&lt;xs:element ref="a"/&gt;&lt;xs:element ref="b"/&gt;&lt;/xs:sequence&gt;&lt;/xs:complexType&gt;&lt;/xs:element&gt;&lt;xs:element name="a" type="xs:NCName"/&gt;&lt;xs:element name="b" type="xs:NCName"/&gt;
&lt;/xs:schema&gt;'
>from porteira.porteira import Schema
>sch = Schema(xsd)
>sch.validate(xml)
>True
</code>
</pre>

Deserialized XML to dict object, method: <b>Schema.deserialize(xml) return dict</b>:
<pre>
<code>
>xml = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;root&gt;&lt;a&gt;bla0&lt;/a&gt;&lt;b&gt;bla1&lt;/b&gt;&lt;/root&gt;'
>xsd = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified"&gt;&lt;xs:element name="root"&gt;&lt;xs:complexType&gt;&lt;xs:sequence&gt;&lt;xs:element ref="a"/&gt;&lt;xs:element ref="b"/&gt;&lt;/xs:sequence&gt;&lt;/xs:complexType&gt;&lt;/xs:element&gt;&lt;xs:element name="a" type="xs:NCName"/&gt;&lt;xs:element name="b" type="xs:NCName"/&gt;
&lt;/xs:schema&gt;'
>from porteira.porteira import Schema
>sch = Schema(xsd)
>sch.deserialize(xml)
>OrderedDict([(u'root', OrderedDict([(u'a', u'bla0'), (u'b', u'bla1')]))])
</code>
</pre>

Serialize dict to XML, method: <b>Schema.serialize(dict) return XML</b>:
<pre>
<code>
>dict_obj = {'a': {'b': '1', 'c': '2'}}
>from porteira.porteira import Schema
>sch = Schema(xsd)
>sch.serialize(dict_obj)
>&lt;?xml version="1.0" encoding="utf-8"?&gt;\n&lt;a&gt;&lt;c&gt;2&lt;/c&gt;&lt;b&gt;1&lt;/b&gt;&lt;/a&gt;
</code>
</pre>

Get_validation_errors return a list of syntax and schema errors otherwise empty list, method: <b>Schema.get_validation_errors(xml) return list</b>:

Valid XML:
<pre>
<code>
>xml = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;root&gt;&lt;a&gt;bla0&lt;/a&gt;&lt;b&gt;bla1&lt;/b&gt;&lt;/root&gt;'
>xsd = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified"&gt;&lt;xs:element name="root"&gt;&lt;xs:complexType&gt;&lt;xs:sequence&gt;&lt;xs:element ref="a"/&gt;&lt;xs:element ref="b"/&gt;&lt;/xs:sequence&gt;&lt;/xs:complexType&gt;&lt;/xs:element&gt;&lt;xs:element name="a" type="xs:NCName"/&gt;&lt;xs:element name="b" type="xs:NCName"/&gt;
&lt;/xs:schema&gt;'
>from porteira.porteira import Schema
>sch = Schema(xsd)
>sch.serialize(dict_obj)
>sch.get_validation_errors(xml)
>[]
</pre>
</code>

Invalid XML:
<pre>
<code>
>invalid_xml = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;root&gt;&lt;a&gt;bla0&lt;/a&gt;&lt;b&gt;bla1&lt;/b&gt;&lt;/root&gt;'
>xsd = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified"&gt;&lt;xs:element name="root"&gt;&lt;xs:complexType&gt;&lt;xs:sequence&gt;&lt;xs:element ref="a"/&gt;&lt;xs:element ref="b"/&gt;&lt;/xs:sequence&gt;&lt;/xs:complexType&gt;&lt;/xs:element&gt;&lt;xs:element name="a" type="xs:NCName"/&gt;&lt;xs:element name="b" type="xs:NCName"/&gt;
&lt;/xs:schema&gt;'
>from porteira.porteira import Schema
>sch = Schema(xsd)
>sch.serialize(dict_obj)
>sch.get_validation_errors(invalid_xml)
>[(u'PARSER', 1, 53, u'FATAL', u'ERR_TAG_NAME_MISMATCH', u'Opening and ending tag mismatch: a line 1 and unparseable')]
</pre>
</code>

<b>Errors format returned from this method:</b>

Output Format:
[(DOMIAN, LINE, COLUMN, LEVEL, TYPE_NAME, MESSAGE),]

Ex.: [(PARSER, 3, 51, FATAL, ERR_TAG_NAME_MISMATCH, Opening and
    ending tag mismatch: statpage line 3 and startpage),
    (SCHEMASV, 2, 0, ERROR, SCHEMAV_CVC_ELT_1, Element 'wizard':
    No matching global declaration available for the validation root)]
    
How to Install?
=================
<pre>
<code>
<code>
>$ pip install porteira
</code>
</pre>