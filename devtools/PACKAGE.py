from bz2 import compress
import os
from pathlib import Path
import shutil
import zipfile
from buildtools.maestro import BuildMaestro
from buildtools.maestro.fileio import CopyFileTarget, CopyFilesTarget

DIST_DIR = Path('dist')
ABOUT_DIR = Path('About')

VER_DIR = Path('1.4')
DEFINJECTED_DIR  = VER_DIR / 'Languages' / 'English' / 'DefInjected'


bm = BuildMaestro()
bm.add(CopyFileTarget(str(DIST_DIR / 'README.md'), str(Path('README.md'))))
bm.add(CopyFileTarget(str(DIST_DIR / 'LICENSE'), str(Path('LICENSE'))))
bm.add(CopyFileTarget(str(DIST_DIR / 'About' / 'About.xml'), str(ABOUT_DIR / 'About.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / 'About' / 'Preview.png'), str(ABOUT_DIR / 'Preview.png')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'AlienRace.BackstoryDef' / 'Backstory.xml'), str(DEFINJECTED_DIR / 'AlienRace.BackstoryDef' / 'Backstory.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'AlienRace.ThingDef_AlienRace' / 'Race_WAE.xml'), str(DEFINJECTED_DIR / 'AlienRace.ThingDef_AlienRace' / 'Race_WAE.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'AlienRace.ThingDef_AlienRace' / 'Race_WHE.xml'), str(DEFINJECTED_DIR / 'AlienRace.ThingDef_AlienRace' / 'Race_WHE.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'BodyDef' / 'Body.xml'), str(DEFINJECTED_DIR / 'BodyDef' / 'Body.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'CultureDef' / 'FuctionCultures.xml'), str(DEFINJECTED_DIR / 'CultureDef' / 'FuctionCultures.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'FactionDef' / 'Factions_NPC.xml'), str(DEFINJECTED_DIR / 'FactionDef' / 'Factions_NPC.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'PawnKindDef' / 'PawnKinds.xml'), str(DEFINJECTED_DIR / 'PawnKindDef' / 'PawnKinds.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'RecipeDef' / 'Recipes_Add_Make.xml'), str(DEFINJECTED_DIR / 'RecipeDef' / 'Recipes_Add_Make.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ResearchProjectDef' / 'ResearchProjects.xml'), str(DEFINJECTED_DIR / 'ResearchProjectDef' / 'ResearchProjects.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ResearchTabDef' / 'ResearchProjects.xml'), str(DEFINJECTED_DIR / 'ResearchTabDef' / 'ResearchProjects.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ScenarioDef' / 'Scenario.xml'), str(DEFINJECTED_DIR / 'ScenarioDef' / 'Scenario.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'StyleItemCategoryDef' / 'Hairs.xml'), str(DEFINJECTED_DIR / 'StyleItemCategoryDef' / 'Hairs.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingCategoryDef' / 'Apparel_UnderMiddle.xml'), str(DEFINJECTED_DIR / 'ThingCategoryDef' / 'Apparel_UnderMiddle.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingDef' / 'Apparel_Backpack.xml'), str(DEFINJECTED_DIR / 'ThingDef' / 'Apparel_Backpack.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingDef' / 'Apparel_Coat.xml'), str(DEFINJECTED_DIR / 'ThingDef' / 'Apparel_Coat.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingDef' / 'Apparel_Neck.xml'), str(DEFINJECTED_DIR / 'ThingDef' / 'Apparel_Neck.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingDef' / 'Apparel_OnSkin.xml'), str(DEFINJECTED_DIR / 'ThingDef' / 'Apparel_OnSkin.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingDef' / 'Apparel_OverHead.xml'), str(DEFINJECTED_DIR / 'ThingDef' / 'Apparel_OverHead.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingDef' / 'Apparel_Shell.xml'), str(DEFINJECTED_DIR / 'ThingDef' / 'Apparel_Shell.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingDef' / 'Weapon_Melee.xml'), str(DEFINJECTED_DIR / 'ThingDef' / 'Weapon_Melee.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingDef' / 'Weapons_Ranged.xml'), str(DEFINJECTED_DIR / 'ThingDef' / 'Weapons_Ranged.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingDef' / 'Weapons_WAE_Ranged.xml'), str(DEFINJECTED_DIR / 'ThingDef' / 'Weapons_WAE_Ranged.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingDef' / 'Weapons_WHE_Ranged.xml'), str(DEFINJECTED_DIR / 'ThingDef' / 'Weapons_WHE_Ranged.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'ThingDef' / 'Weapons_WHEAT_Ranged.xml'), str(DEFINJECTED_DIR / 'ThingDef' / 'Weapons_WHEAT_Ranged.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'TraderKindDef' / 'TraderKinds_Caravan.xml'), str(DEFINJECTED_DIR / 'TraderKindDef' / 'TraderKinds_Caravan.xml')))
bm.add(CopyFileTarget(str(DIST_DIR / DEFINJECTED_DIR / 'TraitDef' / 'Traits_WeebElf.xml'), str(DEFINJECTED_DIR / 'TraitDef' / 'Traits_WeebElf.xml')))
argp = bm.build_argparser()
def existingDirPath(inp: str) -> Path:
    p = Path(inp)
    if p.is_dir():
        return p
    raise Exception(f'Directory {p} does not exist.')

argp.add_argument('--deploy-to', type=Path, default=None, help="Rimworld local Mods directory.")
args = argp.parse_args()
bm.as_app(argp)

print('Writing Ancient_Species_in_English.zip')
total_bytes = 0
with zipfile.ZipFile('Ancient_Species_in_English.zip', 'w', compression=zipfile.ZIP_LZMA) as z:
    for path in DIST_DIR.rglob('*'):
        if path.is_file():
            arcpath = Path('Ancient Species in English') / path.relative_to(DIST_DIR)
            sz = os.path.getsize(path)
            print(f' Compressing {arcpath} ({sz}B)...')
            z.write(filename=path, arcname=arcpath)
            total_bytes += sz
zipsz = os.path.getsize('Ancient_Species_in_English.zip')
print(f'Done. {total_bytes}B -> {zipsz}B ({100-round((zipsz/total_bytes)*100)}%)')

if args.deploy_to is not None:
    if (args.deploy_to / 'Ancient Species in English').is_dir():
        shutil.rmtree(args.deploy_to / 'Ancient Species in English')
    for path in DIST_DIR.rglob('*'):
        if not path.is_file():
            continue
        outpath: Path = args.deploy_to / 'Ancient Species in English' / (path.relative_to(DIST_DIR))
        outpath.parent.mkdir(parents=True, exist_ok=True)
        print(str(path), '->', str(outpath))
        shutil.copy(path,outpath)