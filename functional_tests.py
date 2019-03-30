from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# Usamos para verificar se existe a palavra django no titulo do site
# Caso exista, não vamos receber mensagens do assert
assert 'Django' in browser.title