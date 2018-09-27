
# coding: utf-8

# In[1]:


import facebook
graph = facebook.GraphAPI(access_token='EAAKpsr2BEZAQBAIrzDZAM1KqS39pHTZCj8zGdwDZAq95auZAXkiFuGIfknC3jk1paisDQdeUJp88zYT6Ne2UD9E2Q8gD8JYU5iOadGfVhhqj286w7OfZCLSECm8CfN1KqVZB5wF88YjpIeYTDIM06TXWJ5Bcga0ABYVcPyFXwNgFsCpg55jHrECfk1DWxbeSt3YiMlMA69safNOfc05lPUZAseuPekDQGMoZD', version='3.0')

# Get the messsage of a post
post = graph.get_object(id='1824737664314058_1824739634313861')
print(post['message']) 

# Get the created_time of the posts
post_ids = ['1824737664314058_1223349881119509', '1824737664314058_1223348987786265', '1824737664314058_1824739634313861']
posts = graph.get_objects(ids=post_ids) 
 
# Each given id maps to an object.
for post_id in post_ids:
 print(posts[post_id]['created_time'])

