from operator import contains

__author__ = 'shekhargulati'

import time

number = 731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135332766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450


def product_five_consecutive_numbers():
    number_str = str(number)
    max_product = 0
    for i in range(0, len(number_str), 1):
        five_digit_str = number_str[i:i + 5]
        if '0' not in five_digit_str:
            product = 1
            index = 0
            for x in five_digit_str:
                product *= int(five_digit_str[index])
                index += 1
            if product > max_product:
                max_product = product
    return max_product


if __name__ == "__main__":
    start_time = time.time()
    print(product_five_consecutive_numbers())
    print(time.time() - start_time)
