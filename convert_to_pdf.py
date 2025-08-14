import weasyprint
import os

def html_to_pdf(html_file_path, pdf_file_path):
    """
    Convert HTML file to PDF using WeasyPrint
    """
    try:
        # Check if HTML file exists
        if not os.path.exists(html_file_path):
            print(f"Error: HTML file '{html_file_path}' not found.")
            return False
        
        # Convert HTML to PDF
        html_doc = weasyprint.HTML(filename=html_file_path)
        html_doc.write_pdf(pdf_file_path)
        
        print(f"✅ Successfully converted '{html_file_path}' to '{pdf_file_path}'")
        return True
        
    except Exception as e:
        print(f"❌ Error converting HTML to PDF: {str(e)}")
        print("\n📦 Installing required packages...")
        
        # Try to install weasyprint if not available
        try:
            import subprocess
            subprocess.run(["pip", "install", "weasyprint"], check=True)
            print("✅ WeasyPrint installed successfully. Please run the script again.")
        except Exception as install_error:
            print(f"❌ Failed to install WeasyPrint: {str(install_error)}")
            print("\n🔧 Manual installation instructions:")
            print("1. Run: pip install weasyprint")
            print("2. If on Windows, you might need: pip install weasyprint --find-links https://download.lfd.uci.edu/pythonlibs/archived/")
            print("3. Alternative: Use online HTML to PDF converters")
        
        return False

def create_alternative_pdf_script():
    """
    Create an alternative script using pdfkit (simpler installation)
    """
    alternative_script = '''
import pdfkit
import os

def html_to_pdf_pdfkit(html_file, pdf_file):
    """
    Alternative PDF conversion using pdfkit
    Requires wkhtmltopdf to be installed
    """
    try:
        # Configuration for better PDF output
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None,
            'enable-local-file-access': None
        }
        
        pdfkit.from_file(html_file, pdf_file, options=options)
        print(f"✅ PDF created successfully: {pdf_file}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("\\n📥 Please install wkhtmltopdf:")
        print("1. Download from: https://wkhtmltopdf.org/downloads.html")
        print("2. Install pdfkit: pip install pdfkit")

# Usage
if __name__ == "__main__":
    html_file = r"c:\\Users\\hp\\ss\\subsequence_subarray_problems.html"
    pdf_file = r"c:\\Users\\hp\\ss\\subsequence_subarray_problems.pdf"
    
    html_to_pdf_pdfkit(html_file, pdf_file)
'''
    
    with open(r"c:\Users\hp\ss\convert_to_pdf_alternative.py", "w", encoding="utf-8") as f:
        f.write(alternative_script)
    
    print("📄 Created alternative conversion script: convert_to_pdf_alternative.py")

if __name__ == "__main__":
    # File paths
    html_file = r"c:\Users\hp\ss\subsequence_subarray_problems.html"
    pdf_file = r"c:\Users\hp\ss\subsequence_subarray_problems.pdf"
    
    print("🔄 Converting HTML to PDF...")
    success = html_to_pdf(html_file, pdf_file)
    
    if not success:
        print("\n📋 Creating alternative conversion script...")
        create_alternative_pdf_script()
        
        print("\n🌐 Online alternatives:")
        print("1. Open the HTML file in Chrome/Edge and use 'Print to PDF'")
        print("2. Use online converters like HTML to PDF Rocket, ILovePDF, etc.")
        print("3. Use the alternative script after installing wkhtmltopdf")
    
    print(f"\n📂 Files created in: {os.path.dirname(html_file)}")
    print("   - subsequence_subarray_problems.html (main file)")
    print("   - subsequence_subarray_problems.pdf (if conversion successful)")
    print("   - convert_to_pdf_alternative.py (backup conversion method)")
