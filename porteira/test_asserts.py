# coding: utf-8

DICT_OBJ = dict({'a': {'b': '1', 'c': '2'}})

XSD = '''<?xml version="1.0" encoding="UTF-8"?>
          <schema xmlns="http://www.w3.org/2001/XMLSchema"
            targetNamespace="http://www.example.org/wizard"
            xmlns:tns="http://www.example.org/wizard"
            elementFormDefault="qualified">
            <complexType name="Wizard">
              <sequence>
                <element name="startpage" type="IDREF" />
                <element name="name" type="string" />
                <element name="welcometext" type="string" />
                <element name="choicepage" type="tns:ChoicePage" />
              </sequence>
            </complexType>
            <complexType name="ChoicePage">
              <sequence>
                <element name="title" type="string" />
              </sequence>
              <attribute name="id" type="ID" />
            </complexType>
            <element name="wizard" type="tns:Wizard" />
          </schema>'''


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
