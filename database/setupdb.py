from basic import db,Puppy

# create all the tables, model --> db table
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

# it would print None will happen cuz I haven't provide their ids
print(sam.id)
print(frank.id)

# now sam and frank are in the database
db.session.add_all([sam,frank])

# commit the changes to my database
db.session.commit()

print(sam.id)
print(frank.id)
