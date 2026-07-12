import inspect
import os
import sys
import shutil
from pathlib import Path
import ast 
import cPy
import keyword
import builtins
import enchant
d_en_US = enchant.Dict("en_US")
# --- 1. Import Sphinx functions and check dependencies ---
try:
    from sphinx.cmd.build import main as sphinx_build_main
    from sphinx.ext.apidoc import main as sphinx_apidoc_main
    import pydata_sphinx_theme
except ImportError:
    print("❌ ERROR: Required packages are not installed.", file=sys.stderr)
    print("Please install them manually before running this script:", file=sys.stderr)
    print("\npip install sphinx pydata-sphinx-theme sphinx-gallery\n", file=sys.stderr)
    sys.exit(1)



# --- 2. SETTINGS: Project Configuration ---

PROJECT_NAME = "3DCoat Python API"
AUTHOR_NAME = "3DCoat"
API_MODULE_NAME = "cPy"  # The name of the main API module directory

# --- End of settings ---

# --- Path Configuration ---
# 3DCoat uses a specific directory structure. We locate the PythonAPI folder relative to the install folder.
ROOT_DIR = Path(cPy.cCore.cExtension.getCoatInstallForder() + "/UserPrefs/PythonAPI")
DOCS_DIR = ROOT_DIR / "docs"
DOCS_SOURCE_DIR = DOCS_DIR / "source"
DOCS_BUILD_DIR = DOCS_DIR / "build"

# Directory containing core API modules (cPy, coat.py, CMD.py)
BRIDGE_DIR = ROOT_DIR / "Bridge" 

# Full path to the main API module (used for naming checks)
API_MODULE_PATH = BRIDGE_DIR / API_MODULE_NAME 

# Parent path for Standard Scripts. Added to sys.path so Sphinx can import cModules/cTemplates.
STD_SCRIPTS_PARENT_PATH = Path(cPy.cCore.cExtension.getCoatInstallForder() + "/UserPrefs/StdScripts")

# The specific packages to scan for documentation
CMODULES_PATH = STD_SCRIPTS_PARENT_PATH / "cModules"
CTEMPLATES_PATH = STD_SCRIPTS_PARENT_PATH / "cTemplates"

# --- POST-PROCESSING AUTOLINKER ---
try:
    from bs4 import BeautifulSoup
    from sphinx.util.inventory import InventoryFile
except ImportError:
    BeautifulSoup = None
    InventoryFile = None

# 1. Ключові слова мови (if, while, class...)
_keywords = set(keyword.kwlist)

# 2. Вбудовані імена (list, object, Exception...)
_builtins = set(dir(builtins))

# 3. Твій додатковий список загальних слів, які не є ключовими, 
# але часто зустрічаються і не повинні лінкуватись
_manual_common = {
    'list', 'dict', 'set', 'object', 'string', 'int', 'float', 'bool', 'type', 'create', 'in', 'uv',
    'file', 'sys', 'os', 'system', 'math', 'random', 'time', 'date', 'datetime',
    'io', 'open', 'close', 'read', 'write', 'path', 'url', 'uri', 'http',
    'server', 'client', 'user', 'data', 'value', 'key', 'item', 'element',
    'node', 'tree', 'graph', 'utils', 'core', 'bridge', 'cmd', 'coat',
    'context', 'manager', 'helper', 'base', 'root', 'main', 'test', 'debug',
    'info', 'error', 'warning', 'print', 'log', 'param', 'return', 'result',
    'none', 'true', 'false', 'class', 'def', 'func', 'function', 'method',
    'start', 'end', 'stop', 'run', 'execute', 'process', 'thread', 'task',
    'action', 'event', 'handler', 'listener', 'observer', 'state', 'mode',
    'vec', 'vector', 'mat', 'matrix', 'quat', 'quaternion', 'rect', 'bounds',
    'color', 'image', 'texture', 'material', 'mesh', 'model', 'scene', 'view',
    'camera', 'light', 'render', 'shader', 'window', 'screen', 'input', 'output', "settings", "dialog"
}

COAT_ALIASES = {
    "vec2", "vec3", "vec4", 
    "mat3", "mat4", 
    "rect", "quat", "rotation", "angles", "boundbox"
}

COMMON_ENGLISH_WORDS = _keywords | _builtins | _manual_common


def is_english_word(word):
    """Simple check if a word is in our common blocklist."""
    if word in COAT_ALIASES:
            return False
    
    return (word.lower() in COMMON_ENGLISH_WORDS) or (d_en_US.check(word) and word.islower())

# =============================================================================
#  FUNCTION: load_mappings
# =============================================================================
def load_mappings(inventory_path):
    """
    Завантажує objects.inv і будує мапу. Також додає ручні аліаси (vec3, mat4...).
    """
    mappings = {}
    
    if not os.path.exists(inventory_path):
        return mappings, []

    target_types = {
        'py:class', 'py:function', 'py:method', 'py:classmethod', 
        'py:staticmethod', 'py:attribute', 'py:module', 'py:data'
    }

    try:
        with open(inventory_path, 'rb') as f:
            inv = InventoryFile.load(f, '', os.path.join)

        for type_key, items in inv.items():
            if type_key not in target_types:
                continue
            
            obj_type = 'class' if 'class' in type_key else 'obj'

            for full_name, (project, version, url, display_name) in items.items():
                parts = full_name.split('.')
                
                # Генеруємо всі суфікси (a.b.c -> a.b.c, b.c, c)
                for i in range(len(parts)):
                    suffix = ".".join(parts[i:])
                    
                    if suffix not in mappings:
                        mappings[suffix] = {'url': url, 'type': obj_type, 'count': 0, 'full_names': set()}
                    
                    if url not in mappings[suffix].get('urls', []):
                         mappings[suffix]['count'] += 1
                         if 'urls' not in mappings[suffix]: mappings[suffix]['urls'] = []
                         mappings[suffix]['urls'].append(url)
                    
                    mappings[suffix]['full_names'].add(full_name)

    except Exception as e:
        print(f"Error parsing inventory: {e}")

    # --- BLOCK: INJECT MANUAL ALIASES ---
    # Мапа: Alias -> Real Full Name (як воно записано в документації)
    manual_aliases_map = {
        'vec2':      'cPy.cTypes.cVec2',
        'vec3':      'cPy.cTypes.cVec3',
        'vec4':      'cPy.cTypes.cVec4',
        'mat3':      'cPy.cTypes.cMat3',
        'mat4':      'cPy.cTypes.cMat4',
        'rect':      'cPy.cTypes.cRect',
        'quat':      'cPy.cTypes.cQuat',
        'rotation':  'cPy.cTypes.cRotation',
        'angles':    'cPy.cTypes.cAngles',
        'boundbox':  'cPy.cTypes.cBounds',
    }

    for alias, real_name in manual_aliases_map.items():
        # Шукаємо реальний об'єкт у вже завантажених мапінгах
        # Спочатку шукаємо повне ім'я
        target_data = mappings.get(real_name)
        
        # Якщо не знайшли по повному, спробуємо знайти по короткому (наприклад cVec3)
        if not target_data:
            short_name = real_name.split('.')[-1]
            target_data = mappings.get(short_name)

        if target_data:
            # Створюємо запис для аліаса
            # Force count=1, щоб система вважала це посилання однозначним і безпечним
            mappings[alias] = {
                'url': target_data['url'],
                'type': target_data['type'], 
                'count': 1, 
                'full_names': {real_name}
            }
        else:
            print(f"⚠️ Warning: Could not find target for alias '{alias}' -> '{real_name}'")

    # ------------------------------------

    unique_words = set()
    for key in mappings.keys():
        unique_words.add(key.split('.')[-1])
        
    sorted_regex_keys = sorted(list(unique_words), key=len, reverse=True)
    
    return mappings, sorted_regex_keys

# =============================================================================
#  FUNCTION: apply_autolinks
# =============================================================================
def apply_autolinks(html_content, mappings, sorted_keys, current_file_path, root_doc_dir):
    """
    Шукає слова, збирає їх у ланцюжки (chain), відкидає перший елемент ланцюжка
    і намагається знайти посилання.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    from bs4 import Comment, NavigableString
    import re

    # Regex для пошуку потенційних кінцевих ідентифікаторів
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, sorted_keys)) + r')\b')
    
    changed = False
    replacements_count = 0

    def get_full_chain(node, start_index):
        """
        Дивиться назад від знайденого слова і намагається зібрати повний шлях.
        Повертає список частин: ['cPy', 'cRender', 'RenderUtils', 'draw_text']
        """
        parts = []
        
        # 1. Отримуємо "сирий" текст перед словом
        raw_text_before = str(node)[:start_index]

        # --- FIX: Strict Whitespace Check ---
        # Якщо безпосередньо перед словом є пробіл (наприклад "end. Start"),
        # це кінець речення, а не код. Перериваємось.
        if raw_text_before and raw_text_before[-1].isspace():
            return []
        # ------------------------------------

        # Тепер можна безпечно видаляти пробіли для аналізу структури
        text_before = raw_text_before.rstrip()
        
        # Рухаємось назад
        max_steps = 20
        steps = 0
        
        # Стан: 0 = очікуємо крапку, 1 = очікуємо слово
        state = 0 
        
        curr_node = node
        
        # Якщо безпосередньо перед словом немає крапки, то ланцюжка немає (в межах цього вузла)
        # Хіба що крапка в попередньому вузлі.
        if text_before and not text_before.endswith('.'):
            return [] # Розрив
            
        if text_before.endswith('.'):
             state = 1 # Знайшли крапку, шукаємо слово
             # Можливо перед крапкою в цьому ж вузлі є слово
             remainder = text_before[:-1].strip()
             if remainder:
                 # Спрощена логіка: беремо останнє "слово"
                 last_word_match = re.search(r'([a-zA-Z0-9_]+)$', remainder)
                 if last_word_match:
                     parts.insert(0, last_word_match.group(1))
                     state = 0 # знову очікуємо крапку перед цим словом
                 else:
                     state = 1 # продовжуємо шукати в попередніх вузлах
        
        # Якщо text_before пустий, починаємо перевірку з попереднього siblings
        curr_sibling = curr_node.previous_sibling if not text_before else None

        while steps < max_steps and curr_sibling:
            text = ""
            if isinstance(curr_sibling, NavigableString):
                text = str(curr_sibling)
            elif hasattr(curr_sibling, 'get_text'):
                text = curr_sibling.get_text()
            
            # --- FIX: Whitespace between tags breaks chain ---
            if not text.strip():
                # Якщо нода містить тільки пробіли (наприклад \n між span),
                # ми вважаємо це розривом, бо валідний код "obj.method" 
                # в HTML зазвичай йде підряд без пробілів.
                # Якщо це "obj. method", це розрив.
                break 
            # -------------------------------------------------

            stripped = text.strip()
            
            # Логіка парсингу назад
            if state == 0: # Очікуємо крапку
                if stripped.endswith('.'):
                    state = 1
                    # Перевіряємо, чи є слово перед крапкою в цьому ж шматку
                    pre_dot = stripped[:-1].strip()
                    if pre_dot:
                        lw_match = re.search(r'([a-zA-Z0-9_]+)$', pre_dot)
                        if lw_match:
                            parts.insert(0, lw_match.group(1))
                            state = 0
                else:
                    break # Немає крапки -> кінець ланцюга
            
            elif state == 1: # Очікуємо слово
                # Може бути просто слово "MyClass" або "MyClass."
                if re.match(r'^[a-zA-Z0-9_]+$', stripped):
                    parts.insert(0, stripped)
                    state = 0
                elif stripped == '.':
                    pass # подвійна крапка? ігноруємо
                else:
                    break
            
            steps += 1
            curr_sibling = curr_sibling.previous_sibling

        return parts

    # --- MAIN LOOP ---
    for text_node in soup.find_all(string=True):
        if isinstance(text_node, Comment): continue
        parent = text_node.parent
        # Пропускаємо теги, де не можна робити лінки
        if parent.name in ['a', 'code', 'script', 'style', 'textarea', 'h1', 'h2', 'h3', 'h4']: continue
        if parent.find_parent('a'): continue
            
        text_str = str(text_node)
        if not text_str.strip(): continue
        
        matches = list(pattern.finditer(text_str))
        if not matches: continue
        
        new_text_parts = []
        last_idx = 0
        
        for match in matches:
            word = match.group(0)
            start_pos = match.start()
            
            # Додаємо текст до поточного слова
            new_text_parts.append(text_str[last_idx:start_pos])
            
            # 1. Збираємо повний ланцюжок: [ 'cPy', 'cRender', 'word' ]
            prefix_parts = get_full_chain(text_node, start_pos)
            full_chain = prefix_parts + [word]
            
            target_url = None
            
            # --- ЛОГІКА ВІДБОРУ ---
            
            search_key = ""
            
            if len(full_chain) > 1:
                # В ланцюжку є крапки (cPy.cRender.word)
                parts_to_search = full_chain[1:]
                
                if parts_to_search:
                    search_key = ".".join(parts_to_search)
                    if search_key in mappings:
                        data = mappings[search_key]
                        if data['count'] == 1:
                            target_url = data['url']
                else:
                    search_key = full_chain[-1] # word
                    if search_key in mappings:
                        data = mappings[search_key]
                        if data['count'] == 1:
                            if not is_english_word(search_key):
                                target_url = data['url']

            else:
                # Single Word
                search_key = word
                if search_key in mappings:
                    data = mappings[search_key]
                    if (data['count'] == 1 and 
                        data['type'] == 'class' and 
                        not is_english_word(search_key)):
                        
                        target_url = data['url']

            # ФОРМУВАННЯ HTML
            if target_url:
                if '#' in target_url:
                    base, anc = target_url.split('#')
                    path = os.path.join(root_doc_dir, base)
                    anch = '#' + anc
                else:
                    path = os.path.join(root_doc_dir, target_url)
                    anch = ''
                
                try:
                    rel = os.path.relpath(path, os.path.dirname(current_file_path))
                    href = rel.replace('\\', '/') + anch
                    new_text_parts.append(f'<a href="{href}" class="autolink" title="{search_key}">{word}</a>')
                    replacements_count += 1
                except ValueError:
                    new_text_parts.append(word)
            else:
                new_text_parts.append(word)
                
            last_idx = match.end()
            
        new_text_parts.append(text_str[last_idx:])
        
        if replacements_count > 0:
            frag = "".join(new_text_parts)
            if frag != text_str:
                text_node.replace_with(BeautifulSoup(frag, 'html.parser'))
                changed = True

    return str(soup) if changed else None, replacements_count

def run_autolinking():
    if BeautifulSoup is None:
        print("\n❌ ERROR: 'beautifulsoup4' is not installed! Autolinking skipped.")
        return

    print("\n🔗 Starting Post-Processing Auto-Linking (Strict Mode)...")
    
    html_dir = DOCS_BUILD_DIR / "html"
    inv_path = html_dir / "objects.inv"
    
    mappings, sorted_keys = load_mappings(inv_path)
    print(f"   Indexed {len(mappings)} unique path variations.")
    
    if not mappings:
        return

    count_files = 0
    total_links = 0
    
    for root, dirs, files in os.walk(html_dir):
        for file in files:
            if file.endswith(".html") and file not in ["genindex.html", "search.html", "py-modindex.html"]:
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    new_content, links_added = apply_autolinks(content, mappings, sorted_keys, file_path, str(html_dir))
                    
                    if new_content:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)
                        count_files += 1
                        total_links += links_added
                        print(f"   Linked: {file} ({links_added} links)", end='\r')
                        
                except Exception as e:
                    print(f"\n   ❌ Error processing {file}: {e}")

    print(f"\n✅ Auto-linking finished. Modified {count_files} files with {total_links} links.")

def setup_directories():
    """
    Cleans previous builds and ensures the target directory structure exists.
    """
    print(f"🧹 Cleaning and creating directory structure at {DOCS_DIR}...")
    
    if (DOCS_DIR / "build" / "html").exists():
        shutil.rmtree(DOCS_DIR / "build" / "html")
    if (DOCS_DIR / "source" / "api").exists():
        shutil.rmtree(DOCS_DIR / "source" / "api")

def create_index_rst():
    """
    Generates the main entry point (index.rst) for the documentation.
    """
    print(f"✍️  Generating {DOCS_SOURCE_DIR / 'index.rst'}...")
    
    index_content = f"""
Welcome to {PROJECT_NAME}'s documentation!
==================================================

.. toctree::
   :maxdepth: 2
   :caption: API Reference:
   
   api/modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    (DOCS_SOURCE_DIR / "index.rst").write_text(index_content, encoding='utf-8')


def cleanup_rst_files(directory, find_text, replace_text):
    """
    Iterates through generated .rst files and performs text replacement.
    Useful for removing namespace prefixes from titles (e.g., changing "Bridge.coat" to "coat").
    """
    if not os.path.exists(directory):
        print(f"ERROR: {directory} not found.")
        return

    file_count = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.rst'):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    if not lines:
                        continue

                    # Replace text in the title (first line)
                    first_line = lines[0]
                    if find_text in first_line:
                        lines[0] = first_line.replace(find_text, replace_text)
                        
                        # Fix the underline length to match the new title length
                        if len(lines) > 1:
                            underline_char = lines[1].strip()[0:1] 
                            if underline_char in ('=', '-', '`', ':', '.', "'", '"', '~', '^', '_', '*'):
                                new_title_len = len(lines[0].rstrip())
                                lines[1] = underline_char * new_title_len + '\n'

                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        
                        file_count += 1
                
                except Exception as e:
                    print(f"ERROR {file_path}: {e}")


def add_members_to_rst(directory):
    """
    Injects the ':members:' option into .rst files generated by sphinx-apidoc.
    This ensures all classes and functions are documented, not just the top-level module description.
    """
    print(f"\n--- 3. Adding :members: to RST files in {directory} ---")
    target_text = ":show-inheritance:"
    replacement_text = ":show-inheritance:\n   :members:" 
    file_count = 0

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.rst'):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    made_change = False
                    
                    if target_text in content and ":members:" not in content:
                        content = content.replace(target_text, replacement_text)
                        made_change = True
                        
                    if made_change:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        file_count += 1
                
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")
                    
    print(f"--- 3.1. Added :members: to {file_count} files. ---")

def run_sphinx_commands():
    """
    Orchestrates the Sphinx build process:
    1. Runs sphinx-apidoc on multiple directories.
    2. Filters out empty or undocumented modules.
    3. Groups modules logically for the Table of Contents.
    4. Runs sphinx-build to generate HTML.
    """
    
    print("🤖 Running sphinx-apidoc to scan API...")
    api_output_dir = DOCS_SOURCE_DIR / "api"
    
    # We run apidoc separately for each main directory to keep them distinct/clean
    
    # 1. Scan 'Bridge' (Core API: cPy, coat, CMD)
    apidoc_args_1 = [
        "-o", str(api_output_dir),
        str(API_MODULE_PATH), 
        "--force",
        "--separate",
        "--no-toc",
    ]
        
    # 2. Scan 'cModules' (Standard 3DCoat Scripts)
    apidoc_args_2 = [
        "-o", str(api_output_dir),
        str(CMODULES_PATH), 
        "--force",
        "--separate",
        "--no-toc",
    ]
    
    # 3. Scan 'cTemplates' (Template System)
    apidoc_args_3 = [
        "-o", str(api_output_dir),
        str(CTEMPLATES_PATH), 
        "--force",
        "--separate",
        "--no-toc",
    ]
    
    try:
        print(f"--- Scanning {API_MODULE_PATH}...")
        sphinx_apidoc_main(apidoc_args_1)        
        
        print(f"--- Scanning {CMODULES_PATH}...")
        sphinx_apidoc_main(apidoc_args_2)

        print(f"--- Scanning {CTEMPLATES_PATH}...")
        sphinx_apidoc_main(apidoc_args_3)
        
    except Exception as e:
        print(f"❌ ERROR during sphinx-apidoc: {e}", file=sys.stderr)
        sys.exit(1)

    # --- Filtering Logic ---
    # Analyze generated RST files and check the actual Python source.
    # We skip modules that have no docstrings, classes, functions, or __all__ definitions.
    
    all_rst_stems = sorted([f.stem for f in api_output_dir.glob("*.rst") if f.name != "modules.rst"])
    documented_modules = []

    print(f"🔍 Analyzing {len(all_rst_stems)} found modules for documentation...")

    for stem in all_rst_stems:
        source_file_path = None
        module_path_parts = stem.split('.')
        
        # Determine the base path for the module
        if module_path_parts[0] == API_MODULE_NAME: # "Bridge"
            base_path = API_MODULE_PATH
            relative_path_parts = module_path_parts[1:]
        elif module_path_parts[0] == CMODULES_PATH.name: # "cModules"
            base_path = CMODULES_PATH
            relative_path_parts = module_path_parts[1:]
        elif module_path_parts[0] == CTEMPLATES_PATH.name: # "cTemplates"
            base_path = CTEMPLATES_PATH
            relative_path_parts = module_path_parts[1:]
        else:
            # Files in the root of /StdScripts
            base_path = STD_SCRIPTS_PARENT_PATH
            relative_path_parts = module_path_parts

        # Locate the corresponding .py or __init__.py file
        if not relative_path_parts: 
            test_path_init = base_path / '__init__.py'
            if test_path_init.exists():
                source_file_path = test_path_init
            else:
                test_path_py = base_path.with_suffix('.py')
                if test_path_py.exists():
                    source_file_path = test_path_py
        else: 
            test_path_py = base_path / Path(*relative_path_parts).with_suffix('.py')
            test_path_init = base_path / Path(*relative_path_parts) / '__init__.py'
            
            if test_path_py.exists():
                source_file_path = test_path_py
            elif test_path_init.exists():
                source_file_path = test_path_init

        # Verify content exists using AST parsing
        is_documented = False
        if source_file_path and source_file_path.exists():
            try:
                content = source_file_path.read_text(encoding='utf-8')
                if not content.strip(): 
                    is_documented = False
                else:
                    tree = ast.parse(content)
                    module_docstring = ast.get_docstring(tree)
                    
                    if module_docstring and module_docstring.strip():
                        # 1. Module has a docstring
                        is_documented = True
                    else:
                        for node in tree.body:
                            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                                # 2. Module has functions or classes
                                is_documented = True
                                break
                            if isinstance(node, ast.Assign):
                                for target in node.targets:
                                    if isinstance(target, ast.Name) and target.id == '__all__':
                                        # 3. Module defines __all__ exports
                                        is_documented = True
                                        break
                                if is_documented: break
            except Exception as e:
                print(f"  [Warning] Could not parse {source_file_path}. Including it. Error: {e}")
                is_documented = True 
        else:
            # Include if it's likely a C++ module (no .py source) or specific key files
            if stem not in ("modules"):
                is_documented = True 

        if is_documented:
            documented_modules.append(stem)
        else:
            print(f"  -> Skipping {stem} (no docstring, functions, classes, or __all__ found)")

    print(f"✍️  Generating main API file with {len(documented_modules)} modules: {api_output_dir / 'modules.rst'}...")

    # --- Grouping Modules for Table of Contents ---
    
    BRIDGE_PACKAGE_NAME = API_MODULE_PATH.name 
    
    # Group 1: Core API (Bridge)
    cpy_modules = sorted([m for m in documented_modules if 
                              m.startswith(f"{BRIDGE_PACKAGE_NAME}.") or 
                              m == BRIDGE_PACKAGE_NAME
                             ])
    
    # Group 2: cModules
    cmodules_modules = sorted([m for m in documented_modules if m.startswith(f"{CMODULES_PATH.name}.") or m == CMODULES_PATH.name])

    # Group 3: cTemplates
    ctemplates_modules = sorted([m for m in documented_modules if m.startswith(f"{CTEMPLATES_PATH.name}.") or m == CTEMPLATES_PATH.name])
    
    # Group 4: Others (Miscellaneous scripts)
    all_grouped_modules = set(cpy_modules) | set(cmodules_modules) | set(ctemplates_modules)
    other_modules = sorted([m for m in documented_modules if m not in all_grouped_modules])

    # --- Generate modules.rst content ---
    modules_content = "API Modules\n=========\n\n"

    if not documented_modules:
        modules_content += "(No documented modules found.)"
    else:
        if cpy_modules:
            modules_content += ".. toctree::\n   :maxdepth: 4\n   :caption: cPy API (Bridge)\n\n"
            for module in cpy_modules:
                modules_content += f"   {module}\n"
            modules_content += "\n"

        if cmodules_modules:
            modules_content += ".. toctree::\n   :maxdepth: 4\n   :caption: cModules API\n\n"
            for module in cmodules_modules:
                modules_content += f"   {module}\n"
            modules_content += "\n"

        if ctemplates_modules:
            modules_content += ".. toctree::\n   :maxdepth: 4\n   :caption: cTemplates API\n\n"
            for module in ctemplates_modules:
                modules_content += f"   {module}\n"
            modules_content += "\n"
            
        if other_modules:
            modules_content += ".. toctree::\n   :maxdepth: 4\n   :caption: Other Modules\n\n"
            for module in other_modules:
                modules_content += f"   {module}\n"
            modules_content += "\n"
    
    (api_output_dir / "modules.rst").write_text(modules_content, encoding='utf-8')
    
    # Post-processing generated RST files
    add_members_to_rst(api_output_dir)
  
    # Clean up artifacts in titles (e.g. remove 'Bridge.' prefix)
    cleanup_rst_files(DOCS_DIR / "source" / "api", "Bridge.", "")
    cleanup_rst_files(DOCS_DIR / "source" / "api", "coat.", "")
    
    # --- Execute Sphinx Build ---
    print("🛠️  Running sphinx-build to generate HTML...")
    html_output_dir = DOCS_BUILD_DIR / "html"
    
    SCRIPT_DIR = Path(__file__).resolve().parent

    # Point to the conf.py in the same directory as this script
    conf_path = SCRIPT_DIR / "conf.py"

    build_args = [
        "-b", "html",
        "-c", str(SCRIPT_DIR),
        str(DOCS_SOURCE_DIR),
        str(html_output_dir)
    ]
    
    return_code = sphinx_build_main(build_args)
    
    if return_code != 0:
        print(f"❌ Sphinx build failed with exit code {return_code}", file=sys.stderr)
        sys.exit(return_code)
        
def main():
    """Main script execution function."""
    print(f"--- Starting documentation build for {PROJECT_NAME} (Native Python) ---")
    
    setup_directories()

    # create_index_rst() # Optional: Uncomment to regenerate index.rst
    
    run_sphinx_commands()
    
    run_autolinking()
    
    final_path = (DOCS_BUILD_DIR / "html" / "index.html").resolve()
    print("\n" + "="*50)
    print("🎉 DOCUMENTATION BUILT SUCCESSFULLY! 🎉")
    print(f"Open this file in your browser:\nfile://{final_path}")
    print("="*50)
