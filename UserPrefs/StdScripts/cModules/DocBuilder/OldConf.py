
# conf.py
import os
import sys
import coat_type_aliases
import sphinx.ext.autodoc
from docutils import nodes
import re
import shutil
from pathlib import Path

# --- MODIFIED: Add module paths for Sphinx autodoc ---
# Це критично важливо, щоб Sphinx міг імпортувати ваші модулі
sys.path.insert(0, r"D:/3dcoat/ProjectsData/3d-coat-data-2020/UserPrefs/PythonAPI")
sys.path.insert(0, r"D:/3dcoat/ProjectsData/3d-coat-data-2020/UserPrefs/StdScripts")
# --- END MODIFIED ---

def get_version():
    return "1.0.0"

    
# autosummary_generate = True

# -- Project information -----------------------------------------------------
project = '3DCoat Python API'
copyright = '2025, 3DCoat'
author = '3DCoat'
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
    "Coat_CPP"
]

autodoc_default_options = {
    'undoc-members': True, 
    'show-inheritance': True,
    'show-value': True,
    'imported-members': True,
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

    return True

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
    # --- FIX: Витягуємо опис з об'єкта, якщо Sphinx вважає його змінною ---
    # Якщо lines пустий (Sphinx не знайшов коментарів), а об'єкт має __doc__
    if not lines and hasattr(obj, '__doc__') and isinstance(obj.__doc__, str) and obj.__doc__.strip():
        # Перевіряємо, чи це не стандартний опис класу (щоб не дублювати опис типу для звичайних змінних)
        if obj.__doc__ != type(obj).__doc__:
            from sphinx.util.docstrings import prepare_docstring
            # Додаємо знайдений опис у lines, форматуючи його для Sphinx
            lines.extend(prepare_docstring(obj.__doc__))
    # ---------------------------------------------------------------------
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

    # Now, clean EVERY docstring line of "Coat_CPP."
    if lines:
        for i in range(len(lines)):
            lines[i] = re.sub(r'\bCoat_CPP\.', '', lines[i])

def autodoc_process_signature(app, what, name, obj, options, signature, return_annotation):
    
    # Set initial values
    sig_tuple = (signature, return_annotation)

    if options.get('__my_parsed_type'):
        parsed_type = options.pop('__my_parsed_type')
        
        if signature is None:
            signature = name
        
        original_sig = signature
        value_part = ""
        
        if ' = ' in original_sig:
            parts = original_sig.split(' = ', 1)
            attr_name = parts[0].strip()
            value_part = " = " + parts[1].strip()
        else:
            attr_name = original_sig.strip()
        
        if value_part.startswith(" = <object"):
            value_part = ""
        
        if ' : object' in attr_name:
            attr_name = attr_name.split(' : object', 1)[0].strip()

        new_signature = f"{attr_name} : {parsed_type}{value_part}"
        sig_tuple = (new_signature, None) # Set new signature
            
    else:
        options.pop('__my_parsed_type', None)

    # Now, clean the final signature and return annotation
    final_sig, final_ret = sig_tuple
    
    if final_sig:
        final_sig = re.sub(r'\bCoat_CPP\.', '', final_sig)
    if final_ret:
        final_ret = re.sub(r'\bCoat_CPP\.', '', final_ret)
        
    return (final_sig, final_ret)


class ColorAttributeDocumenter(sphinx.ext.autodoc.AttributeDocumenter):
    priority = 11

    # (No longer needed, 'autodoc_mock_imports' will fix everything)

    # (This is needed to return values and colors)
    def add_directive_header(self, sig: str) -> None:
        super(sphinx.ext.autodoc.AttributeDocumenter, self).add_directive_header(sig)

        if not self.options.get('show-value', True):
            return
            
        try:
            if (self.object is sphinx.ext.autodoc.INSTANCEATTR or 
               (repr(self.object).startswith("<") and " object at " in repr(self.object))):
                return
        except Exception:
            pass

        is_color_name = 'Color' in self.objpath[-1]
        is_int_type = isinstance(self.object, int)

        self.add_line('', self.get_sourcename())

        if is_color_name and is_int_type:
            try:
                val = int(self.object)
                hex_code = f"#{val & 0xFFFFFFFF:08X}"
                self.add_line(f'   :value: :color:`{hex_code}`', self.get_sourcename())
            except Exception:
                val_repr = repr(self.object)
                val_repr = re.sub(r'\bCoat_CPP\.', '', val_repr)
                self.add_line('   :value: ' + val_repr, self.get_sourcename())
        else:
            val_repr = repr(self.object)
            val_repr = re.sub(r'\bCoat_CPP\.', '', val_repr)
            self.add_line('   :value: ' + val_repr, self.get_sourcename())

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
    app.add_autodocumenter(ColorAttributeDocumenter)
