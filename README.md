# Arabian Bing Translator

Plugin for arabian to english translation.

An API key from portal.azure.com is needed to create a token . See Microsoft Translator API Documentation: http://docs.microsofttranslator.com/. 


## Setup

1. Clone this repo.

```
git clone http://lab.cluster.gsi.dit.upm.es/senpy/translator-bing.git
```

1. Move into your repository folder and start the docker container.

``` 
cd translator-bing/
docker-compose up 
```

## Programatical access

1. Run the following query, being <ARAB_TEXT_TO_CONVERT> the text you want to translate and <YOUR_MS_TRANSLATOR_PI_KEY> your API key created from portal.azure.com.

```
localhost:5000/api?algo=TranslatorPlugin&i=<ARAB_TEXT_TO_CONVERT>&conversion=full&expanded-jsonld=false&informat=text&intype=direct&outformat=json-ld&urischeme=RFC5147String&with_parameters=false&lang=ar&key=<YOUR_MS_TRANSLATOR_API_KEY>
``` 

## Web interface access

1. Go to your web browser and search _localhost:5000_.
1. Insert your Microsoft Transalator API key.
1. Paste you text and click the Analyse button.