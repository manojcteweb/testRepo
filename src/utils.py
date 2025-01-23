from marshmallow import Schema, fields, ValidationError

class DataSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)

class LoanApplicationSchema(Schema):
    applicant_name = fields.String(required=True)
    applicant_email = fields.Email(required=True)
    loan_amount = fields.Float(required=True)
    loan_term = fields.Integer(required=True)

class ValidationUtils:
    @staticmethod
    def validate_data(schema, data):
        try:
            validated_data = schema.load(data)
            return validated_data, None
        except ValidationError as err:
            return None, err.messages

class FormattingUtils:
    @staticmethod
    def format_email_body(name):
        return f"Hello {name}, your data has been received."