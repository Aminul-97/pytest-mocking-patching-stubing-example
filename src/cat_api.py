import requests

class CatAPI:
    """
    Class for CatAPI 
    """
    def check_api_connection(link:str):
        """
        Function to check API connection

        Args:
        link: Link as string

        Returns:
        status_code: Connection status code 
        """
        status = requests.get(link).status_code
        return status

    def fetch_api_data(link:str):
        """
        Function to fetch API data

        Args:
        link: Link as string

        Returns:
        fetched link data.
        """
        return requests.get(link).content

def main(link:str):
    print(f"Link status: {CatAPI.check_api_connection(link)}")
    print(f"Data:\n {CatAPI.fetch_api_data(link)}")

if __name__ == "__main__":
    main("https://http.cat/101")