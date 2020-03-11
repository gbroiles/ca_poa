from fpdf import FPDF
import resource

class PDF(FPDF):
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def fill_fields(text, fields)
    for field, value in fields.items():
        print(field, value)

# Instantiation of inherited class

fill_fields(resource.form, resource.testfields)

pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 14)
pdf.multi_cell(0, 6, 'California Uniform Statutory Form Power of Attorney\n(California Probate Code §4401)', border=1, align='C')
pdf.set_font('Times', '', 10)
pdf.multi_cell(0, 4, resource.preamble, align='J', border=0)
pdf.set_font('Times', '', 12)
pdf.multi_cell(0, 5, resource.form, align='L', border=0)
pdf.set_font('Times', '', 10)
pdf.multi_cell(0, 4, resource.notary_box, border=1, align='L')
pdf.multi_cell(0, 4, resource.notary_ack, border=0, align='L')
pdf.output('poa_test.pdf', 'F')

