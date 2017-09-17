def post(self):
	return None

def delete_post(id):
	post = find_post_by_id(id)
	post.delete
