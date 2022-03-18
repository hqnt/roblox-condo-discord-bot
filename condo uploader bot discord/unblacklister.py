import random
import secrets

import lxml.etree

file = 'file.rbxlx'

doc = lxml.etree.parse(file)
def uniqueId():
    print('UniqueId Unpatched')
    for el in doc.xpath("//UniqueId[@name='UniqueId']"):
        el.text = f'ILlmaijji{secrets.token_hex(110)}'
    doc.write(file)
def referentt():
    print('Referent Unpatched')
    for el in doc.xpath("//Item[@referent]"):
        string = ''.join(random.choice('oijj') for i in range(70))
        el.attrib['referent'] = f'Strijg{string}'
    doc.write(file)
def assetId():
    print('AssetId Unpatched')
    for el in doc.xpath("//SourceAssetId[@name='SourceAssetId']"):
        el.text = f'-{secrets.token_hex(20)}'
    doc.write(file)

