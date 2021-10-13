from model import db,Puppy, Owner, Toy

#  create two puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

#  add puppies to db
db.session.add_all([rufus,fido])
db.session.commit()

# check
print(Puppy.query.all())

# in case there are many rufus
rufus = Puppy.query.filter_by(name='Rufus').first()

# create owner object
jose = Owner('Jose',rufus.id)

# give rufus some toys
toy1 = Toy('Chew Toy',rufus.id)
toy2 = Toy('Ball',rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

# grab rufus after those additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rufus.report_toys()
