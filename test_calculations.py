from calculations import winning_per_nationality, get_active_drivers
import pytest


def test_get_active_drivers():
    file_path = (
        "first_20_F1DriversDataSet.csv"  # replace with the actual path to your dataset
    )
    expected_num_active_drivers = (
        2  # replace with the actual number of active drivers in your dataset
    )
    assert get_active_drivers(file_path) == expected_num_active_drivers


@pytest.mark.parametrize(
    "nation, win_ratio_expected, podium_ratio_expected",
    [("Spain", 16.0, 49.5), ("Belgium", 0.0, 0.0), ("United States", 0, 1 / 3)],
    ids=["Spain", "Belgium", "United States"],
)
def test_win_ratio(nation, win_ratio_expected, podium_ratio_expected):

    test_data_path = "first_20_F1DriversDataset.csv"
    win_ratio, podium_ratio = winning_per_nationality(test_data_path)
    assert (
        win_ratio[nation] == win_ratio_expected
    ), f"expected: {win_ratio_expected}, got: {win_ratio[nation]}"
    assert (
        podium_ratio[nation] == podium_ratio_expected
    ), f"expected: {podium_ratio_expected}, got: {podium_ratio[nation]}"
