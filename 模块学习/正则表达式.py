import re

#正则匹配只要有返回就是匹配到了 只要没有返回就是没有匹配到

#re.match()从字符串开头往后匹配
#re.search()从整个文本里去搜索 只返回第一个匹配到的
#re.findall() 返回所有匹配到的
#re.split() #按什么分割
#re.sub() 将匹配到的进行替换

# . 默认匹配出\n之外的任意一个字符 若指定flag dotall 则匹配任意字符 包括换行
print(re.match('.+','liangyawang123')) #如果只是一个点那么返回就是第一个字符 如果加个加号 那么就是任意并一个或多个 那么就是全部返回
# ^ 匹配以字符串开头
print(re.match('^L','Liangyawang123')) #只返回L
# $ 匹配字符串结尾
print(re.match('G$','Liangyawnag123')) #没有匹配到以G结尾的所以没有返回
# \Z 匹配字符串结尾 同$
# \d 匹配数字0-9
# \D 匹配非数字
# \w 匹配 A-Za-z0-9
# \W 匹配非 A-Za-z0-9
# \s 匹配空白字符、\t、\n、\r、
# + 匹配一次到多次
# ?　匹配问号前面的字符一次或０次
print(re.search('L[a-z]+','Liangyawang123'))
print(re.search('#[a-z]+#','123#hello#'))
print(re.search('al?','aliangyawang'))
print(re.search('[0-9]{3}','23liang456')) #匹配数字匹配多少次
print(re.search('[0-9]{1,3}','123liang456')) #匹配数字匹配1到3次
print(re.findall('[0-9]{1,3}','123sadfasv34sva456')) #返回所有匹配到的复合规则的数字
print(re.search('abc|ABC','abcDfABC'))
print(re.search('(abc){2}(\|\|=){2}','abcabc||=||='))
print(re.search('(?P<id>[0-9]+)','abcd1234fsd').groupdict()) #分组匹配实例可用于数据分析
print(re.split('[0-9]+','ab2sdff43b23'))
print(re.sub('[0-9]+','|','acd232sfd5t43sfd231',count=2)) #将所有的数字替换成管道符 count匹配 多少次
print(re.search('[a-z]+','sdfADNS',flags=re.I)) #匹配时忽略大小写
