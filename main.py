from fpdf import FPDF
import json


with open('assets/json/data.json') as f:
    data = json.load(f)
    
with open('assets/templates/template.rtf') as f:
    template = f.read()

# replace placeholders with data
for item in data:
    for key, value in item.items():
        template = template.replace('{' + key + '}', value)
        
# convert to pdf
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)
pdf.write(8, template)
pdf.output('assets/pdfs/output.pdf', 'F')