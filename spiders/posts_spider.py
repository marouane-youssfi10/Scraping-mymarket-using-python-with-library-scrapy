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
        'https://www.iris.ma/17-toner',
        'https://www.iris.ma/26-disque-dur-portable-25',
        'https://www.iris.ma/299-imprimante-a-reservoirs-rechargeables',
        'https://www.iris.ma/12-multifonction-jet-d-encre',
        'https://www.iris.ma/11-imprimante-jet-d-encre',
        'https://www.iris.ma/50-imprimante-multifonction-laser-couleur',
        'https://www.iris.ma/49-imprimante-multifonction-laser-monochrome',
        'https://www.iris.ma/48-imprimante-laser-couleur',
        'https://www.iris.ma/47-imprimante-laser-monochrome',
        'https://www.iris.ma/139-imprimante-a3',
        'https://www.iris.ma/32-scanner',
        'https://www.iris.ma/143-scanner-a-plat-avec-chargeur-automatique',
        'https://www.iris.ma/141-scanner-a-plat-sans-chargeur',
        'https://www.iris.ma/142-scanner-a-defilement',
        'https://www.iris.ma/16-cartouche-d-encre',
        'https://www.iris.ma/17-toner',
        'https://www.iris.ma/106-ruban',
        'https://www.iris.ma/18-papier',
        'https://www.iris.ma/99-etiqueteuse-imprimante-de-tickets',
        'https://www.iris.ma/91-imprimante-grand-format-traceur',
        'https://www.iris.ma/98-imprimante-matricielle',
        'https://www.iris.ma/290-imprimante-3d',
        'https://www.iris.ma/44-ordinateur-portable',
        'https://www.iris.ma/146-pc-tactiles',
        'https://www.iris.ma/147-pc-convertible-tablette',
        'https://www.iris.ma/114-station-d-accueil',
        'https://www.iris.ma/53-cable',
        'https://www.iris.ma/268-memoire-pc-ram',
        'https://www.iris.ma/148-unite-centrale-seule',
        'https://www.iris.ma/149-unite-centrale-avec-ecran',
        'https://www.iris.ma/150-tout-en-un',
        'https://www.iris.ma/61-antivirus-et-securite',
        'https://www.iris.ma/89-bureautique-et-utilitaires',
        'https://www.iris.ma/101-systeme-d-exploitation',
        'https://www.iris.ma/55-ecran-moniteur',
        'https://www.iris.ma/155-serveur',
        'https://www.iris.ma/76-tablette-tactile',
        'https://www.iris.ma/215-accessoires-tablette',
        'https://www.iris.ma/95-onduleur',
        'https://www.iris.ma/151-onduleur-off-line',
        'https://www.iris.ma/152-onduleur-line-interactive-in-line',
        'https://www.iris.ma/153-onduleur-on-line',
        'https://www.iris.ma/160-souris-avec-fil',
        'https://www.iris.ma/161-souris-sans-fil',
        'https://www.iris.ma/162-clavier-avec-fil',
        'https://www.iris.ma/163-clavier-sans-fil',
        'https://www.iris.ma/164-pack-avec-fil',
        'https://www.iris.ma/165-pack-sans-fil',
        'https://www.iris.ma/26-disque-dur-portable-25',
        'https://www.iris.ma/27-disque-dur-de-bureau-35',
        'https://www.iris.ma/29-disque-dur-reseau',
        'https://www.iris.ma/221-disque-dur-interne',
        'https://www.iris.ma/251-serveur-nas',
        'https://www.iris.ma/30-cle-usb',
        'https://www.iris.ma/31-carte-memoire',
        'https://www.iris.ma/266-cartouche-de-donnees',
        'https://www.iris.ma/197-imprimante',
        'https://www.iris.ma/11-imprimante-jet-d-encre',
        'https://www.iris.ma/12-multifonction-jet-d-encre',
        'https://www.iris.ma/48-imprimante-laser-couleur',
        'https://www.iris.ma/47-imprimante-laser-monochrome',
        'https://www.iris.ma/50-imprimante-multifonction-laser-couleur',
        'https://www.iris.ma/49-imprimante-multifonction-laser-monochrome',
        'https://www.iris.ma/95-onduleur',
        'https://www.iris.ma/151-onduleur-off-line',
        'https://www.iris.ma/152-onduleur-line-interactive-in-line',
        'https://www.iris.ma/153-onduleur-on-line',
        'https://www.iris.ma/154-onduleur-rackable',
        'https://www.iris.ma/96-batterie-onduleur',
        'https://www.iris.ma/97-prise-parafoudre',
        'https://www.iris.ma/111-regulateur-de-tension',
        'https://www.iris.ma/92-videoprojecteur',
        'https://www.iris.ma/125-accessoires-videoprojecteur',
        'https://www.iris.ma/183-ecran-sur-trepied',
        'https://www.iris.ma/184-ecran-manuel-mural',
        'https://www.iris.ma/116-appareil-reflex-numerique-maroc',
        'https://www.iris.ma/115-compact',
        'https://www.iris.ma/118-objectif-appareil-photo-maroc',
        'https://www.iris.ma/120-accessoires-appareil-photo',
        'https://www.iris.ma/122-flash-appareil-photo',
        'https://www.iris.ma/123-batterie',
        'https://www.iris.ma/55-ecran-moniteur',
        'https://www.iris.ma/66-haut-parleur-enceinte-pc',
        'https://www.iris.ma/192-systeme-20',
        'https://www.iris.ma/37-casques-ecouteurs',
        'https://www.iris.ma/82-telephone-portable-smartphone-maroc',
        'https://www.iris.ma/209-montre-et-bracelet-connectes',
        'https://www.iris.ma/126-accessoires-telephone-portable',
        'https://www.iris.ma/42-switch',
        'https://www.iris.ma/201-switch-gigabit',
        'https://www.iris.ma/202-switch-non-administrable',
        'https://www.iris.ma/248-switch-administrable',
        'https://www.iris.ma/178-switch-avec-fibre-optique',
        'https://www.iris.ma/40-cle-usb-wifi',
        'https://www.iris.ma/110-courants-porteurs-en-ligne-cpl-',
        'https://www.iris.ma/109-point-d-acces',
        'https://www.iris.ma/41-routeur',
        'https://www.iris.ma/155-serveur',
        'https://www.iris.ma/206-accessoires-serveurs',
        'https://www.iris.ma/153-onduleur-on-line',
        'https://www.iris.ma/152-onduleur-line-interactive-in-line',
        'https://www.iris.ma/151-onduleur-off-line',
        'https://www.iris.ma/154-onduleur-rackable'
       ]

    def parse(self, response):

        categorie = response.css('span.cat-name::text').get().strip()

        # get title, price, link image, link product, name product
        for i in response.css('div.product-container'):
            title = i.css('a.product-name::text').get().strip()
            price = i.css('span.price.product-price::text').get().strip()
            img = i.css('img.replace-2x.img-responsive::attr(src)').get()
            link_produit = i.css('a.product_img_link::attr(href)').get()
            livree = i.css('div.availability_now span::text').extract()

            # put it names in list
            website.append('https://www.iris.ma/')
            categorie_list.append(categorie)
            link_site.append(link_produit)
            price_list.append(price)
            name_list.append(title)
            image_list.append(img)
            delai_de_livraison_list.append(livree)

            # display information when you scraped from website
            print('link_site          = ', link_produit)
            print('categorie          = ', categorie)
            print('name               = ', title)
            print('price              = ', price)
            print('image              = ', img)
            print('delai_de_livraison = ', livree)

            print('\n --------------------------------------------- \n')
            print('link_site_produit = ', len(link_site))
            print('categorie         = ', len(categorie_list))
            print('title             = ', len(name_list))
            print('price             = ', len(price_list))
            print('link_image        = ', len(image_list))
            print('livraison         = ', len(delai_de_livraison_list))
            print('\n --------------------------------------------- \n')

        # move to next page
        next_page = response.css('li.pagination_next a::attr(href)').get()
        if next_page:
            yield response.follow('https://www.iris.ma' + str(next_page))

        # put it in dataframe
        df = pd.DataFrame({
            'websites': website,
            'link_site': link_site,
            'title': name_list,
            'price': price_list,
            'categorie': categorie_list,
            'link_img': image_list,
            'livration': delai_de_livraison_list
        })
        # save in excel
        df.to_excel('iris.xlsx', index=False)