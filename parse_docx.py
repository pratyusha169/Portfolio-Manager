"""Parse AI_Project_Tracker_v2.docx and write projects.csv"""
import zipfile, xml.etree.ElementTree as ET, csv, re, os, sys

DOCX = os.path.expanduser(
    "~/Documents/Claude/Projects/NTAI_TOPS course/AI_Project_Tracker_v2.docx"
)
OUT_CSV = os.path.join(os.path.dirname(__file__), "projects.csv")

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

def extract_paragraphs(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml")
    root = ET.fromstring(xml)
    paras = []
    for p in root.iter(f"{{{W}}}p"):
        text = "".join(r.text or "" for r in p.iter(f"{{{W}}}t")).strip()
        if text:
            paras.append(text)
    return paras

def parse_projects(paras):
    # Find paragraph indices that start a new project  (#01 Title)
    proj_re = re.compile(r"^#(\d+)\s+(.+)$")
    starts = []
    for i, p in enumerate(paras):
        m = proj_re.match(p)
        if m:
            starts.append((i, int(m.group(1)), m.group(2).strip()))

    projects = []
    for idx, (start, pid, title) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(paras)
        block = paras[start + 1 : end]

        category = description = key_tools = ""
        success_lines, validation_lines = [], []
        state = "header"

        for line in block:
            # Skip boilerplate blank / underline / template lines
            if re.match(r"^_+$", line):
                continue
            if re.match(r"^(Start Date|End Date|Duration|GitHub Repo)\s*:", line):
                continue
            if re.match(r"^Status:", line):
                continue
            if re.match(r"^(Learnings & Takeaways|Hiring-Manager Talking Points)", line):
                state = "done"
                continue

            if state == "header":
                if not category:
                    category = line
                    continue
                if line.startswith("Key Tools:"):
                    key_tools = re.sub(r"^Key Tools:\s*", "", line)
                    continue
                if re.match(r"^Success Criteria", line):
                    state = "success"
                    continue
                if re.match(r"^Validation Approach", line):
                    state = "validation"
                    continue
                # Accumulate description until we hit Key Tools
                if not key_tools:
                    description = (description + " " + line).strip()

            elif state == "success":
                if re.match(r"^Validation Approach", line):
                    state = "validation"
                    continue
                success_lines.append(line)

            elif state == "validation":
                validation_lines.append(line)

        projects.append({
            "id": pid,
            "title": title,
            "category": category,
            "description": description,
            "key_tools": key_tools,
            "success_criteria": " | ".join(l for l in success_lines if l),
            "validation_approach": " | ".join(l for l in validation_lines if l),
            "status": "Not Started",
            "github": "",
            "notes": "",
        })
    return projects

def main():
    if not os.path.exists(DOCX):
        sys.exit(f"File not found: {DOCX}")
    paras = extract_paragraphs(DOCX)
    projects = parse_projects(paras)

    fields = ["id", "title", "category", "description", "key_tools",
              "success_criteria", "validation_approach", "status", "github", "notes"]

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(projects)

    print(f"Written {len(projects)} projects → {OUT_CSV}")

if __name__ == "__main__":
    main()
