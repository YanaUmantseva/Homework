from generation import gen_house_list, gen_customer
from recommendation import get_recommendations


def app():
    number_of_houses = 1
    number_of_customers = 1

    houses = gen_house_list(number_of_houses)
    customers = gen_customer(number_of_customers)

    print(f'Сгенерированные дома: {houses}')
    for customer in customers:
        print(f'Сгенерированный покупатель: {customer}')
        try:
            recommendations = get_recommendations(customer, houses)
            print('Рекомендованные дома:')
            for recommendation in recommendations:
                print(recommendation)
        except ValueError as e:
            print(e)



if __name__ == "__main__":
    app()

