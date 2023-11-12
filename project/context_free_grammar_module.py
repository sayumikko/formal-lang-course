from pyformlang.cfg import CFG


def get_cfg_from_file(path):
    file = open(path)
    return CFG.from_text(file.read())


def build_weak_chomsky_normal_form(cfg: CFG):
    new_cfg = cfg.eliminate_unit_productions().remove_useless_symbols()
    new_productions = new_cfg._get_productions_with_only_single_terminals()
    new_productions = new_cfg._decompose_productions(new_productions)
    return CFG(start_symbol=new_cfg.start_symbol, productions=set(new_productions))
