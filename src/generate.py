import os, sys, shutil
from jinja2 import Environment, FileSystemLoader

BASE = os.path.dirname(os.path.abspath(__file__))
# Build into a scratch dir first (outputs/ files can't be deleted/renamed once written,
# so we can't rebuild in place there). Final copy step pushes this into outputs/physics-notes.
OUT = os.environ.get("BUILD_OUT", os.path.join(BASE, "..", "docs"))

sys.path.insert(0, BASE)
import data_class11 as C11
import data_class12 as C12

env = Environment(loader=FileSystemLoader(os.path.join(BASE, "templates")))


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def build_class(mod, folder, active):
    tpl_idx = env.get_template("class_index.html.j2")
    # tags for index cards
    for ch in mod.CHAPTERS_FLAT:
        pass

    html = tpl_idx.render(
        page_title=mod.CLASS_TITLE, description=mod.CLASS_INTRO, root="../",
        active=active, class_label=mod.CLASS_LABEL, class_title=mod.CLASS_TITLE,
        class_intro=mod.CLASS_INTRO, units=mod.UNITS,
    )
    write(f"{folder}/index.html", html)

    flat = mod.CHAPTERS_FLAT
    # map chapter id -> unit roman
    id_to_unit = {}
    for unit in mod.UNITS:
        for ch in unit["chapters"]:
            id_to_unit[ch["id"]] = unit["roman"]

    tpl_ch = env.get_template("chapter.html.j2")
    for i, ch in enumerate(flat):
        prev_ch = flat[i - 1] if i > 0 else None
        next_ch = flat[i + 1] if i < len(flat) - 1 else None
        html = tpl_ch.render(
            page_title=f"{ch['number']}. {ch['title']}", title=ch["title"],
            description=ch["tagline"], root="../", active=active,
            chapter_id=ch["id"], class_label=mod.CLASS_LABEL,
            unit_roman=id_to_unit[ch["id"]], number=ch["number"],
            tagline=ch["tagline"], sections=ch["sections"],
            recap=ch["recap"], prev=prev_ch, next=next_ch,
            exam_corner=ch.get("exam_corner", []),
        )
        write(f"{folder}/{ch['id']}.html", html)

    # Consolidated formula sheet: pull every 'formula' block out of every chapter's sections
    tpl_fs = env.get_template("formula_sheet.html.j2")
    fs_chapters = []
    for ch in flat:
        formulas = []
        for sec in ch["sections"]:
            for blk in sec["blocks"]:
                if blk["type"] == "formula":
                    formulas.append(blk)
        fs_chapters.append({"id": ch["id"], "number": ch["number"], "title": ch["title"], "formulas": formulas})
    fs_html = tpl_fs.render(
        page_title=f"{mod.CLASS_LABEL} Formula Sheet", description="Every formula, one page.",
        root="../", active=active, class_label=mod.CLASS_LABEL, chapters=fs_chapters,
    )
    write(f"{folder}/formula-sheet.html", fs_html)

    return len(flat)


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    # copy assets from existing physics-notes/assets if present in git-ignored backup? We rebuild fresh,
    # so assets must be restored from the assets_src backup copy we keep in build/assets_src
    assets_src = os.path.join(BASE, "assets")
    os.makedirs(OUT, exist_ok=True)
    if os.path.exists(assets_src):
        shutil.copytree(assets_src, os.path.join(OUT, "assets"))

    tpl_home = env.get_template("home.html.j2")
    home_html = tpl_home.render(
        page_title="Home", description="Free CHSE Odisha +2 Physics handwritten notes",
        root="", active="home", c11_count=len(C11.CHAPTERS_FLAT), c12_count=len(C12.CHAPTERS_FLAT),
    )
    write("index.html", home_html)

    tpl_strategy = env.get_template("exam_strategy.html.j2")
    strategy_html = tpl_strategy.render(
        page_title="Exam Strategy", description="How to score 90%+ in CHSE +2 Physics",
        root="", active="strategy",
    )
    write("exam-strategy.html", strategy_html)

    n11 = build_class(C11, "class11", "c11")
    n12 = build_class(C12, "class12", "c12")
    print(f"Built home + class11 ({n11} chapters) + class12 ({n12} chapters)")


if __name__ == "__main__":
    main()
