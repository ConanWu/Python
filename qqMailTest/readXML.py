from xml.dom import minidom

#open xml
dom = minidom.parse('info.xml')

#get the root element object
root = dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)

tagname = root.getElementsByTagName('login')
print(tagname[0].getAttribute("username"))
print(tagname[0].tagName)

print(tagname.count)