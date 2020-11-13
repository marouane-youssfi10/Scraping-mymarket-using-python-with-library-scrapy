import scrapy
import pandas as pd

name_list = []
price_list = []
image = []
link_site = []
categorie_list = []
website = []
image_list = []
name_list_brand = []
name_list_ref = []
delai_de_livraison_list = []
description_list = []
quantite_minimum_list = []
Envoi_dans_list = []

class PostsSpider(scrapy.Spider):

    name = "posts"

    start_urls = [
        'https://www.mymarket.ma/collections/legumes',
        'https://www.mymarket.ma/collections/marche-et-boucherie',
        'https://www.mymarket.ma/collections/fruits',
        'https://www.mymarket.ma/collections/produits-de-la-mer',
        'https://www.mymarket.ma/collections/charcuterie-traiteur',
        'https://www.mymarket.ma/collections/boucherie-volaille',
        'https://www.mymarket.ma/collections/fruits-de-saison-panier-de-fruits',
        'https://www.mymarket.ma/collections/legumes-de-saison-panier-de-legumes',
        'https://www.mymarket.ma/collections/lait-et-boisson-lactee',
        'https://www.mymarket.ma/collections/cremes-fraiches',
        'https://www.mymarket.ma/collections/oeufs',
        'https://www.mymarket.ma/collections/yaourts',
        'https://www.mymarket.ma/collections/fromages',
        'https://www.mymarket.ma/collections/produits-laitiers-bio',
        'https://www.mymarket.ma/collections/beurres-margarines-et-sauces-a-cuisiner',
        'https://www.mymarket.ma/collections/glaces',
        'https://www.mymarket.ma/collections/farines-sucres',
        'https://www.mymarket.ma/collections/aide-a-la-patisserie',
        'https://www.mymarket.ma/collections/biscuits-confiseries',
        'https://www.mymarket.ma/collections/chocolat',
        'https://www.mymarket.ma/collections/shampooings-et-soins-19',
        'https://www.mymarket.ma/collections/soupe',
        'https://www.mymarket.ma/collections/sauces-chaudes',
        'https://www.mymarket.ma/collections/condiments-et-sauces',
        'https://www.mymarket.ma/collections/pates',
        'https://www.mymarket.ma/collections/riz',
        'https://www.mymarket.ma/collections/semoule',
        'https://www.mymarket.ma/collections/puree',
        'https://www.mymarket.ma/collections/huiles-et-vinaigres',
        'https://www.mymarket.ma/collections/conserves',
        'https://www.mymarket.ma/collections/epices',
        'https://www.mymarket.ma/collections/bouillons',
        'https://www.mymarket.ma/collections/biscuits-aperitifs-chips',
        'https://www.mymarket.ma/collections/epices',
        'https://www.mymarket.ma/collections/bouillons',
        'https://www.mymarket.ma/collections/biscuits-aperitifs-chips',
        'https://www.mymarket.ma/collections/produits-du-monde',
        'https://www.mymarket.ma/collections/thes-infusions',
        'https://www.mymarket.ma/collections/confitures-pates-a-tartiner-miel',
        'https://www.mymarket.ma/collections/tartines-biscuits',
        'https://www.mymarket.ma/collections/pains',
        'https://www.mymarket.ma/collections/patisserie',
        'https://www.mymarket.ma/collections/petits-fours',
        'https://www.mymarket.ma/collections/eaux-plates',
        'https://www.mymarket.ma/collections/eaux-gazeuses',
        'https://www.mymarket.ma/collections/eaux-aromatisees',
        'https://www.mymarket.ma/collections/jus-de-fruits-nectar',
        'https://www.mymarket.ma/collections/sodas-boissons-gazeuses',
        'https://www.mymarket.ma/collections/sirops-cocktails',
        'https://www.mymarket.ma/collections/thes-glaces',
        'https://www.mymarket.ma/collections/boissons-energisantes',
        'https://www.mymarket.ma/collections/aperitifs-entrees-et-snacking',
        'https://www.mymarket.ma/collections/pizzas-pate-tartes-et-plats-cuisines',
        'https://www.mymarket.ma/collections/viandes-poissons-et-crustaces',
        'https://www.mymarket.ma/collections/glaces-et-patisseries-surgelees',
        'https://www.mymarket.ma/collections/glaces-et-patisseries-surgelees',
        'https://www.mymarket.ma/collections/1er-age',
        'https://www.mymarket.ma/collections/2eme-age',
        'https://www.mymarket.ma/collections/croissance',
        'https://www.mymarket.ma/collections/alimentation-bebe-bio',
        'https://www.mymarket.ma/collections/alimentation-bebe-sans-gluten',
        'https://www.mymarket.ma/collections/compotes-repas',
        'https://www.mymarket.ma/collections/eaux-adaptees-jus',
        'https://www.mymarket.ma/collections/farines-et-cereales',
        'https://www.mymarket.ma/collections/couches-bebe',
        'https://www.mymarket.ma/collections/lingettes-bebe',
        'https://www.mymarket.ma/collections/soins',
        'https://www.mymarket.ma/collections/shampooings-et-soins',
        'https://www.mymarket.ma/collections/rasage-soins-hommes',
        'https://www.mymarket.ma/collections/dentainre',
        'https://www.mymarket.ma/collections/shampooings-et-soins-6',
        'https://www.mymarket.ma/collections/deodorants-et-aux-de-toilettes',
        'https://www.mymarket.ma/collections/shampooings-et-soins-1',
        'https://www.mymarket.ma/collections/hygiene-intime',
        'https://www.mymarket.ma/collections/soins-du-visages-et-corps',
        'https://www.mymarket.ma/collections/deodorants',
        'https://www.mymarket.ma/collections/shampooings-et-soins-6',
        'https://www.mymarket.ma/collections/epilation',
        'https://www.mymarket.ma/collections/shampooings-et-soins-14',
        'https://www.mymarket.ma/collections/shampooings-et-soins-10',
        'https://www.mymarket.ma/collections/dentaire',
        'https://www.mymarket.ma/collections/shampooings-et-soins-11',
        'https://www.mymarket.ma/collections/couches-adultes',
        'https://www.mymarket.ma/collections/nettoyants-multi-usages',
        'https://www.mymarket.ma/collections/sols',
        'https://www.mymarket.ma/collections/vitres',
        'https://www.mymarket.ma/collections/wc',
        'https://www.mymarket.ma/collections/desodorisants',
        'https://www.mymarket.ma/collections/meubles',
        'https://www.mymarket.ma/collections/insecticides',
        'https://www.mymarket.ma/collections/produits-ecologiques-bio',
        'https://www.mymarket.ma/collections/liquides-vaisselle',
        'https://www.mymarket.ma/collections/torchon-et-abrasif',
        'https://www.mymarket.ma/collections/lave-vaisselle',
        'https://www.mymarket.ma/collections/gants-eponges',
        'https://www.mymarket.ma/collections/sacs-poubelle',
        'https://www.mymarket.ma/collections/essuies-tout',
        'https://www.mymarket.ma/collections/conservation',
        'https://www.mymarket.ma/collections/ustensiles-vaisselles-jetables',
        'https://www.mymarket.ma/collections/bougies-anniversaires',
        'https://www.mymarket.ma/collections/shampooings-et-soins-12',
        'https://www.mymarket.ma/collections/accessoires-de-cuisine',
        'https://www.mymarket.ma/collections/vitroceramique-four-et-metaux',
        'https://www.mymarket.ma/collections/petit-dejeuner-electro',
        'https://www.mymarket.ma/collections/beaute-electro',
        'https://www.mymarket.ma/collections/centrale-vapeur',
        'https://www.mymarket.ma/collections/mixeur-batteur-et-hachoir',
        'https://www.mymarket.ma/collections/petit-appareil-de-cuisine',
        'https://www.mymarket.ma/collections/aspirateurs',
        'https://www.mymarket.ma/collections/robot-et-blender'
       ]

    def parse(self, response):

        categorie = response.css('h1.collection__title.heading.h1::text').get().strip()

        for i in response.css('div.product-item.product-item--vertical'):
            title = i.css('a.product-item__title.text--strong.link::text').get().strip()
            price = i.css('span.price::text').get().strip()
            img = i.css('div.aspect-ratio.aspect-ratio--square img::attr(src)').get().strip()
            link_produit = 'https://www.mymarket.ma/' + i.css('a.product-item__image-wrapper::attr(href)').get().strip()
            # livree = i.css('span.available_later::text').get()

            website.append('https://www.mymarket.ma/')
            categorie_list.append(categorie)
            link_site.append(link_produit)
            price_list.append(price)
            name_list.append(title)
            image_list.append(img)
            # delai_de_livraison_list.append(livree)

            print('link_site          = ', link_produit)
            print('categorie          = ', categorie)
            print('name               = ', title)
            print('price              = ', price)
            print('image              = ', img)
            # print('delai_de_livraison = ', livree)

            print('\n --------------------------------------------- \n')
            print('link_site_produit = ', len(link_site))
            print('categorie         = ', len(categorie_list))
            print('title             = ', len(name_list))
            print('price             = ', len(price_list))
            print('link_image        = ', len(image_list))
            # print('livraison         = ', len(delai_de_livraison_list))
            print('\n --------------------------------------------- \n')


        '''next_page = response.css('a.next.js-search-link::attr(href)').get()
        if next_page:
            yield response.follow(next_page)'''

        df = pd.DataFrame({
            'websites': website,
            'link_site': link_site,
            'title': name_list,
            'price': price_list,
            'categorie': categorie_list,
            'link_img': image_list
        })
        df.to_excel('mymarket.xlsx', index=False)