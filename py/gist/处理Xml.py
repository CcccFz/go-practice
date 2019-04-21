import sys

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


tree = ET.ElementTree(file='doc1.xml')

root = tree.getroot() # 获取根节点元素
root[0].text   # 有__getitem__

# 获取所有直接子节点的tag、名字、内容
for child in root:
    print(child.tag, child.attrib['name'], child.text)

# 获取所有子节点的tag、名字、内容 (深度优先)
for child in tree.iter():
    print(child.tag, child.attrib['name'], child.text)

# 查找
for elem in tree.iter(tag='branch'):
    print(elem.text)

for elem in tree.iterfind('branch/sub-branch'):
    print(elem.text)

for elem in tree.iterfind('branch[@name="release01"]'):
    print(elem.text)

# 修改属性
root[0].set('foo', 'bar')   # 有就修改，没有就增加

# 删除节点
del root[2]

# 新增节点、构建树
a = ET.Element('elem')
c = ET.SubElement(a, 'child1')
c.text = "some text"
d = ET.SubElement(a, 'child2')

b = ET.Element('elem_b')
root = ET.Element('root')
root.extend((a, b))
tree = ET.ElementTree(root)
tree.write(sys.stdout)


# 处理大文件
count = 0
for event, elem in ET.iterparse(sys.argv[2]):
    if event == 'end':
        if elem.tag == 'location' and elem.text == 'Zimbabwe':
            count += 1
    elem.clear() # discard the element
print(count)