import json
import csv

fileobj = open('input.json')
str = fileobj.read()
data = json.loads(str)

for post in data:
	if post['post_id'] == '341':
		target = post
	if post['post_id'] == '342':
		target2 = post
		break

id = [[target['post_id']]]

for comment in target['comments']:
	id.append([comment['comment_id']])
	for reply in comment['comments']:
		id.append([reply['comment_reply_id']])

id.append([target2['post_id']])

for comment in target2['comments']:
	id.append([comment['comment_id']])
	for reply in comment['comments']:
		id.append([reply['comment_reply_id']])

with open('output2.csv', 'w') as fout:
	csvout = csv.writer(fout)
	csvout.writerows(id)