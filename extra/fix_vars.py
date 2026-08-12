import sys

def fix_file(f, replacements):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    for o, n in replacements:
        content = content.replace(o, n)
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

fix_file('main.py', [
    ('SATAN echo = SATANLive(', 'SATAN_echo = SATANLive('),
    ('SATAN echo.plugin_manager', 'SATAN_echo.plugin_manager'),
    ('plugin_manager.register_SATAN(SATAN echo)', 'plugin_manager.register_SATAN(SATAN_echo)'),
    ('plugin_manager.dispatch("on_startup", SATAN echo)', 'plugin_manager.dispatch("on_startup", SATAN_echo)'),
    ('asyncio.run(SATAN echo.run())', 'asyncio.run(SATAN_echo.run())')
])

fix_file('plugin_manager.py', [
    ('self.SATAN echo', 'self.SATAN_echo'),
    ('SATAN echo=self.SATAN_echo', 'SATAN_echo=self.SATAN_echo')
])

print('Fixes applied!')
