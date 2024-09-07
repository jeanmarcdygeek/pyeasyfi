import requests
import bs4
import pickle as pkl



def get_top_n_cryptos(n=3,save_file : str = None):
    data = requests.get("https://crypto.com/price")
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    top50_elements = soup.find_all('span', class_="chakra-text css-1jj7b1a")
    cryptos = [x.text for x in top50_elements]
    if save_file is not None:
        pkl.dump(cryptos[:n], open(save_file, "wb"))
    
    return cryptos[:n]