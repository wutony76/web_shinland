import random
from share.models import Article, ArticleCategory
from django.db import transaction
from django.contrib.auth.models import User


RANDCHARS = u'1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.'

@transaction.commit_on_success
def rand_article():

	categories = ArticleCategory.objects.all()
	users = User.objects.all()

	for i in range(100):
		article = Article(
				author=random.choice(users),
				title=''.join([random.choice(RANDCHARS) for i in range(1, random.randint(10, 30))]),
				body=''.join([random.choice(RANDCHARS) for i in range(50, random.randint(100, 200))]),
				category=random.choice(categories)
				)
		article.save()

