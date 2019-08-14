#此模块用于生成和修改常见配置文档
import configparser
"""
#用python生成一个配置文件
config = configparser.ConfigParser()
config["DEFAULT"] = {
    'ServerAliveInterval':45,
    'Compression':'yes',
    'CompressionLevel':9,
    'ForwardX11':'yes'
}
config['bitbucket.org'] = {
    'User':'hg'
}
config["topsecret.server.com"] = {
    'Port':3306,
    'ForwardX11':'no'
}
with open('config.ini','w') as f:
    config.write(f)
"""
"""
#读取一个配置文件
config = configparser.ConfigParser()

config.read('config.ini')
print(config.defaults()) #读取配置文件里default下的数据
print(config.sections()) #读取配置文件的节点
print(config['bitbucket.org']['User']) #读取配置文件当个节点下的数据
"""
#删除配置文件里的东西
"""
conf = configparser.ConfigParser()
conf.read('config.ini')
sec = conf.remove_section('bitbucket.org')
conf.write(open('config2.ini','w')
"""
#判断有没有这个节点
conf = configparser.ConfigParser()
conf.read('config.ini')
print(conf.has_section('test'))

#