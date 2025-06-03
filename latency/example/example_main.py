import requests
import person_pb2



def create_person():
    person = person_pb2.Person()
    person.name = 'test'

    return person

def main():
    person = create_person()
    serialized_person = person.SerializeToString()
    print(serialized_person)

main()