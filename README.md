Porteira
========
[![Build Status](https://secure.travis-ci.org/scieloorg/porteira.png?branch=master)](https://travis-ci.org/scieloorg/porteira)

Overview
--------
API responsible for validating XML SciELO structures and generate python structures

API Usage
---------

Validating xml against an xsd:
<pre>
  >from schema import Schema
  >sch = Schema('example.xsd')
  >sch.validate('example.xml')
  >True
</pre>