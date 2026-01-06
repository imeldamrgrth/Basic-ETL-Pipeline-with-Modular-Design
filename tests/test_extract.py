from utils.extract import scrape_main

def test_scrape_main():
    data = scrape_main(1)
    assert isinstance(data, list)
    assert len(data) > 0
    first = data[0]
    assert "Title" in first
    assert "Price" in first
    assert "Rating" in first
