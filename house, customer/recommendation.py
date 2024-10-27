from constants import MAX_PRICE

def get_recommendations( customer ,house_list):
    price = int(customer['account'].replace('$', '').replace('.', ''))

    recommendations = []

    for house in house_list:
        house_price = int(house['price'].replace('$', '').replace('.', ''))
        if price >= house_price:
            recommendations.append(house)
    if not recommendations:
        raise ValueError('Нет доступных домов')

    return recommendations



