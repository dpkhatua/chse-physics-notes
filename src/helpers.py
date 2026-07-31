"""Small helper functions to build content-block dicts concisely."""

def p(text):
    return {"type": "p", "text": text}

def lst(items):
    return {"type": "list", "items": items}

def olist(items):
    return {"type": "olist", "items": items}

def formula(title, lines):
    return {"type": "formula", "title": title, "lines": lines}

def diagram(name, caption, width=520, height=260):
    return {"type": "diagram", "name": name, "caption": caption, "width": width, "height": height}

def sticky(title, text, color="yellow"):
    return {"type": "sticky", "title": title, "text": text, "color": color}

def mnemonic(text):
    return {"type": "mnemonic", "text": text}

def derivation(title, given, steps, result):
    """A step-by-step derivation box. given=str or None, steps=list of str, result=final boxed formula."""
    return {"type": "derivation", "title": title, "given": given, "steps": steps, "result": result}

def solved(problem, steps, answer):
    """A fully worked numerical: problem statement, list of solution steps, final answer."""
    return {"type": "solved", "problem": problem, "steps": steps, "answer": answer}

def mistake(text):
    return {"type": "mistake", "text": text}

def tip(text):
    return {"type": "tip", "text": text}

def section(heading, blocks):
    return {"heading": heading, "blocks": blocks}

def pyq(marks, q):
    return {"marks": marks, "q": q}

def chapter(id, number, title, tagline, tags, sections, recap, exam_corner=None, exam_corner_note=None):
    return {
        "id": id, "number": number, "title": title, "tagline": tagline,
        "tags": tags, "sections": sections, "recap": recap,
        "exam_corner": exam_corner or [], "exam_corner_note": exam_corner_note,
    }
