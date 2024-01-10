from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///models.db')

Base= declarative_base
class Restaurant (Base):
    __tablename__='restaurants'
    id = Column(Integer, primary_key=True)
    name=Column(String)
    price = Column(Integer)
    reviews = relationship('Review')

    def reviews(self):
        return self.reviews
    
    def customers(self):
        return self.customers

class Customer(Base):
    __tablename__='customers'
    id= Column(Integer, primary_key=True)
    first_name= Column(String)
    last_name= Column(String)
    reviews=relationship('Review')

    def reviews(self):
        return self.reviews
    
    def restaurants(self):
        return self.restaurants
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def favorite_restaurant(self):
        top_rating = max(review.star_rating for review in self.reviews)
        return next((review.restaurant for review in self.reviews if review.star_rating == top_rating), None)
    
class Review(Base):
    __tablename__='reviews'
    id= Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id= Column(Integer, ForeignKey('restaurants.id'))
    customer_id=Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant')
    customer= relationship('Customer')

    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
    
    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."