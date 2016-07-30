import media
import fresh_tomatoes
#file where class is defined

godfather = media.Movie('The Godfather',
                        'The Corleone family is up to their old antics.',
                        'https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg',
                        'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=21&cad=rja&uact=8&ved=0ahUKEwjGqbmg55TOAhVGHB4KHaXeBH4QryQImwEoADAU&url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D8V2k2YQEQJ4&usg=AFQjCNHguIf-sym7_l-5GgTylGE0l4MiBg&sig2=Rqi4497XEX0RKIXePeJGIQ'
                        )

blood = media.Movie("There Will Be Blood",
                     "An oiling operation goes all wrong.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/d/da/There_Will_Be_Blood_Poster.jpg/220px-There_Will_Be_Blood_Poster.jpg",
                     "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=21&cad=rja&uact=8&ved=0ahUKEwjd16-i6ZTOAhWFJR4KHSQeDiMQryQIogEoADAU&url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D3PXf5iSGIL4&usg=AFQjCNGyB9qqG5UXGhxCiL-twEI3ddN4HQ&sig2=28GNM54183n5VbyKhX41AQ&bvm=bv.128450091,d.dmo"
                     )

lebowski = media.Movie("The Big Lebowski",
                     "A bowling movie.",
                     "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                     "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=21&cad=rja&uact=8&ved=0ahUKEwjyuN696ZTOAhVDbB4KHUVlAVoQryQImgEoADAU&url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DB6s60JdiHJc&usg=AFQjCNEaVCvknrRzkEpz-87seesc29hFIQ&sig2=3sGpCMZw3Oda5lTac8JKSw"
                     )

starwars = media.Movie("Star Wars",
                     "The government vs wizards.",
                     "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/694px-Star_Wars_Logo.svg.png",
                     "www.youtube.com/watch?v=9MqVeJeDfio"
                     )

graduate = media.Movie("The Graduate",
                     "The first day of the rest of Dustin's life.",
                     "https://upload.wikimedia.org/wikipedia/en/8/8b/Graduateposter67.jpg",
                     "https://www.youtube.com/watch?v=hsdvhJTqLak"
                     )

blues = media.Movie("Blues Brothers",
                     "Band practice.",
                     "https://upload.wikimedia.org/wikipedia/en/f/f5/BluesBrothers.jpg",
                     "https://www.youtube.com/watch?v=UPbymWrqXGc"
                     )

movies = [godfather, blood, lebowski, starwars, graduate, blues]
fresh_tomatoes.open_movies_page(movies)
