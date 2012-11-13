#!/usr/bin/env python
# coding: utf-8

import xmltodict
from StringIO import StringIO
from lxml import etree


class Schema:

    def __init__(self, xsd_input=None):
        """
        Parse the XSD and attribute
        """
        if xsd_input:
            xmlschema_doc = etree.parse(StringIO(xsd_input))
            self.xmlschema = etree.XMLSchema(xmlschema_doc)

    def validate(self, xml_input):
        """
        Validate XML
        """
        parsed_xml = etree.parse(StringIO(xml_input))
        if self.xmlschema.validate(parsed_xml):
            return True
        else:
            return False

    def deserialized(self, xml_input, *args, **kwargs):
        """
        Convert XML to dict object
        """
        if self.validate(xml_input):
            return xmltodict.parse(xml_input, *args, **kwargs)

    def serialized(self, dict_input, **kwargs):
        """
        Convert dict to XML
        """
        return xmltodict.unparse(dict_input, **kwargs)
