from random import sample
import pytest
from src.semgrep.exclude_rules import filter_exclude_rule
from src.semgrep.config_resolver import get_config

MAX_RULES_TO_EXCLUDE = 10


@pytest.mark.quick
def test_parse_exclude_rules_auto() -> None:
    configs_obj, _ = get_config(pattern=None,
                                lang=None,
                                config_strs=("auto",),
                                project_url="git@github.com/returntocorp/semgrep")
    all_rules = configs_obj.get_rules(False)
    rule_excluded = list(
        map(lambda r: r.id, sample(all_rules, MAX_RULES_TO_EXCLUDE)))

    all_rules = filter_exclude_rule(all_rules, rule_excluded)

    assert len(set(all_rules) & set(rule_excluded)) == 0
