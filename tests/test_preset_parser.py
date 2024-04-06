from arma_server_tools.preset_parser import clean


def test_clean() -> None:
    """
    Removes spaces and symbols:

    [] () ! . - _ / ' " :
    """
    name = " Space [Brackets] (Parens) Bang! Period. Dash- UScore_ Slash/ SQuote' DQuote\" Colon: SColon;"
    expected = "SpaceBracketsParensBangPeriodDashUScoreSlashSQuoteDQuoteColonSColon"
    result = clean(name)
    assert result == expected
