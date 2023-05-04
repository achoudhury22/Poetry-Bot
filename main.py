## importing prominent modules
import random, time, tweepy, csv


## connecting to api and twitter
CONSUMER_KEY = "sX1V205Qu6rDD3zNx1pGQV1w9"
CONSUMER_SECRET = "Y69OVH7lJHsABnqafi72ZKWegvEmcEq6huX0RKNRv0AkWl0TRW"
ACCESS_KEY = "1390805224399441922-pXXT0PSu1FHa1QeTuETvVo9M6l6dp2"
ACCESS_SECRET = "jgWRziBRRTYqDvFoIl6MNAWKfw7DRDemQB68sGXni24s9"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


## testing to see if credentials are good
try:
  api.verify_credentials()
  print("Authorization okay")
except:
  print("Error during authorizationn check your credentials again")


## general function to read our different stanza files
def read_files(reader):
  index = 0
  for row in reader:
    if index == 0:
      stanza = row
    index += 1
  return stanza


## opening our files as csv and reading them
def read_stanzas():
  with open("1stanza_lines.csv") as csv_file:
    csv_reader1 = csv.reader(csv_file,delimiter = ',') 
    stanza1 = read_files(csv_reader1)
    
  with open("2stanza_lines.csv") as csv_file:
    csv_reader2 = csv.reader(csv_file,delimiter = ',')
    stanza2 = read_files(csv_reader2)

  with open("3stanza_lines.csv") as csv_file:
    csv_reader3 = csv.reader(csv_file, delimiter = ',')
    stanza3 = read_files(csv_reader3)
    
  with open("4stanza_lines.csv") as csv_file:
    csv_reader4 = csv.reader(csv_file, delimiter = ',')
    stanza4 = read_files(csv_reader4)
    
  with open("5stanza_lines.csv") as csv_file:
    csv_reader5 = csv.reader(csv_file, delimiter = ',')
    stanza5 = read_files(csv_reader5)
  
  return stanza1,stanza2,stanza3,stanza4,stanza5 


## to generate a random line from each stanza
def get_random_stanza(stanza):
  num = random.randint(0,6)  #we have 7 lines per stanza
  return stanza[num]


## function to return our randomly generated poem
def poem_maker():
  return (firstLine + "\n" + secondLine + "\n" + thirdLine + "\n" + fourthLine + "\n" + fifthLine)


stanza1, stanza2, stanza3, stanza4, stanza5 = read_stanzas()


firstLine = get_random_stanza(stanza1)
secondLine = get_random_stanza(stanza2)
thirdLine = get_random_stanza(stanza3)
fourthLine = get_random_stanza(stanza4)
fifthLine = get_random_stanza(stanza5)


## iteration to post poem every 30 min AND to put it in put TwitterPoems file
while True:
  Tweet = poem_maker()
  if len(Tweet) <= 280:
    api.update_status(status= Tweet)
    print(Tweet)
    infile2 = open("TwitterPoems.txt", "a")
    infile2.write("---------\n")
    infile2.write(Tweet)
    infile2.write("\n")  
    infile2.close()
  time.sleep(1800) 
