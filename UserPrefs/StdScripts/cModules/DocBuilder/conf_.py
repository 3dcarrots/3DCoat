# conf.py
import inspect
import sys
import os

# import coat_type_aliases
from docutils import nodes
import re
import shutil
from pathlib import Path
from sphinx.ext.autodoc import AttributeDocumenter, Documenter
import sphinx.ext.autodoc
import cModules.DocBuilder.sphinx_builder as sphinx_builder


# --- MODIFIED: Define correct paths for Sphinx ---
bridge_path_str = str(sphinx_builder.ROOT_DIR.resolve()).replace("\\", "/")
# Шлях до /StdScripts, щоб Sphinx міг знайти cModules, cTemplates
std_path_str = str(sphinx_builder.STD_SCRIPTS_PARENT_PATH.resolve()).replace("\\", "/")

print(f"Adding to sys.path in conf.py: {bridge_path_str}")
print(f"Adding to sys.path in conf.py: {std_path_str}")
# --- END MODIFIED ---

# --- MODIFIED: Add module paths for Sphinx autodoc ---
sys.path.insert(0, bridge_path_str)
sys.path.insert(0, std_path_str)
# --- END MODIFIED ---


def get_version():
    return "1.0.0"

    
# autosummary_generate = True

# -- Project information -----------------------------------------------------
project = "3DCoat Python API"
copyright = '2025, 3DCoat'
author = "3DCoat"
release = get_version()
version = '.'.join(release.split('.')[:2])

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',      # Auto-documentation from docstrings
    'sphinx.ext.napoleon',     # Support for Google & NumPy style docstrings
    'sphinx.ext.viewcode',     # Add links to source code
    # 'sphinx.ext.autosummary',  # autosummary
]


autodoc_mock_imports = [
    "cv2",  
    "numpy",
    "PySide6",
    "PIL",
    "Coat_CPP",
]

autodoc_default_options = {
    'undoc-members': True, 
    'show-inheritance': True,
    'show-value': True,
    'imported-members': True,
    'member-order': 'bysource',
}

#autodoc_type_aliases = coat_type_aliases.autodoc_type_aliases
add_module_names = False

templates_path = ['_templates']
exclude_patterns = []
autodoc_typehints_format = 'short'

# -- Options for HTML output (PyData Theme) ---------------------------------
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

html_theme_options = {
    "logo": {
        "text": "3DCoat Python API",
    },
    "github_url": "https://github.com/3dcarrots/3DCoat/tree/main",
    "navbar_end": ["navbar-icon-links.html", "search-field.html"],
    "show_toc_level": 3,
}



def skip_undocumented_members(app, what, name, obj, skip, options):
    # 1. Якщо Sphinx вже вирішив пропустити - погоджуємось
    if name.startswith("__"):
            return True

    # if what in ('class', 'function', 'exception', 'method'):
    try:
        # Отримуємо шлях до файлу, де визначено об'єкт
        file_path = inspect.getfile(obj)
        
        # Нормалізуємо шлях (замінюємо зворотні слеші на звичайні для надійності)
        file_path = file_path.replace('\\', '/')
        
        # Умова: якщо у шляху немає "UserPrefs" -> ПРОПУСКАЄМО
        # Це відсіє PySide6, системні бібліотеки та все, що в site-packages
        if "UserPrefs" not in file_path:
            return True
            
    except (TypeError, OSError):
        # inspect.getfile кидає помилку для вбудованих модулів (C-extensions),
        # наприклад, для багатьох класів PySide6 або `sys`.
        # Оскільки вони скомпільовані, вони точно не у вашій папці UserPrefs.
        pass

    return False
    if skip:
        return True

    # --- ЛОГІКА ДЛЯ imported-members (Bridge/cPy) ---
    # Визначаємо, в якому модулі ми зараз знаходимось
    # name виглядає як 'cTemplates.MainMenu.Textures.TexApproach'
    if '.' in name:
        current_module_name = name.rsplit('.', 1)[0]
    else:
        current_module_name = name

    # Список модулів/папок, де МИ ХОЧЕМО бачити імпортовані мембери
    whitelist_folders = ('Bridge', 'cPy')
    
    # Перевіряємо, чи поточний модуль належить до "білого списку"
    is_whitelisted = False
    for folder in whitelist_folders:
        # Перевірка на входження (наприклад, cPy.cCore починається з cPy)
        if current_module_name.startswith(folder) or f".{folder}." in current_module_name:
            is_whitelisted = True
            break

    # Якщо модуль НЕ в білому списку - ми маємо вручну приховати імпортовані класи/функції
    if not is_whitelisted:
        # Ми перевіряємо тільки класи та функції, щоб випадково не приховати змінні (ваші меню),
        # які є екземплярами класів
        if what in ('class', 'function', 'exception'):
            obj_module = getattr(obj, '__module__', None)
            # Якщо об'єкт визначений в іншому модулі, ніж поточний -> це імпорт. ПРИХОВУЄМО.
            if obj_module and obj_module != current_module_name:
                return True
    # ------------------------------------------------

    # --- ВАША СТАРА ЛОГІКА (з поправкою на docstring у child) ---
    # Перевірка на наявність 'child.Implementation' (для ваших меню)
    if hasattr(obj, 'child') and obj.child is not None:
         impl = getattr(obj.child, 'Implementation', None)
         doc = getattr(impl, '__doc__', None)
         if doc and isinstance(doc, str) and len(doc.strip()) > 3:
             return False 

    # Перевірка власного docstring
    doc = getattr(obj, '__doc__', None)
    if doc and isinstance(doc, str) and len(doc.strip()) > 3:
        return False

    # Глибока перевірка мемберів (якщо ви це використовували раніше)
    if what in ('class', 'module'):
        try:
            members = inspect.getmembers(obj)
            for mem_name, mem_obj in members:
                if mem_name.startswith('_'): continue
                mem_doc = getattr(mem_obj, '__doc__', None)
                if mem_doc and isinstance(mem_doc, str) and len(mem_doc.strip()) > 3:
                    return False
        except Exception:
            pass

    return None


# --- :color: role function (unchanged) ---
def color_swatch_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    hex_code = text.strip()
    if not hex_code.startswith('#') or not (len(hex_code) == 9 or len(hex_code) == 7):
        msg = inliner.reporter.error(f"Invalid hex color code: {text}", line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
    if len(hex_code) == 9: # AARRGGBB
        css_hex = f"#{hex_code[3:]}"
    else: # RRGGBB
        css_hex = hex_code
    swatch_style = (
        f"display: inline-block; "
        f"width: 1em; height: 1em; "
        f"border: 1px solid #888; "
        f"background-color: {css_hex}; "
        f"vertical-align: middle; "
        f"margin-right: 5px;"
    )
    swatch_node = nodes.raw(
        '',
        f'<span style="{swatch_style}"></span>',
        format='html'
    )
    text_node = nodes.Text(hex_code)
    return [swatch_node, text_node], []

def autodoc_process_docstring(app, what, name, obj, options, lines):
    # --- ВИПРАВЛЕННЯ: Очищуємо попередній тип, щоб він не переходив на наступну змінну ---
    options.pop('__my_parsed_type', None)
    # -----------------------------------------------------------------------------------

    # --- 1. Витягування прихованого опису з child.Implementation (без змін) ---
    if not lines:
        if hasattr(obj, 'child') and obj.child is not None:
            impl = getattr(obj.child, 'Implementation', None)
            hidden_doc = getattr(impl, '__doc__', None)
            
            if hidden_doc and isinstance(hidden_doc, str) and hidden_doc.strip():
                from inspect import cleandoc
                lines.extend(cleandoc(hidden_doc).splitlines())

    # --- 2. Обробка (T) типів (без змін) ---
    if lines:
        first_line = lines[0].strip()
        if '(T)' in first_line: 
            parts = first_line.rsplit('(T)', 1)
            if len(parts) == 2:
                type_str = parts[0].strip()
                description_str = parts[1].strip()
                type_str = re.sub(r'\bstatic\b', '', type_str, flags=re.IGNORECASE)
                type_str = re.sub(r'\bconst\b', '', type_str, flags=re.IGNORECASE)
                type_str = type_str.strip()
                options['__my_parsed_type'] = type_str
                lines[0] = description_str
                if not description_str:
                    lines.pop(0)

    # --- 3. Очистка Coat_CPP (без змін) ---
    if lines:
        for i in range(len(lines)):
            lines[i] = re.sub(r'\bCoat_CPP\.', '', lines[i])

    # --- 4. НОВЕ: Обробка Example блоків та Line Blocks ---
    final_lines = []
    in_code_block = False
    
    example_pattern = re.compile(r'^\s*Example.*:$', re.IGNORECASE)

    for line in lines:
        stripped = line.strip()
        
        if in_code_block and stripped:
            if not line.startswith((' ', '\t')):
                in_code_block = False

        if example_pattern.match(line):
            new_line = line.rsplit(':', 1)[0] + '::'
            final_lines.append(new_line)
            final_lines.append("") 
            in_code_block = True
            continue

        if in_code_block:
            final_lines.append(line)
            continue
        
        if not stripped:
            final_lines.append("")
            continue

        if not stripped.startswith(('*', '-', '..', ':', '>', '|')):
             final_lines.append("| " + line)
        else:
             final_lines.append(line)
             
    lines[:] = final_lines

def autodoc_process_signature(app, what, name, obj, options, signature, return_annotation):
    # Видаляємо лише сміття типу Coat_CPP., тип змінної ми вже обробили в Documenter
    if signature:
        signature = re.sub(r'\bCoat_CPP\.', '', signature)
    if return_annotation:
        return_annotation = re.sub(r'\bCoat_CPP\.', '', return_annotation)
    return (signature, return_annotation)


# ==========================================
# 2. ColorAttributeDocumenter (Standard Priority)
# ==========================================
class CoatDocumenter(sphinx.ext.autodoc.AttributeDocumenter):
    priority = 11

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        try:
            impl = getattr(member, 'Implementation', None)
            cnt = getattr(member, 'Content', None)
            
            if not inspect.isclass(member): 
                if impl is not None and cnt is not None:
                    return True
                    
        except Exception:
            return super().can_document_member(member, membername, isattr, parent)
        return super().can_document_member(member, membername, isattr, parent)

    def get_doc(self):
            # Безпечне отримання docstring
            impl = getattr(self.object, 'Implementation', None)
            cnt = getattr(self.object, 'Content', None)
            
            # Якщо це спец-об'єкт 3DCoat
            if impl is not None and cnt is not None:
                doc = getattr(self.object, '__doc__', None)
                if doc:
                    from inspect import cleandoc
                    return [cleandoc(doc).splitlines()]
            
            # Стандартна поведінка для всього іншого
            return super().get_doc()
    
    # --- ВИПРАВЛЕННЯ ТУТ ---
    def add_directive_header(self, sig: str) -> None:
            # 1. Витягуємо тип з (T) коментаря
            _ = self.get_doc()
            if self.options.get('__my_parsed_type'):
                self.annotation = self.options['__my_parsed_type']

            # 2. Генеруємо заголовок (Name : Type)
            super().add_directive_header(sig)

            # 3. Ваша логіка для Value та кольорів (Hex/Color Swatch)
            if not self.options.get('show-value', True):
                return

            is_color_name = 'Color' in self.objpath[-1]
            is_int_type = isinstance(self.object, int)
            
            try:
                if (self.object is sphinx.ext.autodoc.INSTANCEATTR or 
                (repr(self.object).startswith("<") and " object at " in repr(self.object))):
                    return
            except Exception:
                pass

            # Додаємо джерело (source name)
            self.add_line('', self.get_sourcename())

            if is_color_name and is_int_type:
                try:
                    val = int(self.object)
                    hex_code = f"#{val & 0xFFFFFFFF:08X}"
                    self.add_line(f'   :value: :color:`{hex_code}`', self.get_sourcename())
                except Exception:
                    pass
                    # val_repr = repr(self.object)
                    # val_repr = re.sub(r'\bCoat_CPP\.', '', val_repr)
                    # self.add_line('   :value: ' + val_repr, self.get_sourcename())
            else:
                pass
                # val_repr = repr(self.object)
                # val_repr = re.sub(r'\bCoat_CPP\.', '', val_repr)
                # self.add_line('   :value: ' + val_repr, self.get_sourcename())
    # -----------------------

    # (Цей метод add_content залишаємо як є, він не впливає на заголовок)

    def add_content(self, more_content, no_docstring=False):
        # Перевірка опції show-value
        if not self.options.get('show-value', True):
            # ВИПРАВЛЕННЯ: прибрано аргумент no_docstring
            super().add_content(more_content)
            return

        # Ваша додаткова логіка (якщо вона тут потрібна)
        # ...
        
        # ВИПРАВЛЕННЯ: прибрано аргумент no_docstring
        super().add_content(more_content)


def copy_doxygen_assets(app, exception):
    if exception:
        return 

    src_dir = Path(app.srcdir) / "tutorials"
    out_dir = Path(app.outdir) / "tutorials"

    if not src_dir.exists():
        print(f"Doxygen source dir {src_dir} not found. Skipping asset copy.")
        return

    shutil.copytree(
        src_dir,
        out_dir,
        ignore=shutil.ignore_patterns("*.rst", "*.html"),
        dirs_exist_ok=True
    )
    print(f"Copied Doxygen assets from {src_dir} to {out_dir}")

def setup(app):
    app.connect('build-finished', copy_doxygen_assets)
    app.connect('autodoc-skip-member', skip_undocumented_members)
    app.connect('autodoc-process-docstring', autodoc_process_docstring)
    app.connect('autodoc-process-signature', autodoc_process_signature)
    app.add_role("color", color_swatch_role)
    app.add_autodocumenter(CoatDocumenter)
