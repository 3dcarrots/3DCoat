# conf.py
import inspect
import sys
import os
import re
import shutil
from pathlib import Path
import importlib

# Sphinx imports
from docutils import nodes
from sphinx.ext.autodoc import AttributeDocumenter, Documenter
import sphinx.ext.autodoc

# Local build script imports
import cModules.DocBuilder.sphinx_builder as sphinx_builder

# --- Path Configuration ---
# Define paths to ensure Sphinx can locate cModules, cTemplates, and other core libraries.
bridge_path_str = str(sphinx_builder.BRIDGE_DIR.resolve()).replace("\\", "/")
std_path_str = str(sphinx_builder.STD_SCRIPTS_PARENT_PATH.resolve()).replace("\\", "/")

sys.path = [p for p in sys.path if 'Bridge' not in p]

print(f"Adding to sys.path in conf.py: {bridge_path_str}")
print(f"Adding to sys.path in conf.py: {std_path_str}")

sys.path.insert(0, bridge_path_str)
sys.path.insert(0, std_path_str)

def clean_reload():
    targets = ['cPy', 'CMD', 'coat']
    
    # 1. Знаходимо всі завантажені модулі, які починаються з цих назв
    # Використовуємо list(sys.modules.keys()), щоб створити копію ключів,
    # бо ми будемо змінювати словник під час ітерації.
    modules_to_kill = []
    for mod_name in list(sys.modules.keys()):
        for target in targets:
            # Перевіряємо: це сам модуль АБО його підмодуль (наприклад coat.settings)
            if mod_name == target or mod_name.startswith(target + '.'):
                modules_to_kill.append(mod_name)

    # 2. Видаляємо їх з пам'яті Python
    for mod in modules_to_kill:
        del sys.modules[mod]
        # print(f"Вивантажено: {mod}") # Розкоментуйте для дебагу

    # 3. Імпортуємо заново
    # Оскільки ми видалили їх з sys.modules, Python буде змушений 
    # заново прочитати файли з диска.
    global cPy, CMD, coat
    import cPy
    import CMD
    import coat
    
    print("Всі модулі (cPy, CMD, coat) та їх підмодулі успішно перезавантажено!")

# Виклик функції
clean_reload()

def get_version():
    return "1.0.0"

# -- Project information -----------------------------------------------------
project = "3DCoat Python API"
copyright = '2025, 3DCoat'
author = "3DCoat"
release = get_version()
version = '.'.join(release.split('.')[:2])

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',      # Core library for generating docs from docstrings
    'sphinx.ext.napoleon',     # Support for Google & NumPy style docstrings
    'sphinx.ext.viewcode',     # Add links to source code
    'sphinx_codeautolink',
]
codeautolink_autodoc_inject = True
autodoc_preserve_defaults = True

codeautolink_global_preface = """
import cPy
import coat
import cPy.cRender
import cPy.cCore
from cPy.CoreAPI import *
from cPy.cTypes import *
from cPy.PrimAPI import *

from cPy.cTypes import cVec2 as vec2
from cPy.cTypes import cVec3 as vec3
from cPy.cTypes import cVec4 as vec4
from cPy.cTypes import cMat3 as mat3
from cPy.cTypes import cMat4 as mat4
from cPy.cTypes import cRect as rect
from cPy.cTypes import cQuat as quat
from cPy.cTypes import cRotation as rotation
from cPy.cTypes import cAngles as angles
from cPy.cTypes import cBounds as boundbox

"""

# Modules to mock (avoids installation requirements for doc generation)
autodoc_mock_imports = [
    "cv2",  
    "numpy",
    "PySide6",
    "PIL",
]

autodoc_default_options = {
    'undoc-members': True, 
    'show-inheritance': True,
    'show-value': True,
    'imported-members': True,
    'member-order': 'bysource',
}

autodoc_use_legacy_class_based = True

add_module_names = False
templates_path = ['_templates']
exclude_patterns = []
autodoc_typehints_format = 'short'

# -- Options for HTML output (Sphinx Book Theme) -----------------------------
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

default_role = 'any'
# -- Custom Event Handlers ---------------------------------------------------

def skip_undocumented_members(app, what, name, obj, skip, options):
    """
    Визначає, чи слід пропускати член класу під час генерації документації.
    """
    # 1. Якщо Sphinx вже вирішив пропустити (наприклад, приватні __)
    if name.startswith("__"):
        return True

    # 2. Фільтрація UserPrefs (ваш існуючий код)
    try:
        file_path = inspect.getfile(obj)
        file_path = file_path.replace('\\', '/')
        if "UserPrefs" not in file_path:
            return True
    except (TypeError, OSError):
        pass

    # 3. --- НОВА ЛОГІКА ДЛЯ МАСИВІВ (Виправлена) ---
    # Ми перевіряємо, чи належить цей метод/атрибут до класу, який ми хочемо скоротити.
    if what in ('method', 'attribute', 'property', 'data', 'class'):
        # Спробуємо отримати 'qualname' (напр. 'ClassArray_NGObject.Add')
        qualname = getattr(obj, '__qualname__', '')
        
        # Якщо qualname порожній (рідкісні випадки C-ext), пробуємо використати name
        if not qualname:
            qualname = name

        # Розбиваємо ім'я: ClassName.MethodName
        parts = qualname.split('.')
        
        if len(parts) > 1:
            # Передостанній елемент - це назва класу, якому належить метод
            parent_class = parts[-2]
            
            # Якщо батьківський клас є "надлишковим", ми приховуємо цей метод
            if is_redundant_array_class(parent_class):
                return True
                
    # 4. Стандартні фільтри
    if skip:
        return True

    # --- Ваша логіка для Proxy/Implementation ---
    if hasattr(obj, 'child') and obj.child is not None:
         impl = getattr(obj.child, 'Implementation', None)
         doc = getattr(impl, '__doc__', None)
         if doc and isinstance(doc, str) and len(doc.strip()) > 3:
             return False 

    doc = getattr(obj, '__doc__', None)
    if doc and isinstance(doc, str) and len(doc.strip()) > 3:
        return False

    return None


ARRAY_GROUPS = {
    # "Префікс": "Виключення (Головний клас, який треба залишити повним)"
    "ClassArray_": "ClassArray_BaseClass",
    "cArray_": "cArray_int",  # Змініть на ваш реальний базовий клас, якщо інший
    "cList_": "cList_int",    # Змініть на ваш реальний базовий клас
}

def is_redundant_array_class(name):
    """
    Перевіряє, чи є клас 'другорядним' (тим, що треба скоротити).
    name: може бути 'ClassArray_NGObject' або повний шлях 'Bridge.cPy...ClassArray_NGObject'
    """
    clean_name = name.split('.')[-1]
    
    for prefix, master_class in ARRAY_GROUPS.items():
        if clean_name.startswith(prefix):
            # Якщо це головний клас (BaseClass) - залишаємо його
            if clean_name == master_class:
                return False
            # Якщо це будь-який інший клас з таким префіксом - це клон
            return True
    return False

def color_swatch_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Custom Sphinx role to display a color swatch next to a hex code.
    Usage: :color:`#RRGGBB` or :color:`#AARRGGBB`
    """
    hex_code = text.strip()
    if not hex_code.startswith('#') or not (len(hex_code) == 9 or len(hex_code) == 7):
        msg = inliner.reporter.error(f"Invalid hex color code: {text}", line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
    
    # Handle Alpha channel (AARRGGBB) vs Standard (RRGGBB)
    if len(hex_code) == 9: 
        css_hex = f"#{hex_code[3:]}"
    else: 
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
    """
    Post-process docstrings.
    """
    # --- Очищення опису для скорочених масивів ---
    if what == 'class':
        # name тут зазвичай повне: Bridge.cPy.ClassArray.ClassArray_NGObject
        if is_redundant_array_class(name):
            lines.clear() # Видаляємо весь текст опису
            
            # (Опціонально) Додаємо підказку
            clean_name = name.split('.')[-1]
            for prefix, master in ARRAY_GROUPS.items():
                if clean_name.startswith(prefix):
                    lines.append(f"Array class. See :class:`{master}` for full documentation.")
                    break
            return # Зупиняємо обробку для цього класу

    options.pop('__my_parsed_type', None)
    
    # 1. Extract hidden docstrings from Implementation proxies
    if not lines:
        if hasattr(obj, 'child') and obj.child is not None:
            impl = getattr(obj.child, 'Implementation', None)
            hidden_doc = getattr(impl, '__doc__', None)
            
            if hidden_doc and isinstance(hidden_doc, str) and hidden_doc.strip():
                from inspect import cleandoc
                lines.extend(cleandoc(hidden_doc).splitlines())

    # 2. Process custom (T) Type tags
    # Extracts type info usually formatted as "(T) TypeName description"
    if lines:
        first_line = lines[0].strip()
        if '(T)' in first_line: 
            parts = first_line.rsplit('(T)', 1)
            if len(parts) == 2:
                type_str = parts[0].strip()
                description_str = parts[1].strip()
                # Clean up C++ specifiers
                type_str = re.sub(r'\bstatic\b', '', type_str, flags=re.IGNORECASE)
                type_str = re.sub(r'\bconst\b', '', type_str, flags=re.IGNORECASE)
                type_str = type_str.strip()
                
                options['__my_parsed_type'] = type_str
                lines[0] = description_str
                if not description_str:
                    lines.pop(0)

    # 3. Clean Coat_CPP prefixes
    if lines:
        for i in range(len(lines)):
            lines[i] = re.sub(r'\bCoat_CPP\.', '', lines[i])
    
    # 4. Format 'Example' blocks and enforce line blocks
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

        # Force line block formatting for standard text
        if not stripped.startswith(('*', '-', '..', ':', '>', '|')):
             final_lines.append("| " + line)
        else:
             final_lines.append(line)
             
    lines[:] = final_lines


def autodoc_process_signature(app, what, name, obj, options, signature, return_annotation):
    """
    Cleans up C++ namespace artifacts (Coat_CPP) from function signatures.
    """
    if signature:
        signature = re.sub(r'\bCoat_CPP\.', '', signature)
    if return_annotation:
        return_annotation = re.sub(r'\bCoat_CPP\.', '', return_annotation)
    return (signature, return_annotation)


# ==========================================
# Custom Documenter: CoatDocumenter
# ==========================================
class CoatDocumenter(sphinx.ext.autodoc.AttributeDocumenter):
    """
    Custom Documenter for 3DCoat specific attributes.
    Handles 'Implementation' and 'Content' proxy objects and renders color swatches.
    """
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
            # Safely retrieve docstring from the Implementation proxy if available
            impl = getattr(self.object, 'Implementation', None)
            cnt = getattr(self.object, 'Content', None)
            
            if impl is not None and cnt is not None:
                doc = getattr(self.object, '__doc__', None)
                if doc:
                    from inspect import cleandoc
                    return [cleandoc(doc).splitlines()]
            
            return super().get_doc()
    
    def add_directive_header(self, sig: str) -> None:
            # 1. Apply the type extracted from (T) tag in docstrings
            _ = self.get_doc()
            if self.options.get('__my_parsed_type'):
                self.annotation = self.options['__my_parsed_type']

            # 2. Generate standard header (Name : Type)
            super().add_directive_header(sig)

            # 3. Add Value/Color information
            if not self.options.get('show-value', True):
                return

            is_color_name = 'Color' in self.objpath[-1]
            is_int_type = isinstance(self.object, int)
            
            try:
                # Skip internal Python objects
                if (self.object is sphinx.ext.autodoc.INSTANCEATTR or 
                (repr(self.object).startswith("<") and " object at " in repr(self.object))):
                    return
            except Exception:
                pass

            self.add_line('', self.get_sourcename())

            # If it looks like a color and is an integer, render the color swatch
            if is_color_name and is_int_type:
                try:
                    val = int(self.object)
                    # Convert int to Hex (AARRGGBB format)
                    hex_code = f"#{val & 0xFFFFFFFF:08X}"
                    self.add_line(f'   :value: :color:`{hex_code}`', self.get_sourcename())
                except Exception:
                    pass

    def add_content(self, more_content, no_docstring=False):
        if not self.options.get('show-value', True):
            super().add_content(more_content)
            return
        
        super().add_content(more_content)


def copy_doxygen_assets(app, exception):
    """
    Post-build hook: Copies external Doxygen tutorials/assets to the output directory.
    """
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
    """
    Sphinx setup entry point. Connects events and registers custom roles/documenters.
    """
    app.connect('build-finished', copy_doxygen_assets)
    app.connect('autodoc-skip-member', skip_undocumented_members)
    app.connect('autodoc-process-docstring', autodoc_process_docstring)
    app.connect('autodoc-process-signature', autodoc_process_signature)
    app.add_role("color", color_swatch_role)
    app.add_autodocumenter(CoatDocumenter)