from django import forms
from geonode.projects.models import Project


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = '__all__'
		
		# fields = ('title', 'description', 'organization', 'start_date', 'end_date', 'status', 'image', )