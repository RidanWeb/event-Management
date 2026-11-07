
from django import forms
from events.models import Event




class StyledFormMixin:
        
    default_class = "w-full border-4 border-gray-300 rounded-lg shadow-sm py-2 focus:border-red-500 transition duration-700 ease-in-out focus:outline-none"
    default_class2 = "py-2 mb-2 focus:border-red-500 focus:outline-none"
    
    def apply_style_widget(self):
        
        placeholders = {
            'date': 'YYYY-MM-DD (e.g. 2026-05-15)',
            'time': 'HH:MM (e.g. 14:30)',
        }
        
        
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                # field.widget.attrs['class'] = self.default_class
                placeholder_text = placeholders.get(
                    field_name, 
                    f'Enter {field_name.replace("_", " ").title()}'
                )
                field.widget.attrs.update({
                    'class': self.default_class,
                    'placeholder': placeholder_text,
            })
            elif isinstance(field.widget, forms.Textarea):
                # field.widget.attrs['class'] = self.default_class
                field.widget.attrs.update({
                    
                    'class': self.default_class,
                    'placeholder': f'Enter {field_name.replace("_", " ").title()}',
                    'rows': 5
            })
            elif isinstance(field.widget, forms.SelectDateWidget):
                placeholder_text = placeholders.get(
                    field_name, 
                    f'Enter {field_name.replace("_", " ").title()}'
                )
                field.widget.attrs.update({
                    'class': 'border-4 border-gray-300 rounded-lg shadow-sm py-2 focus:border-red-500 transition duration-700 ease-in-out focus:outline-none',
                    'placeholder': placeholder_text
            })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': 'w-full px-4 py-2 bg-white text-gray-700 '
                    'border-4 border-gray-300 rounded-lg shadow-sm '
                    'focus:border-red-500 focus:outline-none '
                    'transition duration-700 ease-in-out cursor-pointer'
            })






class EventModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'category', 'date', 'time', 'location']
       
        # widgets = {
        #     'due_date': forms.SelectDateWidget,
        #     'assigned_to': forms.CheckboxSelectMultiple
        # }
       
       
    #style the form fields using the StyledFormMixin
    def __init__(self, *args, **kwargs):
        # employees = kwargs.pop('employees', []) 
        super().__init__(*args, **kwargs)
        self.apply_style_widget()
            
        




# class CategoryModelForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['name', 'description', ]