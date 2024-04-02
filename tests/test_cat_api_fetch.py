from src.cat_api import CatAPI

def test_cat_api_fetch_data_w_mock(mocker):
    """
    Function to test fatching data from Cat API with mocking
    :return: None
    """
    mocker.patch('src.cat_api.CatAPI.fetch_api_data', return_value="False data from API")
    assert CatAPI.fetch_api_data(" https://http.cat/101") == "False data from API"

def test_cat_api_fetch_data_w_stubbing(mocker):
    """
    Function to test fatching data from Cat API with stubing
    :return: None
    """
    fetch_api_data_stub = mocker.stub(name='fetch_api_data_stubing')
    fetch_api_data_stub.return_value = "False data from API"
    assert fetch_api_data_stub(" https://http.cat/101") == "False data from API"

def test_cat_api_fetch_data_w_monkeypatch(monkeypatch):
    """
    Function to test fatching data from Cat API with Monkeypatch
    :return: None
    """
    def mock_return(value):
        return "False data from API"
    
    monkeypatch.setattr(CatAPI, "fetch_api_data", mock_return)
    assert CatAPI.fetch_api_data(" https://http.cat/101") == "False data from API"