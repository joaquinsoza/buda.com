# Buda simple Script
Script that uses the [Buda.com](https://www.buda.com) API to get the transaction with the highest value for each market in the last 24 hours

## Usage
Python --version = 3.8.10

Install pip requirements
```bash
pip install requests
pip install tabulate
```

Change the **config.json** file to add your API_KEY and SECRET
```json
{
  "API_KEY": "your API_KEY",
  "SECRET": "your SECRET"
}

```

To run simple just run the python script
```bash
python buda.py
```

## Comments (Español)
En la documentacion de [Buda.com](https://api.buda.com/#introduccion) dice que estas llamadas son publicas por las que no deberia necesitar Auth, pero al hacer pruebas el unico endpoint que responde status(200) es el [siguiente](https://www.buda.com/api/v2/markets/btc-clp/ticker) el resto responden con status(503) por lo que intente hacer estas llamadas con Auth y funciono... pero la documentación dice que no deberia ser necesario estar autenticado para esta información.
