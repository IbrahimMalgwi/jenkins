import fire

def hello(name="World Ibrahim"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)