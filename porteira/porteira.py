#!/usr/bin/env python
# coding: utf-8

import xmltodict
from StringIO import StringIO
from lxml import etree


class CannotValidate(Exception):
    pass


class Schema(object):

    def __init__(self, xsd_input=None):
        """
        Parse the XSD
        """
        if xsd_input is not None:
            self.xsd_doc = etree.parse(self._handle_xml(xsd_input))
            self.xmlschema = etree.XMLSchema(self.xsd_doc)

    def _handle_errors(self, errors_list):
        """
        Handles errors list

        Output Format:
        [(DOMIAN, LINE, COLUMN, LEVEL, TYPE_NAME, MESSAGE),]

        Ex.: [(PARSER, 3, 51, FATAL, ERR_TAG_NAME_MISMATCH, Opening and
            ending tag mismatch: statpage line 3 and startpage),
            (SCHEMASV, 2, 0, ERROR, SCHEMAV_CVC_ELT_1, Element 'wizard':
            No matching global declaration available for the validation root)]
        """
        errors = []
        for error in errors_list:
            errors.append((error.domain_name, error.line, error.column,
                error.level_name, error.type_name, error.message))
        return errors

    def _handle_xml(self, xml_input):
        """
        Handles the type of xml_input
        """
        if hasattr(xml_input, 'read'):
            return xml_input
        else:
            return StringIO(xml_input)

    def get_validation_errors(self, xml_input):
        """
        This method returns a list of validation errors. If there are no errors
        an empty list is returned
        """
        errors = []
        try:
            parsed_xml = etree.parse(self._handle_xml(xml_input))
            self.xmlschema.assertValid(parsed_xml)
        except (etree.DocumentInvalid, etree.XMLSyntaxError), e:
            errors = self._handle_errors(e.error_log)
        except AttributeError:
            raise CannotValidate('Set XSD to validate the XML')
        return errors

    def validate(self, xml_input):
        """
        This method validate the parsing and schema, return a boolean
        """
        parsed_xml = etree.parse(self._handle_xml(xml_input))
        try:
            return self.xmlschema.validate(parsed_xml)
        except AttributeError:
            raise CannotValidate('Set XSD to validate the XML')

    def deserialize(self, xml_input, *args, **kwargs):
        """
        Convert XML to dict object
        """
        return xmltodict.parse(xml_input, *args, **kwargs)

    def serialize(self, dict_input, *args, **kwargs):
        """
        Convert dict to XML
        """
        return xmltodict.unparse(dict_input, **kwargs)
