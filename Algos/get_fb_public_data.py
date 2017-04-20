from facepy import GraphAPI
import json
# Test exemples
page_id=597236887003311
post_id='597236887003311_1383061008420891'
comment_id='597236887003311_1383061008420891'



'''
A Post is a dict with these keys:
	text:str
	nb_of_shares:int
	nb_of_comments:int
	created_time:str
	reactions:dict
	comments:list_of_comments

A Reaction is a dict with these keys:
	LIKE:int
	LOVE:int
	WOW:int
	HAHA:int
	SAD:int
	ANGRY:int
A comment is a dict with these keys:
	text:str
	nb_likes:int
	nb_replays
'''
def get_all_page_posts_ids(page_id,graph):
	all_posts_ids=[]
	link_to_posts=str(page_id)+'/posts'
	pages=graph.get(link_to_posts,page=True,limit=100,fields='id')
	for page in pages:
		for d in page["data"]:
			all_posts_ids.append(d['id'])
	return(all_posts_ids)
def get_post_reactions(post_id,graph):
	reactions_fields='reactions.type(LIKE).limit(0).summary(1).as(LIKE),reactions.type(WOW).limit(0).summary(1).as(WOW),reactions.type(SAD).limit(0).summary(1).as(SAD),reactions.type(LOVE).limit(0).summary(1).as(LOVE),reactions.type(ANGRY).limit(0).summary(1).as(ANGRY),reactions.type(HAHA).limit(0).summary(1).as(HAHA)'
	reactions={}
	reactions_raw=dict(graph.get(post_id,fields=reactions_fields))
	for k in reactions_raw:
		if k!='id':
			reactions[k]=reactions_raw[k]['summary']['total_count']
	return(reactions)
def get_post(post_id,graph):
	print('Getting the post :'+post_id)
	post={}
	print('\t Getting the reactions')
	reactions=get_post_reactions(post_id,graph)
	print('\t Getting the text and nb of comments ')
	infos_fields='message,shares,comments.limit(1).summary(1),created_time'
	info_raw=dict(graph.get(post_id,fields=infos_fields))
	post['reactions']=reactions
	post['text']=str(info_raw['message'])
	post['nb_of_comments']=info_raw['comments']['summary']['total_count']
	post['created_time']=str(info_raw['created_time'])
	print('\t Getting all the comments')
	post['comments']=get_all_comments(post_id,graph)
	try:
		post['nb_of_shares']=info_raw['shares']['count']
	except:
		post['nb_of_shares']=0
	return(post)

def get_post_comments_ids(post_id,graph):
	all_comments_ids=[]
	link_to_comments=str(post_id)+'/comments'
	pages=graph.get(link_to_comments,page=True,limit=100,fields='id')
	for page in pages:
		for d in page["data"]:
			all_comments_ids.append(d['id'])
	return(all_comments_ids)
def get_comment_infos(comment_id,graph):
	comment={}
	comment_fields='likes.limit(0).summary(1),message,comment_count'
	comment_raw=dict(graph.get(comment_id,fields=comment_fields))
	comment['text']=str(comment_raw['message'])
	comment['nb_replays']=comment_raw['comment_count']
	comment['nb_likes']=comment_raw['likes']['summary']['total_count']
	return (comment)
def get_all_comments(post_id,graph):
	comments=[]
	comments_ids=get_post_comments_ids(post_id,graph)
	for c_id in comments_ids:
		comments.append(get_comment_infos(c_id,graph))
	return(comments)
def get_all_posts(page_id,graph):
	posts=[]
	posts_ids=get_all_page_posts_ids(page_id,graph)
	with open(file_name, 'w',encoding='utf-16') as outfile:
		for p_id in posts_ids:
			data=get_post(p_id,graph)
			posts.append(data)
			json.dump(data, outfile)
			outfile.write('\n')
	return (posts)

file_name='./Restaurants_en_Algerie.txt'
oauth_access_token='EAACEdEose0cBAJ9duEZAtEawY8LHnDkZBGX4nemWED4eUBwok4w7aq8XVRgOQzKZCLJX4NiHIR68bBIBOINcWOUJeJkDI0imVbSYrQUehIPP2btAf0OCFp15BvG0zvkHngdj0BQcT50HlEq6l0crSc1VEQB2ZCjO91ZC1CjSPgGZBp2ZBaFqPDXFH41LQfpuaAZD'
graph = GraphAPI(oauth_access_token,version='2.9')
posts=get_all_posts(page_id,graph)
print(posts)

