# import libraries
import click
import pymongo
from pprint import pprint

# group main click commands
@click.group()
def main():
    pass

# click command
@main.command()
# click command prompts
@click.option('--name', prompt='You must first register as a freelancer.\nPlease, enter your full name (eg. Edvard Grieg)', type=str)
@click.option('--expertise', prompt='What is your expertise? (eg. music composition)', type=str)
@click.option('--description', prompt='Please, describe your background in your expertise in a couple of sentences', type=str)
@click.option('--address', prompt='What is your street address? (house/apartment number and street name)', type=str)
@click.option('--city', prompt='What city do you live in?', type=str)
@click.option('--postcode', prompt='What is your postcode?', type=str)
@click.option('--phone', prompt='Please, enter your phone number', type=str)
@click.option('--service', prompt='You can now register the service you wish to post.\nWhat service will you be offering? (eg. piano lessons)', type=str)
@click.option('--servicedes', prompt='Describe the service you wish to provide in a couple of sentences', type=str)
@click.option('--pph', prompt='How much will you charge in NOK per hour? eg. 300', type=float)
@click.option('--minhours', prompt='What is the minimum number of hours you require per session? eg. 1.5', type=float)
# function called
def post_a_service(name, expertise, description, address, city, postcode, phone, service, servicedes, pph, minhours):
    '''
    Creates a freelancer record and associated service
    '''
    # database connection
    client = pymongo.MongoClient("mongodb+srv://richelle:mongo@cluster0.7aohq.mongodb.net/finnplus?retryWrites=true&w=majority")
    db = client.finnplus
    # insert user inputs as values in document within freelancers collection
    db.freelancers.insert_one(
        {
        "freelancer_name" : name,
        "freelancer_expertise" : expertise,
        "freelancer_description" : description,
        "freelancer_address" : address,
        "freelancer_city" : city,
        "freelancer_postcode" : postcode,
        "freelancer_phone" : phone,
        "service_name" : service,
        "service_description" : servicedes,
        "price_per_hour" : pph,
        "minimum_hours" : minhours
        }
        );
    # greet user with parameters
    click.echo(f'Welcome to Finnplus, {name}!  You have been registered as a freelancer specialising in {expertise}.\nYour offer for {service} has now been posted.')

# click command
@main.command()
# click command prompt
@click.option("--search_name", prompt='Search for a service', type=str)
# function called
def search_by_service(search_name):
    '''
    Queries freelancers collection and returns document with service name attribute matching user's input
    '''
    # database connection
    client = pymongo.MongoClient("mongodb+srv://richelle:mongo@cluster0.7aohq.mongodb.net/finnplus?retryWrites=true&w=majority")
    db = client.finnplus
    # iteration over cursor to print documents with 'pretty' printer
    for post in db.freelancers.find({"service_name" : search_name}):
        pprint(post)

# click command
@main.command()
# click command prompt
@click.option("--search_freelancer", prompt='Search for a freelancer by entering his/her name', type=str)
# function called
def search_by_freelancer(search_freelancer):
    '''
    Queries freelancers collection and returns document with freelancer name attribute matching user's input
    '''
    # database connection
    client = pymongo.MongoClient("mongodb+srv://richelle:mongo@cluster0.7aohq.mongodb.net/finnplus?retryWrites=true&w=majority")
    db = client.finnplus
    # iteration over cursor to print documents with 'pretty' printer
    for post in db.freelancers.find({"freelancer_name" : search_freelancer}):
        pprint(post)

# click command
@main.command()
# click command prompt
@click.option("--search_city", prompt='Search a freelancer and service by city in Norway', type=str)
# function called
def search_by_city(search_city):
    '''
    Queries freelancers collection and returns document with city attribute matching user's input
    '''
    # database connection
    client = pymongo.MongoClient("mongodb+srv://richelle:mongo@cluster0.7aohq.mongodb.net/finnplus?retryWrites=true&w=majority")
    db = client.finnplus
    # iteration over cursor to print documents with 'pretty' printer
    for post in db.freelancers.find({"freelancer_city" : search_city}):
        pprint(post)

# click command
@main.command()
# click command prompt
@click.option("--search_expertise", prompt='Search by expertise', type=str)
# function called
def search_by_expertise(search_expertise):
    '''
    Queries freelancers collection and returns document with expertise attribute matching user's input
    '''
    # database connection
    client = pymongo.MongoClient("mongodb+srv://richelle:mongo@cluster0.7aohq.mongodb.net/finnplus?retryWrites=true&w=majority")
    db = client.finnplus
    # iteration over cursor to print documents with 'pretty' printer
    for post in db.freelancers.find({"freelancer_expertise" : search_expertise}):
        pprint(post)

# click command
@main.command()
# click command prompt
@click.option("--search_rate", prompt='Enter price per hour in NOK (eg. 130)', type=float)
# function called
def search_by_rate(search_rate):
    '''
    Queries freelancers collection and returns document with price per hour attribute matching user's input
    '''
    # database connection
    client = pymongo.MongoClient("mongodb+srv://richelle:mongo@cluster0.7aohq.mongodb.net/finnplus?retryWrites=true&w=majority")
    db = client.finnplus
    # iteration over cursor to print documents with 'pretty' printer
    for post in db.freelancers.find({"price_per_hour" : search_rate}):
        pprint(post)

# click command
@main.command()
# click command prompt
@click.option("--search_minhours", prompt='Enter a minimum number of hours (eg. 1.5)', type=float)
# function called
def search_by_minimum_time_block(search_minhours):
    '''
    Queries freelancers collection and returns document with minimum hours attribute matching user's input
    '''
    # database connection
    client = pymongo.MongoClient("mongodb+srv://richelle:mongo@cluster0.7aohq.mongodb.net/finnplus?retryWrites=true&w=majority")
    db = client.finnplus
    # iteration over cursor to print documents with 'pretty' printer
    for post in db.freelancers.find({"minimum_hours" : search_minhours}):
        pprint(post)

# click command
@main.command()
# click command prompts
@click.option('--customer_name', prompt='You must first register as a customer.\nPlease, enter your full name', type=str)
@click.option('--add_service', prompt='Which service would you like to add to your cart?', type=str)
@click.option('--add_freelancer', prompt='What is the name of the freelancer providing this service?', type=str)
@click.option('--add_sessions', prompt='How many sessions (of the minimum number of hours required by the freelancer) would you like to book?  Enter a whole number', type=int)
# function called
def add_to_cart(customer_name, add_service, add_freelancer, add_sessions):
    '''
    Creates an order record with associated customer, freelancer and service
    '''
    # database connection
    client = pymongo.MongoClient("mongodb+srv://richelle:mongo@cluster0.7aohq.mongodb.net/finnplus?retryWrites=true&w=majority")
    db = client.finnplus
    # iteration over cursor to get dictionary value of key specified to echo with variable
    for hours in db.freelancers.find({"freelancer_name" : add_freelancer}, {"minimum_hours" : 1}):
        min_hours = hours.get("minimum_hours")
    # iteration over cursor to get dictionary value of key specified to echo with variable and multiply with another
    for price in db.freelancers.find({"freelancer_name" : add_freelancer}, {"price_per_hour" : 1}):
        hourly_price = price .get("price_per_hour")
    order_total = hourly_price * add_sessions
    # insert user inputs as values in document within orders collection
    db.orders.insert_one(
        {
        "customer" : customer_name,
        "order_service" : add_service,
        "order_freelancer" : add_freelancer,
        "order_sessions" : add_sessions,
        "total" : order_total
        }
        );
    # greet user with parameters and variables
    click.echo(f'Welcome to Finnplus, {customer_name}!  You have been registered as a customer with {add_service} by {add_freelancer} in your cart.\nPrice per hour: NOK {hourly_price}\nMinimum number of hours: {min_hours}\nNumber of sessions: {add_sessions}\nTotal: NOK {order_total}.')

# click command
@main.command()
# click command prompts
@click.option('--customer_name', prompt='Please, enter your full name (the same one used when registering as a customer)', type=str)
@click.option('--remove_service', prompt='Which service would you like to remove from your cart?', type=str)
@click.option('--remove_sessions', prompt='How many sessions would you like to remove?  Enter a whole number', type=int)
# function called
def remove_from_cart(customer_name, remove_service, remove_sessions):
    '''
    Updates or deletes an order record with associated customer, freelancer and service
    '''
    # database connection
    client = pymongo.MongoClient("mongodb+srv://richelle:mongo@cluster0.7aohq.mongodb.net/finnplus?retryWrites=true&w=majority")
    db = client.finnplus
    # set customer name as document identifier for query update/deletion
    customer_query = {"customer" : customer_name}
    # iteration over cursor to get dictionary value of key specified to be subtracted from by another
    for sessions in db.orders.find({"customer" : customer_name}, {"order_sessions" : 1}):
        old_sessions = sessions.get("order_sessions")
    update_sessions = old_sessions - remove_sessions
    # condition for deletion
    if update_sessions <= 0:
        db.orders.delete_one(customer_query)
        click.echo(f'{customer_name}, your cart is now empty.')
    # condition for update
    else:
        # set new number of sessions ordered
        new_sessions = {"$set" : {"order_sessions" : update_sessions}}
        # iteration over cursor to get dictionary value of key specified to multiply with another
        for price in db.freelancers.find({"service_name" : remove_service}, {"price_per_hour" : 1}):
            hourly_price = price .get("price_per_hour")
        update_total = hourly_price * update_sessions
        # set new total price
        new_total = {"$set" : {"total" : update_total}}
        # update new number of sessions ordered and new total price
        db.orders.update_one(customer_query, new_sessions)
        db.orders.update_one(customer_query, new_total)
        # iterations over cursor to get dictionary values of keys specified to echo with variable
        for freelancers in db.orders.find({"customer" : customer_name}, {"order_freelancer" : 1}):
            freelancer_name = freelancers.get("order_freelancer")
        for hours in db.freelancers.find({"freelancer_name" : freelancer_name}, {"minimum_hours" : 1}):
            min_hours = hours.get("minimum_hours")
        for sessions in db.orders.find({"customer" : customer_name}, {"order_sessions" : 1}):
            updated_sessions = sessions.get("order_sessions")        
        for total in db.orders.find({"customer" : customer_name}, {"total" : 1}):
            order_total = total.get("total")
        # confirm changes to user with parameters and variables
        click.echo(f'{customer_name}, your cart has been updated.\n{remove_service} by {freelancer_name}\nPrice per hour: NOK {hourly_price}\nMinimum number of hours: {min_hours}\nNumber of sessions: {updated_sessions}\nTotal: NOK {order_total}.')

# click command
@main.command()
# click command prompts
@click.option('--customer_name', prompt='Please, enter your full name (the same one used when registering as a customer)', type=str)
@click.option('--billing_add', prompt='Billing info.\nWhat is your street address? (house/apartment number and street name)', type=str)
@click.option('--billing_city', prompt='What city do you live in?', type=str)
@click.option('--billing_postcode', prompt='What is your postcode?', type=str)
@click.option('--cc_number', prompt='Payment details.\nEnter your card number', type=str)
@click.option('--cc_date', prompt='Enter the expiration date of your card', type=str)
@click.option('--cc_cvv', prompt='Enter your cvv code', type=str)
# function called
def checkout(customer_name, billing_add, billing_city, billing_postcode, cc_number, cc_date, cc_cvv):
    '''
    Queries orders collection and returns confirmation of transaction message
    '''
    # database connection  
    client = pymongo.MongoClient("mongodb+srv://richelle:mongo@cluster0.7aohq.mongodb.net/finnplus?retryWrites=true&w=majority")
    db = client.finnplus
    # set customer name as document identifier for query read
    customer_query = {"customer" : customer_name}
    # set and update document with new fields and values prompted
    upsert_add = {"$set" : {"billing_address" : billing_add}}
    db.orders.update_one(customer_query, upsert_add)
    upsert_city = {"$set" : {"billing_city" : billing_city}}
    db.orders.update_one(customer_query, upsert_city)
    upsert_postcode = {"$set" : {"billing_postcode" : billing_postcode}}
    db.orders.update_one(customer_query, upsert_postcode)
    upsert_cc_number = {"$set" : {"card_number" : cc_number}}
    db.orders.update_one(customer_query, upsert_cc_number)
    upsert_cc_date = {"$set" : {"expiration_date" : cc_date}}
    db.orders.update_one(customer_query, upsert_cc_date)
    upsert_cc_cvv = {"$set" : {"cvv_code" : cc_cvv}}
    db.orders.update_one(customer_query, upsert_cc_cvv)
    # iterations over cursor to get dictionary values of keys specified to echo with variable
    for sessions in db.orders.find({"customer" : customer_name}, {"order_sessions" : 1}):
        checkout_sessions = sessions.get("order_sessions")
    for services in db.orders.find({"customer" : customer_name}, {"order_service" : 1}):
        service = services.get("order_service")
    for freelancers in db.orders.find({"customer" : customer_name}, {"order_freelancer" : 1}):
        freelancer = freelancers.get("order_freelancer")
    for total in db.orders.find({"customer" : customer_name}, {"total" : 1}):
        order_total = total.get("total")
    # confirm transaction to user with parameters and variables
    click.echo(f'Thank you, {customer_name}, for ordering {checkout_sessions} {service} with {freelancer} for a total of NOK {order_total}.')
# invoke main group of click commands
if __name__ == "__main__":
    main()
    