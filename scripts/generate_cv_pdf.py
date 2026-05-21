from pathlib import Path
import textwrap


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Julias-Muyambi-CV.pdf"

W, H = 595, 842
SIDEBAR = 205


def esc(text):
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16) / 255
    g = int(hex_color[2:4], 16) / 255
    b = int(hex_color[4:6], 16) / 255
    return f"{r:.3f} {g:.3f} {b:.3f}"


class Canvas:
    def __init__(self):
        self.ops = []

    def rect(self, x, y, w, h, color):
        self.ops.append(f"{rgb(color)} rg {x} {y} {w} {h} re f")

    def line(self, x1, y1, x2, y2, color="#cfe0f2", width=1):
        self.ops.append(f"{rgb(color)} RG {width} w {x1} {y1} m {x2} {y2} l S")

    def text(self, x, y, text, size=10, color="#102033", bold=False):
        font = "F2" if bold else "F1"
        self.ops.append(
            f"BT /{font} {size} Tf {rgb(color)} rg 1 0 0 1 {x} {y} Tm ({esc(text)}) Tj ET"
        )

    def wrapped(self, x, y, text, width_chars, size=10, color="#102033", bold=False, leading=13):
        lines = textwrap.wrap(text, width=width_chars)
        for line in lines:
            self.text(x, y, line, size=size, color=color, bold=bold)
            y -= leading
        return y


c = Canvas()
c.rect(0, 0, W, H, "#ffffff")
c.rect(0, 0, SIDEBAR, H, "#07192d")
c.rect(SIDEBAR, 0, 4, H, "#38bdf8")

# Sidebar
y = 792
c.text(24, y, "Julias Muyambi", 24, "#eaf6ff", True)
y -= 22
c.wrapped(24, y, "AI Researcher | Agentic AI Passionate | Software Developer", 27, 10, "#38bdf8", True, 12)
y -= 58
y = c.wrapped(
    24,
    y,
    "Software developer and emerging AI researcher based in Kampala, Uganda. Focused on practical business systems, AI-powered products, agentic AI, AI modeling, generative AI, and AI prompt engineering.",
    28,
    9,
    "#c9d9ea",
    False,
    11,
)

def side_section(title, items, y):
    y -= 20
    c.text(24, y, title.upper(), 10, "#38bdf8", True)
    y -= 16
    for item in items:
        y = c.wrapped(28, y, item, 30, 9, "#d7e7f7", False, 11)
        y -= 4
    return y


y = side_section(
    "Contact",
    [
        "Email: muyambijulias@gmail.com",
        "Phone: +256 776 828 355",
        "Location: Kampala, Uganda",
        "GitHub: Julias-Ai-Developer",
    ],
    y,
)
y = side_section(
    "Core Skills",
    [
        "AI Research",
        "Agentic AI",
        "Generative AI",
        "AI Prompt Engineering",
        "AI Modeling",
        "Python",
        "PHP",
        "Laravel",
        "MySQL",
        "SQLite",
    ],
    y,
)
y = side_section(
    "Credentials",
    [
        "OCI Generative AI Foundations - Oracle University",
        "AI Prompt Engineering credential",
        "Python Workshop certificate",
    ],
    y,
)

# Main content
x = 235
y = 792

def main_heading(title, y):
    c.text(x, y, title.upper(), 11, "#0f4f85", True)
    c.line(x, y - 6, 555, y - 6, "#cfe0f2", 0.8)
    return y - 22


def item(title, meta, bullets, y):
    c.text(x, y, title, 13, "#102033", True)
    y -= 14
    if meta:
        c.text(x, y, meta, 9, "#52657a", True)
        y -= 13
    for bullet in bullets:
        y = c.wrapped(x + 8, y, "- " + bullet, 60, 9.5, "#34485f", False, 12)
    return y - 10


y = main_heading("Professional Summary", y)
y = c.wrapped(
    x,
    y,
    "I am an AI researcher, Agentic AI passionate, and Software Developer. I build practical web systems for businesses and I am currently starting research work in applied AI, with a focus on agentic AI, AI modeling, generative AI, and AI prompt engineering.",
    62,
    10,
    "#34485f",
    False,
    13,
)
y -= 18

y = main_heading("Experience", y)
y = item(
    "CEO & Founder, Kamatrust AI",
    "Founder | AI and Software Product Direction",
    [
        "Shaping a long-term direction around AI research, agentic AI, AI modeling, and AI-powered software products.",
        "Focused on practical AI tools and business systems that support real client operations.",
    ],
    y,
)
y = item(
    "Freelance Software Developer",
    "Business Systems and Client Projects",
    [
        "Builds practical systems for business operations, retail workflows, asset tracking, and livestock management.",
        "Works with PHP, Laravel, Python, MySQL, SQLite, clean interfaces, dashboards, and reliable data structures.",
    ],
    y,
)
y = item(
    "AI Researcher and Agentic AI Learner",
    "Current Focus",
    [
        "Currently starting applied AI research and growing practical skills in AI agents, AI prompt systems, and applied AI features.",
        "Brings software engineering discipline into AI products so they are useful, maintainable, and business-ready.",
    ],
    y,
)

y = main_heading("Selected Projects", y)
y = item(
    "Assetlite - Asset Management System",
    "",
    ["System for organisations to register, track, and monitor assets, covering lifecycle, location, custodian, and maintenance."],
    y,
)
y = item(
    "Sell Safe - Retail POS System",
    "",
    ["Point of sale system for retailers, covering sales, stock movement, receipts, users, reports, and daily business tracking."],
    y,
)
y = item(
    "Farmclick - Livestock Management",
    "",
    ["Livestock management platform for farm records, animal tracking, operational data, and easier management of livestock activities."],
    y,
)

y = main_heading("Open To", y)
c.wrapped(
    x,
    y,
    "Job opportunities, freelance gigs, AI-powered product work, business system development, and research-oriented opportunities connected to AI, agentic AI, software development, and practical automation.",
    62,
    10,
    "#34485f",
    False,
    13,
)

content = "\n".join(c.ops).encode("latin-1")
objects = [
    b"<< /Type /Catalog /Pages 2 0 R >>",
    b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
    b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> /Contents 6 0 R >>",
    b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>",
    b"<< /Length " + str(len(content)).encode("ascii") + b" >>\nstream\n" + content + b"\nendstream",
]

pdf = [b"%PDF-1.4\n"]
offsets = [0]
for i, obj in enumerate(objects, start=1):
    offsets.append(sum(len(part) for part in pdf))
    pdf.append(f"{i} 0 obj\n".encode("ascii") + obj + b"\nendobj\n")

xref_at = sum(len(part) for part in pdf)
pdf.append(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
pdf.append(b"0000000000 65535 f \n")
for off in offsets[1:]:
    pdf.append(f"{off:010d} 00000 n \n".encode("ascii"))
pdf.append(
    f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_at}\n%%EOF\n".encode("ascii")
)

OUT.write_bytes(b"".join(pdf))
print(OUT)
