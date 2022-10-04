import pdfkit


def htmltopdf(html, pdf_path):
    """
    Convert html to pdf using pdfkit which is a wrapper of wkhtmltopdf
    """
    options = {"enable-local-file-access": None,'page-size': 'Letter'}
    pdfkit.from_string(html, pdf_path, options=options)