from pathlib import Path
from typing import Callable
import click

from rim4py.definject import DefInjectedFile

# def check(msg: str, test: Callable[[DefInjectedFile,DefInjectedFile], bool]) -> None:
#     click.secho(msg+'...')
#     assert test()
#     click.secho(' OK!', fg='green')

ourdefs = DefInjectedFile()
for path in (Path('1.4') / 'Languages' / 'English' / 'DefInjected').rglob('*.xml'):
    print(path)
    d = DefInjectedFile.FromFile(path)
    ourdefs.defs.update(d.defs)
theirdefs = DefInjectedFile.FromFile(Path('Source') / 'data' / '1.4' / 'Languages' / 'English' / 'DefInjected' / 'all.xml')

allkeys = sorted(set(ourdefs.keyset()) | set(theirdefs.keyset()))
new_to_us = set(theirdefs.keyset()) - set(ourdefs.keyset())
missing_in_theirs = set(ourdefs.keyset()) - set(theirdefs.keyset())

REPORT_PATH = Path('report.diff')
with REPORT_PATH.open('w') as f:
    for k in allkeys:
        if k in new_to_us:
            click.secho(f'+ {k}', fg='green')
            f.write(f'+ {k}\n')
        if k in missing_in_theirs:
            click.secho(f'- {k}', fg='red')
            f.write(f'- {k}\n')