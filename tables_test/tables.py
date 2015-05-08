import django_tables2 as tables
from tables_test.models import Person

class PersonTable(tables.Table):
	calculate = tables.Column(order_by=("first_name", "last_name"))
	newColumn = tables.TemplateColumn("<b>Hola</b> {{record.last_name}}")
	
	class Meta:
		model = Person
		# add class="paleblue" to <table> tag
		attrs = {"class": "paleblue"}
	