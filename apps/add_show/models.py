from django.db import models
from time import localtime, strftime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        all_shows = Show.objects.all()
        all_show_titles = []
        for x in all_shows:
            all_show_titles.append(x.title)

        if postData['add_edit'] == 'edit_show':
            current_show = Show.objects.get(id=postData['show_id'])

        if len(postData['title']) < 2:
            errors['title'] = "Show title should be at least 2 characters"
        if postData['add_edit'] == 'edit_show' and postData['title'] != current_show.title:
                if postData['title'] in all_show_titles:
                    errors['title'] = "Show title alreay exists"
        if postData['add_edit'] == "add_show" and postData['title'] in all_show_titles:
                errors['title'] = "Show title alreay exists"
        if len(postData['network']) < 3:
            errors['network'] = "Show network should be at least 3 characters"
        if postData['release_date'] > strftime("%Y-%m-%d %H:%M %p", localtime()):
            errors['release_date'] = "Show release date should be in the past"
        if postData['description']:
            if len(postData['description']) < 10:
                errors['description'] = "Show description should be at least 10 characters"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    objects = ShowManager()

    def __repr__(self):
        return f"<Show object: {self.title} ({self.id}), release date: {self.release_date}>"