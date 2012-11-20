Porteira
========
[![Build Status](https://secure.travis-ci.org/scieloorg/porteira.png?branch=master)](https://travis-ci.org/scieloorg/porteira)

Overview
--------
API responsible for validating XML SciELO structures and generate python structures

API Usage
---------

Validating xml against an xsd, method: <b>Schema.validate()</b>:
<pre>
<code>
>xml = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;root&gt;&lt;a&gt;bla0&lt;/a&gt;&lt;b&gt;bla1&lt;/b&gt;&lt;/root&gt;'
>xsd = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified"&gt;&lt;xs:element name="root"&gt;&lt;xs:complexType&gt;&lt;xs:sequence&gt;&lt;xs:element ref="a"/&gt;&lt;xs:element ref="b"/&gt;&lt;/xs:sequence&gt;&lt;/xs:complexType&gt;&lt;/xs:element&gt;&lt;xs:element name="a" type="xs:NCName"/&gt;&lt;xs:element name="b" type="xs:NCName"/&gt;
&lt;/xs:schema&gt;'
>from schema import Schema
>sch = Schema(xsd)
>sch.validate(xml)
>True
</code>
</pre>

Deserialized XML to dict object, method: <b>Schema.deserialize()</b>
<pre>
<code>
>xml = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;root&gt;&lt;a&gt;bla0&lt;/a&gt;&lt;b&gt;bla1&lt;/b&gt;&lt;/root&gt;'
>xsd = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified"&gt;&lt;xs:element name="root"&gt;&lt;xs:complexType&gt;&lt;xs:sequence&gt;&lt;xs:element ref="a"/&gt;&lt;xs:element ref="b"/&gt;&lt;/xs:sequence&gt;&lt;/xs:complexType&gt;&lt;/xs:element&gt;&lt;xs:element name="a" type="xs:NCName"/&gt;&lt;xs:element name="b" type="xs:NCName"/&gt;
&lt;/xs:schema&gt;'
>from schema import Schema
>sch = Schema(xsd)
>sch.deserialize(xml)
>OrderedDict([(u'root', OrderedDict([(u'a', u'bla0'), (u'b', u'bla1')]))])
</code>
</pre>

Serialize dict tom XML, method: <b>Schema.serialize()</b>
<pre>
<code>
>dict_obj = {'a': {'b': '1', 'c': '2'}}
>from schema import Schema
>sch = Schema(xsd)
>sch.serialize(dict_obj)
>&lt;?xml version="1.0" encoding="utf-8"?&gt;\n&lt;a&gt;&lt;c&gt;2&lt;/c&gt;&lt;b&gt;1&lt;/b&gt;&lt;/a&gt;
</code>
</pre>
