from pathlib import Path
from typing import FrozenSet

from rim4py.definject import DefInjectedFile
POSSIBLE_VERSIONS: FrozenSet[str] = frozenset({
    '1.4',
    '1.3',
    '1.2',
    '1.1'
})
def existingDirPath(s: str) -> Path:
    if not (p := Path(s)).is_dir():
        raise Exception(f'{s} is not a directory.')
    return p

def main():
    import argparse

    argp = argparse.ArgumentParser()
    argp.add_argument('--from-mod', type=existingDirPath)
    argp.add_argument('--to-dir', type=Path)
    argp.add_argument('--lang', type=str, default='English')

    args = argp.parse_args()
    
    dif = DefInjectedFile()
    all_defs = []
    all_defs += list((args.from_mod / '1.4' / 'Defs').rglob('*.xml'))
    all_defs += list((args.from_mod / 'Defs').rglob('*.xml'))
    for defpath in all_defs:
        print(f'Parsing {defpath}...')
        ndif = DefInjectedFile.FromDef(defpath)
        dif.defs.update(ndif.defs)
    dif.save(args.to_dir / '1.4' / 'Languages' / args.lang / 'DefInjected' / 'all.xml', verbose=True)

if __name__ == '__main__':
    main()