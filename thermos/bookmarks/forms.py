from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url, Regexp

from thermos.models import User

class BookmarkForm(FlaskForm):
    url = URLField('Enter URL for your bokmark: ', validators=[DataRequired(), url()])
    description = StringField('Add a description:')
    tags = StringField('Tags: ', validators=[Regexp(r'^[A-Za-z0-9, ]*$', message="Tags can only contain letters and numbers")])

    def validate(self):
        if not (self.url.data.startswith("http://") or self.url.data.startswith("https://")):
            self.url.data = "http://" + self.url.data

        if not FlaskForm.validate(self):
            return False

        if not self.description.data:
            self.description.data = self.url.data

        #filter out empty and duplicate tag names
        stripped = [t.strip() for t in self.tags.data.split(',')]
        not_empty = [tag for tag in stripped if tag]    #remove empty strings
        tagset = set(not_empty) #to remove duplicates
        self.tags.data = ",".join(tagset)   #creating comma seperated values

        return True