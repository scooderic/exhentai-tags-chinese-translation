""" author: Lyric
since: 2018-05-09
modat: 2018-05-09
"""
import codecs
import json

CHARSET = 'utf-8'

def write_html(data, out):
    try:
        out.write('<!DOCTYPE html>\n<html><head>\n')
        out.write('<meta charset=\"UTF-8\">\n')
        out.write('<style type=\"text/css\">table,td{border:1px solid silver;border-collapse:collapse;}</style>\n')
        out.write('</head><body>\n')
        out.write('<table>\n')
        out.write('<tr><td><strong>TAG</strong><td><strong>TRANSLATION</strong></tr>\n')
        for element in data:
            out.write('<tr><td>%s<td>%s</tr>\n' % (element['k'], element['v']))
        out.write('</table>\n')
        out.write('</body></html>\n')
        out.flush()
    finally:
        out.close()

def write_txt(data, out):
    spaces = '                    '
    try:
        out.write('TAG                 |TRANSLATION\n')
        out.write('=========================================\n')
        for element in data:
            k = element['k']
            out.write(k + spaces[len(k):len(spaces)])
            out.write('|')
            out.write(element['v'])
            out.write('\n')
        out.flush()
    finally:
        out.close()

def write(content_type):
    try:
        file = codecs.open('../../dist/ehtags-cn.json', 'r', CHARSET)
        out = codecs.open('out.' + content_type, 'w', CHARSET)
        data = json.loads(file.read())
        if content_type == 'html':
            write_html(data, out)
        elif content_type == 'txt':
            write_txt(data, out)
    finally:
        file.close()
