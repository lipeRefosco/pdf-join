from PyPDF2 import PdfReader, PdfMerger

JOIN_CMD = "join"

VALID_COMMANDS = [JOIN_CMD]

def join_run(user_input_parsed):
    # pdf_reader = PdfReader()
    pdf_merger = PdfMerger()
    pdf_merger.set_page_layout(layout="/OneColumn")

    [pdf_merger.append(file) for file in user_input_parsed.get("inputs")]

    pdf_merger.write(open(user_input_parsed.get("output"), 'wb'))
    pdf_merger.close()

    print(user_input_parsed)
    

EXEC_COMMAND = {
    JOIN_CMD: join_run
}
