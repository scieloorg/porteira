# coding: utf-8

DICT_OBJ = dict({'a': {'b': '1', 'c': '2'}})

XSD = '''<?xml version="1.0" encoding="UTF-8"?>
          <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" targetNamespace="http://www.example.org/wizard" xmlns:wizard="http://www.example.org/wizard">
            <xs:element name="wizard">
              <xs:complexType>
                <xs:sequence>
                  <xs:element ref="wizard:startpage"/>
                  <xs:element ref="wizard:name"/>
                  <xs:element ref="wizard:welcometext"/>
                  <xs:element ref="wizard:choicepage"/>
                </xs:sequence>
              </xs:complexType>
            </xs:element>
            <xs:element name="startpage" type="xs:NCName"/>
            <xs:element name="name" type="xs:string"/>
            <xs:element name="welcometext" type="xs:string"/>
            <xs:element name="choicepage">
              <xs:complexType>
                <xs:sequence>
                  <xs:element ref="wizard:title"/>
                </xs:sequence>
                <xs:attribute name="id" use="required" type="xs:NCName"/>
              </xs:complexType>
            </xs:element>
            <xs:element name="title" type="xs:string"/>
          </xs:schema>'''

XML = '''<?xml version="1.0" encoding="UTF-8"?>
          <wizard xmlns="http://www.example.org/wizard">
            <startpage>start</startpage>
              <name>My Example Setup</name>
              <welcometext>Welcome to this little demo application.</welcometext>
              <choicepage id="start">
              <title>Wizard Page One</title>
            </choicepage>
          </wizard>'''

XML_INVALID = '''<?xml version="1.0" encoding="UTF-8"?>
                  <wizard>
                    <startpage>start</startpage>
                      <name>My Example Setup</name>
                      <welcometext>Welcome to this little demo application.</welcometext>
                      <choicepage id="start">
                      <title>Wizard Page One</title>
                    </choicepage>
                  </wizard>'''
