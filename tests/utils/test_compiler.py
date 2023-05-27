import pytest
from altair import vegalite_compilers, Chart


@pytest.fixture
def chart():
    return (
        Chart("cars.json")
        .mark_point()
        .encode(
            x="Horsepower:Q",
            y="Miles_per_Gallon:Q",
        )
    )


def assert_is_vega_spec(vega_spec):
    assert vega_spec["$schema"] == "https://vega.github.io/schema/vega/v5.json"
    assert "data" in vega_spec
    assert "marks" in vega_spec
    assert "scales" in vega_spec
    assert "axes" in vega_spec


def test_vegalite_compiler(chart):
    vegalite_spec = chart.to_dict()
    vega_spec = vegalite_compilers.get()(vegalite_spec)
    assert_is_vega_spec(vega_spec)


def test_to_vega(chart):
    vega_spec = chart.to_vega()
    assert_is_vega_spec(vega_spec)
