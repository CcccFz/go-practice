import pinyin

@register.filter
def getHead(s):
    return '%s-%s' % (pinyin.get(s[0], format="strip")[0].upper(), s)