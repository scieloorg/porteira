# coding: utf-8

import unittest
import test_asserts
from porteira import Schema


class SchemaTestCase(unittest.TestCase):

    def setUp(self):

        self.xsd_string = test_asserts.XSD
        self.xml_string = test_asserts.XML
        self.xml_string_invalid = test_asserts.XML_INVALID
        self.xsd_file = open('example/example.xsd')
        self.xml_file = open('example/example.xml')
        self.xml_file_invalid = open('example/example_invalid.xml')

    def test_get_validation_errors(self):
        sch = Schema(self.xsd_string)
        errors = sch.get_validation_errors(self.xml_string)
        self.assertEqual(errors, list())

    def test_get_validation_errors_invalid_XML(self):
        sch = Schema(self.xsd_string)
        errors = sch.get_validation_errors(self.xml_string_invalid)
        self.assertTrue(len(errors) > 0)
        self.assertItemsEqual([(u'SCHEMASV', 2, 0, u'ERROR', u'SCHEMAV_CVC_ELT_1',
            u"Element 'wizard': No matching global declaration available for the validation root.")], errors)

    def test_deserialize(self):
        sch = Schema(self.xsd_string)
        des = sch.deserialize(self.xml_string)
        self.assertIsInstance(des, dict)
        self.assertIn('wizard', des)

    def test_serialize(self):
        sch = Schema()
        ser = sch.serialize(test_asserts.DICT_OBJ)
        self.assertEqual(ser,
            '<?xml version="1.0" encoding="utf-8"?>\n<a><c>2</c><b>1</b></a>')

    def test_validate_without_XSD(self):
        from porteira import CannotValidate
        sch = Schema()
        self.assertRaises(CannotValidate,
            lambda: sch.validate(self.xml_string))

    def test_validate_with_valid_XML(self):
        sch = Schema(self.xsd_string)
        validated = sch.validate(self.xml_string)
        self.assertTrue(validated)

    def test_validate_with_invalid_XML(self):
        sch = Schema(self.xsd_string)
        validated = sch.validate(self.xml_string_invalid)
        self.assertFalse(validated)

    def test_get_validation_errors_using_file(self):
        sch = Schema(self.xsd_file)
        errors = sch.get_validation_errors(self.xml_string)
        self.assertEqual(errors, list())

    def test_get_validation_errors_invalid_XML_using_file(self):
        sch = Schema(self.xsd_file)
        errors = sch.get_validation_errors(self.xml_file_invalid)
        self.assertTrue(len(errors) > 0)
        self.assertItemsEqual([(u'SCHEMASV', 2, 0, u'ERROR', u'SCHEMAV_CVC_ELT_1',
            u"Element 'wizard': No matching global declaration available for the validation root.")], errors)

    def test_deserialize_using_file(self):
        sch = Schema(self.xsd_file)
        des = sch.deserialize(self.xml_file)
        self.assertIsInstance(des, dict)
        self.assertIn('wizard', des)

    def test_validate_with_valid_XML_using_file(self):
        sch = Schema(self.xsd_file)
        validated = sch.validate(self.xml_file)
        self.assertTrue(validated)

    def test_validate_with_invalid_XML_using_file(self):
        sch = Schema(self.xsd_file)
        validated = sch.validate(self.xml_file_invalid)
        self.assertFalse(validated)
