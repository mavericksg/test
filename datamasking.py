import re

input_string = ""

print("1. reading input file ...")
with open('input.xml') as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        input_string = input_string + data

print("2. masking debtor name ...")
input_string = re.sub(r"<bs:Dbtr><bs:Nm>.*</bs:Nm></bs:Dbtr>", "<bs:Dbtr><bs:Nm>MASKED DEBTOR NAME</bs:Nm></bs:Dbtr>", input_string)

print("3. masking ultimate creditor ...")
input_string = re.sub(r"<bs:UltmtCdtr><bs:Nm>.*</bs:Nm></bs:UltmtCdtr>", "<bs:UltmtCdtr><bs:Nm>MASKED ULTIMATE CREDIOR NAME</bs:Nm></bs:UltmtCdtr>", input_string)

print("   MASKING COMPLETED.")

print("4. Writing output file.")

with open('output.xml', 'w') as out_file:
    out_file.write(input_string)

print("DONE.")