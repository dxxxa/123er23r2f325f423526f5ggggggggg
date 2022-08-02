# -*- coding: UTF-8 -*-
from pathlib import Path

directory = Path(r'C:\Users\nUser\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04LTS_79rhkp1fndgsc\LocalState\rootfs\home\BreachCompilation_Last\data')
line_count = 0

for f in directory.rglob('*.txt'):
    if not f.is_file() or not f.exists():
        continue

    local_count = 0
    for line in f.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith(('#', '"', "'")):
            continue
        local_count += 1

    print(f'{f} - {local_count} ст')
    line_count += local_count

print("=====================================")
print(f"Всего строк - {line_count}")
