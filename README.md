# Bing Translator

Plugin for arabian to english translation, belonging to the [Senpy](http://senpy.readthedocs.io/en/latest/) plugins catalogue. This plugin along with many others can be used together in order to create additional value via pipelines, being [GSI Crawler](http://gsicrawler.readthedocs.io/en/latest/) an example of how to enrich data through these procedures. 

An API key from portal.azure.com is needed to create a token . See Microsoft Translator API Documentation: http://docs.microsofttranslator.com/. 


## Setup

First,  clone this repo.

```
git clone http://lab.cluster.gsi.dit.upm.es/senpy/translator-bing.git
```

Then, move into your repository folder and start the docker container.

``` 
cd translator-bing/
docker-compose up 
```

## Programatical access

Run the following query, being ARAB_TEXT_TO_TRANSLATE the text you want to translate and YOUR_MS_TRANSLATOR_API_KEY your API key created from portal.azure.com.

```
localhost:5000/api?algo=TranslatorPlugin&i=<ARAB_TEXT_TO_TRANSLATE>&conversion=full&expanded-jsonld=false&informat=text&intype=direct&outformat=json-ld&urischeme=RFC5147String&with_parameters=false&lang=ar&key=<YOUR_MS_TRANSLATOR_API_KEY>
``` 
## Web interface access

1. Go to your web browser and search _localhost:5000_.
2. Insert your Microsoft Transalator API key.
3. Paste you text and click the Analyse button.

![alt text](images/translator.png "Web interface access")
