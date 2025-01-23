from flask import current_app
from marshmallow import Schema, fields, ValidationError
from flask_sqlalchemy import SQLAlchemy

# Initialize database
app = current_app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
db = SQLAlchemy(app)

# Define a schema for loan application validation
class LoanApplicationSchema(Schema):
    applicant_name = fields.String(required=True)
    applicant_email = fields.Email(required=True)
    loan_amount = fields.Float(required=True)
    loan_term = fields.Integer(required=True)

# Define a LoanApplication model
class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    applicant_email = db.Column(db.String(100), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    loan_term = db.Column(db.Integer, nullable=False)

    def __init__(self, applicant_name, applicant_email, loan_amount, loan_term):
        self.applicant_name = applicant_name
        self.applicant_email = applicant_email
        self.loan_amount = loan_amount
        self.loan_term = loan_term

# Function to process loan application
class LoanApplicationService:
    @staticmethod
    def process_application(data):
        schema = LoanApplicationSchema()
        try:
            # Validate incoming data
            validated_data = schema.load(data)
            current_app.logger.debug('Loan application data validated successfully')

            # Create a new loan application record
            loan_application = LoanApplication(
                applicant_name=validated_data['applicant_name'],
                applicant_email=validated_data['applicant_email'],
                loan_amount=validated_data['loan_amount'],
                loan_term=validated_data['loan_term']
            )

            # Add to the database
            db.session.add(loan_application)
            db.session.commit()
            current_app.logger.debug('Loan application saved to database')

            return {"message": "Loan application processed successfully!"}, 200
        except ValidationError as err:
            current_app.logger.error('Validation error: %s', err.messages)
            return err.messages, 400
        except Exception as e:
            current_app.logger.error('An error occurred: %s', str(e))
            return {"message": "An error occurred while processing the loan application."}, 500