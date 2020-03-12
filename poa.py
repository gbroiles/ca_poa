from fpdf import FPDF
import resource

MARGIN = 15


class PDF(FPDF):
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font("Arial", "I", 8)
        # Page number
        self.cell(0, 10, "Page " + str(self.page_no()) + "/{nb}", 0, 0, "C")


def fill_fields(text, fields):
    for field, value in fields.items():
        field = "[{}]".format(field)
        if text.find(field):
#            print("Found {}".format(field))
            text = text.replace(field, value)
    return text


# Instantiation of inherited class

appointment = fill_fields(resource.appointment, resource.testfields)
form = fill_fields(resource.form, resource.testfields)
supplement = fill_fields(resource.supplement, resource.testfields)
multiple_agent = fill_fields(resource.multiple_agent, resource.testfields)
supplement = fill_fields(resource.supplement, resource.testfields)
signature_block = fill_fields(resource.signature_block, resource.testfields)
notary_ack = fill_fields(resource.notary_ack, resource.testfields)


pdf = PDF(orientation="P", format="letter")
pdf.alias_nb_pages()
pdf.set_margins(MARGIN, MARGIN, MARGIN)
pdf.add_page()
pdf.set_font("Times", "", 14)
pdf.multi_cell(
    0,
    6,
    "California Uniform Statutory Form\nPower of Attorney\n(California Probate Code §4401)",
    border=0,
    align="C",
)
pdf.set_font("Times", "", 9)
pdf.write(4, resource.preamble)
pdf.set_font("Times", "", 12)
pdf.write(5, appointment)
pdf.set_font("Times", "", 9)
pdf.write(4, resource.preamble2)
pdf.set_font("Times", "", 12)
pdf.write(5, form)
pdf.set_font("Times", "", 9)
pdf.write(4, supplement)
pdf.add_page()
pdf.set_font("Times", "", 12)
pdf.write(5, multiple_agent)
pdf.write(5, signature_block)
pdf.set_font("Times", "", 10)
pdf.multi_cell(80, 4, resource.notary_box, border=1, align="L")
pdf.write(4, notary_ack)
pdf.output("poa_test.pdf", "F")
