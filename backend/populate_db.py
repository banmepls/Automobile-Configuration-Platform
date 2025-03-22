from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()


# client = MongoClient(os.getenv('MONGO_URI'))
client = MongoClient(
    host=os.getenv('MONGO_DOCKER'),
    authSource="admin"
)

db = client['automobile_db']
collection = db['automobiles']
print("Successfully connected to MongoDB.")


# collection.delete_many({})
# print("Successfully deleted all documents from the automobiles collection.")


automobiles = [
    {
        "manufacturer": "BMW",
        "model": "M2 Coupe",
        "full_name": "BMW M2 Coupe",
        "price": 73602,
        "fuel": "Gasoline",
        "chassis": "Coupe",
        "transmission": "Automatic",
        "engine": "3.0L",
        "power_kw": 353,
        "power_hp": 480,
        "acceleration": 4,
        "fuel_consumption": 9.7,
        "colors": {
            "Alpine_White": {
                "image": "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIGzmydptvX%25oKNHkJENmb4Ws86OG7c1QUD36kxbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v6%25yX3242NnTQdjcjqN3azDx4a7dnkq8cHEzOALUxnXkIFJG8OxABKupUP8FeWS6GbSKMPVYp9gWhbNmQtiPo90yWAIbHi4TPFo9%25wc3b%25eiftxd9fKw178zi1qtECUkwDo7slGAtqjCrXpF7LflZQ6KCHyXRaYWlItQ5nmPXJ2agOybQfanvIT9FvZO2B3iKHRIjedwW%252BDMztPuZeqhk7bIUMLoAC9BAhJHFlieCou%25KXsnDHSfWQry0%25V1PaZcMfNEbnRxT10s9O58dE4riIgkYscZwBvg7rxRte2yzZ857MjuvRUgChD2B5Gvloq3lgp2XH3ccv6jQ%25db22YDafDsZjmqn1qiCDyLOELA9qTJIsJZWL3uBruRQJdSeZS37uzVMRVbcSkNh5N9RVA0ogKLNNF4HvWBf0KEfIhH%25kTAusvgpVmlDTI0Ccy2oWimuzHJZ0uDShtD5eqKDsH%25fMA8OSr9%25UsDOPSE2VZ8XgY1nTNIowJ4HO3zkyXqcfbYGnHR",
                "cost": 0,
            },
            "Sao_Paulo_Yellow": {
                "image": "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIGzmydptvX%25oKNHkJENmb4Ws86OG7c1QUDCYLxbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v6%25yX3242NnTQdjcjqN3azDx4a7dnkq8cHEzOALUxnXkIFJG8OxABKupUP8FeWS6GbSKMPVYp9gWhbNmQtiPo90yWAIbHi4TPFo9%25wc3b%25eiftxd9fKw178zi1qtECUkwDo7slGAtqjCrXpF7LflZQ6KCHyXRaYWlItQ5nmPXJ2agOybQfanvIT9FvZO2B3iKHRIjedwW%252BDMztPuZeqhk7bIUMLoAC9BAhJHFlieCou%25KXsnDHSfWQry0%25V1PaZcMfNEbnRxT10s9O58dE4riIgkYscZwBvg7rxRte2yzZ857MjuvRUgChD2B5Gvloq3lgp2XH3ccv6jQ%25db22YDafDsZjmqn1qiCDyLOELA9qTJIsJZWL3uBruRQJdSeZS37uzVMRVbcSkNh5N9RVA0ogKLNNF4HvWBf0KEfIhH%25kTAusvgpVmlDTI0Ccy2oWimuzHJZ0uDShtD5eqKDsH%25fMA8OSr9%25UsDOPSE2VZ8XgY1nTNIowJ4HO3zkyXqcfbYGnHR",
                "cost": 0,
            },
            "Fire_Red": {
                "image": "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIGzmydptvX%25oKNHkJENmb4Ws86OG7c1QUDCkWxbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v6%25yX3242NnTQdjcjqN3azDx4a7dnkq8cHEzOALUxnXkIFJG8OxABKupUP8FeWS6GbSKMPVYp9gWhbNmQtiPo90yWAIbHi4TPFo9%25wc3b%25eiftxd9fKw178zi1qtECUkwDo7slGAtqjCrXpF7LflZQ6KCHyXRaYWlItQ5nmPXJ2agOybQfanvIT9FvZO2B3iKHRIjedwW%252BDMztPuZeqhk7bIUMLoAC9BAhJHFlieCou%25KXsnDHSfWQry0%25V1PaZcMfNEbnRxT10s9O58dE4riIgkYscZwBvg7rxRte2yzZ857MjuvRUgChD2B5Gvloq3lgp2XH3ccv6jQ%25db22YDafDsZjmqn1qiCDyLOELA9qTJIsJZWL3uBruRQJdSeZS37uzVMRVbcSkNh5N9RVA0ogKLNNF4HvWBf0KEfIhH%25kTAusvgpVmlDTI0Ccy2oWimuzHJZ0uDShtD5eqKDsH%25fMA8OSr9%25UsDOPSE2VZ8XgY1nTNIowJ4HO3zkyXqcfbYGnHR",
                "cost": 0,
            },
        }
    },
    {
        "manufacturer": "BMW",
        "model": "M3 Competition M xDrive Sedan",
        "full_name": "BMW M3 Competition xDrive Sedan",
        "price": 101150,
        "fuel": "Diesel",
        "chassis": "Sedan",
        "transmission": "Automatic",
        "engine": "3.0L",
        "power_kw": 390,
        "power_hp": 530,
        "acceleration": 3.5,
        "fuel_consumption": 10.1,
        "colors": {
            "Alpine_White": {
                "image":  "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIG29YoptvX%25oKNHkJENmb4Ws86OG7c1QUD36kxbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v1SyX3242YfTQdjcjqN3azDxDi7dnkq8cnCzOALUx%25skIFJG8OQABKupUP8FeWS6GbSKMPVYp9gWhbNmQtiPo90yWAIbHi4TPFo9%25wc3b%25eiftxd9fKw178ziFNtECUkwB17slGAtqjCrXpF7LflZQ6KCHyXRaYWlXfQ5nmPXB7agOybQfsnvIT9FvZO2B3iKHRIjedwW%252BDMztPuZeqhk7bIUMLoAC9BAhJHFlieCou%25KXsnDHSfWQrgu%25V1PaZcMfNEbnRxT10s9O58dE4riIgkSscZwBvg7rxRte2yzZ857MjuTRUgChD2B5GvloTejgp2XH3ccv6jQ%25db22YDafzO7jmqn1qrRDyLOELwlqTJIsJ1tL3uBruKwJdSeZS5buzVMRVgnSkNh5N0iVA0og0kXNF4Hv4wU0Kc%252ctv4Ws1Bo%25fA3FSr3vLKyXq3B4lxTjHPwySk%25uR4SqVo7qgMLWqr%25f1hFUIVZifGrqIbVsjNRUQvmEO30BHtuc%25IdkATQLx19mpO%255",
                "cost": 0,
            },
            "Frozen_Portimao_Blue": {
                "image":  "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIG29YoptvX%25oKNHkJENmb4Ws86OG7c1QUDXvVxbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v1SyX3242YfTQdjcjqN3azDxDi7dnkq8cnCzOALUx%25skIFJG8OQABKupUP8FeWS6GbSKMPVYp9gWhbNmQtiPo90yWAIbHi4TPFo9%25wc3b%25eiftxd9fKw178ziFNtECUkwB17slGAtqjCrXpF7LflZQ6KCHyXRaYWlXfQ5nmPXB7agOybQfsnvIT9FvZO2B3iKHRIjedwW%252BDMztPuZeqhk7bIUMLoAC9BAhJHFlieCou%25KXsnDHSfWQrgu%25V1PaZcMfNEbnRxT10s9O58dE4riIgkSscZwBvg7rxRte2yzZ857MjuTRUgChD2B5GvloTejgp2XH3ccv6jQ%25db22YDafzO7jmqn1qrRDyLOELwlqTJIsJ1tL3uBruKwJdSeZS5buzVMRVgnSkNh5N0iVA0og0kXNF4Hv4wU0Kc%252ctv4Ws1Bo%25fA3FSr3vLKyXq3B4lxTjHPwySk%25uR4SqVo7qgMLWqr%25f1hFUIVZifGrqIbVsjNRUQvmEO30BHtuc%25IdkATQLx19mpO%255",
                "cost": 4141,
            },
            "Isle_of_Man_Green": {
                "image":  "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIG29YoptvX%25oKNHkJENmb4Ws86OG7c1QUDCYbxbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v1SyX3242YfTQdjcjqN3azDxDi7dnkq8cnCzOALUx%25skIFJG8OQABKupUP8FeWS6GbSKMPVYp9gWhbNmQtiPo90yWAIbHi4TPFo9%25wc3b%25eiftxd9fKw178ziFNtECUkwB17slGAtqjCrXpF7LflZQ6KCHyXRaYWlXfQ5nmPXB7agOybQfsnvIT9FvZO2B3iKHRIjedwW%252BDMztPuZeqhk7bIUMLoAC9BAhJHFlieCou%25KXsnDHSfWQrgu%25V1PaZcMfNEbnRxT10s9O58dE4riIgkSscZwBvg7rxRte2yzZ857MjuTRUgChD2B5GvloTejgp2XH3ccv6jQ%25db22YDafzO7jmqn1qrRDyLOELwlqTJIsJ1tL3uBruKwJdSeZS5buzVMRVgnSkNh5N0iVA0og0kXNF4Hv4wU0Kc%252ctv4Ws1Bo%25fA3FSr3vLKyXq3B4lxTjHPwySk%25uR4SqVo7qgMLWqr%25f1hFUIVZifGrqIbVsjNRUQvmEO30BHtuc%25IdkATQLx19mpO%255",
                "cost": 0,
            },
        }
    },
    {
        "manufacturer": "BMW",
        "model": "M4 CS Coupe",
        "full_name": "BMW M4 Competition Coupe",
        "price": 154284,
        "fuel": "Diesel",
        "chassis": "Coupe",
        "transmission": "Automatic",
        "engine": "3.0L",
        "power_kw": 405,
        "power_hp": 551,
        "acceleration": 3.4,
        "fuel_consumption": 10.2,
        "colors": {
            "Brooklyn_Grey": {
                "image":  "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIGtAlaptvX%25oKNHkJENmb4Ws86OG7c1QUDCYexbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v1SyX3242YfTQdjcji23azDxDL0dnkq8cnCzOALUx%25skIFJG8OQABKupUP8FeWS6GbSKMPVYp9gWhbNmQtiPo90yaAwbHi4Tnx99%25wc3O8Qiftxd9W%25w178zi1htECUkwEP7slGAtW4CrXpF7MplZQ6KCJqXRaYWluEQ5nmPXf3agOybQ3ynvIT9aMlO2B3iK2RIjedwW%255BDMztPfjeqhk7bXHMLoAC9VAhJHFliNgou%25KXwM6HSfWQthX%25V1PaZILfNEbnR2V10s9O58oE4riIgUdscZwBvGkrxRte2FNZ857Mj2lRUgChD3A5GvloqVdgp2XHLDMv6jQ%25dJW2YDafzoajmqn1kUUDyLOEAwqqTJIsFevL3uBru5vJdSeZSCauzVMRVrlSkNh5NbCVA0og02wNF4Hv4jB0Kc%252cx74Wxfjx7pcP81D8CjxbZsM%251EKzWNRxjuE3aJzMxQUdqf973NF1VgxNJ0%25lJ2oubJR1EsHWpe05tE6RJei0Zq4gpnjTrBzcMfCV81ekFKdnuUswTYB1v",
                "cost": 0,
            },
            "Sapphire_Black": {
                "image":  "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIGtAlaptvX%25oKNHkJENmb4Ws86OG7c1QUD4IxxbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v1SyX3242YfTQdjcji23azDxDL0dnkq8cnCzOALUx%25skIFJG8OQABKupUP8FeWS6GbSKMPVYp9gWhbNmQtiPo90yaAwbHi4Tnx99%25wc3O8Qiftxd9W%25w178zi1htECUkwEP7slGAtW4CrXpF7MplZQ6KCJqXRaYWluEQ5nmPXf3agOybQ3ynvIT9aMlO2B3iK2RIjedwW%255BDMztPfjeqhk7bXHMLoAC9VAhJHFliNgou%25KXwM6HSfWQthX%25V1PaZILfNEbnR2V10s9O58oE4riIgUdscZwBvGkrxRte2FNZ857Mj2lRUgChD3A5GvloqVdgp2XHLDMv6jQ%25dJW2YDafzoajmqn1kUUDyLOEAwqqTJIsFevL3uBru5vJdSeZSCauzVMRVrlSkNh5NbCVA0og02wNF4Hv4jB0Kc%252cx74Wxfjx7pcP81D8CjxbZsM%251EKzWNRxjuE3aJzMxQUdqf973NF1VgxNJ0%25lJ2oubJR1EsHWpe05tE6RJei0Zq4gpnjTrBzcMfCV81ekFKdnuUswTYB1v",
                "cost": 0,
            },
        }
    },
    {
        "manufacturer": "BMW",
        "model": "M8 Coupe",
        "full_name": "BMW M8 Coupe",
        "price": 165172,
        "fuel": "Gasoline",
        "chassis": "Coupe",
        "transmission": "Automatic",
        "engine": "4.4L",
        "power_kw": 441,
        "power_hp": 600,
        "acceleration": 3.3,
        "fuel_consumption": 11.3,
        "colors": {
            "Alpine_White": {
                "image":  "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIG29YoptvX%25oKNHkJENmb4Ws86OG7c1QUD36kxbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v6%25yX3242tmTQdjc0Qt3azDx4o1dnkq8calzOALUxKckIFJG8WJABKupC9PFeWS6ldbKMPVYXzsWhbNmQ4vPo90yWAhbHi4TPao9%25wc3bvMiftxd9Uxw178zmaftECUkyRU7slGAT5MCrXpF3golZQ6KdvCXRaYWzCKQ5nmPeisagOybMDCnvIT9hqcO2B3ioL8IjedwHG5BDMzt%25Hpeqhk7fZ4MLoAC0w%25hJHFl422ou%25KXcmNHSfWQxsn%25V1Pa1IefNEbnE3A10s9OsGTE4riIreYscZwBZMWrxRteRckZ857M5yjRUgChgTL5GaXbtClxN8snxhcjSk%25Nb5zvVo7pySscCEI5s%25rt3%25eifG%25nClXw8jPrOmlDn%25P6raoZIjAMuQWNRb7TEgCP0cxVAfvXYuqWCB",
                "cost": 0,
            },
            "Aventurine_Red": {
                "image":  "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIG29YoptvX%25oKNHkJENmb4Ws86OG7c1QUDCJfxbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v6%25yX3242tmTQdjc0Qt3azDx4o1dnkq8calzOALUxKckIFJG8WJABKupC9PFeWS6ldbKMPVYXzsWhbNmQ4vPo90yWAhbHi4TPao9%25wc3bvMiftxd9Uxw178zmaftECUkyRU7slGAT5MCrXpF3golZQ6KdvCXRaYWzCKQ5nmPeisagOybMDCnvIT9hqcO2B3ioL8IjedwHG5BDMzt%25Hpeqhk7fZ4MLoAC0w%25hJHFl422ou%25KXcmNHSfWQxsn%25V1Pa1IefNEbnE3A10s9OsGTE4riIreYscZwBZMWrxRteRckZ857M5yjRUgChgTL5GaXbtClxN8snxhcjSk%25Nb5zvVo7pySscCEI5s%25rt3%25eifG%25nClXw8jPrOmlDn%25P6raoZIjAMuQWNRb7TEgCP0cxVAfvXYuqWCB",
                "cost": 0,
            },
            "Dravit_Grey": {
                "image":  "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIG29YoptvX%25oKNHkJENmb4Ws86OG7c1QUDCPixbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v6%25yX3242tmTQdjc0Qt3azDx4o1dnkq8calzOALUxKckIFJG8WJABKupC9PFeWS6ldbKMPVYXzsWhbNmQ4vPo90yWAhbHi4TPao9%25wc3bvMiftxd9Uxw178zmaftECUkyRU7slGAT5MCrXpF3golZQ6KdvCXRaYWzCKQ5nmPeisagOybMDCnvIT9hqcO2B3ioL8IjedwHG5BDMzt%25Hpeqhk7fZ4MLoAC0w%25hJHFl422ou%25KXcmNHSfWQxsn%25V1Pa1IefNEbnE3A10s9OsGTE4riIreYscZwBZMWrxRteRckZ857M5yjRUgChgTL5GaXbtClxN8snxhcjSk%25Nb5zvVo7pySscCEI5s%25rt3%25eifG%25nClXw8jPrOmlDn%25P6raoZIjAMuQWNRb7TEgCP0cxVAfvXYuqWCB",
                "cost": 2501,
            },
        }
    },
    {
        "manufacturer": "BMW",
        "model": "X6 M Competition",
        "full_name": "BMW X6 M Competition",
        "price": 148929,
        "fuel": "Gasoline",
        "chassis": "SUV",
        "transmission": "Automatic",
        "engine": "4.4L",
        "power_kw": 460,
        "power_hp": 625,
        "acceleration": 3.9,
        "fuel_consumption": 12.7,
        "colors": {
            "Mineral_White": {
                "image":  "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIGtA2FptvX%25oKNHkJENmb4Ws86OG7c1QUDAQixbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v1GyX3242YfTQdjcjqf3azDxDQEdnkq8cnCzOALUx%25skIFJG8WxABKupUPuFeWS6libKMPVYXz9WhbNmKkrPo90yWAhbHi4TPzu9%25wc3bIUiftxd9i3w178ziGqtECUkwQ37slGATOECrXpF3PalZQ6Kdv6XRaYWz2MQ5nmPkj%25agOybAD1nvIT9FQbO2B3io7RIjedwHE2BDMzt%25uaeqhk7fSGMLoAC1V6hJHFlEmxou%25KXsEPHSfWQrUY%25V1PaZ2GfNEbnUiA10s9OsehE4riIrzKscZwBZ6drxRteRhyZ857M5obRUgChg8F5Gvlov3hgp2XHYrvv6OaiCXQU4GZIHoRiNF14ivAj0%25lY3NZ8XrevZ1RCz1htE61IXQa7Gq9RBTQLI19mRO%255eqKoVnb4gildr2X9c8U0KEjayVJbXM",
                "cost": 0,
            },
            "Carbon_Black": {
                "image":  "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIGtA2FptvX%25oKNHkJENmb4Ws86OG7c1QUD4vixbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v1GyX3242YfTQdjcjqf3azDxDQEdnkq8cnCzOALUx%25skIFJG8WxABKupUPuFeWS6libKMPVYXz9WhbNmKkrPo90yWAhbHi4TPzu9%25wc3bIUiftxd9i3w178ziGqtECUkwQ37slGATOECrXpF3PalZQ6Kdv6XRaYWz2MQ5nmPkj%25agOybAD1nvIT9FQbO2B3io7RIjedwHE2BDMzt%25uaeqhk7fSGMLoAC1V6hJHFlEmxou%25KXsEPHSfWQrUY%25V1PaZ2GfNEbnUiA10s9OsehE4riIrzKscZwBZ6drxRteRhyZ857M5obRUgChg8F5Gvlov3hgp2XHYrvv6OaiCXQU4GZIHoRiNF14ivAj0%25lY3NZ8XrevZ1RCz1htE61IXQa7Gq9RBTQLI19mRO%255eqKoVnb4gildr2X9c8U0KEjayVJbXM",
                "cost": 0,
            },
            "Frozen_Pure_Grey": {
                "image":  "https://prod.cosy.bmw.cloud/connext-bmw/cosySec?COSY-EU-100-7331c9Nv2Z7d5yKlHS9gwyljT5lkQM37fNw2M2CpLjSk%25S8QvsrGZIGtA2FptvX%25oKNHkJENmb4Ws86OG7c1QUDCJnxbZG%25I4Y%25E9CpL0FkP%250hy2YIxZU2hilpRBqSrxlzK%25yoKG%25Ty8nvzTomvhv0v1GyX3242YfTQdjcjqf3azDxDQEdnkq8cnCzOALUx%25skIFJG8WxABKupUPuFeWS6libKMPVYXz9WhbNmKkrPo90yWAhbHi4TPzu9%25wc3bIUiftxd9i3w178ziGqtECUkwQ37slGATOECrXpF3PalZQ6Kdv6XRaYWz2MQ5nmPkj%25agOybAD1nvIT9FQbO2B3io7RIjedwHE2BDMzt%25uaeqhk7fSGMLoAC1V6hJHFlEmxou%25KXsEPHSfWQrUY%25V1PaZ2GfNEbnUiA10s9OsehE4riIrzKscZwBZ6drxRteRhyZ857M5obRUgChg8F5Gvlov3hgp2XHYrvv6OaiCXQU4GZIHoRiNF14ivAj0%25lY3NZ8XrevZ1RCz1htE61IXQa7Gq9RBTQLI19mRO%255eqKoVnb4gildr2X9c8U0KEjayVJbXM",
                "cost": 3895,
            },
        }
    },
    {
        "manufacturer": "Porsche",
        "model": "718 Spyder RS",
        "full_name": "Porsche 718 Spyder RS",
        "price": 171854,
        "fuel": "Gasoline",
        "chassis": "Cabriolet",
        "transmission": "Automatic",
        "engine": "4.0L",
        "power_kw": 368,
        "power_hp": 500,
        "acceleration": 3.4,
        "fuel_consumption": 12.7,
        "colors": {
            "White": {
                "image":  "https://pictures.porsche.com/rtt/iris?COSY-EU-100-1711coMvsi60AAt5FwcmBEgA4qP8iBUDxPE3Cb9pNXkBuNYdMGF4tl3U0%25z8rMHIspMBvMZq6G5OtgSv31nBJaA4qh4NSEGewirQ91wRmWBi2WdMZ4v7e0Dkt%25XkYW1jpJ1s5VbaZB1juh0mtdWqGAHg8D6QrJK51%25LDs91NsMK3Th6o4atiru5kb1CWR",
                "cost": 0,
            },
            "GT_Silver": {
                "image":  "https://pictures.porsche.com/rtt/iris?COSY-EU-100-1711coMvsi60AAt5FwcmBEgA4qP8iBUDxPE3Cb9pNXkBuNYdMGF4tl3U0%25z8rMHIspMBvMZq6G5OtgSv31nBJaA4qh4NSEGewirQ9wDRmWBiNYI7gVdcg1Dkt%25XkFbnL8W6ktQyIEVRDCHv39h7fxKXj4AUJqJK51%25LDs91NsMK3Th6o4atiru5kb1CWR",
                "cost": 3366,
            },
            "Shark_Blue": {
                "image":  "https://pictures.porsche.com/rtt/iris?COSY-EU-100-1711coMvsi60AAt5FwcmBEgA4qP8iBUDxPE3Cb9pNXkBuNYdMGF4tl3U0%25z8rMHIspMBvMZq6G5OtgSv31nBJaA4qh4NSEGewirQ9wDRmWBiNYI7gVdcg1Dkt%25XkFbnL8W6ktQyIEVRtyh0mtdWqGAHg8D6QrJK51%25LDs91NsMK3Th6o4atiru5kb1CWR",
                "cost": 3366,
            },
        }
    },
    {
        "manufacturer": "Porsche",
        "model": "911 GT3",
        "full_name": "Porsche 911 GT3",
        "price": 225817,
        "fuel": "Gasoline",
        "chassis": "Coupe",
        "transmission": "Manual",
        "engine": "4.0L",
        "power_kw": 375,
        "power_hp": 510,
        "acceleration": 3.9,
        "fuel_consumption": 13.8,
        "colors": {
            "Ice_Grey": {
                "image":  "https://pictures.porsche.com/rtt/iris?COSY-EU-100-1711coMvsi60AAt5FwcmBEgA4qP8iBUDxPE3Cb9pNXkBuNYdMGF4tl3U0%25z8rMHIspMBvMZq6G5OtgSv31nBJaA4qh4NSEGewirQ9wpRmWBi2Ow7gVdcJItUlhDfDJmspAnPOY0iZJyN2HMctBvoQcXj4AUw9l6a%25JsNEwRmWBio6J7gVdcFVtUlSjv8cqnjYqZl%25bRhV0iDRrpKmhE8gfjb",
                "cost": 1296,
            },
            "Gentian_Blue": {
                "image":  "https://pictures.porsche.com/rtt/iris?COSY-EU-100-1711coMvsi60AAt5FwcmBEgA4qP8iBUDxPE3Cb9pNXkBuNYdMGF4tl3U0%25z8rMHIspMBvMZq6G5OtgSv31nBJaA4qh4NSEGewirQ9wpRmWBi2hdMZ4vFN2Dkt%25X90jnL8W6W9MyIEVRNeCv39h7FGxXj4AUw9l6a%25JsNEwRmWBio6J7gVdcFVtUlSjv8cqnjYqZl%25bRhV0iDRrpKmhE8gfjb",
                "cost": 2070,
            },
            "Oak_Green": {
                "image":  "https://pictures.porsche.com/rtt/iris?COSY-EU-100-1711coMvsi60AAt5FwcmBEgA4qP8iBUDxPE3Cb9pNXkBuNYdMGF4tl3U0%25z8rMHIspMBvMZq6G5OtgSv31nBJaA4qh4NSEGewirQ9wpRmWBi2Ow7gVdcJItUlhDfDJmspAnPOY0iZJyN2HMctBvoSJ4f8dXFcA6a%25JsNEwRmWBio6J7gVdcFVtUlSjv8cqnjYqZl%25bRhV0iDRrpKmhE8gfjb",
                "cost": 3928,
            },
        }
    },
    {
        "manufacturer": "Porsche",
        "model": "Taycan Turbo GT",
        "full_name": "Porsche Taycan Turbo GT",
        "price": 250016,
        "fuel": "Electric",
        "chassis": "Limousine",
        "transmission": "Automatic",
        "engine": "Electric",
        "power_kw": 580,
        "power_hp": 789,
        "acceleration": 2.3,
        "energy_consumption": 21.6,
        "colors": {
            "White": {
                "image":  "https://pictures.porsche.com/rtt/iris?COSY-EU-100-1711coMvsi60AAt5FwcmBEgA4qP8iBUDxPE3Cb9pNXkBuNYdMGF4tl3U0%25z8rMHIspMBvMZq6G5OtgSv31nBJaA4qh4NSEGewirQ91cRmWBiYfn7gVdc5QDkt%25XuoQnL8W6G90yIEVRPdwv39h7WTnXj4AUVMl6a%25Jsh0VRmWBiBhj7gVdcmZJUlhDfObPspAnPHhEiZJyNzHlctBvoqiyf8dXFOd%25PED6uTdLN9nReWlMo4atiheCUt1CW5IPI%25iIu7PK%25jEyAh9zt5",
                "cost": 0,
            },
            "Purple_Sky": {
                "image":  "https://pictures.porsche.com/rtt/iris?COSY-EU-100-1711coMvsi60AAt5FwcmBEgA4qP8iBUDxPE3Cb9pNXkBuNYdMGF4tl3U0%25z8rMHIspMBvMZq6G5OtgSv31nBJaA4qh4NSEGewirQ91cRmWBiYfn7gVdcQTxUlhDfHJIspAnPqRSiZJyNDrUctBvonm4f8dXFyInPED6u6ytN9nRetX7gVdcmZJUlhDfObPspAnPHhEiZJyNzHlctBvoqiyf8dXFOd%25PED6uTdLN9nReWlMo4atiheCUt1CW5IPI%25iIu7PK%25jEyAh9zt5",
                "cost": 0,
            },
            "Pale_Blue": {
                "image":  "https://pictures.porsche.com/rtt/iris?COSY-EU-100-1711coMvsi60AAt5FwcmBEgA4qP8iBUDxPE3Cb9pNXkBuNYdMGF4tl3U0%25z8rMHIspMBvMZq6G5OtgSv31nBJaA4qh4NSEGewirQ91cRmWBiYfn7gVdc5TDkt%25XuoQnL8W6G90yIEVRPdwv39h7WTnXj4AUVMl6a%25Jsh0VRmWBiBhj7gVdcmZJUlhDfObPspAnPHhEiZJyNzHlctBvoqiyf8dXFOd%25PED6uTdLN9nReWlMo4atiheCUt1CW5IPI%25iIu7PK%25jEyAh9zt5",
                "cost": 3678,
            },
        }
    },
    {
        "manufacturer": "Mercedes-AMG",
        "model": "S 63 E Performance",
        "full_name": "Mercedes-AMG S 63 E Performance",
        "price": 214660,
        "fuel": "Hybrid (Gasoline)",
        "chassis": "Limousine",
        "transmission": "Automatic",
        "engine": "4.0L",
        "power_kw": 590,
        "power_hp": 802,
        "acceleration": 3.3,
        "fuel_consumption": 4.6,
        "energy_consumption": 22.2,
        "colors": {
            "Obsidian_Black": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/223182/805_055/iris.webp?q=COSY-EU-100-1713d0VXqrEFqtyO67PobzIr3eWsrrCsdRRzwQZgk4ZbMw3SGtGyjtsd2spcUfp8cXGEubYJ0l36xOB2NbcbApRAlI5ux4YQC31gFkzNwtnm7jA7mhKV50L%25vqCJTyLRgc6YaxPa9rH1enun8w0A4oiZB5lM4FAyrTg9LQ36PDaPpSeWHXutsd8ZDcUfiMcXGE4TEJ0lg6fOB2Pb%25bApeIXI5usQMQC3UvrkzNGLKm7juyIhKV0SQ%25vqGugyLRKG6YaxvbYrH1pL4n8wi8boiZ45gM4FgKuTg9P6Z6PKNCZnX2f3SNsQ3sDwDkSW9wUwopoL24PvEa2zq7dXrCgQ&IMGT=W27&POV=BE040&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1280",
                "cost": 0,
            },
            "Mystic_Blue": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/223182/805_055/iris.webp?q=COSY-EU-100-1713d0VXqrEFqtyO67PobzIr3eWsrrCsdRRzwQZQTRZbMw3SGtGyjtsd2spcUfp8cXGEubYJ0l36xOB2NbcbApRAlI5ux4YQC31gFkzNwtnm7jA6ohKV5Kh%25vqCBkyLRzAHYax7oErH1KItn8wsOcoiZUidM4FGTjTg95ze6PDC7uSeWznMtsd7oNcUfi%25qXGE4GjJ0lgIVOB2PWEbApetpI5usc2QC3UkrkzNGmbm7j0hShKVBHM%25vqA8ayLRjnmYax5XhrH1Ajsn8waAcoiZHkoM4FN8eTg9Pgk6PDe7sSeWsajtsdUcDcUaqKDTb32VXq0hV0f9f%25XEd9B96N683eUHpi3v1LlbMKsh&IMGT=W27&POV=BE040&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1280",
                "cost": 4701,
            },
            "Magno_Opalite_Bright_White": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/223182/805_055/iris.webp?q=COSY-EU-100-1713d0VXqrEFqtyO67PobzIr3eWsrrCsdRRzwQZx3pZbMw3SGtGyjtsd2spcUfp8cXGEubYJ0l36xOB2NbcbApRAlI5ux4YQC31gFkzNwtnm7jA6ohKV5Kh%25vqCBkyLRzAHYax7oErH1KItn8wsOcoiZUidM4FGTjTg95ze6PDC7uSeWznMtsd7oNcUfi%25qXGE4GjJ0lgIVOB2PWEbApetpI5usc2QC3UkrkzNGmbm7j0hShKVBHM%25vqA8ayLRjnmYax5XhrH1Ajsn8waAcoiZHkoM4FN8eTg9Pgk6PDe7sSeWsajtsdUcDcUaqKDTb32VXq0hV0f9f%25XEd9B96N683eUHpi3v1LlbMKsh&IMGT=W27&POV=BE040&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1280",
                "cost": 1488,
            },
        }
    },
    {
        "manufacturer": "Mercedes-AMG",
        "model": "GLC 63 S E Performance Coupe",
        "full_name": "Mercedes-AMG GLC 63 S E Performance Coupe",
        "price": 129570,
        "fuel": "Hybrid (Gasoline)",
        "chassis": "SUV",
        "transmission": "Automatic",
        "engine": "2.0L",
        "power_kw": 375,
        "power_hp": 510,
        "acceleration": 3.9,
        "fuel_consumption": 13.8,
        "colors": {
            "Black": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/254387/805_055/iris.webp?q=COSY-EU-100-1713d0VXqNEFqtyO67PobzIr3eWsrrCsdRRzwQZQ9vZbMw3SGtGyjtsd1JpcUfwFuXGEZT3J0l3YhOB2NrjbApjPpI5uVeZQC3qhrkzNR%25bm7jxymhKV1XQ%25vqwJjyLRZQfYaxFrprH1dJZn8wfOWoiZEiEM4Fl4wTg92gk6PDp7bSeWuKjtsd3JVcUfNrkXGEjnRJ0lVDxOB2qWFbApRIXI5uG4YQC30gRkzNBUxm7jAcShKV5pV%25vqCIdyLRgcDYaxPXSrH1eHrn8ws8WoiZU51M4FGKjTg90626PDBSqSeWTK9tsd6o3cUfK%25jXGEvaXJ0lLoZOB2aMRbApHtXI5u8czQC3ivwkzN4okm7j06DhKVBYF%25vqAJTyLR53VYaxCkYrH1zmin8w7oboiZKeEM4FvsJTg9LUT6PDaGDSeWH0Utsd8BxcUfD%25NXGEWymJ0ldItOB2zr%25bAp7nCI5uK6YQC3vSTkzNUlNm7js2ihKVzKE%25vq7BdyLRKn2YaxvoJrH1LOWn8waepoiZHVbM4F8OITg9jQO6PDV4jSeWsmItsdUs3cUfGUyXGE0aSJ0lBHAOB2Ag2bAp5PwI5uCmZQC3zkpkzN7L9m7jc6DhKUWP3IrZxD%25WLqzAVvVS%25qjuauQFQ0ZzKG1BZeEsRrbP76&IMGT=W27&POV=BE040&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1280",
                "cost": 0,
            },
            "Patagonia_Red": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/254387/805_055/iris.webp?q=COSY-EU-100-1713d0VXqNEFqtyO67PobzIr3eWsrrCsdRRzwQZUkwZbMw3SGtGyjtsd1JpcUfwFuXGEZT3J0l3YhOB2NrjbApjPpI5uVeZQC3qhrkzNR%25bm7jxymhKV1XQ%25vqwJjyLRZQfYaxFrprH1dJZn8wfOWoiZEiEM4Fl4wTg92gk6PDp7bSeWuKjtsd3JVcUfNrkXGEjnRJ0lVDxOB2qWFbApRIXI5uG4YQC30gRkzNBUxm7jAcShKV5pV%25vqCIdyLRgcDYaxPXSrH1eHrn8ws8WoiZU51M4FGKjTg90626PDBSqSeWTK9tsd6o3cUfK%25jXGEvaXJ0lLoZOB2aMRbApHtXI5u8czQC3ivwkzN4okm7j06DhKVBYF%25vqAJTyLR53VYaxCkYrH1zmin8w7oboiZKeEM4FvsJTg9LUT6PDaGDSeWH0Utsd8BxcUfD%25NXGEWymJ0ldItOB2zr%25bAp7nCI5uK6YQC3vSTkzNUlNm7js2ihKVzKE%25vq7BdyLRKn2YaxvoJrH1LOWn8waepoiZHVbM4F8OITg9jQO6PDV4jSeWsmItsdUs3cUfGUyXGE0aSJ0lBHAOB2Ag2bAp5PwI5uCmZQC3zkpkzN7L9m7jc6DhKUWP3IrZxD%25WLqzAVvVS%25qjuauQFQ0ZzKG1BZeEsRrbP76&IMGT=W27&POV=BE040&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1280",
                "cost": 1833,
            },
            "Magno_Graphite_Grey": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/254387/805_055/iris.webp?q=COSY-EU-100-1713d0VXqNEFqtyO67PobzIr3eWsrrCsdRRzwQZ6OGZbMw3SGtGyjtsd1JpcUfwFuXGEZT3J0l3YhOB2NrjbApjPpI5uVeZQC3qhrkzNR%25bm7jxymhKV1XQ%25vqwJjyLRZQfYaxFrprH1dJZn8wfOWoiZEiEM4Fl4wTg92gk6PDp7bSeWuKjtsd3JVcUfNrkXGEjnRJ0lVDxOB2qWFbApRIXI5uG4YQC30gRkzNBUxm7jAcShKV5pV%25vqCIdyLRgcDYaxPXSrH1eHrn8ws8WoiZU51M4FGKjTg90626PDBSqSeWTK9tsd6o3cUfK%25jXGEvaXJ0lLoZOB2aMRbApHtXI5u8czQC3ivwkzN4okm7j06DhKVBYF%25vqAJTyLR53VYaxCkYrH1zmin8w7oboiZKeEM4FvsJTg9LUT6PDaGDSeWH0Utsd8BxcUfD%25NXGEWymJ0ldItOB2zr%25bAp7nCI5uK6YQC3vSTkzNUlNm7js2ihKVzKE%25vq7BdyLRKn2YaxvoJrH1LOWn8waepoiZHVbM4F8OITg9jQO6PDV4jSeWsmItsdUs3cUfGUyXGE0aSJ0lBHAOB2Ag2bAp5PwI5uCmZQC3zkpkzN7L9m7jc6DhKUWP3IrZxD%25WLqzAVvVS%25qjuauQFQ0ZzKG1BZeEsRrbP76&IMGT=W27&POV=BE040&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1280",
                "cost": 5117,
            },
        }
    },
    {
        "manufacturer": "Mercedes-AMG",
        "model": "G 63",
        "full_name": "Mercedes-AMG G 63",
        "price": 206651,
        "fuel": "Gasoline",
        "chassis": "SUV",
        "transmission": "Automatic",
        "engine": "4.0L",
        "power_kw": 430,
        "power_hp": 585,
        "acceleration": 4.4,
        "fuel_consumption": 14.7,
        "colors": {
            "Magno_Black": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/465250/X24_055/iris.webp?q=COSY-EU-100-1713d0VXqbWFqtyO67PobzIr3eWsrrCsdRRzwQZQ3IZbMw3SGtGyjtsd2HdcUfp8yXGEPGEJ0l7YhOB2XQcbApeARI5usmxQC3UnpkzNL2nm7jicohKV4PQ%25vqga9yLRNyfYaxj%25WrH1MQdn8w5VUoiZH6EM4F8yPTg9jLk6PDV4pSeWqZItsdTc3cUfGXWXGERbSJ0lbHlOB2MM%25bApdrXI5gZ8lXhRjwQZteHP9UuoQ3pE7EJxJeRB5PVsRiD4Nhc8An&IMGT=W27&POV=BE040&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1280",
                "cost": 7021,
            },
            "Desert_Sand_Brown": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/465250/X24_055/iris.webp?q=COSY-EU-100-1713d0VXqbWFqtyO67PobzIr3eWsrrCsdRRzwQZteBZbMw3SGtGyjtsd2HdcUfp8yXGEPGEJ0l7YhOB2XQcbApeARI5usmxQC3UnpkzNL2nm7jicohKV4PQ%25vqga9yLRNyfYaxj%25WrH1MQdn8w5VUoiZH6EM4F8yPTg9jLk6PDV4pSeWqZItsdTc3cUfGXWXGERbSJ0lbHlOB2MM%25bApdrXI5gZ8lXhRjwQZteHP9UuoQ3pE7EJxJeRB5PVsRiD4Nhc8An&IMGT=W27&POV=BE040&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1280",
                "cost": 4701,
            },
            "Emerald_Green": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/465250/X24_055/iris.webp?q=COSY-EU-100-1713d0VXqbWFqtyO67PobzIr3eWsrrCsdRRzwQZUZpZbMw3SGtGyjtsd2HdcUfp8yXGEPGEJ0l7YhOB2XQcbApeARI5usmxQC3UnpkzNL2nm7jicohKV4PQ%25vqga9yLRNyfYaxj%25WrH1MQdn8w5VUoiZH6EM4F8yPTg9jLk6PDV4pSeWqZItsdTc3cUfGXWXGERbSJ0lbHlOB2MM%25bApdrXI5gZ8lXhRjwQZteHP9UuoQ3pE7EJxJeRB5PVsRiD4Nhc8An&IMGT=W27&POV=BE040&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1280",
                "cost": 0,
            },
        }
    },
    {
        "manufacturer": "Mercedes-AMG",
        "model": "GT 63 S E Performance",
        "full_name": "Mercedes-AMG GT 63 S E Performance",
        "price": 229241,
        "fuel": "Hybrid (Gasoline)",
        "chassis": "Coupe",
        "transmission": "Automatic",
        "engine": "4.0L",
        "power_kw": 450,
        "power_hp": 612,
        "acceleration": 2.8,
        "fuel_consumption": 8.2,
        "colors": {
            "Obsidian_Black": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/192382/805_055/iris.webp?q=COSY-EU-100-1713d0VXqrWFqtyO67PobzIr3eWsrrCsdRRzwQZgk4ZbMw3SGtGyjtsd2HdcUfpMqXGEjnmJ0leIJOB2Kr%25bApvAVI5uLmIQC3akpkzN4PZm7j06DhKVBKF%25vqAI%25yLR5QRYaxC4SrH1qM%25n8wPO3oiZ7MEM4FzR0Tg9jH66PDecNSevjzFoJpENtjvcp8WZWmtdDZGZMuMapgeLlHp7RKfJnzPk&IMGT=W27&POV=BE020&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1920",
                "cost": 0,
            },
            "Magno_Hell_Green": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/192382/805_055/iris.webp?q=COSY-EU-100-1713d0VXqrWFqtyO67PobzIr3eWsrrCsdRRzwQZvVIZbMw3SGtGyjtsd2HdcUfpMqXGEjnmJ0leIJOB2Kr%25bApvAVI5uLmIQC3akpkzN4PZm7j06DhKVBKF%25vqAI%25yLR5QRYaxC4SrH1qM%25n8wPO3oiZ7MEM4FzR0Tg9jH66PDecNSevjzFoJpENtjvcp8WZWmtdDZGZMuMapgeLlHp7RKfJnzPk&IMGT=W27&POV=BE020&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1920",
                "cost": 8687,
            },
            "Magno_Hyper_Blue": {
                "image":  "https://media.oneweb.mercedes-benz.com/images/dynamic/europe/RO/192382/805_055/iris.webp?q=COSY-EU-100-1713d0VXqrWFqtyO67PobzIr3eWsrrCsdRRzwQZUeBZbMw3SGtGyjtsd2HdcUfpMqXGEjnmJ0leIJOB2Kr%25bApvAVI5uLmIQC3akpkzN4PZm7j06DhKVBKF%25vqAI%25yLR5QRYaxC4SrH1qM%25n8wPO3oiZ7MEM4FzR0Tg9jH66PDecNSevjzFoJpENtjvcp8WZWmtdDZGZMuMapgeLlHp7RKfJnzPk&IMGT=W27&POV=BE020&BKGND=9&uni=m&cp=o1Yw6tbhjdvotoOJyaA8nQ&imwidth=1920",
                "cost": 7021,
            },
        }
    }
]


collection.insert_many(automobiles)
print("Successfully populated the database with the automobiles data.")
