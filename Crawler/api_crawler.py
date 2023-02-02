# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import requests
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
lasthotcommentid = ''
comments = []

for pagenum in range(6):
    params = {
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'GB2312',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
        'cid': '205360772',
        'reqtype': '2',
        'biztype': '1',
        'topid': '212877900',
        'cmd': '8',
        'needmusiccrit': '0',
        'pagenum': pagenum,
        'pagesize': '25',
        'lasthotcommentid': lasthotcommentid,
        'domain': 'qq.com',
        'ct': '24',
        'cv': '10101010'
    }
    res = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg', headers=headers, params=params)
    data = res.json()
    for item in data['comment']['commentlist']:
        if 'rootcommentcontent' in item:
            # ���ǳƺ��������ݴ����Ԫ�飬��ӵ��б� comments ��
            comments.append((item['nick'], item['rootcommentcontent']))
    # ��ǰҳ���һ�����۵� commentid ��Ϊ��һҳ�� lasthotcommentid
    lasthotcommentid = data['comment']['commentlist'][-1]['commentid']
    # ��ֹ��ȡ̫�챻��
    time.sleep(3)

# ʹ�� set() ������ comments �б����ȥ��
comments = set(comments)
for nick, content in comments:
    print('{}��{}'.format(nick, content))
