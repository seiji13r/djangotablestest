from django.shortcuts import render
from django_tables2   import RequestConfig
from tables_test.models  import Person
from tables_test.tables  import PersonTable

def people(request):
	table = PersonTable(Person.objects.all())
	RequestConfig(request, paginate={"per_page": 2}).configure(table)
	return render(request, 'people.html', {'table': table})