from fastapi import FastAPI, HTTPException
from pathlib import Path
import os

app = FastAPI()

TEMPLATES_DIR = Path(__file__).parent / "templates-available"

def get_templates_list():
    templates = {}
    for category in os.listdir(TEMPLATES_DIR):
        category_path = TEMPLATES_DIR / category
        if category_path.is_dir():
            templates[category] = []
            for template_file in os.listdir(category_path):
                if template_file.endswith(".md"):
                    templates[category].append(template_file)
    return templates

@app.get("/templates")
def list_templates():
    """
    Lists all available writing templates, categorized by type.
    """
    return get_templates_list()

@app.get("/templates/{category}")
def get_category_templates(category: str):
    """
    Retrieves all templates for a given category, including writing-tips.
    """
    category_path = TEMPLATES_DIR / category
    if not category_path.is_dir():
        raise HTTPException(status_code=404, detail="Category not found")

    templates = []
    for template_file in os.listdir(category_path):
        if template_file.endswith(".md"):
            template_path = category_path / template_file
            templates.append({
                "template_name": template_file,
                "content": template_path.read_text()
            })

    writing_tips_path = TEMPLATES_DIR / "writing-tips.md"
    if writing_tips_path.is_file():
        templates.append({
            "template_name": "writing-tips.md",
            "content": writing_tips_path.read_text()
        })

    return templates

@app.get("/")
def read_root():
    return {"message": "Welcome to the MCP Writing Templates Service!"}