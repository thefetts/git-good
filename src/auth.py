def auth(user):
  if user.authed:
    return True
  else:
    redirect(403)
