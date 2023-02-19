from sys import argv
import PyPDF4

def getIdx(t, s):
  for i in range(len(t)):
    if s in t[i]:
      return i
  raise KeyError()

for fn in argv[1:]:
    
  f=open(fn, 'rb')

  re = PyPDF4.PdfFileReader(f)
  tokens = re.getPage(0).extractText().split('\n')
  # print(tokens)

  date_idx = getIdx(tokens, "Date")+1
  subtotal_idx = getIdx(tokens, "Subtotal")+1
  total_taxes_idx = getIdx(tokens, "Total taxes")+1
  invoice_total_idx = getIdx(tokens, "Invoice Total")+1

  print(f'{tokens[date_idx]},,,{tokens[subtotal_idx]},,,,,{tokens[total_taxes_idx]},{tokens[invoice_total_idx]}')
