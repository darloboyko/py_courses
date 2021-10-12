def validate_hello(greetings):
    voc = {
          'hello' :'english', 
          'ciao':'italian', 
          'salut':'french',
          'hallo':'german',
          'hola':'spanish',
          'ahoj':'czech republic',
          'czesc':'polish'
    }

    return [True for key in voc if key in greetings.lower()]

greetings = str(input("String: "))

print(validate_hello(greetings))
