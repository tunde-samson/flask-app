from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SubmitField, SelectMultipleField, FloatField
from wtforms.validators import InputRequired, NumberRange
from wtforms.widgets import ListWidget, CheckboxInput


class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class ExpensesForms(FlaskForm):
    age = IntegerField("Age (Must be 18years +): ", validators=[InputRequired(), NumberRange(min=18)])
    gender = RadioField('Gender: ', choices=[('male', 'Male'), ('female', 'Female')], validators=[InputRequired()])
    total_income = IntegerField('Total Income (Minimum of $10): ', validators=[InputRequired(), NumberRange(min=10)])

    expenses = MultiCheckboxField(
        'Select Expense Categories',
        choices=[
            ('utilites', 'Utilities'),
            ('entertainment', 'Entertainment'),
            ('school_fees', 'School Fees'),
            ('shopping', 'Shopping'),
            ('healthcare', 'Healthcare')
        ],
        
    )

    utilities = FloatField('Amount Spend on Utilities : ', default=0)
    entertainment = FloatField('Amount Spend on Entertainment : ', default=0)
    school_fees = FloatField('Amount Spend on School Fees : ', default=0)
    shopping = FloatField('Amount Spend Shopping : ', default=0)
    healthcare = FloatField('Amount Spend Health Care : ', default=0)

    submit = SubmitField('Submit')

