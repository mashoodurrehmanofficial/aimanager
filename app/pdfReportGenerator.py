import os
from fpdf import FPDF 

def generatePdfReport(customer_name, customer_email, customer_property_name, customer_billing_address, dates):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt=f"{customer_name}", ln=1, align='L')
    pdf.cell(200, 10, txt=f"{customer_email}", ln=2, align='L')
    pdf.cell(200, 10, txt=f"{customer_property_name}", ln=3, align='L')
    pdf.cell(200, 10, txt=f"{customer_billing_address}", ln=4, align='L')
    pdf.cell(200, 10, txt="Start Date: 12/12/2012", ln=5, align='L')
    for date_index, date in enumerate(dates):
        pdf.cell(200, 10, txt=f"Day {date['day']} :	  {date['display_name']} - {date['date']}", ln=6+date_index, align='L')

    if not os.path.exists(os.path.join(os.getcwd(), 'PDF Reports')):
    	os.mkdir(os.path.join(os.getcwd(), 'PDF Reports'))

    pdf_file_path = os.path.join(os.getcwd(), 'PDF Reports', f'{customer_name}.pdf')
    pdf.output(pdf_file_path)



if __name__ == '__main__':

	dates = [{'display_name': 'CIDRS In', 'id': 'seeder', 'day': 0, 'date': '19/02/2022', 'status': True}, {'display_name': 'PG Injection', 'id': 'bomerol', 'day': 2, 'date': '21/02/2022', 'status': True}, {'display_name': 'Bomerol', 'id': 'bomerol', 'day': 6, 'date': '22/02/2022', 'status': True},
			{'display_name': 'CIDRS Out', 'id': 'cidrs_out', 'day': 8, 'date': '27/02/2022', 'status': True}, {'display_name': 'Insemination', 'id': 'insemination', 'day': 10, 'date': '01/03/2022', 'status': False}, {'display_name': 'Pregnancy Test', 'id': 'pregnancy_test', 'day': 46, 'date': '06/04/2022', 'status': False}]

	generatePdfReport(customer_name='Customer Name', customer_email="Customer email@gmail.com",
					customer_property_name="123", customer_billing_address="134", dates=dates)