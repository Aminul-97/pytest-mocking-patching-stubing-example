from src.cat_api import CatAPI

def test_cat_api_connection_w_mock(mocker):
    """
    Function to test Cat API connection with mocking
    :return: None
    """
    mocker.patch('src.cat_api.CatAPI.check_api_connection', return_value=401)
    assert CatAPI.check_api_connection(" https://http.cat/101") == 401

def test_cat_api_connection_w_stubbing(mocker):
    """
    Function to test Cat API connection with stubing
    :return: None
    """
    check_api_connection_stub = mocker.stub(name='check_api_connection_stubing')
    check_api_connection_stub.return_value = 401
    assert check_api_connection_stub(" https://http.cat/101") == 401

def test_cat_api_connection_w_monkeypatch(monkeypatch):
    """
    Function to test Cat API connection with Monkeypatch
    :return: None
    """
    def mock_return(value):
        return 401
    
    monkeypatch.setattr(CatAPI, "check_api_connection", mock_return)
    assert CatAPI.check_api_connection(" https://http.cat/101") == 401
