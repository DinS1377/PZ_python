"""
 Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
 Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция,
 Австралия. .Определить:
 1 в каких турагенствах можно одновременно приобрести туры в Италию и Канаду.
 2 в турагенство РейнаТур добавить тур в Индию.
 3 полный список всех туров.
"""

c = 0

voyage = {'mexico', 'canada', 'israel', 'italy', 'usa'}
reyna_tour = {'england', 'japan', 'canada', 'sar'}
rainbow = {'usa', 'spain', 'scotland', 'australia', 'italy', 'canada'}

a = {'italy', 'canada'}
tours = [voyage, reyna_tour, rainbow]
tours_names = ['voyage', 'reyna_tour', 'rainbow']

# в каких турагенствах туры в италию и канаду
for tour in tours:
    if a & tour == a:
        print(f'В туре {tours_names[c]}')
    c = +1

# добавление страны в турагенство
reyna_tour.update(['india'])
print(reyna_tour)

# список всех туров
print(f'список всех туров: {voyage|reyna_tour|rainbow}')


