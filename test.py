# coding: utf-8

import unittest
import test_asserts
from schema import Schema


class SchemaTestCase(unittest.TestCase):

    def setUp(self):

        self.xsd_string = test_asserts.XSD
        self.xml_string = test_asserts.XML
        self.xml_string_invalid = test_asserts.XML_INVALID

    def test_instance(self):
        sch = Schema(self.xsd_string)
        self.assertIsInstance(sch, Schema)

    def test_validate(self):
        sch = Schema(self.xsd_string)
        validated = sch.validate(self.xml_string)
        self.assertTrue(validated)

    def test_deserialized(self):
        sch = Schema(self.xsd_string)
        des = sch.deserialized(self.xml_string)
        self.assertIsInstance(des, dict)
        self.assertIn('wizard', des)

    def test_serialized(self):
        sch = Schema()
        ser = sch.serialized(test_asserts.DICT_OBJ)
        self.assertEqual(ser,
            '<?xml version="1.0" encoding="utf-8"?>\n<a><c>2</c><b>1</b></a>')

    def test_invalid_xml(self):
        sch = Schema(self.xsd_string)
        invalid = sch.validate(self.xml_string_invalid)
        self.assertFalse(invalid)

    def test_deserialized_invalid_xml(self):
        sch = Schema(self.xsd_string)
        des = sch.deserialized(self.xml_string_invalid)
        self.assertNotIsInstance(des, dict)
